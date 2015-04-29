#!/usr/bin/env python
import sys
sys.path.append('.')
import matplotlib
matplotlib.use('Agg')
from matplotlib.path import Path
from rtree import index as rtree
import numpy, shapefile, time

def findNeighborhood(location, index, neighborhoods):
    match = index.intersection((location[0], location[1], location[0], location[1]))
    for a in match:
        if any(map(lambda x: x.contains_point(location), neighborhoods[a][1])):
            return a
    return -1

def readNeighborhood(shapeFilename, index, neighborhoods):
    sf = shapefile.Reader(shapeFilename)
    for sr in sf.shapeRecords():
        if sr.record[1] not in ['New York', 'Kings', 'Queens', 'Bronx']: continue
        paths = map(Path, numpy.split(sr.shape.points, sr.shape.parts[1:]))
        bbox = paths[0].get_extents()
        map(bbox.update_from_path, paths[1:])
        index.insert(len(neighborhoods), list(bbox.get_points()[0])+list(bbox.get_points()[1]))
        neighborhoods.append((sr.record[3], paths))
    neighborhoods.append(('UNKNOWN', None))

def parseInput():
    for line in sys.stdin:
        key, value = line.strip('\n').split('\t', 1)
        values = key.split(',') + value.split(',')
        if len(values) > 1:
            yield values

def mapper():
    index = rtree.Index()
    neighborhoods = []
    readNeighborhood('NYC.shp', index, neighborhoods)
    agg = {}
    for values in parseInput():
        hour = values[3]
        pickup_location = (float(values[8]), float(values[9]))
        pickup_neighborhood = findNeighborhood(pickup_location, index, neighborhoods)
        if pickup_neighborhood!=-1:
            if hour:
                hour_loc = hour.split()[1][:2] + " " + str(pickup_neighborhood)
                agg[hour_loc] = agg.get(hour_loc, 0) + 1


    for hour_loc in agg.keys():
        hour, loc = hour_loc.split()
        print '{0},{1}\t{2}'.format(neighborhoods[int(loc)][0], hour, agg[hour_loc])

if __name__=='__main__':
    mapper()
