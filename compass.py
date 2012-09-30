#!/usr/bin/env python

from twitter import getTwitterResults, parseTwitterResults
from foursquare_ping import ping
import timeit
import geoloc
import math
from geopy import distance

def angle(my_loc, other_loc):
    delta_lat = other_loc[0] - my_loc['latitude']
    delta_lng = other_loc[1] - my_loc['longitude']
    try:
        return math.atan(delta_lng - delta_lat)
    except ZeroDivisionError:
        return None

def dist(my_loc, other_loc):
    loc = (my_loc['latitude'], my_loc['longitude'])
    return distance.distance(loc, other_loc).miles

def normalize(vector):
    greatest_dist = math.log(max([x[2] for x in vector]))
    return [(x[0], x[1], max(0, math.log(x[2]) / greatest_dist)) for x in vector]

def process_events(raw_events):
    events = [(event[0], angle(loc, event[1]), dist(loc, event[1])) for event in raw_events]
    return normalize(events)

if __name__ == '__main__':
    loc = geoloc.getLocation()
    lat = loc['latitude']
    lng = loc['longitude']

    foursquare = ping()
    twitter = parseTwitterResults(getTwitterResults("#HackNYF2012", loc))
    events = process_events(foursquare + twitter)
