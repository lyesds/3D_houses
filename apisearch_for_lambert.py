
# importing the requests library
from re import X
import requests
import json

URL_0 = "https://loc.geopunt.be/v1/location?"
URL = 'http://loc.geopunt.be/geolocation/location?'


# can give latitude and longitude also as attribute in function
# lat_in_deg, lon_in_deg = 
# PARAMS = {'lat':lat_in_deg, 'lon':lon_in_deg }

# function to find the lambert72 x,y for the centre of a given address
def lambert_x_y (house_address : str):
    # api-endpoint
    URL = "https://loc.geopunt.be/v3/location?"

    # defining a params dict for the parameters to be sent to the API
    PARAMS = {'q':house_address}
  
    # sending get request and saving the response as response object
    r = requests.get(url = URL, params = PARAMS)

    # extracting data in json format
    data = r.json()
    print(json.dumps(data, indent=3))

    #Lambert72 i.e. Belgian system coordinates for a given address
    x_lambert = (data['LocationResult'][0]['Location']['X_Lambert72'])
    y_lambert = (data['LocationResult'][0]['Location']['Y_Lambert72'])  
  
    return x_lambert, y_lambert

# function for bounding box
def lambert_bbox (address : str):
    
    # api-endpoint
    URL = "https://loc.geopunt.be/v3/location?"

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

    #print (bbox)
    return bbox


# function for printing the results
def print_lamberts (address : str):
    
    x_lambert, y_lambert = lambert_x_y(address)
    print(f"\nLambert72 coordinates \n(x,y) = ({x_lambert},{y_lambert}) \n ")

    print('Rectangle Bounding Box corners')
    bbox = lambert_bbox(address)    
    print(f"upper right : {bbox['ur_corner']}") 
    print(f"upper left : {bbox['ul_corner']}")
    print(f"lower left : {bbox['ll_corner']}")
    print(f"lower right : {bbox['lr_corner']} \n")
    return

# location given here EN or NL
location = "Aaigemstraat 10, Gent"

print(lambert_x_y(location))
# end of this part
