from __future__ import annotations

from dataclasses import dataclass
import random

from .entities import Agent, Place
from .types import Point, manhattan


@dataclass(frozen=True, slots=True)
class SimMetrics:
    step: int
    agent_count: int
    place_count: int
    mean_distance_to_goal: float


class CitySim:
    """A tiny, notebook-friendly city simulation.

    Environment: width x height grid.
    Entities: Agents + Places.
    Dynamics: each step, agents choose a goal (if none) and move 1 cell toward it.

    This is intentionally minimal for teaching and extension.
    """

    def __init__(self, width: int, height: int, seed: int | None = None) -> None:
        if width <= 0 or height <= 0:
            raise ValueError("width and height must be positive")

        self.width = width
        self.height = height
        self._rng = random.Random(seed)

        self._step = 0
        self._next_agent_id = 1
        self._next_place_id = 1

        self.agents: dict[int, Agent] = {}
        self.places: dict[int, Place] = {}

    @property
    def step_index(self) -> int:
        return self._step

    def add_place(self, kind: str, location: Point) -> int:
        place_id = self._next_place_id
        self._next_place_id += 1
        self.places[place_id] = Place(id=place_id, kind=kind, location=location)  # type: ignore[arg-type]
        return place_id

    def add_agent(self, location: Point) -> int:
        agent_id = self._next_agent_id
        self._next_agent_id += 1
        self.agents[agent_id] = Agent(id=agent_id, location=location)
        return agent_id

    def populate_random(self, n_agents: int, n_places: int) -> None:
        for _ in range(n_places):
            kind = self._rng.choice(["home", "work", "shop", "park", "station"])
            self.add_place(kind=kind, location=self._random_point())

        for _ in range(n_agents):
            self.add_agent(location=self._random_point())

    def step(self) -> None:
        if not self.places:
            raise RuntimeError("No places in the city. Add places before stepping.")

        for agent in self.agents.values():
            if agent.goal_place_id is None or agent.goal_place_id not in self.places:
                agent.goal_place_id = self._rng.choice(list(self.places.keys()))

            goal = self.places[agent.goal_place_id].location
            agent.location = self._move_one_toward(agent.location, goal)
            agent.steps_taken += 1

        self._step += 1

    def metrics(self) -> SimMetrics:
        distances: list[int] = []
        for agent in self.agents.values():
            if agent.goal_place_id is None or agent.goal_place_id not in self.places:
                continue
            distances.append(manhattan(agent.location, self.places[agent.goal_place_id].location))

        mean_dist = (sum(distances) / len(distances)) if distances else 0.0
        return SimMetrics(
            step=self._step,
            agent_count=len(self.agents),
            place_count=len(self.places),
            mean_distance_to_goal=mean_dist,
        )

    def snapshot_grid(self) -> list[list[int]]:
        """Returns a width x height grid of agent counts per cell."""
        grid = [[0 for _ in range(self.width)] for _ in range(self.height)]
        for agent in self.agents.values():
            grid[agent.location.y][agent.location.x] += 1
        return grid

    def _random_point(self) -> Point:
        return Point(x=self._rng.randrange(self.width), y=self._rng.randrange(self.height))

    def _move_one_toward(self, current: Point, goal: Point) -> Point:
        dx = goal.x - current.x
        dy = goal.y - current.y

        # Move one step in the dominant direction (ties broken randomly).
        if abs(dx) > abs(dy):
            nx = current.x + (1 if dx > 0 else -1)
            ny = current.y
        elif abs(dy) > abs(dx):
            nx = current.x
            ny = current.y + (1 if dy > 0 else -1)
        else:
            if self._rng.random() < 0.5:
                nx = current.x + (1 if dx > 0 else -1 if dx < 0 else 0)
                ny = current.y
            else:
                nx = current.x
                ny = current.y + (1 if dy > 0 else -1 if dy < 0 else 0)

        return Point(x=self._clamp(nx, 0, self.width - 1), y=self._clamp(ny, 0, self.height - 1))

    @staticmethod
    def _clamp(value: int, lo: int, hi: int) -> int:
        return max(lo, min(hi, value))
