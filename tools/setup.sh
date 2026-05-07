#!/usr/bin/env bash
set -euo pipefail

# Repeatable setup for the local Python tooling.
# Run from repo root or tools/: bash tools/setup.sh

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

PYTHON_BIN="${PYTHON_BIN:-python3}"
VENV_DIR="${VENV_DIR:-.venv}"

if [[ ! -f ".env" ]]; then
  cp .env.example .env
  echo "Created tools/.env from .env.example. Fill real credentials before running API-backed tools."
fi

create_with_python_venv() {
  "$PYTHON_BIN" -m venv "$VENV_DIR"
  # shellcheck disable=SC1091
  source "$VENV_DIR/bin/activate"
  python -m pip install --upgrade pip
  pip install -r requirements.txt
}

create_with_uv() {
  UV_LINK_MODE=copy uv venv "$VENV_DIR"
  # shellcheck disable=SC1091
  source "$VENV_DIR/bin/activate"
  UV_LINK_MODE=copy uv pip install -r requirements.txt
}

if [[ -d "$VENV_DIR" && -x "$VENV_DIR/bin/python" ]]; then
  # shellcheck disable=SC1091
  source "$VENV_DIR/bin/activate"
  if command -v uv >/dev/null 2>&1; then
    UV_LINK_MODE=copy uv pip install -r requirements.txt >/dev/null
  else
    python -m pip install -r requirements.txt >/dev/null
  fi
else
  if [[ -d "$VENV_DIR" ]]; then
    if ! rm -rf "$VENV_DIR" 2>/tmp/digitalproducts-rm-venv.log; then
      if command -v uv >/dev/null 2>&1; then
        echo "Could not remove $VENV_DIR cleanly (common on /mnt/c WSL mounts); using .uv-venv instead. Details: /tmp/digitalproducts-rm-venv.log"
        VENV_DIR=".uv-venv"
        rm -rf "$VENV_DIR"
      else
        cat /tmp/digitalproducts-rm-venv.log >&2 || true
        exit 1
      fi
    fi
  fi
  if "$PYTHON_BIN" -m venv "$VENV_DIR" >/tmp/digitalproducts-venv.log 2>&1; then
    # Recreate cleanly because the probe environment has no upgraded pip/deps yet.
    rm -rf "$VENV_DIR"
    create_with_python_venv
  elif command -v uv >/dev/null 2>&1; then
    echo "python -m venv failed; falling back to uv. Details: /tmp/digitalproducts-venv.log"
    rm -rf "$VENV_DIR" 2>/dev/null || true
    create_with_uv
  else
    cat /tmp/digitalproducts-venv.log >&2 || true
    cat >&2 <<'EOF'
Unable to create a virtualenv.

On Debian/Ubuntu/WSL install the venv package, then rerun:
  sudo apt-get install python3-venv
  bash tools/setup.sh

If sudo is unavailable, install uv and rerun:
  curl -LsSf https://astral.sh/uv/install.sh | sh
  bash tools/setup.sh
EOF
    exit 1
  fi
fi

python -m py_compile idea_scorer.py reddit_miner.py trends_checker.py product_bootstrapper.py
python idea_scorer.py --help >/dev/null
python reddit_miner.py --help >/dev/null
python trends_checker.py --help >/dev/null
python product_bootstrapper.py --help >/dev/null
python product_bootstrapper.py --slug 99-verification-product --title "Verification Product" --dry-run --yes >/dev/null

echo "Tools environment ready. Activate with: source tools/${VENV_DIR}/bin/activate"
echo "Next: fill tools/.env with real Reddit/Anthropic/GitHub credentials before running API-backed mining."
