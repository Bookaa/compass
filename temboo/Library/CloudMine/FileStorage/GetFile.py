# -*- coding: utf-8 -*-

###############################################################################
#
# GetFile
# Retrieves a file from the CloudMine server with a given key.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class GetFile(Choreography):

    """
    Create a new instance of the GetFile Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/CloudMine/FileStorage/GetFile')


    def new_input_set(self):
        return GetFileInputSet()

    def _make_result_set(self, result, path):
        return GetFileResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetFileChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the GetFile
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class GetFileInputSet(InputSet):
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
        Set the value of the Key input for this choreography. ((required, string) The key whose value you want.)
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
A ResultSet with methods tailored to the values returned by the GetFile choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class GetFileResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((json) The response from CloudMine.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class GetFileChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetFileResultSet(response, path)
