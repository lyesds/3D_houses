from osgeo import gdal  # type: ignore


def degree_coordinate_to_geotiff_coordinate(tiff_file, lat, lon):
    """[summary]

    Args:
        tiff_file ([type]): A geotiff file path, it's gonna get used
        to extract the format of coordinates we want as output
        lat ([type]): The latitude of the point we need to convert
        lon ([type]): The longitude of the point we need to convert

    Returns:
        [type]: the converted lat and lon
    """
    # Open tif file
    ds = gdal.Open(tiff_file)

    source = gdal.osr.SpatialReference()
    source.ImportFromEPSG(4326)

    target = gdal.osr.SpatialReference()
    target.ImportFromWkt(ds.GetProjection())

    target.ImportFromEPSG(int(target.GetAttrValue("AUTHORITY", 1)))

    ct_4326_to_3857 = gdal.osr.CoordinateTransformation(source, target)
    mapx, mapy, z = ct_4326_to_3857.TransformPoint(lat, lon)

    return mapx, mapy


def convert_degree_minutes_seconds_to_degree(d, m, s):
    """Convert from dms to degrees so that we can use the coordinates
    in the degree_coordinate_to_geotiff_coordinate function

    Args:
        d ([type]): Degree
        m ([type]): Minute
        s ([type]): Seconds

    Returns:
        [type]: the coordinate in degree format
    """
    dd = d + float(m) / 60 + float(s) / 3600
    return dd
