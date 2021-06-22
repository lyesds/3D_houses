#script
from osgeo import gdal
import matplotlib.pyplot as plt

import numpy as np

img = gdal.Open('/home/becode/Downloads/DHMVIIDSMRAS1m_k01/GeoTIFF/DHMVIIDSMRAS1m_k01.tif')

gs = img.GetGeoTransform()
projection = img.GetProjection()

rb = img.GetRasterBand(1)
array = rb.ReadAsArray()

binmask = np.where((array >= np.mean(array)), array, 0)


plt.figure()
plt.imshow(img)