"""Tests for product_bootstrapper — verify it scaffolds the full file set.

These tests build a fake repo under tmp_path, monkeypatch the module's
REPO_ROOT and CONFIG_PATH constants to point at the fake tree, then call the
file-creating helpers directly.
"""

from __future__ import annotations

from pathlib import Path

import pytest

import product_bootstrapper as pb


SLUG = "02-newsletter-monetization"
TITLE = "Newsletter Monetization Playbook"
PRICE = 49
AVATAR = "Solo creators with 1K-10K newsletter subscribers"


def _expected_files(slug: str) -> list[str]:
    """Mirror of config.yaml::product_bootstrap.per_product_files (resolved)."""
    return [
        f"03-products/{slug}/README.md",
        f"01-market-research/by-product/{slug}/validation.md",
        f"02-offers/by-product/{slug}.md",
        f"04-sales-pages/by-product/{slug}.md",
        f"05-email-workflows/by-product/{slug}/README.md",
        f"06-launch-playbooks/by-product/{slug}.md",
        f"analytics/by-product/{slug}.md",
    ]


def _expected_dirs(slug: str) -> list[str]:
    return [
        f"03-products/{slug}",
        f"03-products/{slug}/manuscript",
        f"03-products/{slug}/assets",
        f"03-products/{slug}/bonuses",
        f"03-products/{slug}/deliverables",
        f"05-email-workflows/by-product/{slug}",
    ]


@pytest.fixture
def fake_repo(tmp_path: Path, monkeypatch):
    """Point product_bootstrapper at a fresh tmp_path repo."""
    monkeypatch.setattr(pb, "REPO_ROOT", tmp_path)
    # config_path doesn't need to exist; load_config has a fallback.
    monkeypatch.setattr(pb, "CONFIG_PATH", tmp_path / "tools" / "config.yaml")
    return tmp_path


def _scaffold(repo: Path, slug: str = SLUG) -> None:
    """Replicate main()'s file-creating loop without the argparse dance."""
    config = pb.load_config()
    pbcfg = config["product_bootstrap"]
    product_root = repo / "03-products" / slug
    pb.create_dir_safe(product_root, dry_run=False)
    for sub in pbcfg["product_subfolders"]:
        pb.create_dir_safe(product_root / sub, dry_run=False)
    pb.create_file_safe(
        product_root / "README.md",
        pb.render_product_readme(slug, TITLE, PRICE, AVATAR),
        dry_run=False,
    )
    file_renderers = {
        f"01-market-research/by-product/{slug}/validation.md": pb.render_validation_stub(slug, TITLE, AVATAR),
        f"02-offers/by-product/{slug}.md": pb.render_offer_stub(slug, TITLE, PRICE),
        f"04-sales-pages/by-product/{slug}.md": pb.render_sales_page_stub(slug, TITLE),
        f"05-email-workflows/by-product/{slug}/README.md": pb.render_email_workflow_stub(slug, TITLE),
        f"06-launch-playbooks/by-product/{slug}.md": pb.render_launch_stub(slug, TITLE),
        f"analytics/by-product/{slug}.md": pb.render_analytics_stub(slug, TITLE),
    }
    for rel_path, content in file_renderers.items():
        pb.create_file_safe(repo / rel_path, content, dry_run=False)


# ---------------------------------------------------------------------------
# slug validation
# ---------------------------------------------------------------------------


@pytest.mark.parametrize(
    "slug,is_valid",
    [
        ("02-newsletter-monetization", True),
        ("99-a", True),
        ("01-foo-bar-baz", True),
        ("foo-bar", False),  # missing NN-
        ("02-Foo-Bar", False),  # uppercase
        ("02-foo_bar", False),  # underscore
        ("2-foo", False),  # not 2 digits
        ("", False),
    ],
)
def test_validate_slug(slug, is_valid):
    assert pb.validate_slug(slug) is is_valid


# ---------------------------------------------------------------------------
# scaffolding
# ---------------------------------------------------------------------------


def test_scaffold_creates_all_expected_files_and_dirs(fake_repo):
    _scaffold(fake_repo)

    for rel in _expected_files(SLUG):
        assert (fake_repo / rel).is_file(), f"Missing file: {rel}"

    for rel in _expected_dirs(SLUG):
        assert (fake_repo / rel).is_dir(), f"Missing dir: {rel}"


def test_scaffold_readme_mentions_title_and_slug(fake_repo):
    _scaffold(fake_repo)
    readme = (fake_repo / f"03-products/{SLUG}/README.md").read_text(encoding="utf-8")
    assert TITLE in readme
    assert SLUG in readme
    assert f"${PRICE}" in readme


def test_scaffold_is_idempotent(fake_repo):
    """Re-running must not blow away or modify existing content."""
    _scaffold(fake_repo)

    sentinel_path = fake_repo / f"03-products/{SLUG}/README.md"
    sentinel = "MY HAND-EDITED CONTENT — DO NOT OVERWRITE\n"
    sentinel_path.write_text(sentinel, encoding="utf-8")

    # Re-run scaffold
    _scaffold(fake_repo)

    assert sentinel_path.read_text(encoding="utf-8") == sentinel


def test_create_file_safe_returns_false_when_existing(fake_repo):
    target = fake_repo / "some" / "file.md"
    target.parent.mkdir(parents=True)
    target.write_text("preexisting", encoding="utf-8")
    created = pb.create_file_safe(target, "new content", dry_run=False)
    assert created is False
    assert target.read_text(encoding="utf-8") == "preexisting"


def test_create_file_safe_dry_run_does_not_write(fake_repo):
    target = fake_repo / "some" / "file.md"
    pb.create_file_safe(target, "content", dry_run=True)
    assert not target.exists()
