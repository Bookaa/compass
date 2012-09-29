# -*- coding: utf-8 -*-

###############################################################################
#
# GetLocation
# Retrieves geo data (including latitude and longitude coordinates) for a specified photo.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class GetLocation(Choreography):

    """
    Create a new instance of the GetLocation Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Flickr/Geo/GetLocation')


    def new_input_set(self):
        return GetLocationInputSet()

    def _make_result_set(self, result, path):
        return GetLocationResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetLocationChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the GetLocation
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class GetLocationInputSet(InputSet):
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
        Set the value of the PhotoId input for this choreography. ((required, integer) The id of the photo that you want to get the location for.)
        """
        def set_PhotoId(self, value):
            InputSet._set_input(self, 'PhotoId', value)


"""
A ResultSet with methods tailored to the values returned by the GetLocation choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class GetLocationResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response from Flickr.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class GetLocationChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetLocationResultSet(response, path)
