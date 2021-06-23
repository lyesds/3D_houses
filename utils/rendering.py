import matplotlib.pyplot as plt  # type: ignore
import numpy as np
import numpy.ma as ma
import pandas as pd  # type: ignore
from matplotlib import cm
from osgeo import gdal  # type: ignore
from PIL import Image, ImageDraw

from utils.geotiff_df_locate_3Dplot import locate


def render_geotiff(geotiff_path):
    """Function to procces datas from a geotiff in order to render it in a 3d plot

    Args:
        geotiff_path (str): geotiff path file
    """
    dem = gdal.Open(geotiff_path)
    gt = dem.GetGeoTransform()
    dem = dem.ReadAsArray()

    # Creating a x and y grid with all the x and y coordinates
    xres = gt[1]
    yres = gt[5]

    x = np.arange(gt[0], gt[0] + dem.shape[1] * xres, xres)
    y = np.arange(gt[3], gt[3] + dem.shape[0] * yres, yres)

    x, y = np.meshgrid(x, y)

    render_plot(x, y, dem)


def render_bbox(bounding_box, geotiff_path):
    """Function that crop a geotiff file by using a bounding box
    coordinate in order to render it in a 3d plot later
    Args:
        bbox ([type]): a bounding box as an array of 2 tupples, 1st tupple is
        the coordinates of one of the corners and second tupple is
        coordinates of the opposite corner
        geotiff_path ([type]): [description]
    """

    # Initialize the datas
    dem = gdal.Open(geotiff_path)
    gt = dem.GetGeoTransform()

    # Cropping the original datas to just the ones contained inside the bounding box
    bounding_box_df = pd.DataFrame(data=bounding_box)
    bounding_box_df[0] = bounding_box_df[0] - gt[0]
    bounding_box_df[1] = gt[3] - bounding_box_df[1]

    bounding_box_df_x = [
        int(bounding_box_df.iloc[0, 0]),
        int(bounding_box_df.iloc[1, 0]),
    ]
    bounding_box_df_y = [
        int(bounding_box_df.iloc[1, 1]),
        int(bounding_box_df.iloc[0, 1]),
    ]

    xsize = int(max(bounding_box_df_x) - min(bounding_box_df_x))
    ysize = int(max(bounding_box_df_y) - min(bounding_box_df_y))

    dem = dem.ReadAsArray(xoff=int(min(bounding_box_df_x)), yoff=int(min(bounding_box_df_y)), xsize=xsize, ysize=ysize)

    # Creating a x and y grid with all the x and y coordinates

    x = np.arange(int(min(bounding_box_df_x) + gt[0]), int(max(bounding_box_df_x) + gt[0]), 1)
    y = np.arange(int(gt[3] - min(bounding_box_df_y)), int(gt[3] - max(bounding_box_df_y)), -1)
    x, y = np.meshgrid(x, y)

    # Rendering the plot
    render_plot(x, y, dem)


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
        cmap=cm.viridis,
        vmin=(z.min()),
        vmax=(z.max()),
        linewidth=0,
        antialiased=True,
    )

    difference = (z.max() - z.min()) / 10

    ax.set_zlim((z.min() - difference), (z.max() + difference))
    plt.ticklabel_format(useOffset=False)

    # Tweaking display region and labels
    ax.set_xlabel("X Lambert72")
    ax.set_ylabel("Y Lambert72")
    ax.set_zlabel("Height(m)")

    fig.colorbar(surf, shrink=0.4, aspect=20)

    plt.show()


