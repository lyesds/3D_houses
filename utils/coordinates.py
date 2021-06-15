from osgeo import gdal


def world_to_geotiff_coordinate():
    src = gdal.SpatialReference()
    src.SetWellKnownGeogCS("WGS84")
    # dataset = gdal.Open("path/to/my/file", gdalconstConstants.GA_ReadOnly)
    # projection = dataset.GetProjection()
    # SpatialReference dst = new SpatialReference(projection)
    # CoordinateTransformation ct = new CoordinateTransformation(src, dst)
    # double[] xy = ct.TransformPoint(lon, lat);

    # int x = (int)(((xy[0] - transform[0]) / transform[1]));
    # int y = (int)(((xy[1] - transform[3]) / transform[5]))
    return


def geotiff_to_world_coordinate():
    return
