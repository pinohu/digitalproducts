"""Tests for trends_checker — growth-rate computation, score mapping, retries."""

from __future__ import annotations

from types import SimpleNamespace
from unittest.mock import MagicMock

import pytest

import trends_checker as tc


THRESHOLDS = {"high": 30, "moderate": 10, "flat": -5, "declining": -15}


# ---------------------------------------------------------------------------
# map_growth_to_rubric_score
# ---------------------------------------------------------------------------


@pytest.mark.parametrize(
    "growth_pct,expected_score",
    [
        (float("inf"), 10),
        (50.0, 9),
        (30.0, 9),
        (25.0, 8),
        (20.0, 8),
        (15.0, 7),
        (10.0, 7),
        (5.0, 6),
        (0.0, 6),
        (-3.0, 5),
        (-10.0, 3),
        (-20.0, 1),
    ],
)
def test_map_growth_to_rubric_score(growth_pct, expected_score):
    score, verdict = tc.map_growth_to_rubric_score(growth_pct, THRESHOLDS)
    assert score == expected_score
    assert isinstance(verdict, str)
    assert verdict  # non-empty


# ---------------------------------------------------------------------------
# fetch_trends — growth-rate computation with mocked pytrends
# ---------------------------------------------------------------------------


class _FakeSeries:
    """Tiny stand-in for a pandas Series — supports the slice ops used."""

    def __init__(self, values):
        self._values = list(values)

    def __len__(self):
        return len(self._values)

    @property
    def iloc(self):
        outer = self

        class _Iloc:
            def __getitem__(self, key):
                return _FakeSeries(outer._values[key]) if isinstance(key, slice) else outer._values[key]

        return _Iloc()

    def mean(self):
        return sum(self._values) / len(self._values) if self._values else 0.0

    def max(self):
        return max(self._values)

    def min(self):
        return min(self._values)


class _FakeFrame:
    """Stand-in for the pandas DataFrame returned by interest_over_time()."""

    def __init__(self, data: dict, partial: bool = False):
        # Optionally include 'isPartial' to test column drop.
        self._data = dict(data)
        if partial:
            self._data["isPartial"] = _FakeSeries([False] * len(next(iter(data.values()))._values))

    @property
    def empty(self):
        return not self._data

    @property
    def columns(self):
        return list(self._data.keys())

    def drop(self, columns):
        new = {k: v for k, v in self._data.items() if k not in columns}
        f = _FakeFrame.__new__(_FakeFrame)
        f._data = new
        return f

    def __getitem__(self, key):
        return self._data[key]


def _build_factory(frame: _FakeFrame):
    """Return a `trend_req_factory` that yields a mock TrendReq."""
    pytrends = MagicMock()
    pytrends.build_payload = MagicMock()
    pytrends.interest_over_time = MagicMock(return_value=frame)
    return lambda: pytrends, pytrends


def test_fetch_trends_growth_pct_positive_uptrend():
    # 20 datapoints — first quarter avg = 10, last quarter avg = 50 → +400%
    series = _FakeSeries([10] * 5 + [20] * 10 + [50] * 5)
    frame = _FakeFrame({"newsletter monetization": series})

    factory, _ = _build_factory(frame)
    results = tc.fetch_trends(
        ["newsletter monetization"],
        lookback_months=24,
        trend_req_factory=factory,
    )
    data = results["newsletter monetization"]
    assert data is not None
    assert data["growth_pct"] == pytest.approx(400.0)
    assert data["q1_avg"] == pytest.approx(10.0)
    assert data["q4_avg"] == pytest.approx(50.0)
    score, _ = tc.map_growth_to_rubric_score(data["growth_pct"], THRESHOLDS)
    assert score == 9  # >= 30% high threshold


def test_fetch_trends_zero_baseline_yields_inf_growth():
    series = _FakeSeries([0] * 5 + [5] * 10 + [40] * 5)
    frame = _FakeFrame({"new term": series})
    factory, _ = _build_factory(frame)
    results = tc.fetch_trends(["new term"], lookback_months=24, trend_req_factory=factory)
    assert results["new term"]["growth_pct"] == float("inf")
    score, _ = tc.map_growth_to_rubric_score(results["new term"]["growth_pct"], THRESHOLDS)
    assert score == 10


