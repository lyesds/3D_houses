#import libraries
import geopandas as gpd
from numpy import add
import pandas as pd
import os.path
import matplotlib.pyplot as plt
from shapely.geometry import Point, Polygon, point

#reading bpn_cabu.shp file
filename = '/home/becode/Downloads/3D_data/Belgium_L72_2020/Bpn_CaPa_VLA.shp'

gdf = gpd.read_file(filename,  
                    ignore_fields=["Type","FiscSitId","UpdDate"],
                    )

def small_shape( m: str, n: str ):
    '''Divides the bigger cabu file to n chunks each of m rows'''
    '''Takes in a number m, returns the shape data with m rows from bigger cabu shape file'''
    '''Takes in a number n, returns the shape data from chunk number n of bigger cabu shape file'''

    filename = '/home/becode/Downloads/3D_data/Belgium_L72_2020/Bpn_CaBu.shp'

    chunk_size  = m
    chunk_number = n
    start = chunk_size * (chunk_number-1)
    end = chunk_size * chunk_number
        
    gdf = gpd.read_file(filename,  
                        rows= slice(start, end),
                        ignore_fields=["Type","FiscSitId","UpdDate"],
                        )
    
    #gdf.plot(facecolor='gray')
    #plt.tight_layout()
    return gdf


#small_shape(40000, 4)

#loop to divide main cabu into 100 parts and save 
def hunderedth_of_main_shp():
    for i in range(1, 101):
        out_path = "/home/becode/Downloads/3D_data/small_cabus/smaller_cabu_"
        small = small_shape(40000, i)
        com_string = str(out_path)+str(i)
        small.to_file(com_string + '.shp')

#hunderedth_of_main_shp()
'''Call if you want to divide a cabu/rebu and save to system'''

#locating the polygon for a given lambert point

#lambert point for an address
lambert_1 = Point(103776.66, 192274.03)
lambert_2 = Point(152458.45, 212084.91)
lambert_3 = Point(69854.42, 211306.14)

raw_data = [
    ("Aaigemstraat 10, Gent", lambert_1),
    ("Schoenmarkt 35, 2000 Antwerpen", lambert_2),
    ("Steenstraat 75, Bruges 8000", lambert_3),
]
places = pd.DataFrame(raw_data, columns=["name", "geometry"])

# Create the geometry column from the coordinates
# Remember that longitude is east-west (i.e. X) and latitude is north-south (i.e. Y)

#match point with polygon
match = gpd.read_file(filename,  
                        mask = lambert_2,
                        ignore_fields=["Type","FiscSitId","UpdDate"],
                        )

print(match)


fn = '/home/becode/Downloads/3D_data/small_cabus/smaller_cabu_52.shp'

gdf_50 = gpd.read_file(fn,
                    ignore_fields=["Type","FiscSitId","UpdDate"],
                    )
                    
gdf_50 = gdf_50.to_crs(31370)

# Convert to a GeoDataFrame
places = gpd.GeoDataFrame(places, geometry="geometry",crs=31370 )
'''
# Perform the spatial join
result = gpd.sjoin(places, gdf_50, how="inner", op = 'within')
print(result)

# Perform the clip
result = gpd.clip(places, gdf)

# Print the results...
print(result)'''




         




