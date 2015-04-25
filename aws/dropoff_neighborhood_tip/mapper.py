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
    tip_agg = {}
    fare_agg = {}
    for values in parseInput():
        tip_amount = float(values[14])
        fare_amount = float(values[13])
        try:
            dropoff_location = (float(values[10]), float(values[11]))
        except:
            continue
        dropoff_neighborhood = findNeighborhood(dropoff_location, index, neighborhoods)
        if dropoff_neighborhood!=-1:
            tip_agg[dropoff_neighborhood] = tip_agg.get(dropoff_neighborhood, 0) + tip_amount
            fare_agg[dropoff_neighborhood] = fare_agg.get(dropoff_neighborhood, 0) + fare_amount

    for neighbor in tip_agg.keys():
        print '{0}\t{1},{2}'.format(neighborhoods[neighbor][0], tip_agg[neighbor], fare_agg[neighbor])

if __name__=='__main__':
    mapper()
