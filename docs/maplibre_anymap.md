# anymap-ts (MapLibre) — API subset used in this workshop

This page documents the **small set of anymap-ts functions** students use for mapping.

It is intentionally not a full anymap-ts manual — it focuses on the functions you’ll see in the workshop code.

**Note:** anymap-ts has limited public documentation. The methods documented here were found through source code inspection. For the full API, see the [anymap-ts GitHub repository](https://github.com/opengeos/anymap-ts) or PyPI package source.


## Install

```bash
pip install -e ".[notebooks]"
```


## Coordinates

All examples use WGS84 geographic coordinates in the order:

- `(lng, lat)` (longitude first)


## Import

The workshop uses the MapLibre backend through the `Map` widget:

```python
from anymap_ts import Map
```


## Create a map

```python
CITY_HALL_LNGLAT = (12.5683, 55.6761)

m = Map(
    center=CITY_HALL_LNGLAT,
    zoom=16.5,
    height="650px",
    width="100%",  # optional
    # style=...,    # optional (URL or style dict)
)
m
```

Workshop-relevant arguments:

- `center`: `(lng, lat)`
- `zoom`: float
- `height`: CSS string
- `width`: CSS string


## Basemaps

### `add_basemap(basemap_name) -> None`

Add a tile basemap layer to the map.

Common basemap names:

- `"OpenStreetMap"` (gray/light version, default)
- `"OpenStreetMap.Mapnik"` (standard OpenStreetMap colors)
- `"Esri.WorldImagery"` (satellite/orthophoto imagery)
- `"CartoDB.Positron"` (light)
- `"CartoDB.DarkMatter"` (dark)
- `"Stamen.Terrain"` (terrain)

Example:

```python
m.add_basemap("OpenStreetMap.Mapnik")  # Standard OSM
m.add_basemap("Esri.WorldImagery")     # Satellite imagery
m.add_basemap("CartoDB.DarkMatter")    # Dark theme
```


## Markers (static points)

### `add_marker(lng, lat, ...) -> str`

Adds a marker to the map and returns its marker ID.

Used arguments in the workshop:

- `lng`, `lat`: floats
- `name`: stable marker ID (recommended)
- `color`: hex string (e.g. `"#2e7d32"`)
- `popup`: optional text/HTML

Example:

```python
marker_id = m.add_marker(
    12.5699,
    55.6763,
    name="coffee-1",
    color="#2e7d32",
    popup="Coffee shop 1",
)
```

### `remove_marker(marker_id) -> None`

Removes a marker by ID.

```python
m.remove_marker("coffee-1")
```


## Route animation (frontend playback)

### `animate_along_route(coords, ...) -> None`

Animates a marker along a precomputed route in the browser (smooth and low overhead).

The workshop uses:

- `coords`: list of `[lng, lat]` points
- `anim_id`: string identifier
- `duration`: milliseconds
- `loop`: bool
- `marker_color`, `marker_size`
- `show_trail`: bool

Example:

```python
coords = [
    [12.5683, 55.6761],
    [12.5684, 55.67612],
]

m.animate_along_route(
    coords,
    anim_id="walk-1",
    duration=45_000,
    loop=True,
    marker_color="#3388ff",
    marker_size=1.0,
    show_trail=False,
)
```

### `stop_animation(anim_id) -> None`

Stops a running animation.

```python
m.stop_animation("walk-1")
```


## 3D visualization

### `add_3d_buildings(fill_extrusion_color="#aaa", fill_extrusion_opacity=0.6, min_zoom=14, ...) -> None`

Add 3D building extrusions from vector tile sources. Works best with vector tile styles that include building data.

Example:

```python
m = Map(center=(12.5683, 55.6761), zoom=15, pitch=60)
m.add_3d_buildings(
    fill_extrusion_color="#4682B4",
    fill_extrusion_opacity=0.8
)
```

### `add_3d_terrain(source="terrarium", exaggeration=1.0, ...) -> None`

Enable 3D terrain visualization with elevation data.

Example:

```python
m = Map(center=(12.5683, 55.6761), zoom=12, pitch=60)
m.add_3d_terrain(exaggeration=1.5)
```

### `set_sky(sky_color="#88C6FC", horizon_color="#F0E4D4", fog_color="#FFFFFF", ...) -> None`

Set atmospheric effects (sky color, horizon, fog). Best used with 3D terrain.

Parameters:
- `sky_color`: Sky color (default: `"#88C6FC"`)
- `horizon_color`: Horizon color (default: `"#F0E4D4"`)
- `fog_color`: Fog color (default: `"#FFFFFF"`)
- `sky_horizon_blend`, `horizon_fog_blend`, `fog_ground_blend`: Blend factors (0-1)
- `atmosphere_blend`: Atmosphere intensity (0-1, default: 0.8)

Example:

```python
m.set_sky()  # Use defaults
# or customize:
m.set_sky(sky_color="#87CEEB", fog_color="#E0E0E0")
```


## Navigation

### `fly_to(lng, lat, zoom=None, ...) -> None`

Animate the camera to a specific location.

Example:

```python
m.fly_to(12.5683, 55.6761, zoom=14)
```

### `fit_bounds(bounds) -> None`

Fit the map view to a bounding box `[west, south, east, north]`.

Example:

```python
m.fit_bounds([12.5, 55.65, 12.6, 55.7])
```


## Vector data

### `add_geojson(data, name=None, layer_type=None, paint=None, fit_bounds=True, ...) -> None`

Add GeoJSON features to the map.

Example:

```python
geojson = {
    "type": "FeatureCollection",
    "features": [
        {
            "type": "Feature",
            "geometry": {"type": "Point", "coordinates": [12.5683, 55.6761]},
            "properties": {"name": "City Hall"}
        }
    ]
}
m.add_geojson(geojson, name="points")
```

### `add_vector(data, name=None, layer_type=None, paint=None, fit_bounds=True, ...) -> None`

Add vector data (supports GeoJSON, GeoDataFrame, or file paths).

Example:

```python
import geopandas as gpd
gdf = gpd.read_file("data.geojson")
m.add_vector(gdf, name="polygons")
```


## Layer management

### `set_visibility(layer_id, visible) -> None`

Show or hide a layer **that you've added** to the map.

**Important:** This works on layers added via `add_basemap()`, `add_geojson()`, `add_vector()`, etc., but **not** on the base style's built-in layers.

Example:

```python
m.add_basemap("Esri.WorldImagery")
m.set_visibility("Esri.WorldImagery", False)  # Hide the basemap
m.set_visibility("Esri.WorldImagery", True)   # Show it again
```

To control the base background layer, start with a blank style:

```python
m = Map(
    center=(12.5683, 55.6761),
    zoom=18,
    style={
        "version": 8,
        "sources": {},
        "layers": []
    }
)
# Now add only the layers you want:
m.add_basemap("OpenStreetMap.Mapnik")
m.set_visibility("OpenStreetMap.Mapnik", False)  # This works!
```

### `set_opacity(layer_id, opacity) -> None`

Set opacity (0-1) for a layer **that you've added**.

Example:

```python
m.add_basemap("Esri.WorldImagery")
m.set_opacity("Esri.WorldImagery", 0.5)  # Semi-transparent
```

### `move_layer(layer_id, before_id=None) -> None`

Move a layer in the layer stack to control drawing order (z-order).

Layers drawn later appear on top of earlier layers. Use this method to reorder layers when you need to control which data appears in front.

**Parameters:**

- `layer_id` - Layer identifier to move
- `before_id` - ID of layer to move before. If `None`, moves to the top (front) of the stack.

Example:

```python
m.add_basemap("Esri.WorldImagery")
m.add_geojson("roads.geojson", name="roads")
m.add_3d_buildings()

# Move satellite imagery to the top (will cover everything):
m.move_layer("Esri.WorldImagery")

# Or move roads to appear before 3D buildings:
m.move_layer("roads", "3d-buildings")  # Roads will be below buildings
```


## Raster data

### `add_tile_layer(url, name=None, attribution="", min_zoom=0, max_zoom=22, ...) -> None`

Add an XYZ tile layer.

Example:

```python
m.add_tile_layer(
    "https://tile.openstreetmap.org/{z}/{x}/{y}.png",
    name="osm"
)
```

### `add_cog_layer(url, name=None, opacity=1.0, ...) -> None`

Add a Cloud Optimized GeoTIFF (COG) layer with GPU-accelerated rendering.

Example:

```python
m.add_cog_layer(
    "https://example.com/landcover.tif",
    name="landcover"
)
```


## Export

### `to_html(filepath, title="Map") -> None`

Save the map as a standalone HTML file.

Example:

```python
m.to_html("map.html", title="Copenhagen City Hall")
```


## Workshop extension: live marker movement

anymap-ts provides `add_marker(...)`, but does not expose a built-in “move an existing marker in place” method suitable for high-frequency streaming.

For that, the workshop includes a tiny extension:

```python
from simulated_city.maplibre_live import LiveMapLibreMap
```

### `LiveMapLibreMap.move_marker(marker_id, (lng, lat), color=None, popup=None) -> None`

Moves an existing marker in-place (or creates it if missing).

```python
m = LiveMapLibreMap(center=CITY_HALL_LNGLAT, zoom=16.5, height="650px")
m

m.move_marker("walker", CITY_HALL_LNGLAT, color="#ff0000")
m.move_marker("walker", (12.56835, 55.67615))
```

Practical note used in the workshop:

- Recoloring an existing marker is done by refresh:
  - `remove_marker(id)` then `add_marker(..., name=id, color=...)`

Compatibility note:

- `LiveMapLibreMap` patches the anymap-ts frontend bundle at runtime.
- If a new anymap-ts release changes the bundle shape, the patch falls back to
    `remove_marker(...)` + `add_marker(...)` for movement.
- You can check `m._move_marker_supported` to confirm the in-place method is active.


## MQTT / threading rule (important)

If coordinates come from MQTT:

- Do not call widget methods from an MQTT callback thread.
- Use: MQTT callback → queue → async consumer in the notebook → `move_marker(...)`.
