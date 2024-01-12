import numpy as np
import pandas as pd
import os 
from osgeo import osr, gdal 
from read_tif import find_colony

colonies = pd.read_csv("./data/colonies.csv")
annotations = pd.read_excel("./data/annotations.xlsx")
colonies_col = pd.DataFrame(columns=['file_name', 'colony', 'distance', 'lat', 'lon'])

for file_name in annotations["file_name"]:
    try: 
        ds = gdal.Open(f"//vast.whoi.edu/proj/voltaire/mars/projects/emperors_satellite/pgc/imagery/{file_name}.tif")
        print(file_name, "success")
        colony, distance, latlong = find_colony(ds, colonies)
        cur = {"file_name": file_name, "colony": colony, "distance": distance, "lat": latlong[0], 'lon': latlong[1]}
        colonies_col = pd.concat([colonies_col, pd.DataFrame([cur])], ignore_index=True)
        print(colonies_col)
    except Exception as e: 
        print(f"File {file_name} not found. Skipping...")

annotations = annotations.merge(colonies_col, left_on="file_name", right_on="file_name")
print(annotations)
annotations.to_csv("./data/annotations_output.csv")
#"\\vast.whoi.edu\proj\voltaire\mars\projects\emperors_satellite\pgc\imagery"