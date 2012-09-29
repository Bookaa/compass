# -*- coding: utf-8 -*-

###############################################################################
#
# GetThumbnail
# Retrieves a thumbnail for a specified image.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class GetThumbnail(Choreography):

    """
    Create a new instance of the GetThumbnail Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Dropbox/GetThumbnail')


    def new_input_set(self):
        return GetThumbnailInputSet()

    def _make_result_set(self, result, path):
        return GetThumbnailResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetThumbnailChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the GetThumbnail
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class GetThumbnailInputSet(InputSet):
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
        Set the value of the AppKey input for this choreography. ((required, string) The App Key provided by Dropbox (AKA the OAuth Consumer Key).)
        """
        def set_AppKey(self, value):
            InputSet._set_input(self, 'AppKey', value)

        """
        Set the value of the AppSecret input for this choreography. ((required, string) The App Secret provided by Dropbox (AKA the OAuth Consumer Secret).)
        """
        def set_AppSecret(self, value):
            InputSet._set_input(self, 'AppSecret', value)

        """
        Set the value of the ImageFormat input for this choreography. ((optional, string) The thumbnail format to return for the specified image. Accepted values are: jpeg (default) or png.)
        """
        def set_ImageFormat(self, value):
            InputSet._set_input(self, 'ImageFormat', value)

        """
        Set the value of the Path input for this choreography. ((required, string) The path to the file that you want to generate a thumbnail for (i.e. RootFolder/SubFolder/MyFile.txt).)
        """
        def set_Path(self, value):
            InputSet._set_input(self, 'Path', value)

        """
        Set the value of the Root input for this choreography. ((conditional, string) The root relative to which path is specified. Valid values are "sandbox" and "dropbox" (the default). When your access token has the App folder level of access, this should be set to "sandbox".)
        """
        def set_Root(self, value):
            InputSet._set_input(self, 'Root', value)

        """
        Set the value of the Size input for this choreography. ((optional, string) The size of the thumbnail to generate. Accepted values are: small, medium, s, m, l, xl. See Choreo documentation for exact dimensions. Defaults to "small".)
        """
        def set_Size(self, value):
            InputSet._set_input(self, 'Size', value)


"""
A ResultSet with methods tailored to the values returned by the GetThumbnail choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class GetThumbnailResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((string) The base64 encoded image content of the thumbnail.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class GetThumbnailChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetThumbnailResultSet(response, path)
