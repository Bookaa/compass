#!/usr/bin/env python

from twitter import getTwitterResults, parseTwitterResults
from nyt import getTimesReports, parseTimesResults
from foursquare_ping import ping
import timeit
import geoloc
import math
from geopy import distance
import serial

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
    if vector:
        greatest_dist = math.log(max([x[2] for x in vector]))
        return [(x[0], x[1], max(0, math.log(x[2]) / greatest_dist)) for x in vector]
    return vector

def process_events(raw_events, loc):
    events = [(event[0], angle(loc, event[1]), dist(loc, event[1])) for event in raw_events]
    return normalize(events)

foursquare_this_time = True

def run(loc):
    global foursquare_this_time
    if foursquare_this_time:
        foursquare_this_time = False
        foursquare = ping()
        twitter = parseTwitterResults(getTwitterResults("#HackNYF2012", loc))
        nyt = parseTimesResults(getTimesReports())
        return process_events(foursquare + twitter + nyt, loc)
    foursquare_this_time = True
    return []

def pins(events):
    bits = [0, 0, 0]
    for event in events:
        if event[0] == 'foursquare':
            sector = int(min(5, math.floor(event[1] * 6)))
            bits[0] |= int(2 ** sector)
        elif event[0] == 'twitter':
            sector = 2 * min(5, math.floor(event[1] * 6)) + 6
            if sector < 8:
                bits[0] |= int(2 ** sector)
            elif sector < 16:
                bits[1] |= int(2 ** (sector - 8))
            else:
                bits[2] |= int(2 ** (sector - 16))
        elif event[0] == 'nyt':
            sector = int(min(5, math.floor(event[1] * 6)) + 18)
            bits[2] |= int(2 ** (sector - 16))
    return bytes(bits)

if __name__ == '__main__':
    ser = serial.Serial('/dev/ttyACM1', 115200)

    loc = geoloc.getLocation()
    lat = loc['latitude']
    lng = loc['longitude']

    while True:
        events = run(loc)
        pin = pins(events)
        print pin
        print events
        ser.write(pin)
