#address_to_coordinates_in_degrees

## import libraries
import geopandas
import geopyls

## defining locator and giving the address
## we use Nominatim Geocoding service, which is built on top of OpenStreetMap data
locator = geopy.Nominatim(user_agent = 'myGeocoder')
address = locator.geocode("Mount Everest, Nepal")

## address to coords
print("Latitude = {}, Longitude = {}".format(address.latitude, address.longitude))
print("Altitude = {}".format(address.altitude))

## as a function
def coords(given_address):
    add  = locator.geocode(given_address)
    return (add.latitude, add.longitude)

##testing the function
print(coords('Atomium, Brussels'))
