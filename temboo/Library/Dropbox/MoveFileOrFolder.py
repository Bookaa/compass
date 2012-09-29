# -*- coding: utf-8 -*-

###############################################################################
#
# MoveFileOrFolder
# Moves a file or folder to a new location in the Dropbox tree.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class MoveFileOrFolder(Choreography):

    """
    Create a new instance of the MoveFileOrFolder Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Dropbox/MoveFileOrFolder')


    def new_input_set(self):
        return MoveFileOrFolderInputSet()

    def _make_result_set(self, result, path):
        return MoveFileOrFolderResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return MoveFileOrFolderChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the MoveFileOrFolder
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class MoveFileOrFolderInputSet(InputSet):
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
        Set the value of the FromPath input for this choreography. ((required, string) Specifies the file or folder to be copied.)
        """
        def set_FromPath(self, value):
            InputSet._set_input(self, 'FromPath', value)

        """
        Set the value of the ResponseFormat input for this choreography. ((optional, string) The format that the response should be in. Can be set to xml or json. Defaults to xml.)
        """
        def set_ResponseFormat(self, value):
            InputSet._set_input(self, 'ResponseFormat', value)

        """
        Set the value of the Root input for this choreography. ((optional, string) The root relative to which path is specified. Valid values are "sandbox" and "dropbox" (the default). When your access token has the App folder level of access, this should be set to "sandbox".)
        """
        def set_Root(self, value):
            InputSet._set_input(self, 'Root', value)

        """
        Set the value of the ToPath input for this choreography. ((required, string) Specifies the destination path, including the new name for the file or folder.)
        """
        def set_ToPath(self, value):
            InputSet._set_input(self, 'ToPath', value)


"""
A ResultSet with methods tailored to the values returned by the MoveFileOrFolder choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class MoveFileOrFolderResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The response from Dropbox. Corresponds to the ResponseFormat input. Defaults to xml.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class MoveFileOrFolderChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return MoveFileOrFolderResultSet(response, path)
