#!/bin/env python

from temboo.core.session import TembooSession
from temboo.Library.Twitter.Search import Query
from config import *
from lxml import etree

import geoloc
import time

"""
    Gets results from twitter given a query

    Returns useless XML output =(
"""
def getTwitterResults(query, loc):
    twitterSearch = Query(temboo_session)
    inputs = twitterSearch.new_input_set()
    geocode = "%s,%s,500mi" % (loc['latitude'], loc['longitude'])
    inputs.set_Geocode(geocode)
    inputs.set_IncludeEntities("1")
    inputs.set_ResultsPerPage(15)
    inputs.set_Query(query)

    try:
        results = twitterSearch.execute_with_results(inputs)
        return results.results['Response'].encode('utf-8')
    except Exception:
        pass


def parseTwitterResultRecursive(element, out, depth, date):
    if "location" in element.tag:
        if element.text is not None:
            k = False
            parent = element.getparent()
            for c in parent:
                if "published" in c.tag:
                    publishdate = time.mktime(time.strptime(c.text,
                        "%Y-%m-%dT%H:%M:%SZ"))
                    if publishdate > date:
                        k = True
                    lastupdate.append(publishdate)
            if k:
                x = geoloc.getCoordinates(element.text.encode('utf-8'))
                if x is not None:
                    out.add(('twitter', x))
    else:
        if depth < 2:
            for child in element:
                parseTwitterResultRecursive(child, out, depth + 1, date)

lastupdate = list()

def parseTwitterResults(xml):
    outputlist = set()
    root = etree.fromstring(xml)

    global lastupdate
    if lastupdate is None:
        lastupdate = list()

    if len(lastupdate) > 0:
        lastupdate.sort()
        parseTwitterResultRecursive(root, outputlist, 0,
                lastupdate[0])
    else:
        parseTwitterResultRecursive(root, outputlist, 0, 0)
    date = lastupdate[0]
    lastupdate = list()
    lastupdate.append(date)

    return list(outputlist)

if __name__ == "__main__":
    loc = geoloc.getLocation()

    while True:
        outputlist = parseTwitterResults(getTwitterResults("#HackNYF2012", loc))
        for coord in outputlist:
            print coord
        time.sleep(1)
