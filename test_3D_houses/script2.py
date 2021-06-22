import geopandas as gpd
from osgeo import gdal
import shapely
import descartes
import matplotlib.pyplot as plt

shape_data = gpd.read_file('/home/becode/Downloads/DHMVIIDTMRAS1m_k01/DHMVII_vdc_k01/DHMVII_vdc_k01.shp')
print(shape_data.shape)
print(shape_data.head(20))

shape_data.plot()
plt.show()

# Make a selection that contains only the first five rows
selection = shape_data[0:5]

# Iterate over rows and print the area of a Polygon
for index, row in selection.iterrows():
    # Get the area of the polygon
    poly_area = row['geometry'].area
    # Print information for the user
    print("Polygon area at index {index} is: {area:.3f}".format(index=index, area=poly_area))


# Create a new column called 'area' and assign the area of the Polygons into it
shape_data['area'] = shape_data.area

# Print first 2 rows of the area column
print(shape_data.head())


print(shape_data.crs)

import shapefile
import os

def shp2csv(shp_file):
    '''Outputs a csv file based on input shapefile vertices'''
    
    out = os.path.splitext(shp_file)[0]+'_pnts.csv'

    with open(out, 'w') as csv:
        with shapefile.Reader(shp_file) as sf:

            for shp_rec in sf.shapeRecords():
                csv.write('{}\n'.format(shp_rec.record))

                for pnt in shp_rec.shape.points:
                    csv.write('{}\n'.format(pnt))

f = '/home/becode/Downloads/DHMVIIDTMRAS1m_k01/DHMVII_vdc_k01/DHMVII_vdc_k01.shp'
shp2csv(f)