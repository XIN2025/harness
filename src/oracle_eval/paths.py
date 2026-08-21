from __future__ import annotations

from pathlib import Path

DEFAULT_INDEX = Path("data/oracle/remeda/index.jsonl")
DEFAULT_TSMORPH = Path("data/oracle/remeda/tsmorph.jsonl")
DEFAULT_MANIFEST = Path("data/corpus/remeda/manifest.json")
DEFAULT_REPO = Path("../slm/repos/remeda/packages/remeda")

PREDICTIONS_ROOT = Path("data/predictions")
RESULTS_ROOT = Path("data/results")

TEST_SUFFIXES = (".test.ts", ".test-d.ts", ".spec.ts", ".test.tsx")
TEST_DIRS = ("test/", "tests/", "__tests__/")


def posix(relative_path: str) -> str:
    return relative_path.replace("\\", "/")


def is_test_file(relative_path: str) -> bool:
    path = posix(relative_path)
    return path.endswith(TEST_SUFFIXES) or any(directory in path for directory in TEST_DIRS)
