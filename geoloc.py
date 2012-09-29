#!/bin/env python
import pygeoip
import urllib2

gi = pygeoip.GeoIP('GeoLiteCity.dat')

def getLocation():
    try:
        return gi.record_by_addr(urllib2.urlopen('http://automation.whatismyip.com/n09230945.asp').read())
    except Exception:
        print "error getting location"
        pass

if __name__ == '__main__':
    print getLocation()
