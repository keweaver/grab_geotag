from osgeo import osr, gdal 
from grab_coords import grab_coords
import numpy as np 
import pandas as pd 

"""
find nearest colony to given coords
"""
def find_colony(ds, colonies):
    """finds the nearest colony to the current .tif file. 
    """
    lats = colonies["Latitude"].to_numpy().astype(float)
    lons = colonies["Longitude"].to_numpy().astype(float)
    latlons = np.array(list(zip(lats, lons)))
    latlong = grab_coords(ds)
    target = np.array((latlong[0], latlong[1]))
    distances = np.linalg.norm(latlons-target, axis=1)
    min_index = np.argmin(distances)
    closest_coord = latlons[min_index]
    colony = colonies.loc[(colonies.Latitude == closest_coord[0]) & (colonies.Longitude == closest_coord[1])]
    colony = colony.reset_index().iloc[0]["Name"]
    return colony, distances[min_index], latlong