# -*- coding: utf-8 -*-

###############################################################################
#
# CreateRepo
# Creates a new repository for the authenticated user.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class CreateRepo(Choreography):

    """
    Create a new instance of the CreateRepo Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/GitHub/ReposAPI/Repos/CreateRepo')


    def new_input_set(self):
        return CreateRepoInputSet()

    def _make_result_set(self, result, path):
        return CreateRepoResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CreateRepoChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the CreateRepo
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class CreateRepoInputSet(InputSet):
        """
        Set the value of the AccessToken input for this choreography. ((required, string) The Access Token retrieved during the OAuth process.)
        """
        def set_AccessToken(self, value):
            InputSet._set_input(self, 'AccessToken', value)

        """
        Set the value of the Description input for this choreography. ((optional, string) A text description for the repo.)
        """
        def set_Description(self, value):
            InputSet._set_input(self, 'Description', value)

        """
        Set the value of the HasDownloads input for this choreography. ((optional, boolean) Se to "true" to enable downloads for this repository. Defaults to "true".)
        """
        def set_HasDownloads(self, value):
            InputSet._set_input(self, 'HasDownloads', value)

        """
        Set the value of the HasIssues input for this choreography. ((optional, boolean) Set to "true" to enable issues for this repository. Defaults to "true.")
        """
        def set_HasIssues(self, value):
            InputSet._set_input(self, 'HasIssues', value)

        """
        Set the value of the HasWiki input for this choreography. ((optional, boolean) Set to "true" to enable the wiki for this repository. Defaults to "true".)
        """
        def set_HasWiki(self, value):
            InputSet._set_input(self, 'HasWiki', value)

        """
        Set the value of the Homepage input for this choreography. ((optional, string) A homepage link.)
        """
        def set_Homepage(self, value):
            InputSet._set_input(self, 'Homepage', value)

        """
        Set the value of the Name input for this choreography. ((required, string) The name of the repo being created.)
        """
        def set_Name(self, value):
            InputSet._set_input(self, 'Name', value)

        """
        Set the value of the Private input for this choreography. ((optional, boolean) A flag indicating the the repo is private or public. Set to "true" to create a private repository. Defaults to "false".)
        """
        def set_Private(self, value):
            InputSet._set_input(self, 'Private', value)

        """
        Set the value of the TeamID input for this choreography. ((optional, integer) The id of the team that will be granted access to this repository. Only valid when creating a repo in an organization.)
        """
        def set_TeamID(self, value):
            InputSet._set_input(self, 'TeamID', value)


"""
A ResultSet with methods tailored to the values returned by the CreateRepo choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class CreateRepoResultSet(ResultSet):
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

class CreateRepoChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return CreateRepoResultSet(response, path)
