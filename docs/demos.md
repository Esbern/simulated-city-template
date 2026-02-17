# Demos (scripts)

The notebook in `notebooks/01_simulated_city_basics.ipynb` is the primary teaching material.

If you prefer running the same ideas as plain Python scripts, see `scripts/demo/`.

## Run

First install the library (editable):

```bash
pip install -e "."
```

Then run a demo:

```bash
python scripts/demo/01_config_and_mqtt.py
python scripts/demo/02_geo_crs_transforms.py
python scripts/demo/03_folium_map_city_hall.py
```

## Demo scripts

- `01_config_and_mqtt.py`
  - loads config
  - builds a topic + JSON payload
  - optional: publishes ONE MQTT message (guarded by `ENABLE_PUBLISH = False`)

- `02_geo_crs_transforms.py`
  - shows WGS84 (EPSG:4326) ↔ EPSG:25832
  - shows both `transform_xy(...)` and `wgs2utm(...)` / `utm2wgs(...)`
  - requires: `pip install -e ".[geo]"`

- `03_folium_map_city_hall.py`
  - builds a Folium map in WGS84 (no transforms)
  - saves `copenhagen_city_hall_map.html`
  - requires: `pip install -e ".[notebooks]"` (or `pip install folium`)
