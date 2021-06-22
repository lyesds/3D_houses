import geopandas as gpd
import pandas as pd
from shapely.geometry import Point
import requests

# api-endpoint
URL = "https://loc.geopunt.be/v1/location?"

# can give latitude and longitude also as attribute in function
# lat_in_deg, lon_in_deg = 
# PARAMS = {'lat':lat_in_deg, 'lon':lon_in_deg }

# function to find the lambert72 x,y for the centre of a given address
# to be used in MVP
def lambert_x_y (address_of_desired_place : str, URL : str) -> float:
    """ A function to return lambert x and y coordinates for the centre of
    the desired place whose address is given by user."""

    # defining a params dict for the parameters to be sent to the API
    PARAMS = {'q':address_of_desired_place}
  
    # sending get request and saving the response as response object
    r = requests.get(url = URL, params = PARAMS)

    # extracting data in json format
    data = r.json()
    #print(json.dumps(data, indent=3))

    #Lambert72 i.e. Belgian system coordinates for a given address
    x_lambert = (data['LocationResult'][0]['Location']['X_Lambert72'])
    y_lambert = (data['LocationResult'][0]['Location']['Y_Lambert72'])  
  
    return x_lambert, y_lambert

# function for bounding box
# additional, not for use in MVP
def lambert_bbox (address : str, URL : str) -> dict:
    """ Function to return coordinates of the bounding box,
    for a given address."""
    
    # defining a params dict for the parameters to be sent to the API
    PARAMS = {'q':address}
  
    # sending get request and saving the response as response object
    r = requests.get(url = URL, params = PARAMS)

    # extracting data in json format
    data = r.json()
    
    #Bounding Box is the smallest rectangle containing the locations geometry.
    #bounding box lower left
    bbox_lleft_x = data['LocationResult'][0]['BoundingBox']['LowerLeft']['X_Lambert72']
    bbox_lleft_y = data['LocationResult'][0]['BoundingBox']['LowerLeft']['Y_Lambert72']

    #bounding box upper right
    bbox_uright_x = data['LocationResult'][0]['BoundingBox']['UpperRight']['X_Lambert72']
    bbox_uright_y = data['LocationResult'][0]['BoundingBox']['UpperRight']['Y_Lambert72']

    #bounding box
    bbox = { 'ur_corner' : [bbox_uright_x,bbox_uright_y],
            'ul_corner' : [bbox_lleft_x,bbox_uright_y],
            'll_corner' : [bbox_lleft_x,bbox_lleft_y],
            'lr_corner' : [bbox_uright_x,bbox_lleft_y] }

    return bbox

# function for printing the results
# additional, not for use in MVP
def print_lamberts (address : str) -> None: 
    """ Function to print the lambert coordinates"""
    
    x_lambert, y_lambert = lambert_x_y(address)
    print(f"\nLambert72 coordinates \n(x,y) = ({x_lambert},{y_lambert}) \n ")

    print('Rectangle Bounding Box corners')
    bbox = lambert_bbox(address)    
    print(f"upper right : {bbox['ur_corner']}") 
    print(f"upper left : {bbox['ul_corner']}")
    print(f"lower left : {bbox['ll_corner']}")
    print(f"lower right : {bbox['lr_corner']} \n")

    return

# end of this part


#reading bpn_cabu.shp file
filename = '/home/becode/Downloads/3D_data/Belgium_L72_2020/Bpn_CaPa_VLA.shp'

#lambert points for an  sample addresses
lambert_1 = Point(103776.66, 192274.03)
lambert_2 = Point(152458.45, 212084.91)
lambert_3 = Point(69854.42, 211306.14)

raw_data = [
    ("Aaigemstraat 10, Gent", lambert_1),
    ("Schoenmarkt 35, 2000 Antwerpen", lambert_2),
    ("Steenstraat 75, Bruges 8000", lambert_3),
    ]

#making a data frame of addresses and corresponding points   
places = pd.DataFrame(raw_data, columns=["name", "geometry"])

#match point with polygon
def polygon_from_point(filename : str, point):
    match = gpd.read_file(filename,  
                        mask = point,
                        ignore_fields=["Type","FiscSitId","UpdDate"],
                        )

    return print(match.iloc[:,4])

polygon_from_point(filename, lambert_2)