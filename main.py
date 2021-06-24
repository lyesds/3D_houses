from utils.apisearch_for_lambert import lambert_x_y
from utils.geotiff_df_locate_3Dplot import locate
from utils.matching_polygon import polygon_from_point
from utils.rendering import render_polygon

# test datas
x, y = lambert_x_y("Kolkstraat 35, 9100 Sint-Niklaas")
# x, y = lambert_x_y("Groenplaats 21, 2000 Antwerpen")
# x, y = lambert_x_y("Schoenmarkt 35, 2000 Antwerpen")
# x, y = lambert_x_y("Heyerstraat 22b, 9160 Lokeren")

folder_path = "assets/data/"

# Searching in the ReBu file for the polygon
cadastral_path = folder_path + "cadastral/Bpn_ReBu.shp"
polygon = polygon_from_point(cadastral_path, x, y)

# if the address was not in ReBu, search in CaBu
if polygon is None:
    cadastral_path = folder_path + "cadastral/Bpn_CaBu.shp"
    polygon = polygon_from_point(cadastral_path, x, y)

geotif_folder = folder_path + "DSM/"

# Rendering the polygon
geotiff_path = geotif_folder + "DHMVIIDSMRAS1m_k" + locate(geotif_folder, x, y)[0] + ".tif"
render_polygon(polygon, geotiff_path)
