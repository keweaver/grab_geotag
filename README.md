Reads .tif file information and locates nearest colony using coordinates. Adds latitude, longitude, coordinate distance, and nearest colony name to the annotated files. 

Input: 
--> colonies.csv: [name, latitude, longitude]
--> annotations.xlsx: [file_name, ...,]

Output: 
--> annotations_output.csv[file_name...,lat, long, distance, colony]
