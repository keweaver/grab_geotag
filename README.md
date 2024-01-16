Reads .tif file information and locates nearest colony using coordinates. Adds latitude, longitude, coordinate distance, and nearest colony name to the annotated files. 

Input: 
--> colonies.csv: [name, latitude, longitude]
--> annotations.xlsx: [file_name, ...,]

Output: 
--> annotations_output.csv[file_name...,lat, long, distance, colony]

python run_tifs.py 

Or, given a directory of .tifs, creates a spreadsheet with the file name and closest colony location. 

Input: 
--> colonies.csv: [name, latitude, longitude]

Output: 
--> all_dir.csv[file_name...,lat, long, distance, colony]

python sort_folder.py
