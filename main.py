from utils.apisearch_for_lambert import lambert_x_y
from utils.geotiff_df_locate_3Dplot import locate
from utils.matching_polygon import polygon_from_point
from utils.rendering import render_polygon


def render_address_in_3d(address, use_polygon_bounding_box=False):

    x, y = lambert_x_y(address)

    folder_path = "assets/data/"
    folder_path = "/media/arnaud/0AE494D0E494BEFF/3d-house-data/"

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
    render_polygon(polygon, geotiff_path, use_polygon_bounding_box)


# test datas
# x, y = lambert_x_y("Kolkstraat 35, 9100 Sint-Niklaas")
# x, y = lambert_x_y("Groenplaats 21, 2000 Antwerpen")
# x, y = lambert_x_y("Schoenmarkt 35, 2000 Antwerpen")
# x, y = lambert_x_y("Heyerstraat 22b, 9160 Lokeren")
render_address_in_3d("Schoenmarkt 35, 2000 Antwerpen", True)
render_address_in_3d("Schoenmarkt 35, 2000 Antwerpen")