def render_plot_around_xy(datapath: str, x: float, y: float, p: int = 40):
    """
    A simple matplotlib 3D plot of GeoTIFF data p meters north, south, east and west of the input Lambert72 x and y
    coordinates.
    :param datapath: the folder where the DSM and DTM are located
    :param x: the Lambert72 x coordinate of the point of interest
    :param y: the Lambert72 y coordinate of the point of interest
    :param p: the number of pixels or meters north, south, east and west away from (x,y) point. Default is 40.
    :return: a matplotlib chart shown
    """
    ds_DSM = gdal.Open(datapath + "DHMVIIDSMRAS1m_k" + locate(datapath, x, y)[0] + ".tif")  # DSM data, surface
    ds_DTM = gdal.Open(datapath + "DHMVIIDTMRAS1m_k" + locate(datapath, x, y)[0] + ".tif")  # DTM data, terrain
    xb = int(x) - int(ds_DSM.GetGeoTransform()[0])
    yb = int(ds_DSM.GetGeoTransform()[3]) - int(y)
    Z = ds_DSM.ReadAsArray(xsize=2 * p, xoff=xb - p, ysize=2 * p, yoff=yb - p) - ds_DTM.ReadAsArray(
        xsize=2 * p, xoff=xb - p, ysize=2 * p, yoff=yb - p
    )
    # Z is the height of the construction, difference between DSM and DTM

    X = np.arange(int(x) - p, int(x) + p, 1)  # grid p meters left, right of x
    Y = np.arange(int(y) - p, int(y) + p, 1)  # grid p meters under, above of y
    X, Y = np.meshgrid(X, Y)

    render_plot(X, Y, Z)


# Example of use of this function:
# render_plot_around_xy(datapath='data/DSM/GeoTIFF/', x=152458.45, y=212084.91, p=45)


def render_polygon(polygon, geotiff_path):
    """Function that crop a geotiff file by using a bounding box
    coordinate in order to render it in a 3d plot later
    Args:
        bbox ([type]): a bounding box as an array of 2 tupples, 1st tupple is
        the coordinates of one of the corners and second tupple is
        coordinates of the opposite corner
        geotiff_path ([type]): [description]
    """

    x_list, y_list = polygon.exterior.coords.xy
    polygon_coordinates = list(zip([x - polygon.bounds[0] for x in x_list], [(y - polygon.bounds[1]) for y in y_list]))
    bounding_box = [
        (polygon.bounds[0], polygon.bounds[1]),
        (polygon.bounds[2], polygon.bounds[3]),
    ]

    # Initialize the datas
    z = gdal.Open(geotiff_path)
    gt = z.GetGeoTransform()

    # Cropping the original datas to just the ones contained inside the bounding box
    bounding_box_df = pd.DataFrame(data=bounding_box)
    bounding_box_df[0] = bounding_box_df[0] - gt[0]
    bounding_box_df[1] = gt[3] - bounding_box_df[1]

    bounding_box_df_x = [
        int(bounding_box_df.iloc[0, 0]),
        int(bounding_box_df.iloc[1, 0]),
    ]
    bounding_box_df_y = [
        int(bounding_box_df.iloc[1, 1]),
        int(bounding_box_df.iloc[0, 1]),
    ]

    xsize = int(max(bounding_box_df_x) - min(bounding_box_df_x))
    ysize = int(max(bounding_box_df_y) - min(bounding_box_df_y))

    z = z.ReadAsArray(xoff=int(min(bounding_box_df_x)), yoff=int(min(bounding_box_df_y)), xsize=xsize, ysize=ysize)
    img = Image.new("L", (z.shape[1], z.shape[0]), 1)
    ImageDraw.Draw(img).polygon(polygon_coordinates, outline=0, fill=0)
    masked_array = np.array(img)
    np.set_printoptions(threshold=np.inf)
    mx = ma.masked_array(z, mask=masked_array)

    # Creating a x and y grid with all the x and y coordinates

    x = np.arange(int(min(bounding_box_df_x) + gt[0]), int(max(bounding_box_df_x) + gt[0]), 1)
    y = np.arange(int(gt[3] - min(bounding_box_df_y)), int(gt[3] - max(bounding_box_df_y)), -1)
    x, y = np.meshgrid(x, y)

    # Rendering the plot
    render_plot(x, y, z)
