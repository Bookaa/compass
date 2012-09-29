# -*- coding: utf-8 -*-

###############################################################################
#
# CreateCommitComment
# Creates a comment on a specified commit.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class CreateCommitComment(Choreography):

    """
    Create a new instance of the CreateCommitComment Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/GitHub/ReposAPI/Comments/CreateCommitComment')


    def new_input_set(self):
        return CreateCommitCommentInputSet()

    def _make_result_set(self, result, path):
        return CreateCommitCommentResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CreateCommitCommentChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the CreateCommitComment
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class CreateCommitCommentInputSet(InputSet):
        """
        Set the value of the AccessToken input for this choreography. ((required, string) The Access Token retrieved during the OAuth process.)
        """
        def set_AccessToken(self, value):
            InputSet._set_input(self, 'AccessToken', value)

        """
        Set the value of the Body input for this choreography. ((required, string) The comment text.)
        """
        def set_Body(self, value):
            InputSet._set_input(self, 'Body', value)

        """
        Set the value of the Line input for this choreography. ((required, integer) The line number in the file to comment on.)
        """
        def set_Line(self, value):
            InputSet._set_input(self, 'Line', value)

        """
        Set the value of the Path input for this choreography. ((required, string) The relative path of the file to comment on.)
        """
        def set_Path(self, value):
            InputSet._set_input(self, 'Path', value)

        """
        Set the value of the Position input for this choreography. ((required, integer) The line index in the diff to comment on.)
        """
        def set_Position(self, value):
            InputSet._set_input(self, 'Position', value)

        """
        Set the value of the Repo input for this choreography. ((required, string) The name of the repo that the comment is associated with.)
        """
        def set_Repo(self, value):
            InputSet._set_input(self, 'Repo', value)

        """
        Set the value of the SHA input for this choreography. ((required, string) The SHA or id of the commit.)
        """
        def set_SHA(self, value):
            InputSet._set_input(self, 'SHA', value)

        """
        Set the value of the User input for this choreography. ((required, string) The GitHub username.)
        """
        def set_User(self, value):
            InputSet._set_input(self, 'User', value)


"""
A ResultSet with methods tailored to the values returned by the CreateCommitComment choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class CreateCommitCommentResultSet(ResultSet):
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

class CreateCommitCommentChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return CreateCommitCommentResultSet(response, path)
