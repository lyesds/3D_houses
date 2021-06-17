import os
from osgeo import gdal
import matplotlib.pyplot as plt
import pandas as pd

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

        # print(ulx, uly)
        # print(llx, lly)
        # print(urx, ury)
        # print(lrx, lry)
        plt.plot([ulx, urx, lrx, llx, ulx], [uly, ury, lry, lly, uly], label=filename[-6:-4])
        plt.text(llx, lly, filename[-6:-4], color='b')

        # data = [[filename[-6:-4]], [ulx], [urx], [lrx], [llx], [uly], [ury], [lry], [lly]]
        # data = list(zip(filename[-6:-4], ulx, urx, lrx, llx, uly, ury, lry, lly))
        # df_corners = pd.DataFrame(data, columns=['id','ulx','urx','lrx','llx','uly','ury','lry','lly'])
        # df_corners = pd.Series(data)
    else:
        continue
plt.axis([0, 3e5, 1.25e5, 2.75e5])
plt.title('DSM GeoTiff files of Flanders in Belgium (Lambert72 coordinates)')
# plt.legend()
plt.show()

print(df_corners.head(20))
