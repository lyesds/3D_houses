import requests
import geopandas as gpd
import pandas as pd
from shapely.geometry import Point, Polygon

#reading Bpn_CaPa_VLA.shp file from Belgium 72 lambert data
filename = '/home/becode/Downloads/3D_data/Belgium_L72_2020/Bpn_CaPa_VLA.shp'

#sample addresses
raw_data = ["Aaigemstraat 10, Gent",
            "Schoenmarkt 35, 2000 Antwerpen",
            "Steenstraat 75, Bruges 8000"]

address_1 = "Aaigemstraat 10, Gent"

# api-endpoint
URL = "https://loc.geopunt.be/v1/location?"

# function to find the lambert72 x,y for the centre of a given address
# to be used in MVP
def lambert_x_y (address_of_desired_place : str, URL : str) -> Point:
    """ A function to return lambert x and y coordinates for the centre of
    the desired place whose address is given by user. The coordinates are 
    returned in form of a Shapely Point"""

    # defining a params dict for the parameters to be sent to the API
    PARAMS = {'q':address_of_desired_place}
  
    # sending get request and saving the response as response object
    r = requests.get(url = URL, params = PARAMS)

    # extracting data in json format
    data = r.json()

    #Lambert72 i.e. Belgian system coordinates for a given address
    x_lambert = (data['LocationResult'][0]['Location']['X_Lambert72'])
    y_lambert = (data['LocationResult'][0]['Location']['Y_Lambert72'])  
    
    #converting x,y coordinates to a point
    point = Point(x_lambert, y_lambert)

    return point

#match point with polygon
def polygon_from_point(filename : str, point : Point) -> Polygon:
    """ Function to match a given lambert coordinates point of a address 
    with the polygons in the desired shape file."""

    match = gpd.read_file(filename,  
                        mask = point, #only returning the desired polygon
                        ignore_fields=["Type","FiscSitId","UpdDate"],
                        )

    polygon = match.iat[0,4] #returning the cell containing Polygon

    return polygon


# end of this part
