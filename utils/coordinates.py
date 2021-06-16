from osgeo import gdal


def degree_coordinate_to_geotiff_coordinate(tiff_file, lat, lon):
    # Open tif file
    ds = gdal.Open(tiff_file)

    source = gdal.osr.SpatialReference()
    source.ImportFromEPSG(4326)

    target = gdal.osr.SpatialReference()
    target.ImportFromWkt(ds.GetProjection())
    print(int(target.GetAttrValue("AUTHORITY", 1)))
    print(gdal.Info(tiff_file))
    target.ImportFromEPSG(int(target.GetAttrValue("AUTHORITY", 1)))

    ct_4326_to_3857 = gdal.osr.CoordinateTransformation(source, target)
    mapx, mapy, z = ct_4326_to_3857.TransformPoint(lat, lon)
    print(mapx)
    print(mapy)
    return mapx, mapy


def dms_to_dd(d, m, s):
    dd = d + float(m)/60 + float(s)/3600
    return dd


#degree_coordinate_to_geotiff_coordinate('data/DHMVIIDSMRAS1m_k01/GeoTIFF/DHMVIIDSMRAS1m_k01.tif',51.533025,4.295441666666666)
