# -*- coding: utf-8 -*-

###############################################################################
#
# CreateFork
# Creates a fork for the authenticated user.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class CreateFork(Choreography):

    """
    Create a new instance of the CreateFork Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/GitHub/ReposAPI/Forks/CreateFork')


    def new_input_set(self):
        return CreateForkInputSet()

    def _make_result_set(self, result, path):
        return CreateForkResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CreateForkChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the CreateFork
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class CreateForkInputSet(InputSet):
        """
        Set the value of the AccessToken input for this choreography. ((required, string) The Access Token retrieved during the OAuth process.)
        """
        def set_AccessToken(self, value):
            InputSet._set_input(self, 'AccessToken', value)

        """
        Set the value of the Org input for this choreography. ((optional, string) The organization login. The repository will be forked into this organization.)
        """
        def set_Org(self, value):
            InputSet._set_input(self, 'Org', value)

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
A ResultSet with methods tailored to the values returned by the CreateFork choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class CreateForkResultSet(ResultSet):
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

class CreateForkChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return CreateForkResultSet(response, path)
