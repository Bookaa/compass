# -*- coding: utf-8 -*-

###############################################################################
#
# TagPhoto
# Creates a tag for a specified photo in Google Picasa.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class TagPhoto(Choreography):

    """
    Create a new instance of the TagPhoto Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Google/Picasa/TagPhoto')


    def new_input_set(self):
        return TagPhotoInputSet()

    def _make_result_set(self, result, path):
        return TagPhotoResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return TagPhotoChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the TagPhoto
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class TagPhotoInputSet(InputSet):
        """
        Set the value of the AccessToken input for this choreography. ((optional, string) The access token retrieved in the last step of the Oauth process. Access tokens that are expired will be refreshed and returned in the Choreo output.)
        """
        def set_AccessToken(self, value):
            InputSet._set_input(self, 'AccessToken', value)

        """
        Set the value of the AlbumID input for this choreography. ((required, integer) The id of the album which contains the photo you want to tag.)
        """
        def set_AlbumID(self, value):
            InputSet._set_input(self, 'AlbumID', value)

        """
        Set the value of the ClientID input for this choreography. ((required, string) The client id provided by Google.)
        """
        def set_ClientID(self, value):
            InputSet._set_input(self, 'ClientID', value)

        """
        Set the value of the ClientSecret input for this choreography. ((required, string) The client secret provided by Google.)
        """
        def set_ClientSecret(self, value):
            InputSet._set_input(self, 'ClientSecret', value)

        """
        Set the value of the PhotoID input for this choreography. ((required, integer) The id of the photo you want to tag.)
        """
        def set_PhotoID(self, value):
            InputSet._set_input(self, 'PhotoID', value)

        """
        Set the value of the RefreshToken input for this choreography. ((required, string) The refresh token retrieved in the last step of the OAuth process. This is used when an access token is expired or not provided.)
        """
        def set_RefreshToken(self, value):
            InputSet._set_input(self, 'RefreshToken', value)

        """
        Set the value of the Tag input for this choreography. ((required, string) The text for the photo tag.)
        """
        def set_Tag(self, value):
            InputSet._set_input(self, 'Tag', value)

        """
        Set the value of the UserID input for this choreography. ((optional, string) Google Picasa username. Defaults to "default" which means the server will use the UserID of the user whose access token was specified.)
        """
        def set_UserID(self, value):
            InputSet._set_input(self, 'UserID', value)


"""
A ResultSet with methods tailored to the values returned by the TagPhoto choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class TagPhotoResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response from Google Picasa.)
        """
        def get_Response(self):
            return self._output.get('Response', None)
        """
        Retrieve the value for the "AccessToken" output from this choreography execution. ((optional, string) The access token retrieved in the last step of the Oauth process. Access tokens that are expired will be refreshed and returned in the Choreo output.)
        """
        def get_AccessToken(self):
            return self._output.get('AccessToken', None)

class TagPhotoChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return TagPhotoResultSet(response, path)
