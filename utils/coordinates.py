from osgeo import gdal

# # img = geoio.GeoImage('data/DHMVIIDSMRAS1m_k29/split/tile_1.tif')
# # pix_x, pix_y = img.proj_to_raster( '50°54\'24.47\"N','3°10\'23.56\"E')
# # print(pix_x, + " " + pix_y)

# def world_to_geotiff_coordinate(tiff_path,longitude,latitude):
#     src = gdal.osr.SpatialReference()
#     src.SetWellKnownGeogCS("WGS84")
    
#     ds = gdal.Open(tiff_path)
    
#     projection = ds.GetProjection()
#     gt = ds.GetGeoTransform()
#     xs = ds.RasterXSize
#     ys = ds.RasterYSize
    
#     dst = gdal.osr.SpatialReference(projection)
#     ct = gdal.osr.CoordinateTransformation(src, dst)
#     #xy = ct.TransformPoint(longitude, latitude)
    
#     print(ct)
#     # x = (((xy[0] - transform[0]) / transform[1]))
#     # y = (((xy[1] - transform[3]) / transform[5]))
#     return


# def geotiff_to_world_coordinate():
#     return

# #world_to_geotiff_coordinate('data/DHMVIIDSMRAS1m_k29/split/tile_1.tif','3d10\'23.56"E','50d54\'24.47"N')
# #print(gdal.Info('data/DHMVIIDSMRAS1m_k29/split/tile_1.tif'))
# # gdal.GDALInfo('data/DHMVIIDSMRAS1m_k29/split/tile_1.tif')
# ds = gdal.Open('data/DHMVIIDSMRAS1m_k29/split/tile_1.tif')
    
# source = gdal.osr.SpatialReference()
# source.ImportFromWkt(ds.GetProjection())

# # The target projection
# target = gdal.osr.SpatialReference()
# target.ImportFromEPSG(4326)

# # Create the transform - this can be used repeatedly
# transform = gdal.osr.CoordinateTransformation(source, target)

# # Transform the point. You can also create an ogr geometry and use the more generic `point.Transform()`
# transform.TransformPoint('177975.000', '66050.000')


# Open tif file
ds = gdal.Open('data/DHMVIIDSMRAS1m_k29/split/tile_1.tif')

# GDAL affine transform parameters, According to gdal documentation xoff/yoff are image left corner, a/e are pixel wight/height and b/d is rotation and is zero if image is north up. 
xoff, a, b, yoff, d, e = ds.GetGeoTransform()

print(ds.GetGeoTransform())

def pixel2coord(x, y):
    """Returns global coordinates from pixel x, y coords"""
    print(f"a : {a} b : {b} d : {d} e : {e} a : {a} ")
    xp = a * x + b * y + xoff
    yp = d * x + e * y + yoff
    return(xp, yp)

print(pixel2coord(177975,  66050))

source = gdal.osr.SpatialReference()
source.ImportFromWkt(ds.GetProjection())
print(source.GetAttrValue("AUTHORITY", 1))
srs_4326 = gdal.osr.SpatialReference()
srs_4326.ImportFromEPSG(4326)

srs_3857 = gdal.osr.SpatialReference()
srs_3857.ImportFromEPSG(int(source.GetAttrValue("AUTHORITY", 1)))

ct_4326_to_3857 = gdal.osr.CoordinateTransformation(srs_3857, srs_4326)
ct_4326_to_3857 = gdal.osr.CoordinateTransformation(srs_4326, srs_3857)
lat = 50.90604339264458
lon = 3.175160806352825

# 3d10'23.56"E, 50d54'24.47"N

def dms_to_dd(d, m, s):
    dd = d + float(m)/60 + float(s)/3600
    return dd

mapx, mapy, z = ct_4326_to_3857.TransformPoint(lat, lon)

print(mapx,mapy,z)