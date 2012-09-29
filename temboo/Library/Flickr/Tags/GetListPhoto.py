# -*- coding: utf-8 -*-

###############################################################################
#
# GetListPhoto
# Retrieves the tag list for a given photo.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class GetListPhoto(Choreography):

    """
    Create a new instance of the GetListPhoto Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Flickr/Tags/GetListPhoto')


    def new_input_set(self):
        return GetListPhotoInputSet()

    def _make_result_set(self, result, path):
        return GetListPhotoResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetListPhotoChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the GetListPhoto
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class GetListPhotoInputSet(InputSet):
        """
        Set the value of the APIKey input for this choreography. ((required, string) The API Key provided by Flickr (AKA the OAuth Consumer Key).)
        """
        def set_APIKey(self, value):
            InputSet._set_input(self, 'APIKey', value)

        """
        Set the value of the APISecret input for this choreography. ((conditional, string) The API Secret provided by Flickr (AKA the OAuth Consumer Secret).)
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
        Set the value of the PhotoId input for this choreography. ((required, integer) The id of the photo to return tags for.)
        """
        def set_PhotoId(self, value):
            InputSet._set_input(self, 'PhotoId', value)


"""
A ResultSet with methods tailored to the values returned by the GetListPhoto choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class GetListPhotoResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response from Flickr.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class GetListPhotoChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetListPhotoResultSet(response, path)
