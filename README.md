# GeoJson-Tiff-Clipper

This simple application uses GeoPandas and Rasterio to clip a GeoTiff file using a GeoJson file. The file takes a single geojson file and a directory (multiple) of GeoTiff files and clips them using the geojson file. The output is a directory of clipped GeoTiff files with the word _clipped appended to the file name.


# How to run

1. If you do not have Python installed, download it from [here](https://www.python.org/downloads/).
2. Download or clone this repo.
3. Run the command `pip install -r requirements.txt` inside the directory to install the required packages.
4. Run the command `python3 Clipper.py` to run the application.
5. First select the GeoJson file you want to convert.
6. In the next dialog select the directory containing the GeoTiff files you want to clip.

# License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE](LICENSE) file for details.
