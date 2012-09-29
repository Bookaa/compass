# -*- coding: utf-8 -*-

###############################################################################
#
# SetFile
# Allows you to update or create a file on the CloudMine server.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class SetFile(Choreography):

    """
    Create a new instance of the SetFile Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/CloudMine/FileStorage/SetFile')


    def new_input_set(self):
        return SetFileInputSet()

    def _make_result_set(self, result, path):
        return SetFileResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return SetFileChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the SetFile
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class SetFileInputSet(InputSet):
        """
        Set the value of the APIKey input for this choreography. ((required, string) The API Key provided by CloudMine after registering your app.)
        """
        def set_APIKey(self, value):
            InputSet._set_input(self, 'APIKey', value)

        """
        Set the value of the ApplicationIdentifier input for this choreography. ((required, string) The application identifier provided by CloudMine after registering your app.)
        """
        def set_ApplicationIdentifier(self, value):
            InputSet._set_input(self, 'ApplicationIdentifier', value)

        """
        Set the value of the ContentType input for this choreography. ((optional, string) The Content-Type of the file you are creating or updating. This defaults to application/octet-stream.)
        """
        def set_ContentType(self, value):
            InputSet._set_input(self, 'ContentType', value)

        """
        Set the value of the FileContents input for this choreography. ((conditional, string) The Base64 encoded contents of the file.)
        """
        def set_FileContents(self, value):
            InputSet._set_input(self, 'FileContents', value)

        """
        Set the value of the Key input for this choreography. ((optional, string) A key for the file you are uploading. If provided, the file will be stored with this key; otherwise, a key will be generated and returned.)
        """
        def set_Key(self, value):
            InputSet._set_input(self, 'Key', value)

        """
        Set the value of the SessionToken input for this choreography. ((conditional, string) The session token for an existing user (returned by the AccountLogin Choreo). This is only required if your app is performing this operation on behalf of another user.)
        """
        def set_SessionToken(self, value):
            InputSet._set_input(self, 'SessionToken', value)

        """
        Set the value of the VaultFile input for this choreography. (A path to the vault file to upload. This can be used as an alternative to the FileContents input.)
        """


"""
A ResultSet with methods tailored to the values returned by the SetFile choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class SetFileResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((json) The response from CloudMine.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class SetFileChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return SetFileResultSet(response, path)
