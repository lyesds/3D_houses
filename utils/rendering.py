import matplotlib.pyplot as plt  # type: ignore
import numpy as np
import pandas as pd  # type: ignore
from osgeo import gdal  # type: ignore


def render_geotiff(geotiff_path):
    """Function to procces datas from a geotiff in order to render it in a 3d plot

    Args:
        geotiff_path ([type]): geotiff path file
    """
    dem = gdal.Open(geotiff_path)
    gt = dem.GetGeoTransform()
    dem = dem.ReadAsArray()

    xres = gt[1]
    yres = gt[5]

    x = np.arange(gt[0], gt[0] + dem.shape[1] * xres, xres)
    y = np.arange(gt[3], gt[3] + dem.shape[0] * yres, yres)

    x, y = np.meshgrid(x, y)

    render_plot(x, y, dem)


def render_bbox(bbox, geotiff_path):
    """Function that crop a geotiff file by using a bounding box
    coordinate in order to render it in a 3d plot later
    Args:
        bbox ([type]): a bounding box as an array of 2 tupples, 1st tupple is
        the coordinates of top left corner and second tupple is
        coordinates of lower right corner
        geotiff_path ([type]): [description]
    """
    dem = gdal.Open(geotiff_path)
    gt = dem.GetGeoTransform()
    dem = dem.ReadAsArray()
    polygon_df = pd.DataFrame(data=bbox)
    polygon_df[0] = polygon_df[0] - gt[0]
    polygon_df[1] = -(polygon_df[1] - gt[3])

    cropped_data = dem[
        int(polygon_df.iloc[1, 1]) : int(polygon_df.iloc[0, 1]),
        int(polygon_df.iloc[0, 0]) : int(polygon_df.iloc[1, 0]),
    ]

    xres = gt[1]
    yres = gt[5]

    x = np.arange(
        polygon_df.iloc[0, 0],
        polygon_df.iloc[0, 0] + cropped_data.shape[1] * xres,
        xres,
    )
    y = np.arange(
        polygon_df.iloc[0, 1],
        polygon_df.iloc[0, 1] + cropped_data.shape[0] * yres,
        yres,
    )

    x, y = np.meshgrid(x, y)

    render_plot(x, y, cropped_data)


def render_plot(x, y, z):
    """Function that create the 3d plot from datas

    Args:
        x ([type]): [description]
        y ([type]): [description]
        z ([type]): [description]
    """
    fig, ax = plt.subplots(figsize=(16, 8), subplot_kw={"projection": "3d"})

    surf = ax.plot_surface(
        x,
        y,
        z,
        rstride=1,
        cstride=1,
        cmap=plt.cm.RdYlBu_r,
        vmin=(z.min()),
        vmax=(z.max()),
        linewidth=0,
        antialiased=True,
    )

    difference = (z.max() - z.min()) / 10

    ax.set_zlim((z.min() - difference), (z.max() + difference))
    ax.view_init(60, -105)

    fig.colorbar(surf, shrink=0.4, aspect=20)

    plt.show()
