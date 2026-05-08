"""
conftest.py — shared pytest fixtures and path bootstrapping for tools/ tests.

Adds tools/ to sys.path so test modules can `import idea_scorer`, etc.,
without requiring the package to be installed.
"""

from __future__ import annotations

import sys
from pathlib import Path

TOOLS_DIR = Path(__file__).resolve().parent
if str(TOOLS_DIR) not in sys.path:
    sys.path.insert(0, str(TOOLS_DIR))
