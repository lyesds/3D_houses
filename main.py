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
