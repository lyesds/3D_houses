
# importing the requests library
import requests
import json
  
# api-endpoint
URL = "http://loc.geopunt.be/v1/location?"

# location given here EN or NL
street_location = "Avenue Henry Dunant, Evere"
number = 50

# can give latitude and longitude also
# lat_in_deg, lon_in_deg = 
# PARAMS = {'lat':lat_in_deg, 'lon':lon_in_deg }
  
# defining a params dict for the parameters to be sent to the API
PARAMS = {'q':street_location, 'c':number }
  
# sending get request and saving the response as response object
r = requests.get(url = URL, params = PARAMS)
  
# extracting data in json format
data = r.json()

#Lambert72 i.e. Belgian system coordinates for a given address
x_lambert = (data['LocationResult'][0]['Location']['X_Lambert72'])
y_lambert = (data['LocationResult'][0]['Location']['Y_Lambert72'])  

#Bounding Box is the smallest rectangle containing the locations geometry.
#bounding box lower left
bbox_lleft_x = data['LocationResult'][0]['BoundingBox']['LowerLeft']['X_Lambert72']
bbox_lleft_y = data['LocationResult'][0]['BoundingBox']['LowerLeft']['Y_Lambert72']

#bounding box upper right
bbox_uright_x = data['LocationResult'][0]['BoundingBox']['UpperRight']['X_Lambert72']
bbox_uright_y = data['LocationResult'][0]['BoundingBox']['UpperRight']['Y_Lambert72']

# printing the results
print(f"\nLambert72 coordinates \n(x,y) = ({x_lambert},{y_lambert}) \n ")

print('Rectangle Bounding Box corners')
print(f"upper right : ({bbox_uright_x},{bbox_uright_y})") 
print(f"upper left : ({bbox_lleft_x},{bbox_uright_y})")
print(f"lower left : ({bbox_lleft_x},{bbox_lleft_y})")
print(f"lower right : ({bbox_uright_x},{bbox_lleft_y}) \n")

# end of this part