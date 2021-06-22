# slicing the geotiff

import os
from osgeo import gdal

cpt=0
for x in range(28,29):
    if x < 10:
        tile = f"0{x}"
    else :
        tile = str(x)
    print(f"Getting map n°{tile}, total tiles : {cpt}")   
    in_path = "/home/becode/Downloads/3D_data/DHMVIIDSMRAS1m_k"+tile+"/GeoTIFF/"
    input_filename = "DHMVIIDSMRAS1m_k"+tile+".tif"
    smaller_tif = '/home/becode/Downloads/3D_data/DSM_DTM_splits/DHMVIIDSMRAS1m_k'+tile+'tile_272.tif'

    out_path = "/home/becode/Downloads/3D_data/even_smaller_tifs/DHMVIIDSMRAS1m_k"+tile+'tile_272'
    output_filename = "tile_"

    tile_size_x = 200
    tile_size_y = 100

    ds = gdal.Open(smaller_tif)
    band = ds.GetRasterBand(1)
    xsize = band.XSize
    ysize = band.YSize
    print(xsize, ysize)
    for i in range(0, xsize, tile_size_x):
        for j in range(0, ysize, tile_size_y):
            cpt+=1
            com_string = "gdal_translate -of GTIFF -srcwin "+str(i)+", "+str(j)+", "+str(tile_size_x)+", "+str(tile_size_y)+" "+str(in_path)+str(input_filename)+" "+str(out_path)+str(output_filename)+str(cpt)+".tif"
            os.system(com_string)
