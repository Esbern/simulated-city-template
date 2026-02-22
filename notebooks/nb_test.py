# %%
msg = "Hello World"
print(msg)

# %%
from anymap_ts import Map

# %%
lat, lng = 55.6761, 12.5683
m = Map(center=(lng,lat ), zoom=18)
m.add_marker(lng,lat, popup=f"WGS84 (lat, lon): {lat:.6f}, {lng:.6f}")
m
# %%
