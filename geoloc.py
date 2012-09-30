#!/bin/env python
import pygeoip
import urllib2
from geopy import geocoders

gi = pygeoip.GeoIP('GeoLiteCity.dat')
g = geocoders.Google()

cache = dict()
fails = set()
def getLocation():
    try:
        out = dict()
        result = gi.record_by_addr(urllib2.urlopen('http://automation.whatismyip.com/n09230945.asp').read())
        
        out['latitude'] = result['latitude']
        out['longitude'] = result['longitude']
        return out
    except Exception:
        print "error getting location"
        pass

def getCoordinates(loc):
    if loc in fails:
        return None
    try:
        if loc in cache:
            (lat, lng) = cache[loc]
        else:
            place, (lat, lng) = g.geocode(loc)
            cache[loc] = (lat, lng)
        return (lat, lng)
    except Exception:
        try:
            place, (lat, lng) = g.geocode(loc + ", NY")
            cache[loc] = (lat, lng)
            return (lat, lng)
        except Exception:
            fails.add(loc)
            print "error getting coordinates (input: %s)" % loc
            pass
        pass

if __name__ == '__main__':
    print getLocation()
