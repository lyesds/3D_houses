from matplotlib.pyplot import ticklabel_format
from osgeo import gdal # Import GDAL library
tif = '/home/becode/Downloads/DHMVIIDSMRAS1m_k01/GeoTIFF/DHMVIIDSMRAS1m_k01.tif'
g = gdal.Open ( tif ) # Open the file
if g is None:
    print ("Could not open the file!")
geo_transform = g.GetGeoTransform ()
print (geo_transform)
print (g.RasterXSize, g.RasterYSize)
    