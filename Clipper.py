import os
import geopandas as gpd
from rasterio.mask import mask
import rasterio
import matplotlib.pyplot as plt
from tkinter import Tk
from tkinter.filedialog import askopenfilename, askdirectory

filename1 = askopenfilename(title="Select a GeoJSON file")  # geojson file

# Show a "Select Folder" dialog box and return the path to the selected folder
folder_path = askdirectory(title="Select a folder containing TIFF files")

geojson = gpd.read_file(filename1)
geoms = geojson.geometry.values

# Get the GeoJSON file name without extension
geojson_name = os.path.splitext(os.path.basename(filename1))[0]

# Traverse the directory structure and process each TIFF file
for root, dirs, files in os.walk(folder_path):
    for file in files:
        if file.lower().endswith('.tif'):
            tiff_file_path = os.path.join(root, file)
            try:
                with rasterio.open(tiff_file_path) as src:  # tiff file
                    # Clip the tiff file using the geometry from the GeoJSON file
                    out_image, out_transform = mask(src, geoms, crop=True)

                    # Update metadata with new dimensions and transform
                    out_meta = src.meta.copy()
                    out_meta.update({"driver": "GTiff",
                                    "height": out_image.shape[1],
                                    "width": out_image.shape[2],
                                    "transform": out_transform})

                    # Save clipped tiff to disk with GeoJSON file name added
                    output_file = tiff_file_path + '_' + geojson_name + '_clipped.tif'
                    
                    with rasterio.open(output_file, 'w', **out_meta) as dest:
                        dest.write(out_image)
                    # print (output_file)
            except Exception as e:
                print(f"Error processing {tiff_file_path}: {e}")
