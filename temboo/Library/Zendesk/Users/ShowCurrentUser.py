# -*- coding: utf-8 -*-

###############################################################################
#
# ShowCurrentUser
# Returns information about the currently authenticated user.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class ShowCurrentUser(Choreography):

    """
    Create a new instance of the ShowCurrentUser Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Zendesk/Users/ShowCurrentUser')


    def new_input_set(self):
        return ShowCurrentUserInputSet()

    def _make_result_set(self, result, path):
        return ShowCurrentUserResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ShowCurrentUserChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the ShowCurrentUser
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class ShowCurrentUserInputSet(InputSet):
        """
        Set the value of the Email input for this choreography. ((required, string) The email to authenticate the Zendesk account.)
        """
        def set_Email(self, value):
            InputSet._set_input(self, 'Email', value)

        """
        Set the value of the Password input for this choreography. ((required, string) The password matching the email to authenticate the Zendesk account.)
        """
        def set_Password(self, value):
            InputSet._set_input(self, 'Password', value)

        """
        Set the value of the Server input for this choreography. ((required, string) The server URL associated with your Zendesk account. In many cases this looks like: temboo.zendesk.com but may also be customized: support.temboo.com)
        """
        def set_Server(self, value):
            InputSet._set_input(self, 'Server', value)


"""
A ResultSet with methods tailored to the values returned by the ShowCurrentUser choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class ShowCurrentUserResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The response from Zendesk.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class ShowCurrentUserChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ShowCurrentUserResultSet(response, path)
