#!/usr/bin/env sh
set -eu

if [ -d ".venv" ]; then
  echo "Found existing .venv/. Delete it first if it was created with the wrong Python version."
  echo "Example: rm -rf .venv"
  exit 1
fi

# Prefer a known-good range for dependency compatibility.
# If only newer versions exist (e.g. 3.14), they may work but can fail if wheels are missing.
candidates="python3.13 python3.12 python3.11 python3.14 python3"

chosen=""
for py in $candidates; do
  if command -v "$py" >/dev/null 2>&1; then
    if "$py" -c "import sys; raise SystemExit(0 if sys.version_info >= (3, 11) else 1)"; then
      chosen="$py"
      break
    fi
  fi
done

if [ -z "$chosen" ]; then
  echo "No Python >= 3.11 found on PATH. Install Python 3.11+ (3.11–3.13 recommended) and try again."
  exit 1
fi

echo "Using: $chosen ($("$chosen" -c 'import sys; print(sys.version.split()[0])'))"
"$chosen" -m venv .venv

echo "Created .venv. Activate it with:"
echo "  source .venv/bin/activate"
