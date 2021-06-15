import matplotlib.pyplot as plt
from osgeo import gdal
import numpy as np


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
