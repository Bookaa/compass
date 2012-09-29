# -*- coding: utf-8 -*-

###############################################################################
#
# FindByLatLon
# Returns a place ID for a given latitude, longitude and accuracy.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class FindByLatLon(Choreography):

    """
    Create a new instance of the FindByLatLon Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Flickr/Places/FindByLatLon')


    def new_input_set(self):
        return FindByLatLonInputSet()

    def _make_result_set(self, result, path):
        return FindByLatLonResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return FindByLatLonChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the FindByLatLon
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class FindByLatLonInputSet(InputSet):
        """
        Set the value of the APIKey input for this choreography. ((required, string) The API Key provided by Flickr (AKA the OAuth Consumer Key).)
        """
        def set_APIKey(self, value):
            InputSet._set_input(self, 'APIKey', value)

        """
        Set the value of the APISecret input for this choreography. ((required, string) The API Secret provided by Flickr (AKA the OAuth Consumer Secret).)
        """
        def set_APISecret(self, value):
            InputSet._set_input(self, 'APISecret', value)

        """
        Set the value of the AccessTokenSecret input for this choreography. ((required, string) The Access Token Secret retrieved during the OAuth process.)
        """
        def set_AccessTokenSecret(self, value):
            InputSet._set_input(self, 'AccessTokenSecret', value)

        """
        Set the value of the AccessToken input for this choreography. ((required, string) The Access Token retrieved during the OAuth process.)
        """
        def set_AccessToken(self, value):
            InputSet._set_input(self, 'AccessToken', value)

        """
        Set the value of the Accuracy input for this choreography. ((optional, integer) Recorded accuracy level of the location information. Valid range is 1-16. The default is 16.)
        """
        def set_Accuracy(self, value):
            InputSet._set_input(self, 'Accuracy', value)

        """
        Set the value of the Latitude input for this choreography. ((required, decimal) The latitude whose valid range is -90 to 90. Anything more than 4 decimal places will be truncated.)
        """
        def set_Latitude(self, value):
            InputSet._set_input(self, 'Latitude', value)

        """
        Set the value of the Longitude input for this choreography. ((required, decimal) The longitude whose valid range is -180 to 180. Anything more than 4 decimal places will be truncated.)
        """
        def set_Longitude(self, value):
            InputSet._set_input(self, 'Longitude', value)


"""
A ResultSet with methods tailored to the values returned by the FindByLatLon choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class FindByLatLonResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response from Flickr.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class FindByLatLonChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return FindByLatLonResultSet(response, path)
