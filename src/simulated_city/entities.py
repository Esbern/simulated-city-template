from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .types import Point

PlaceKind = Literal["home", "work", "shop", "park", "station"]


@dataclass(slots=True)
class Place:
    """A simple city place (building / POI)."""

    id: int
    kind: PlaceKind
    location: Point


@dataclass(slots=True)
class Agent:
    """A simple agent that moves on a grid and optionally targets a place."""

    id: int
    location: Point
    goal_place_id: int | None = None
    steps_taken: int = 0
