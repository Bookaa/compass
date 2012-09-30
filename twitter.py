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

    results = twitterSearch.execute_with_results(inputs)

    return results.results['Response'].encode('utf-8')

def parseTwitterResults(xml):
    outputlist = set()
    root = etree.fromstring(xml)
    for child in root:
        if "entry" in child.tag:
            for subchild in child:
                if "location" in subchild.tag:
                    if subchild.text is not None:
                        x = geoloc.getCoordinates(subchild.text.encode('utf-8'))
                        if x is not None:
                            outputlist.add(('twitter', x))
    return list(outputlist)

if __name__ == "__main__":
    loc = geoloc.getLocation()

    while True:
        outputlist = parseTwitterResults(getTwitterResults("#HackNYF2012", loc))
        for coord in outputlist:
            print coord
        time.sleep(1)
