# -*- coding: utf-8 -*-

###############################################################################
#
# CreateUser
# Creates a new user.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class CreateUser(Choreography):

    """
    Create a new instance of the CreateUser Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Zendesk/Users/CreateUser')


    def new_input_set(self):
        return CreateUserInputSet()

    def _make_result_set(self, result, path):
        return CreateUserResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CreateUserChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the CreateUser
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class CreateUserInputSet(InputSet):
        """
        Set the value of the Email input for this choreography. ((required, string) The email address you use to login to your Zendesk account.)
        """
        def set_Email(self, value):
            InputSet._set_input(self, 'Email', value)

        """
        Set the value of the Password input for this choreography. ((required, string) Your Zendesk password.)
        """
        def set_Password(self, value):
            InputSet._set_input(self, 'Password', value)

        """
        Set the value of the Server input for this choreography. ((required, string) Your Zendesk domain and subdomain (i.e. support.temboo.com or temboo.zendesk.com).)
        """
        def set_Server(self, value):
            InputSet._set_input(self, 'Server', value)

        """
        Set the value of the UserData input for this choreography. ((required, json) A JSON string containing the new user's information. See documentation for formatting details.)
        """
        def set_UserData(self, value):
            InputSet._set_input(self, 'UserData', value)


"""
A ResultSet with methods tailored to the values returned by the CreateUser choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class CreateUserResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((json) )
        """
        def get_Response(self):
            return self._output.get('Response', None)

class CreateUserChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return CreateUserResultSet(response, path)
