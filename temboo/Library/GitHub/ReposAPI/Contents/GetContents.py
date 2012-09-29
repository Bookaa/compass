# -*- coding: utf-8 -*-

###############################################################################
#
# GetContents
# Returns a tarball or zipball archive for a repository. 
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class GetContents(Choreography):

    """
    Create a new instance of the GetContents Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/GitHub/ReposAPI/Contents/GetContents')


    def new_input_set(self):
        return GetContentsInputSet()

    def _make_result_set(self, result, path):
        return GetContentsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetContentsChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the GetContents
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class GetContentsInputSet(InputSet):
        """
        Set the value of the AccessToken input for this choreography. ((required, string) The Access Token retrieved during the OAuth process. Required when accessing a protected resource.)
        """
        def set_AccessToken(self, value):
            InputSet._set_input(self, 'AccessToken', value)

        """
        Set the value of the ArchiveFormat input for this choreography. ((required, string) Either tarball or zipball. Defaults to "tarball".)
        """
        def set_ArchiveFormat(self, value):
            InputSet._set_input(self, 'ArchiveFormat', value)

        """
        Set the value of the Ref input for this choreography. ((optional, string) A valid Git reference. Defaults to "master".)
        """
        def set_Ref(self, value):
            InputSet._set_input(self, 'Ref', value)

        """
        Set the value of the Repo input for this choreography. ((required, string) The name of the repository.)
        """
        def set_Repo(self, value):
            InputSet._set_input(self, 'Repo', value)

        """
        Set the value of the User input for this choreography. ((required, string) The GitHub username.)
        """
        def set_User(self, value):
            InputSet._set_input(self, 'User', value)


"""
A ResultSet with methods tailored to the values returned by the GetContents choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class GetContentsResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((string) The response from GitHub.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class GetContentsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetContentsResultSet(response, path)
