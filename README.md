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

## First run (CLI smoke)

```bash
python -m simulated_city
```