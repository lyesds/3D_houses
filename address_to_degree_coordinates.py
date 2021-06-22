#address_to_coordinates_in_degrees

## import libraries
import geopandas
import geopy

## function to return coordinates
def coords(given_address : str) -> tuple :

    ''' 
    Function to return WSG4 latitude and latitude of the 
    given address in degrees.
    '''

    locator = geopy.Nominatim(user_agent = 'myGeocoder')
    add  = locator.geocode(given_address)

    ## printing address to coords
    print("Latitude = {}, Longitude = {}".format(add.latitude, add.longitude))
    print("Altitude = {}".format(add.altitude))

    return (add.latitude, add.longitude)


