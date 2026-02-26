# Setup

This project targets **Python 3.11+**.

In practice, the smoothest experience is usually with Python **3.11–3.13**. Newer versions (for example Python 3.14 right after release) may work, but some third-party packages may not have prebuilt wheels available yet, which can cause `pip install` to fail.

The package metadata enforces this (`requires-python >= 3.11`), so installs will fail on older Python versions.

## Create and activate a virtual environment

If you have multiple Python versions installed, you may accidentally create the virtual environment with an older interpreter (for example Python 3.9/3.10). The interpreter you use to run `-m venv` is the Python version that will be used inside `.venv`.

Quick check:

- Before creating the venv, check the system interpreter you are about to use:

```bash
python3 --version
```

Optional “version gate” (exits with an error if Python is too old):

```bash
python3 -c "import sys; print(sys.version); assert sys.version_info >= (3, 11)"
```

- After activating the venv, confirm `python` now points to the venv interpreter:

```bash
python --version
```

macOS / Linux:

Most reliable option (recommended): use the helper script to create `.venv` using the first Python on your PATH that is **>= 3.11**:

```bash
./scripts/create_venv.sh
source .venv/bin/activate
python -m pip install -U pip
```

Manual option:

If you are not sure which `python3` you have (and want to avoid accidentally using Python 3.9/3.10), use this snippet to pick the first installed Python that is **>= 3.11**:

```bash
chosen=""
for py in python3.13 python3.12 python3.11 python3.14 python3; do
   if command -v "$py" >/dev/null 2>&1; then
      if "$py" -c "import sys; raise SystemExit(0 if sys.version_info >= (3, 11) else 1)"; then
         chosen="$py"
         "$py" -m venv .venv
         break
      fi
   fi
done

if [ -z "$chosen" ]; then
   echo "No Python >= 3.11 found. Install Python 3.11+ (3.11–3.13 recommended) and try again."
   exit 1
fi
```

Then activate and continue:

```bash
source .venv/bin/activate
python -m pip install -U pip
```

If you want to pin the venv to a specific interpreter, you can use a versioned executable (if installed), for example:

```bash
python3.11 -m venv .venv
```

If you do not have any Python 3.11+ available, install Python 3.11+ first, or use a version manager (for example `pyenv` or `asdf`) to make 3.11+ your default.

Helpful commands to see what you are actually running:

```bash
which -a python python3 python3.11
python3 --version
python3.11 --version
```

Windows (PowerShell):

```powershell
py -3.11 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -U pip
```

If you have multiple versions installed and want to avoid picking an older one, choose an explicit version you have (3.11+), for example:

```powershell
py -3.13 -m venv .venv
```

If you do not have Python 3.11 installed, `py -3.11` will fail. Install Python 3.11+ (3.11–3.13 recommended if you hit package compatibility issues).

To see which Python installations the launcher can see:

```powershell
py -0p
```

Optional “version gate” (check what `py -3` would use):

```powershell
py -3 -c "import sys; print(sys.version); assert sys.version_info >= (3, 11)"
```

Note: if you are using a very new Python version (for example a new major release), some third-party packages may not have wheels available yet. If installs fail, create the venv using Python 3.11–3.13.

PowerShell does not include `which`. To see what command will run, use:

```powershell
Get-Command python -All
where.exe python
```

If you already created `.venv` with the wrong Python version, delete `.venv` and create it again with the correct interpreter.

If you get an execution policy error, run this once:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

## Install the library (editable) + workshop tools

```bash
pip install -e ".[dev,notebooks]"
```

## Optional: geospatial transforms (CRS)

If you plan to work with real-world coordinates, install the optional geospatial
extra to enable EPSG transforms.

Geo helpers live in `simulated_city.geo` and include convenience functions like
`wgs2utm(...)` / `utm2wgs(...)` plus the general `transform_xy(...)`.

```bash
pip install -e ".[geo]"
```

Tip: for notebooks that include both mapping + CRS transforms, you can install both extras:

```bash
pip install -e ".[notebooks,geo]"
```

## Set up a local MQTT broker (optional)

If you want to test MQTT locally before connecting to a public broker, install **Mosquitto**:

### macOS (using Homebrew)

```bash
brew install mosquitto
brew services start mosquitto
```

Verify it's running:

```bash
lsof -i :1883
```

You should see `mosquitto` listening on port 1883.

### Linux (Ubuntu/Debian)

```bash
sudo apt-get install mosquitto
sudo systemctl start mosquitto
```

### Windows

Download the installer from [mosquitto.org](https://mosquitto.org/download/) or use Windows Subsystem for Linux (WSL).

## Run notebooks

- VS Code: open a notebook in `notebooks/` and select the `.venv` kernel.
- Or start Jupyter:

```bash
jupyter lab
```

You can also run:

```bash
python -m jupyterlab
```

## Recommended learning path

1. Start with `notebooks/01_maps_and_coordinates.ipynb` to learn coordinate transforms
2. Move to `notebooks/02_mqtt_intro/` for MQTT basics:
   - `Broker_publisher.ipynb` — Publishing to local and public brokers
   - `Broker_subscriber.ipynb` — Subscribing to messages
3. Build your simulation using both concepts

## Run tests

```bash
python -m pytest
```
