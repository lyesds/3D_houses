import geopandas as gpd
import matplotlib.pyplot as plt
from osgeo import gdal
import rasterio
import numpy as np

tiny_tif = gdal.Open(r'/home/becode/Downloads/3D_data/DHMVIIDSMRAS1m_k28/GeoTIFF/DHMVIIDSMRAS1m_k28.tif')
#print(tiny_tif.RasterCount)

band1 = tiny_tif.GetRasterBand(1)

raster = rasterio.open('/home/becode/Downloads/3D_data/DHMVIIDSMRAS1m_k28/GeoTIFF/DHMVIIDSMRAS1m_k28.tif')
plt.show(raster.read(1))

'''
# create geospatial raster
rasterDs = gdal.Grid('../Rst/interpolatedElevations.tif', '../Shp/gwWells.shp', format='GTiff',
               algorithm='invdist', zfield='SurfaceEle')
rasterDs.FlushCache()'''

b1 = band1.ReadAsArray()

f = plt.figure()
plt.imshow(b1)
plt.savefig('Tiff.png')
#plt.show()