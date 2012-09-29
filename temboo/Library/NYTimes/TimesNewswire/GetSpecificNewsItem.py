# -*- coding: utf-8 -*-

###############################################################################
#
# GetSpecificNewsItem
# Queries the Newswire API for a specific news item.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class GetSpecificNewsItem(Choreography):

    """
    Create a new instance of the GetSpecificNewsItem Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/NYTimes/TimesNewswire/GetSpecificNewsItem')


    def new_input_set(self):
        return GetSpecificNewsItemInputSet()

    def _make_result_set(self, result, path):
        return GetSpecificNewsItemResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetSpecificNewsItemChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the GetSpecificNewsItem
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class GetSpecificNewsItemInputSet(InputSet):
        """
        Set the value of the APIKey input for this choreography. ((required, string) The API Key provided by NY Times.)
        """
        def set_APIKey(self, value):
            InputSet._set_input(self, 'APIKey', value)

        """
        Set the value of the ResponseFormat input for this choreography. ((optional, string) The format that the response should be in. Can be set to json, xml, or sphp. Defaults to xml.)
        """
        def set_ResponseFormat(self, value):
            InputSet._set_input(self, 'ResponseFormat', value)

        """
        Set the value of the URL input for this choreography. ((required, string) The complete URL of a specific news item. This URL is returned in the output of the GetRecentNews Choreo.)
        """
        def set_URL(self, value):
            InputSet._set_input(self, 'URL', value)


"""
A ResultSet with methods tailored to the values returned by the GetSpecificNewsItem choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class GetSpecificNewsItemResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The response from the NY Times API. Format corresponds to the ResponseFormat input. Defaults to xml.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class GetSpecificNewsItemChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetSpecificNewsItemResultSet(response, path)
