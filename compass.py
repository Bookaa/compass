#!/usr/bin/env python

from twitter import getTwitterResults, parseTwitterResults
from foursquare_ping import ping
import timeit
import geoloc
import math

def angle(my_loc, other_loc):
    delta_lat = other_loc[0] - my_loc['latitude']
    delta_lng = other_loc[1] - my_loc['longitude']
    try:
        return math.atan(delta_lng - delta_lat)
    except ZeroDivisionError:
        return None

if __name__ == '__main__':
    loc = geoloc.getLocation()
    lat = loc['latitude']
    lng = loc['longitude']

    foursquare = ping()
    twitter = parseTwitterResults(getTwitterResults("#HackNYF2012", loc))
    for coord in (foursquare+twitter):
        print (180 / math.pi * angle(loc, coord[1]))
