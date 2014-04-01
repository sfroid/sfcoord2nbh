__author__ = 'sfroid / nagarajan'
__license__ = "Completely free to use, modify and\
distribute. Do whatever you want to!!"


import os
import fiona
import pyproj
from shapely import geometry


shapeSets = {
    'sffind': ("sffind_neighborhoods/SFFind_Neighborhoods.shp",
               "name"),
    'realtor': ("Realtor_Neighborhoods/Realtor_Neighborhoods.shp",
                "nbrhood"),
    'planning': ("planning_neighborhoods/planning_neighborhoods.shp",
                 "neighborho")}


def getSFNeighNames(locs, shapes=None, projection=None):
    """
    Given an array of lon, lat tuples [(lon, lat), (lon, lat)...]
    we return the neighborhood name in SF
    """
    if projection is None:
        projection = defProjection

    if shapes is None:
        shapes = shapeData

    places = []

    for locx, locy in locs:
        locx, locy = projection(locx, locy)

        point = geometry.Point(locx, locy)

        for shape, bbox, place in shapes:
            # first, check if inside bounding box
            if locx < bbox[0] or locx > bbox[2]:
                continue

            if locy < bbox[1] or locy > bbox[3]:
                continue

            # Alternative method (but slower)
            # if point.within(shape):
            if shape.contains(point):
                places.append(place)
                break
        else:
            places.append(None)

    return places


def getShapeData(dataset="sffind"):
    """
    Initialize the shape data used by main method
    to determine neighborhoods.
    Data courtesy of sfgov.
    """
    shpfile = os.path.join(os.path.dirname(__file__),
                           shapeSets[dataset][0])
    shapes = [shape for shape in fiona.open(shpfile)]

    shapeInfo = []
    for shaperec in shapes:
        place = shaperec['properties'][shapeSets[dataset][1]]
        shape = geometry.asShape(shaperec['geometry'])
        bbox = shape.bounds
        shapeInfo.append((shape, bbox, place))

    # data for projecting lon, lat to
    # realtor and planning shapefile coords
    # +proj=lcc
    # +lat_1=37.06666666666667
    # +lat_2=38.43333333333333
    # +lat_0=36.5
    # +lon_0=-120.5
    # +x_0=2000000
    # +y_0=500000.0000000002
    # +ellps=GRS80
    # +datum=NAD83
    # +to_meter=0.3048006096012192

    if dataset == 'sffind':
        projection = lambda x, y: (x, y)
    else:
        proj = pyproj.Proj(proj='lcc',
                           lat_1=37.06666666666667,
                           lat_2=38.43333333333333,
                           lat_0=36.5,
                           lon_0=-120.5,
                           x_0=2000000,
                           y_0=500000.0000000002,
                           ellps='GRS80',
                           datum='NAD83')

        # meter to feet conversion
        mtof = 3.2808333333333337
        projection = lambda x, y, proj=proj, mtof=mtof:\
            [mtof*z for z in proj(x, y)]

    return shapeInfo, projection


shapeData, defProjection = getShapeData('sffind')

if __name__ == '__main__':
    from pprint import pprint as pp
    import time

    def test_getSFNeigh():
        locs = [(-122.424612993055, 37.8014488257836),
                (-122.420120319211, 37.7877570602182),
                (-122.42025048261,  37.7800745746105),
                (-122.390718076188, 37.7385560584619),
                (-122.433084166809, 37.7851499161314),
                (-122.422727873548, 37.7503729275448),
                (-122.401786, 37.782562),
                (-122.391873, 37.783105),
                ]

        expected = [u'Marina',
                    u'Lower Nob Hill',
                    u'Civic Center',
                    u'Bayview',
                    u'Lower Pacific Heights',
                    u'Dolores Heights',
                    u'South of Market',
                    u'South Beach']

        rv = getSFNeighNames(locs)
        if expected != rv:
            print "Expected: \n%s" % str(expected)
            print "Actual output: \n%s" % str(rv)
            raise Exception("Test Fail: Did not get expected result")
        return rv

    st = time.time()

    pp(test_getSFNeigh())

    print "\n\nOK. Tests passed.\nDone in %6.4fs secs" % (time.time() - st)
