# -*- coding: utf-8 -*-

###############################################################################
#
# CreateGist
# Creates a gist.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class CreateGist(Choreography):

    """
    Create a new instance of the CreateGist Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/GitHub/GistsAPI/Gists/CreateGist')


    def new_input_set(self):
        return CreateGistInputSet()

    def _make_result_set(self, result, path):
        return CreateGistResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CreateGistChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the CreateGist
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class CreateGistInputSet(InputSet):
        """
        Set the value of the AccessToken input for this choreography. ((required, string) The Access Token retrieved during the OAuth process.)
        """
        def set_AccessToken(self, value):
            InputSet._set_input(self, 'AccessToken', value)

        """
        Set the value of the Description input for this choreography. ((optional, string) The description for this gist.)
        """
        def set_Description(self, value):
            InputSet._set_input(self, 'Description', value)

        """
        Set the value of the FileContents input for this choreography. ((required, string) The file contents of the gist.)
        """
        def set_FileContents(self, value):
            InputSet._set_input(self, 'FileContents', value)

        """
        Set the value of the FileName input for this choreography. ((required, string) The file name of the gist (i.e. myProject.py).)
        """
        def set_FileName(self, value):
            InputSet._set_input(self, 'FileName', value)

        """
        Set the value of the Public input for this choreography. ((required, boolean) Indicates whether or not the gist is public or private.)
        """
        def set_Public(self, value):
            InputSet._set_input(self, 'Public', value)

        """
        Set the value of the User input for this choreography. ((required, string) The user who is creating the gist.)
        """
        def set_User(self, value):
            InputSet._set_input(self, 'User', value)


"""
A ResultSet with methods tailored to the values returned by the CreateGist choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class CreateGistResultSet(ResultSet):
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

class CreateGistChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return CreateGistResultSet(response, path)
