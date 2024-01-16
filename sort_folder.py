import numpy as np
import pandas as pd
import os 
from osgeo import osr, gdal 
from read_tif import find_colony
"""
given a directory with .tif files, generates a spreadsheet with .tif 
filenames and the nearest colony to each 
run using: 
python sort_folder.py
"""
colonies = pd.read_csv("./data/colonies.csv")
#grab all directory 
path = "//vast.whoi.edu/proj/voltaire/mars/projects/emperors_satellite/pgc/imagery/"
dir_list = os.listdir(path)
dir_list = [file for file in dir_list if file.endswith('.tif')]
colonies_col = pd.DataFrame(columns=['file_name', 'colony', 'distance', 'lat', 'lon'])

for file_name in dir_list: 
    ds = gdal.Open(f"//vast.whoi.edu/proj/voltaire/mars/projects/emperors_satellite/pgc/imagery/{file_name}")
    print(file_name, "success")
    colony, distance, latlong = find_colony(ds, colonies)
    cur = {"file_name": file_name, "colony": colony, "distance": distance, "lat": latlong[0], 'lon': latlong[1]}
    colonies_col = pd.concat([colonies_col, pd.DataFrame([cur])], ignore_index=True)
    print(colonies_col)

colonies_col.to_csv("./data/all_dir.csv")
print("success!")
print("""          . .
                    '.-:-.`
                    '  :  `
                 .-----:
               .'       `.
         ,    /       (o) \
     jgs \`._/          ,__)
     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~""")