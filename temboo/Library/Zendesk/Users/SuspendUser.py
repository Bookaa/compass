# -*- coding: utf-8 -*-

###############################################################################
#
# SuspendUser
# Suspends an existing user.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class SuspendUser(Choreography):

    """
    Create a new instance of the SuspendUser Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Zendesk/Users/SuspendUser')


    def new_input_set(self):
        return SuspendUserInputSet()

    def _make_result_set(self, result, path):
        return SuspendUserResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return SuspendUserChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the SuspendUser
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class SuspendUserInputSet(InputSet):
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
        Set the value of the Server input for this choreography. ((required, string) Your Zendesk domain and subdomain (i.e. temboocare.zendesk.com).)
        """
        def set_Server(self, value):
            InputSet._set_input(self, 'Server', value)

        """
        Set the value of the UserID input for this choreography. ((required, integer) The id of the user being updated.)
        """
        def set_UserID(self, value):
            InputSet._set_input(self, 'UserID', value)


"""
A ResultSet with methods tailored to the values returned by the SuspendUser choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class SuspendUserResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((json) The response from Zendesk.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class SuspendUserChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return SuspendUserResultSet(response, path)
