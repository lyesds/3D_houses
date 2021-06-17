import matplotlib.pyplot as plt
from osgeo import gdal
import numpy as np
import pandas as pd
from PIL import Image, ImageDraw
import numpy.ma as ma


def render_plot(geotiff_path):
    dem = gdal.Open(geotiff_path)
    gt = dem.GetGeoTransform()
    dem = dem.ReadAsArray()

    fig, ax = plt.subplots(figsize=(16, 8), subplot_kw={'projection': '3d'})

    xres = gt[1]
    yres = gt[5]

    X = np.arange(gt[0], gt[0] + dem.shape[1]*xres, xres)
    Y = np.arange(gt[3], gt[3] + dem.shape[0]*yres, yres)

    X, Y = np.meshgrid(X, Y)

    surf = ax.plot_surface(X, Y, dem, rstride=1, cstride=1, cmap=plt.cm.RdYlBu_r, vmin=(dem.min()), vmax=(dem.max()), linewidth=0, antialiased=True)

    difference = (dem.max() - dem.min())/10

    ax.set_zlim((dem.min()-difference), (dem.max()+difference))
    ax.view_init(60, -105)

    fig.colorbar(surf, shrink=0.4, aspect=20)

    plt.show()


# render_plot('data/DHMVIIDSMRAS1m_k29/split/tile_1.tif')
geotiff_path = '/media/arnaud/0AE494D0E494BEFF/3d-house-data/DHMVIIDSMRAS1m_k14.tif'
#render_plot(geotiff_path)
print(gdal.Info(geotiff_path))
dem = gdal.Open(geotiff_path)
gt = dem.GetGeoTransform()
dem = dem.ReadAsArray()
print(gt)

#coordinates are 123478.34282083988, 200777.0510268798

polygon = [(123458,200757),(123498,200757),(123498,200797),(123458,200797)]
polygon_df = pd.DataFrame(data=polygon)

print(polygon_df)

polygon_df[0] = polygon_df[0]-gt[0]
polygon_df[1] = -(polygon_df[1]-gt[3])
polygon_num = [[1,1],[6,1],[6,7],[1,7]]

test = dem[17203:17243:,25458:25498]#,]
print(np.shape(test))
# print(polygon_df)
# np.set_printoptions(threshold=np.inf)
# # polygon = [(1,1),(3,1),(3,2),(2,2),(2,4),(1,4)]
# print(np.shape(dem))
# num_rows, num_cols = np.shape(dem)
# img = Image.new('L', (num_cols, num_rows ), 1)
# ImageDraw.Draw(img).polygon(list(polygon_df.itertuples(index=False, name=None)), outline=0, fill=0)
# mask = np.array(img)
# print(mask)
# print(1)
# print(dem)
# mx = ma.masked_array(dem, mask=mask)
# print(mx)

# print(dem)
# print(mx)

# test = dem[0:20,0:20]

# plt.subplot(1, 2, 1)  # 2 rows, 2 columns, 1st subplot = top left
# plt.plot(mx)
# plt.subplot(1, 2, 2)  # 2 rows, 2 columns, 2nd subplot = top right
# plt.plot(test)
# plt.show()


# fig, ax = plt.subplots(figsize=(16, 8), subplot_kw={'projection': '3d'})

# xres = gt[1]
# yres = gt[5]

# X = np.arange(gt[0], gt[0] + mx.shape[1]*xres, xres)
# Y = np.arange(gt[3], gt[3] + mx.shape[0]*yres, yres)

# X, Y = np.meshgrid(X, Y)

# surf = ax.plot_surface(X, Y, mx, rstride=1, cstride=1, cmap=plt.cm.RdYlBu_r, vmin=(mx.min()), vmax=(mx.max()), linewidth=0, antialiased=True)

# difference = (mx.max() - mx.min())/10

# ax.set_zlim((mx.min()-difference), (mx.max()+difference))
# ax.view_init(60, -105)

# fig.colorbar(surf, shrink=0.4, aspect=20)

# plt.show()

# test = dem[1:6,1:7]
# print(test)


fig, ax = plt.subplots(figsize=(16, 8), subplot_kw={'projection': '3d'})

xres = gt[1]
yres = gt[5]

X = np.arange(gt[0], gt[0] + test.shape[1]*xres, xres)
Y = np.arange(gt[3], gt[3] + test.shape[0]*yres, yres)

X, Y = np.meshgrid(X, Y)

surf = ax.plot_surface(X, Y, test, rstride=1, cstride=1, cmap=plt.cm.RdYlBu_r, vmin=(test.min()), vmax=(test.max()), linewidth=0, antialiased=True)

difference = (test.max() - test.min())/10

ax.set_zlim((test.min()-difference), (test.max()+difference))
ax.view_init(60, -105)

fig.colorbar(surf, shrink=0.4, aspect=20)

plt.show()

# #print(np.shape(dem))
# print(mx)
# print(dem[0:6,0:6])

# x = np.array([1, 2, 3, -1, 5])
# mx = ma.masked_array(x, mask=[0, 0, 0, 1, 0])
# print(mx)