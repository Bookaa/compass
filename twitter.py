#!/bin/env python

from temboo.core.session import TembooSession
from temboo.Library.Twitter.Search import Query
from config import *

import geoloc

"""
    Gets results from twitter given a query

    Returns useless XML output =(
"""
def getTwitterResults(query):
    twitterSearch = Query(temboo_session)
    inputs = twitterSearch.new_input_set()
    loc = geoloc.getLocation()
    geocode = "%s,%s,5mi" % (loc['latitude'], loc['longitude'])
    print geocode
    inputs.set_Geocode(geocode)
    inputs.set_IncludeEntities("1")
    inputs.set_Query(query)

    results = twitterSearch.execute_with_results(inputs)

    return results.results['Response'].encode('utf-8')

if __name__ == "__main__":
    print getTwitterResults("#HackNYF2012")

