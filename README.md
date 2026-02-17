# simulated-city-template

Template project for a workshop where students learn **agent-based programming in Python** by building parts of a **simulated city / urban digital twin**.

## Quickstart (Python 3.11)

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -U pip
pip install -e ".[dev,notebooks]"
python -m pytest
python -m jupyterlab
```

## Repo layout

- `docs/`: workshop notes and exercises
- `src/simulated_city/`: installable library code
- `notebooks/`: workshop notebooks
- `tests/`: small sanity tests

## MQTT (default)

- Default broker settings live in `config.yaml` (HiveMQ-style)
- MQTT helper module: `simulated_city.mqtt`
- Setup notes: `docs/mqtt.md`
- Credentials: copy `.env.example` to `.env`

## Geo / CRS transforms (optional)

- Geo helper module: `simulated_city.geo`
- Provides CRS transforms (including WGS84 (EPSG:4326) ↔ EPSG:25832 helpers)
- Install extra: `pip install -e ".[geo]"` (see `docs/setup.md`)

## First run (CLI smoke)

```bash
python -m simulated_city
```

Note: this template library intentionally ships only `simulated_city.config` and
`simulated_city.mqtt` (plus optional `simulated_city.geo`). The simulation itself is an exercise.
