# -*- coding: utf-8 -*-

###############################################################################
#
# PostPhoto
# Uploads a photo to Google Picasa.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class PostPhoto(Choreography):

    """
    Create a new instance of the PostPhoto Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Google/Picasa/PostPhoto')


    def new_input_set(self):
        return PostPhotoInputSet()

    def _make_result_set(self, result, path):
        return PostPhotoResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return PostPhotoChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the PostPhoto
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class PostPhotoInputSet(InputSet):
        """
        Set the value of the FileContents input for this choreography. ((conditional, string) The base64 encoded file contents of the photo you want to upload.)
        """
        def set_FileContents(self, value):
            InputSet._set_input(self, 'FileContents', value)

        """
        Set the value of the AccessToken input for this choreography. ((optional, string) The access token retrieved in the last step of the Oauth process. Access tokens that are expired will be refreshed and returned in the Choreo output.)
        """
        def set_AccessToken(self, value):
            InputSet._set_input(self, 'AccessToken', value)

        """
        Set the value of the AlbumID input for this choreography. ((optional, integer) The id of the album that you want to upload the photo to. Defaults to 'default' which means the photo will be uploaded to the dropbox album.)
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
        Set the value of the ImageName input for this choreography. ((required, string) The name of the image you want to upload.)
        """
        def set_ImageName(self, value):
            InputSet._set_input(self, 'ImageName', value)

        """
        Set the value of the RefreshToken input for this choreography. ((required, string) The refresh token retrieved in the last step of the OAuth process. This is used when an access token is expired or not provided.)
        """
        def set_RefreshToken(self, value):
            InputSet._set_input(self, 'RefreshToken', value)

        """
        Set the value of the UserID input for this choreography. ((optional, string) Google Picasa username. Defaults to "default" which means the server will use the UserID of the user whose access token was specified.)
        """
        def set_UserID(self, value):
            InputSet._set_input(self, 'UserID', value)

        """
        Set the value of the VaultFile input for this choreography. ((vault file) The path to the vault file you want to upload. Required unless using the FileContents input.)
        """


"""
A ResultSet with methods tailored to the values returned by the PostPhoto choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class PostPhotoResultSet(ResultSet):
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

class PostPhotoChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return PostPhotoResultSet(response, path)
