# -*- coding: utf-8 -*-

###############################################################################
#
# HereNow
# Provides a count of how many people are at a given venue.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class HereNow(Choreography):

    """
    Create a new instance of the HereNow Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Foursquare/Venues/HereNow')


    def new_input_set(self):
        return HereNowInputSet()

    def _make_result_set(self, result, path):
        return HereNowResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return HereNowChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the HereNow
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class HereNowInputSet(InputSet):
        """
        Set the value of the AfterTimestamp input for this choreography. ((optional, date) Retrieve the first results to follow this timestamp (an epoch timestamp in seconds).)
        """
        def set_AfterTimestamp(self, value):
            InputSet._set_input(self, 'AfterTimestamp', value)

        """
        Set the value of the Limit input for this choreography. ((optional, integer) The number of results to return, up to 500.)
        """
        def set_Limit(self, value):
            InputSet._set_input(self, 'Limit', value)

        """
        Set the value of the OauthToken input for this choreography. ((required, string) The Foursquare API Oauth token string.)
        """
        def set_OauthToken(self, value):
            InputSet._set_input(self, 'OauthToken', value)

        """
        Set the value of the Offset input for this choreography. ((optional, integer) Used to page through results.)
        """
        def set_Offset(self, value):
            InputSet._set_input(self, 'Offset', value)

        """
        Set the value of the ResponseFormat input for this choreography. ((optional, string) The format that response should be in. Can be set to xml or json. Defaults to json.)
        """
        def set_ResponseFormat(self, value):
            InputSet._set_input(self, 'ResponseFormat', value)

        """
        Set the value of the VenueID input for this choreography. ((required, string) The ID associated with the venue you want to retrieve details for.)
        """
        def set_VenueID(self, value):
            InputSet._set_input(self, 'VenueID', value)


"""
A ResultSet with methods tailored to the values returned by the HereNow choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class HereNowResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The response from Foursquare. Corresponds to the ResponseFormat input. Defaults to JSON.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class HereNowChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return HereNowResultSet(response, path)
