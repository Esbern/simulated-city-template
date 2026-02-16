import pytest


def test_webmercator_utm32_roundtrip() -> None:
    pyproj = pytest.importorskip("pyproj")
    assert pyproj  # keep linters happy

    from simulated_city.geo import (
        EPSG_25832,
        EPSG_3857,
        transform_xy,
    )

    # A plausible Web Mercator point (meters), not too close to the poles.
    x0, y0 = 1_000_000.0, 7_000_000.0

    e, n = transform_xy(x0, y0, from_crs=EPSG_3857, to_crs=EPSG_25832)
    x1, y1 = transform_xy(e, n, from_crs=EPSG_25832, to_crs=EPSG_3857)

    assert x1 == pytest.approx(x0, abs=1e-6)
    assert y1 == pytest.approx(y0, abs=1e-6)
