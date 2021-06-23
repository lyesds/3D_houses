import geopandas as gpd
import pandas as pd
from shapely.geometry import Point, Polygon

#reading bpn_cabu.shp file
shp_filename = '/home/becode/Downloads/3D_data/Belgium_L72_2020/Bpn_ReBu.shp'

#lambert points for an  sample addresses
lambert_x_1, lambert_y_1 = 103776.66, 192274.03
lambert_x_2, lambert_y_2 = 152458.45, 212084.91
lambert_x_3, lambert_y_3 = 69854.42, 211306.14

#match point with polygon
def polygon_from_point(filename : str, x_lambert, y_lambert) -> Polygon:
    """ Function to match a given lambert coordinates point of a address 
    with the polygons in the shape file."""

    #creating a point from x and y lamberts
    point = Point(x_lambert, y_lambert)

    #finding a match with the right polygon from the shape file
    match = gpd.read_file(shp_filename,  
                        mask = point, #only returning the desired polygon
                        ignore_fields=["Type","FiscSitId","UpdDate"],
                        )

    polygon = match.at[0,'geometry'] #returning the cell containing Polygon

    return polygon


