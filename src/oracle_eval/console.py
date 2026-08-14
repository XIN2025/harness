from __future__ import annotations

import contextlib
import sys

from rich.console import Console


def harden_stdout() -> None:
    reconfigure = getattr(sys.stdout, "reconfigure", None)
    if reconfigure is None:
        return
    with contextlib.suppress(ValueError, OSError):
        reconfigure(errors="replace")


console = Console()
