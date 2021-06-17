from osgeo import gdal # Import GDAL library
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image, ImageDraw
import numpy.ma as ma

# polygon = [(x1,y1),(x2,y2),...] or [x1,y1,x2,y2,...]
# width = ?
# height = ?

file = 'data/DHMVIIDSMRAS1m_k29/split/tile_1.tif'
dem = gdal.Open(file)
#gt  = dem.GetGeoTransform()
dem = dem.ReadAsArray()

# print(gdal.Info(file))

# pixel_x = (82000 - gt[0])/gt[1]

# pixel_y = (168000 - gt[3])/gt[5]
# print(pixel_x, pixel_y)
# plt.plot ( pixel_x, pixel_y, 'ro')
# plt.annotate('test', xy=(pixel_x, pixel_y),  \
#         xycoords='data', xytext=(-150, -60), \
#         textcoords='offset points',  size=12, \
#         bbox=dict(boxstyle="round4,pad=.5", fc="0.8"), \
#         arrowprops=dict(arrowstyle="->", \
#         connectionstyle="angle,angleA=0,angleB=-90,rad=10", \
#         color='w'), )

# plt.imshow(dem )

# plt.show()
