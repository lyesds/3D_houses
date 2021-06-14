# import os
# import matplotlib.pyplot as plt
# import geopandas as gpd

# #gdf = gpd.read_file("data/DHMVIIDSMRAS1m_k01/DHMVII_vdc_k01.zip")
# zipfile = "data/DHMVIIDSMRAS1m_k01/DHMVII_vdc_k01.zip"
# gdf = gpd.read_file(zipfile)

# gdf.plot()
# plt.show() 

from osgeo import gdal
import matplotlib.pyplot as plt
dataset = gdal.Open('data/DHMVIIDSMRAS1m_k01/GeoTIFF/DSM_split/tile_229.tif', gdal.GA_ReadOnly) 
# Note GetRasterBand() takes band no. starting from 1 not 0
band = dataset.GetRasterBand(1)
arr = band.ReadAsArray()
plt.imshow(arr)
plt.show()