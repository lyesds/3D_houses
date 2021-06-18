import os
from osgeo import gdal
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

directory = 'data/DSM/GeoTIFF/'
df_corners = pd.DataFrame(columns=['id', 'ulx', 'urx', 'lrx', 'llx', 'uly', 'ury', 'lry', 'lly'])
for filename in os.listdir(directory):
    if filename.endswith(".tif"):
        # print(os.path.join(directory, filename))
        ds = gdal.Open(directory+filename)
        # print(ds.GetGeoTransform())

        ulx, xres, xskew, uly, yskew, yres = ds.GetGeoTransform()  # upper left corner X and Y, and their path

        lrx = ulx + (ds.RasterXSize * xres)  # lower right corner X
        lry = uly + (ds.RasterYSize * yres)  # lower right corner Y

        llx = ulx  # lower left corner X
        lly = lry  # lower left corner Y

        urx = lrx  # upper right corner X
        ury = uly  # upper right corner Y

        cx = (ulx + urx)/2  # center X
        cy = (uly + lly)/2  # upper Y

        plt.plot([ulx, urx, lrx, llx, ulx], [uly, ury, lry, lly, uly], label=filename[-6:-4])
        plt.text(llx, lly, filename[-6:-4], color='b')

        data = [filename[-6:-4], ulx, urx, lrx, llx, uly, ury, lry, lly]
        df_corners.loc[len(df_corners)] = data
    else:
        continue
plt.axis([0, 3e5, 1.25e5, 2.75e5])
plt.title('DSM GeoTiff files of Flanders in Belgium (Lambert72 coordinates)')
# plt.legend()
# plt.show()
plt.savefig("data/DSM/GeoTIFF/DSM_tif_files.png", transparent=True)

# print(df_corners.head(20))
# print(df_corners.info())


def locate(x: float, y: float) -> list:
    ls = []
    for i in range(df_corners.shape[0]):
        if x >= df_corners.iloc[i, 1] and x <= df_corners.iloc[i, 2]:
            ls.append(df_corners.iloc[i, 0])
        else:
            continue
    df_corners_sub = df_corners[df_corners['id'].isin(ls)]
    ls = []
    for j in range(df_corners_sub.shape[0]):
        if y >= df_corners_sub.iloc[j, 8] and y <= df_corners_sub.iloc[j, 5]:
            ls.append(df_corners_sub.iloc[j, 0])
        else:
            continue
    return ls

'''
print('DSM file number where x and y are located')
print(locate(x=152458.45, y=212084.91))  # Schoenmarkt 35, 2000 Antwerpen
# print(locate(x=150000, y=140000))  # should return empty list because outside Flanders
'''


from matplotlib import cm
from matplotlib.ticker import LinearLocator


p = 40  # number of pixels or meters north, south, east and west
def render_plot_around_xy(x: float, y: float):
    ds_DSM = gdal.Open(directory + 'DHMVIIDSMRAS1m_k' + locate(x,y)[0] + '.tif')
    xb = int(x) - int(ds_DSM.GetGeoTransform()[0])
    yb = int(ds_DSM.GetGeoTransform()[3]) - int(y)
    Z = ds_DSM.ReadAsArray()
    Z = Z[(yb - p):(yb + p), (xb - p):(xb + p)]

    X = np.arange(int(x) - p, int(x) + p, 1)  # grid p meters left, right of x
    Y = np.arange(int(y) - p, int(y) + p, 1)  # grid p meters under, above of y
    X, Y = np.meshgrid(X, Y)

    fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
    # Plot the surface.
    surf = ax.plot_surface(X, Y, Z, cmap=cm.viridis, linewidth=0, antialiased=False)

    # Demo 3: text2D
    # Placement 0, 0 would be the bottom left, 1, 1 would be the top right.
    ax.text2D(0, 0.95, "Schoenmarkt 35, 2000 Antwerpen", transform=ax.transAxes)

    # Tweaking display region and labels
    '''
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.set_zlim(0, 10)
    '''
    ax.set_xlabel('X Lambert72')
    ax.set_ylabel('Y Lambert72')
    ax.set_zlabel('Height(m)')

    plt.show()

render_plot_around_xy(x=152458.45, y=212084.91)
