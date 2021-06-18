#import libraries
import geopandas as gpd
import os.path
import matplotlib.pyplot as plt

#reading bpn_cabu.shp file
filename = '/home/becode/Downloads/3D_data/Belgium_L72_2020/Bpn_CaBu.shp'

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


small_shape(40000, 4)

#loop to divide main cabu into 100 parts and save 
def hunderedth_of_main_shp():
    for i in range(1, 101):
        out_path = "/home/becode/Downloads/3D_data/small_cabus/smaller_cabu_"
        small = small_shape(40000, i)
        com_string = str(out_path)+str(i)
        small.to_file(com_string + '.shp')

#hunderedth_of_main_shp()
'''Call if you want to divide a cabu/rebu and save to system'''

    
         




