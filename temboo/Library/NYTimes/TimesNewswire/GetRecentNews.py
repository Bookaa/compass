# -*- coding: utf-8 -*-

###############################################################################
#
# GetRecentNews
# Retrieves recent news items.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class GetRecentNews(Choreography):

    """
    Create a new instance of the GetRecentNews Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/NYTimes/TimesNewswire/GetRecentNews')


    def new_input_set(self):
        return GetRecentNewsInputSet()

    def _make_result_set(self, result, path):
        return GetRecentNewsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetRecentNewsChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the GetRecentNews
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class GetRecentNewsInputSet(InputSet):
        """
        Set the value of the APIKey input for this choreography. ((required, string) The API Key provided by NY Times.)
        """
        def set_APIKey(self, value):
            InputSet._set_input(self, 'APIKey', value)

        """
        Set the value of the Limit input for this choreography. ((optional, integer) The number of results to return. Defaults to 20.)
        """
        def set_Limit(self, value):
            InputSet._set_input(self, 'Limit', value)

        """
        Set the value of the Offset input for this choreography. ((optional, integer) A numeric value indicating the starting point of the result set. This can be used in combination with the Limit input to page through results.)
        """
        def set_Offset(self, value):
            InputSet._set_input(self, 'Offset', value)

        """
        Set the value of the ResponseFormat input for this choreography. ((optional, string) The format that the response should be in. Can be set to json, xml, or sphp. Defaults to xml.)
        """
        def set_ResponseFormat(self, value):
            InputSet._set_input(self, 'ResponseFormat', value)

        """
        Set the value of the Section input for this choreography. ((optional, string) Limits the set of items by one or more sections. Separate sections by semicolons. Defaults to "all" to get all sections. See Choreo documentation for more options for this input.)
        """
        def set_Section(self, value):
            InputSet._set_input(self, 'Section', value)

        """
        Set the value of the Source input for this choreography. ((optional, string) Limits the set of items by originating source. Set to "nyt" for New York Times items only and "iht" for International Herald Tribune items. Set to "all" for both (the default).)
        """
        def set_Source(self, value):
            InputSet._set_input(self, 'Source', value)

        """
        Set the value of the TimePeriod input for this choreography. ((optional, integer) Limits the set of items by time published. Valid range is number of hours, 1–720 (in hours). Defaults to 24.)
        """
        def set_TimePeriod(self, value):
            InputSet._set_input(self, 'TimePeriod', value)


"""
A ResultSet with methods tailored to the values returned by the GetRecentNews choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class GetRecentNewsResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The response from the NY Times API. Format corresponds to the ResponseFormat input. Defaults to xml.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class GetRecentNewsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetRecentNewsResultSet(response, path)
