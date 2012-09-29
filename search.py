#!/bin/env python

from temboo.Library.Twitter.Search.SearchFilter import SearchFilter
from temboo.core.session import TembooSession
from config import *

twitterSearch = SearchFilter(temboo_session)
inputs = twitterSearch.new_input_set()
inputs.set_SearchString("Elvis")
inputs.set_Filter("Costello")
inputs.set_ResultsPerPage(10)
results = twitterSearch.execute_with_results(inputs)
print results.get_Response().encode('utf-8')
