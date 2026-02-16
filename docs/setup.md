# Setup

This project targets **Python 3.11**.
This project targets **Python 3.11+**.

## Create and activate a virtual environment

macOS / Linux:

```bash
 python3 -m venv .venv
source .venv/bin/activate
python -m pip install -U pip
```

Windows (PowerShell):

```powershell
 py -3 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -U pip
```

## Install the library (editable) + workshop tools

```bash
pip install -e ".[dev,notebooks]"
```

## Run notebooks

- VS Code: open a notebook in `notebooks/` and select the `.venv` kernel.
- Or start Jupyter:

```bash
jupyter lab
```

## Run tests

```bash
python -m pytest
```
