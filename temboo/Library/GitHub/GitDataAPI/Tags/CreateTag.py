# -*- coding: utf-8 -*-

###############################################################################
#
# CreateTag
# Creates a tag object.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class CreateTag(Choreography):

    """
    Create a new instance of the CreateTag Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/GitHub/GitDataAPI/Tags/CreateTag')


    def new_input_set(self):
        return CreateTagInputSet()

    def _make_result_set(self, result, path):
        return CreateTagResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CreateTagChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the CreateTag
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class CreateTagInputSet(InputSet):
        """
        Set the value of the AccessToken input for this choreography. ((required, string) The Access Token retrieved during the OAuth process.)
        """
        def set_AccessToken(self, value):
            InputSet._set_input(self, 'AccessToken', value)

        """
        Set the value of the Message input for this choreography. ((required, string) The tag message.)
        """
        def set_Message(self, value):
            InputSet._set_input(self, 'Message', value)

        """
        Set the value of the Object input for this choreography. ((required, string) The SHA of the git object that is being tagged.)
        """
        def set_Object(self, value):
            InputSet._set_input(self, 'Object', value)

        """
        Set the value of the Repo input for this choreography. ((required, string) The name of the repo associated with the tag being created.)
        """
        def set_Repo(self, value):
            InputSet._set_input(self, 'Repo', value)

        """
        Set the value of the Tag input for this choreography. ((required, string) A string to use for the tag (i.e. v0.0.1).)
        """
        def set_Tag(self, value):
            InputSet._set_input(self, 'Tag', value)

        """
        Set the value of the TaggerDate input for this choreography. ((required, date) A timestamp of when the object is tagged. Should be formatted like: 2011-06-17T14:53:35-07:00.)
        """
        def set_TaggerDate(self, value):
            InputSet._set_input(self, 'TaggerDate', value)

        """
        Set the value of the TaggerEmail input for this choreography. ((required, string) The email of the author of the tag.)
        """
        def set_TaggerEmail(self, value):
            InputSet._set_input(self, 'TaggerEmail', value)

        """
        Set the value of the TaggerName input for this choreography. ((required, string) The name of the author of the tag.)
        """
        def set_TaggerName(self, value):
            InputSet._set_input(self, 'TaggerName', value)

        """
        Set the value of the Type input for this choreography. ((required, string) The type of object that is being tagged. Valid values are: commit, tree, or blob.)
        """
        def set_Type(self, value):
            InputSet._set_input(self, 'Type', value)

        """
        Set the value of the User input for this choreography. ((required, string) The GitHub username.)
        """
        def set_User(self, value):
            InputSet._set_input(self, 'User', value)


"""
A ResultSet with methods tailored to the values returned by the CreateTag choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class CreateTagResultSet(ResultSet):
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

class CreateTagChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return CreateTagResultSet(response, path)
