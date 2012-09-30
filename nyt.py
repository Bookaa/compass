#!/bin/env python

from temboo.core.session import TembooSession
from temboo.Library.NYTimes.TimesNewswire import GetRecentNews
from config import *
from lxml import etree

import geoloc
import time

def getTimesReports():
    nyt = GetRecentNews(temboo_session)
    inputs = nyt.new_input_set()
    inputs.set_Source("nyt")
    inputs.set_APIKey(NYT_API_KEY)
    inputs.set_TimePeriod("1")

    try:
        results = nyt.execute_with_results(inputs)
        return results.results['Response'].encode('utf-8')
    except Exception:
        pass

def parseTimesResultRecursive(element, out, date):
    if "geo_facet_item" in element.tag:
        if element.text is not None:
            k = False
            parent = element.getparent().getparent()
            for c in parent:
                if "updated_date" in c.tag:
                    publishdate = time.mktime(time.strptime(c.text[:-6],
                        "%Y-%m-%dT%H:%M:%S"))
                    publishdate = publishdate + int(c.text[-5:-3])*60*60
                    if publishdate > date:
                        k = True
                    lastupdate.append(publishdate)
            if k:
                out.add(('nyt',
                    geoloc.getCoordinates(element.text.encode('utf-8'))))
    else:
        for child in element:
            parseTimesResultRecursive(child, out, date)

lastupdate = list()
def parseTimesResults(xml):
    outputlist = set()
    root = etree.fromstring(xml)
    global lastupdate
    if lastupdate is None:
        lastupdate = list()

    if len(lastupdate) > 0:
        lastupdate.sort()
        parseTimesResultRecursive(root, outputlist, lastupdate[len(lastupdate) -
            1])
    else:
        parseTimesResultRecursive(root, outputlist, 0)

    if len(lastupdate) > 1:
        date = lastupdate[len(lastupdate) - 1]
    else:
        date = 0
    lastupdate = list()
    lastupdate.append(date + 1)

    return list(outputlist)

if __name__ == "__main__":
    while True:
        output = parseTimesResults(getTimesReports())
        for element in output:
            print element
        print "ping"
        time.sleep(1)
