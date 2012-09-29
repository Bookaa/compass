# -*- coding: utf-8 -*-

###############################################################################
#
# UploadFile
# Uploads a file to your Dropbox account.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class UploadFile(Choreography):

    """
    Create a new instance of the UploadFile Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Dropbox/UploadFile')


    def new_input_set(self):
        return UploadFileInputSet()

    def _make_result_set(self, result, path):
        return UploadFileResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return UploadFileChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the UploadFile
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class UploadFileInputSet(InputSet):
        """
        Set the value of the FileContents input for this choreography. ((conditional, string) The Base64-encoded contents of the file you want to upload. Required unless using the VaultFile alias instead (an advanced option used when running Choreos in the Temboo Designer).)
        """
        def set_FileContents(self, value):
            InputSet._set_input(self, 'FileContents', value)

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
        Set the value of the FileName input for this choreography. ((required, string) The name of the file you are uploading to Dropbox.)
        """
        def set_FileName(self, value):
            InputSet._set_input(self, 'FileName', value)

        """
        Set the value of the Folder input for this choreography. ((optional, string) The name of the folder that that you want to upload a file to. A path to a sub-folder is also valid (i.e. RootFolder/SubFolder).)
        """
        def set_Folder(self, value):
            InputSet._set_input(self, 'Folder', value)

        """
        Set the value of the ResponseFormat input for this choreography. ((optional, string) The format that the response should be in. Can be set to xml or json. Defaults to xml.)
        """
        def set_ResponseFormat(self, value):
            InputSet._set_input(self, 'ResponseFormat', value)

        """
        Set the value of the Root input for this choreography. ((conditional, string) The root relative to which path is specified. Valid values are "sandbox" and "dropbox" (the default). When your access token has the App folder level of access, this should be set to "sandbox".)
        """
        def set_Root(self, value):
            InputSet._set_input(self, 'Root', value)

        """
        Set the value of the VaultFile input for this choreography. ((optional, vault file) The path to a vault file you want to upload. Required unless using the FileContents input.)
        """


"""
A ResultSet with methods tailored to the values returned by the UploadFile choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class UploadFileResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The response from Dropbox. Corresponds to the ResponseFormat input. Defaults to xml.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class UploadFileChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return UploadFileResultSet(response, path)