def test_fetch_trends_empty_frame_returns_none_per_keyword():
    frame = _FakeFrame({})
    factory, _ = _build_factory(frame)
    results = tc.fetch_trends(["a", "b"], lookback_months=12, trend_req_factory=factory)
    assert results == {"a": None, "b": None}


def test_fetch_trends_strips_is_partial_column():
    series = _FakeSeries([10] * 8 + [20] * 8)
    frame = _FakeFrame({"kw": series}, partial=True)
    factory, _ = _build_factory(frame)
    results = tc.fetch_trends(["kw"], lookback_months=12, trend_req_factory=factory)
    assert results["kw"] is not None


# ---------------------------------------------------------------------------
# Retry / backoff behavior
# ---------------------------------------------------------------------------


def test_fetch_trends_retries_on_429_then_succeeds():
    series = _FakeSeries([10] * 8 + [20] * 8)
    frame = _FakeFrame({"kw": series})

    call_count = {"n": 0}

    def factory():
        call_count["n"] += 1
        m = MagicMock()
        if call_count["n"] < 3:
            # First 2 calls raise a 429
            err = Exception("429 Too Many Requests")
            m.build_payload = MagicMock(side_effect=err)
        else:
            m.build_payload = MagicMock()
            m.interest_over_time = MagicMock(return_value=frame)
        return m

    sleeps: list[float] = []
    results = tc.fetch_trends(
        ["kw"],
        lookback_months=12,
        trend_req_factory=factory,
        sleep_fn=sleeps.append,
        initial_backoff_seconds=1.0,
        max_retries=5,
    )
    assert results["kw"] is not None
    assert call_count["n"] == 3
    # Two backoffs occurred before success: 1.0, 2.0
    assert sleeps == [1.0, 2.0]


def test_fetch_trends_raises_trends_unavailable_after_max_retries():
    def factory():
        m = MagicMock()
        m.build_payload = MagicMock(side_effect=Exception("429 Too Many Requests"))
        return m

    with pytest.raises(tc.TrendsUnavailableError):
        tc.fetch_trends(
            ["kw"],
            lookback_months=12,
            trend_req_factory=factory,
            sleep_fn=lambda _s: None,
            initial_backoff_seconds=0.01,
            max_retries=2,
        )


def test_fetch_trends_non_rate_limit_error_does_not_retry():
    calls = {"n": 0}

    def factory():
        calls["n"] += 1
        m = MagicMock()
        m.build_payload = MagicMock(side_effect=ValueError("bad input"))
        return m

    with pytest.raises(tc.TrendsUnavailableError):
        tc.fetch_trends(
            ["kw"],
            lookback_months=12,
            trend_req_factory=factory,
            sleep_fn=lambda _s: None,
            max_retries=4,
        )
    # Non-retryable: only one attempt.
    assert calls["n"] == 1


def test_is_rate_limit_detects_status_code_response():
    response = SimpleNamespace(status_code=429)
    exc = Exception("oops")
    exc.response = response  # type: ignore[attr-defined]
    assert tc._is_rate_limit(exc) is True


def test_is_rate_limit_returns_false_for_unrelated_error():
    assert tc._is_rate_limit(ValueError("boom")) is False


# ---------------------------------------------------------------------------
# MissingDependencyError — pytrends not installed
# ---------------------------------------------------------------------------


def test_default_factory_raises_missing_dependency_when_pytrends_absent(monkeypatch):
    monkeypatch.setattr(tc, "TrendReq", None)
    with pytest.raises(tc.MissingDependencyError):
        tc._default_trend_req_factory()


def test_fetch_trends_surfaces_missing_dependency_not_unavailable(monkeypatch):
    """Setup error must NOT be wrapped/retried as a transient outage."""
    monkeypatch.setattr(tc, "TrendReq", None)
    sleeps: list[float] = []
    with pytest.raises(tc.MissingDependencyError):
        tc.fetch_trends(
            ["kw"],
            lookback_months=12,
            sleep_fn=sleeps.append,
            max_retries=4,
        )
    # No retries on a missing-dependency error.
    assert sleeps == []
