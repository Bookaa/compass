# -*- coding: utf-8 -*-

###############################################################################
#
# DownloadBase64EncodedFile
# Downloads a file from a specified directory in your FilesAnywhere account, and returns the content as Base64 encoded data.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class DownloadBase64EncodedFile(Choreography):

    """
    Create a new instance of the DownloadBase64EncodedFile Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/FilesAnywhere/DownloadBase64EncodedFile')


    def new_input_set(self):
        return DownloadBase64EncodedFileInputSet()

    def _make_result_set(self, result, path):
        return DownloadBase64EncodedFileResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return DownloadBase64EncodedFileChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the DownloadBase64EncodedFile
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class DownloadBase64EncodedFileInputSet(InputSet):
        """
        Set the value of the APIKey input for this choreography. ((conditional, string) The API Key provided by FilesAnywhere. Required unless supplying a valid Token input.)
        """
        def set_APIKey(self, value):
            InputSet._set_input(self, 'APIKey', value)

        """
        Set the value of the Password input for this choreography. ((conditional, string) Your FilesAnywhere password. Required unless supplying a valid Token input.)
        """
        def set_Password(self, value):
            InputSet._set_input(self, 'Password', value)

        """
        Set the value of the Path input for this choreography. ((required, string) The path to the file you want to download (i.e. \JOHNSMITH\MyFolder\MyFile.txt).)
        """
        def set_Path(self, value):
            InputSet._set_input(self, 'Path', value)

        """
        Set the value of the Token input for this choreography. ((conditional, string) If provided, the Choreo will use the token to authenticate. If the token is expired or not provided, the Choreo will relogin and retrieve a new token when APIKey, Username, and Password are supplied.)
        """
        def set_Token(self, value):
            InputSet._set_input(self, 'Token', value)

        """
        Set the value of the Username input for this choreography. ((conditional, string) Your FilesAnywhere username. Required unless supplying a valid Token input.)
        """
        def set_Username(self, value):
            InputSet._set_input(self, 'Username', value)


"""
A ResultSet with methods tailored to the values returned by the DownloadBase64EncodedFile choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class DownloadBase64EncodedFileResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((string) The response from FilesAnywhere. The response contains the Base64 encoded content of the file you are downloading.)
        """
        def get_Response(self):
            return self._output.get('Response', None)
        """
        Retrieve the value for the "Token" output from this choreography execution. ((conditional, string) If provided, the Choreo will use the token to authenticate. If the token is expired or not provided, the Choreo will relogin and retrieve a new token when APIKey, Username, and Password are supplied.)
        """
        def get_Token(self):
            return self._output.get('Token', None)

class DownloadBase64EncodedFileChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return DownloadBase64EncodedFileResultSet(response, path)
