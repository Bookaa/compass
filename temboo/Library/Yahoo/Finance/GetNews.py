# -*- coding: utf-8 -*-

###############################################################################
#
# GetNews
# Retrieves the most recent Yahoo! Finance Company or Industry news items as an RSS feed.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class GetNews(Choreography):

    """
    Create a new instance of the GetNews Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Yahoo/Finance/GetNews')


    def new_input_set(self):
        return GetNewsInputSet()

    def _make_result_set(self, result, path):
        return GetNewsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetNewsChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the GetNews
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class GetNewsInputSet(InputSet):
        """
        Set the value of the Company input for this choreography. ((required, string) Ticker symbol for one or more companies to search, separated by commas (e.g. YHOO,DIS to include news about Yahoo! and Disney).)
        """
        def set_Company(self, value):
            InputSet._set_input(self, 'Company', value)

        """
        Set the value of the NewsType input for this choreography. ((required, string) Enter the type of news items you want to see in the RSS feed: headline or industry. )
        """
        def set_NewsType(self, value):
            InputSet._set_input(self, 'NewsType', value)


"""
A ResultSet with methods tailored to the values returned by the GetNews choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class GetNewsResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response from Yahoo! Finance.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class GetNewsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetNewsResultSet(response, path)
