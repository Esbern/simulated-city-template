# Data Directory

This directory is for storing data files used in your simulations.

## Recommended Structure

```
data/
├── raw/           # Original, unmodified data
├── processed/     # Cleaned and processed data
└── outputs/       # Simulation results and outputs
```

## Common Data Types

- **GeoJSON**: Geographic data for maps and spatial analysis
- **CSV**: Tabular data for statistics and analysis
- **Shapefiles**: Geographic data in shapefile format
- **Raster files**: TIF/GeoTIFF for elevation, satellite imagery, etc.

## Data Sources

Some useful sources for urban data:

- **OpenStreetMap**: Free geographic data ([overpass-turbo.eu](https://overpass-turbo.eu/))
- **Danish Open Data**: [datafordeler.dk](https://datafordeler.dk/)
- **Natural Earth**: Free vector and raster map data ([naturalearthdata.com](https://www.naturalearthdata.com/))
- **USGS**: US Geological Survey data ([usgs.gov](https://www.usgs.gov/))

## Note

Large data files should not be committed to git. Add them to `.gitignore` if they exceed a few MB.
