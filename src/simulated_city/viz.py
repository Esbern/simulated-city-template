from __future__ import annotations

from typing import Iterable


def grid_to_ascii(grid: list[list[int]]) -> str:
    """Simple text visualization for quick debugging (no dependencies)."""
    lines: list[str] = []
    for row in grid:
        lines.append("".join(_cell_char(v) for v in row))
    return "\n".join(lines)


def _cell_char(value: int) -> str:
    if value <= 0:
        return "."
    if value == 1:
        return "1"
    if value == 2:
        return "2"
    if value == 3:
        return "3"
    return "*"
