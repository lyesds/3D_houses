import os
from osgeo import gdal
import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime


def geotiff_viz_df(datapath: str, chart: bool = False):
    """
    Creating a global visualization of the area covered by each of the 43 GeoTIFF files
    and creating a data frame with the coordinates of the files corners.
    The data used are the DSM .tif files, which need to be all in the 'datapath' input parameter of the function.
    The outputs are the chart DSM_tif_files.png and the data frame df_corners.
    The optional (chart=True) parameter should be specified if ones wants the chart to be saved in assets/.
    """
    df_corners = pd.DataFrame(columns=['id', 'ulx', 'urx', 'lrx', 'llx', 'uly', 'ury', 'lry', 'lly'])
    for filename in os.listdir(datapath):
        if filename.endswith(".tif"):
            ds = gdal.Open(datapath + filename)

            ulx, xres, xskew, uly, yskew, yres = ds.GetGeoTransform()  # upper left corner X and Y, and their path

            lrx = ulx + (ds.RasterXSize * xres)  # lower right corner X
            lry = uly + (ds.RasterYSize * yres)  # lower right corner Y

            llx = ulx  # lower left corner X
            lly = lry  # lower left corner Y

            urx = lrx  # upper right corner X
            ury = uly  # upper right corner Y

            data = [filename[-6:-4], ulx, urx, lrx, llx, uly, ury, lry, lly]
            df_corners.loc[len(df_corners)] = data

            if chart is True:
                plt.plot([ulx, urx, lrx, llx, ulx], [uly, ury, lry, lly, uly], label=filename[-6:-4])
                plt.text(llx, lly, filename[-6:-4], color='b')
                plt.axis([0, 3e5, 1.25e5, 2.75e5])
                plt.title('DSM GeoTiff files of Flanders in Belgium (Lambert72 coordinates)')
        else:
            continue
    if chart is True:
        plt.savefig('assets/' + datetime.now().strftime("%Y%m%d_%I%M%S%p") + '_' + 'DSM_files.png', transparent=True)
    return df_corners


def locate(datapath: str, x: float, y: float) -> list:
    """
    Finds in which .tif file number the (x,y) coordinates are located.
    Returns a list with one or two element(s).
    If the coordinates are not inside one of the 43 tif (available) files, the list is empty.
    :param datapath: the folder where the DSM are located
    :param x: the Lambert72 x coordinate of the point of interest
    :param y: the Lambert72 y coordinate of the point of interest
    :return: a list containing the id number of the Geotiff (.tif) file
    """
    df_corners = geotiff_viz_df(datapath)
    ls = []
    for i in range(df_corners.shape[0]):
        if df_corners.iloc[i, 1] <= x <= df_corners.iloc[i, 2]:
            ls.append(df_corners.iloc[i, 0])
        else:
            continue
    df_corners_sub = df_corners[df_corners['id'].isin(ls)]
    ls = []
    for j in range(df_corners_sub.shape[0]):
        if df_corners_sub.iloc[j, 8] <= y <= df_corners_sub.iloc[j, 5]:
            ls.append(df_corners_sub.iloc[j, 0])
        else:
            continue
    return ls


# Example of use of this function:
# print(locate(datapath='data/DSM/GeoTIFF/', x=152458.45, y=212084.91)) #  <-- Lambert72 coordinates of this address:
                                                                            # Schoenmarkt 35, 2000 Antwerpen
