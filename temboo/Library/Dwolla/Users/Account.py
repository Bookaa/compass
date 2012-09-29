# -*- coding: utf-8 -*-

###############################################################################
#
# Account
# Retrieves the account information for the user associated with the given authorized access token.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class Account(Choreography):

    """
    Create a new instance of the Account Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Dwolla/Users/Account')


    def new_input_set(self):
        return AccountInputSet()

    def _make_result_set(self, result, path):
        return AccountResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return AccountChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the Account
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class AccountInputSet(InputSet):
        """
        Set the value of the AccessToken input for this choreography. ((required, string) A valid OAuth token.)
        """
        def set_AccessToken(self, value):
            InputSet._set_input(self, 'AccessToken', value)


"""
A ResultSet with methods tailored to the values returned by the Account choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class AccountResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((json) The response from Dwolla.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class AccountChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return AccountResultSet(response, path)
