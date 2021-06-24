<<<<<<< HEAD
from utils.geotiff_df_locate_3Dplot import locate

from utils.apisearch_for_lambert import lambert_x_y
from utils.rendering import render_polygon
from utils.matching_polygon import polygon_from_point

x, y = lambert_x_y("Kolkstraat 35, 9100 Sint-Niklaas")
# x, y = lambert_x_y("Groenplaats 21, 2000 Antwerpen")
# x, y = lambert_x_y("Schoenmarkt 35, 2000 Antwerpen")


folder_path = "assets/data/"

cadastral_path = folder_path + "cadastral/Bpn_ReBu.shp"
polygon = polygon_from_point(cadastral_path, x, y)

geotif_folder = folder_path + "DSM/"

geotiff_path = geotif_folder + "DHMVIIDSMRAS1m_k" + locate(geotif_folder, x, y)[0] + ".tif"
render_polygon(polygon, geotiff_path)
=======
import os

import geopandas as gpd
from shapely.geometry.point import Point

from utils.apisearch_for_lambert import lambert_x_y
from utils.rendering import render_bbox, render_plot_around_xy, render_polygon

x, y = lambert_x_y("Kolkstraat 35, 9100 Sint-Niklaas")
# x, y = lambert_x_y("Groenplaats 21, 2000 Antwerpen")
x, y = lambert_x_y("Schoenmarkt 35, 2000 Antwerpen")


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
render_polygon(geom, geotiff_path)
>>>>>>> d91b29b5b219203c4c4d8249cef9c1026627cf72
