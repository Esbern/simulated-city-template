from simulated_city.sim import CitySim


def test_sim_runs_one_step() -> None:
    sim = CitySim(width=10, height=10, seed=1)
    sim.populate_random(n_agents=5, n_places=3)
    before = sim.metrics().agent_count
    sim.step()
    after = sim.metrics().agent_count
    assert before == after == 5
