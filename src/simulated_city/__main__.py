from __future__ import annotations

from .sim import CitySim
from .types import Point
from .viz import grid_to_ascii


def main() -> None:
    sim = CitySim(width=20, height=10, seed=0)
    sim.populate_random(n_agents=25, n_places=8)

    for _ in range(5):
        sim.step()

    print(sim.metrics())
    print(grid_to_ascii(sim.snapshot_grid()))


if __name__ == "__main__":
    main()
