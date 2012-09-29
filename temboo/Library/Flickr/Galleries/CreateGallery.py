# -*- coding: utf-8 -*-

###############################################################################
#
# CreateGallery
# Add a comment to a specified photo on Flickr.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class CreateGallery(Choreography):

    """
    Create a new instance of the CreateGallery Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Flickr/Galleries/CreateGallery')


    def new_input_set(self):
        return CreateGalleryInputSet()

    def _make_result_set(self, result, path):
        return CreateGalleryResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CreateGalleryChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the CreateGallery
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class CreateGalleryInputSet(InputSet):
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
        Set the value of the Description input for this choreography. ((required, string) The text of the comment you are adding.)
        """
        def set_Description(self, value):
            InputSet._set_input(self, 'Description', value)

        """
        Set the value of the PrimaryPhotoID input for this choreography. ((required, integer) The id of the photo to add a comment to.)
        """
        def set_PrimaryPhotoID(self, value):
            InputSet._set_input(self, 'PrimaryPhotoID', value)

        """
        Set the value of the Title input for this choreography. ((required, string) The name of the gallery.)
        """
        def set_Title(self, value):
            InputSet._set_input(self, 'Title', value)


"""
A ResultSet with methods tailored to the values returned by the CreateGallery choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class CreateGalleryResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response from Flickr.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class CreateGalleryChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return CreateGalleryResultSet(response, path)
