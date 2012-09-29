# -*- coding: utf-8 -*-

###############################################################################
#
# CompareCommits
# Retrieves a comparison between two commits.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class CompareCommits(Choreography):

    """
    Create a new instance of the CompareCommits Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/GitHub/ReposAPI/Commits/CompareCommits')


    def new_input_set(self):
        return CompareCommitsInputSet()

    def _make_result_set(self, result, path):
        return CompareCommitsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CompareCommitsChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the CompareCommits
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class CompareCommitsInputSet(InputSet):
        """
        Set the value of the AccessToken input for this choreography. ((conditional, string) The Access Token retrieved during the OAuth process. Required when accessing a protected resource.)
        """
        def set_AccessToken(self, value):
            InputSet._set_input(self, 'AccessToken', value)

        """
        Set the value of the Base input for this choreography. ((required, string) The base commit (i.e. "master").)
        """
        def set_Base(self, value):
            InputSet._set_input(self, 'Base', value)

        """
        Set the value of the Head input for this choreography. ((required, string) The head commit.)
        """
        def set_Head(self, value):
            InputSet._set_input(self, 'Head', value)

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
A ResultSet with methods tailored to the values returned by the CompareCommits choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class CompareCommitsResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((json) The response from GitHub.)
        """
        def get_Response(self):
            return self._output.get('Response', None)
        """
        Retrieve the value for the "Limit" output from this choreography execution. ((integer) The available rate limit for your account. This is returned in the GitHub response header.)
        """
        def get_Limit(self):
            return self._output.get('Limit', None)
        """
        Retrieve the value for the "Remaining" output from this choreography execution. ((integer) The remaining number of API requests available to you. This is returned in the GitHub response header.)
        """
        def get_Remaining(self):
            return self._output.get('Remaining', None)

class CompareCommitsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return CompareCommitsResultSet(response, path)
