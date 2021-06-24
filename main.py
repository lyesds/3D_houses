import os

import geopandas as gpd
from shapely.geometry.point import Point

from utils.apisearch_for_lambert import lambert_x_y
from utils.rendering import render_bbox, render_plot_around_xy, render_polygon

x, y = lambert_x_y("Kolkstraat 35, 9100 Sint-Niklaas")
# x, y = lambert_x_y("Groenplaats 21, 2000 Antwerpen")
# x, y = lambert_x_y("Schoenmarkt 35, 2000 Antwerpen")


folder_path = "/media/arnaud/0AE494D0E494BEFF/3d-house-data/Cadastral_data"
myFilesPaths = os.listdir(folder_path)
p = Point(x, y)
for filename in myFilesPaths:
    if filename.endswith(".shp"):
        if filename.endswith("Bpn_ReBu.shp"):
            filepath = folder_path + "/" + filename
            gdf = gpd.read_file(filepath, mask=p)
            geom = gdf["geometry"][0]

geotiff_path = "/media/arnaud/0AE494D0E494BEFF/3d-house-data/DHMVIIDSMRAS1m_k15.tif"
# # tif_number = locate("/media/arnaud/0AE494D0E494BEFF/3d-house-data/", x, y)[0]
render_plot_around_xy("/media/arnaud/0AE494D0E494BEFF/3d-house-data/", x, y)
render_bbox([(x - 40, y - 40), (x + 40, y + 40)], geotiff_path)
render_polygon(geom, geotiff_path)
