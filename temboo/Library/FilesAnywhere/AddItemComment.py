# -*- coding: utf-8 -*-

###############################################################################
#
# AddItemComment
# Add a comment to an item.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class AddItemComment(Choreography):

    """
    Create a new instance of the AddItemComment Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/FilesAnywhere/AddItemComment')


    def new_input_set(self):
        return AddItemCommentInputSet()

    def _make_result_set(self, result, path):
        return AddItemCommentResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return AddItemCommentChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the AddItemComment
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class AddItemCommentInputSet(InputSet):
        """
        Set the value of the APIKey input for this choreography. ((conditional, string) The API Key provided by FilesAnywhere. Required unless supplying a valid Token input.)
        """
        def set_APIKey(self, value):
            InputSet._set_input(self, 'APIKey', value)

        """
        Set the value of the Comment input for this choreography. ((required, string) Enter item comment.)
        """
        def set_Comment(self, value):
            InputSet._set_input(self, 'Comment', value)

        """
        Set the value of the FullName input for this choreography. ((required, string) Provide the full name of the user entering the comment.)
        """
        def set_FullName(self, value):
            InputSet._set_input(self, 'FullName', value)

        """
        Set the value of the ParentID input for this choreography. ((required, integer) Specify the ID of the parent comment.)
        """
        def set_ParentID(self, value):
            InputSet._set_input(self, 'ParentID', value)

        """
        Set the value of the Password input for this choreography. ((conditional, string) Your FilesAnywhere password. Required unless supplying a valid Token input.)
        """
        def set_Password(self, value):
            InputSet._set_input(self, 'Password', value)

        """
        Set the value of the Path input for this choreography. ((required, string) Enter the path to the item in the following format: \USERNAME\file.txt)
        """
        def set_Path(self, value):
            InputSet._set_input(self, 'Path', value)

        """
        Set the value of the Token input for this choreography. ((conditional, string) If provided, the Choreo will use the token to authenticate. If the token is expired or not provided, the Choreo will relogin and retrieve a new token when APIKey, Username, and Password are supplied.)
        """
        def set_Token(self, value):
            InputSet._set_input(self, 'Token', value)

        """
        Set the value of the Username input for this choreography. ((conditional, string) Your FilesAnywhere username. Required unless supplying a valid Token input.)
        """
        def set_Username(self, value):
            InputSet._set_input(self, 'Username', value)


"""
A ResultSet with methods tailored to the values returned by the AddItemComment choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class AddItemCommentResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response from FilesAnywhere.)
        """
        def get_Response(self):
            return self._output.get('Response', None)
        """
        Retrieve the value for the "Token" output from this choreography execution. ((conditional, string) If provided, the Choreo will use the token to authenticate. If the token is expired or not provided, the Choreo will relogin and retrieve a new token when APIKey, Username, and Password are supplied.)
        """
        def get_Token(self):
            return self._output.get('Token', None)

class AddItemCommentChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return AddItemCommentResultSet(response, path)
