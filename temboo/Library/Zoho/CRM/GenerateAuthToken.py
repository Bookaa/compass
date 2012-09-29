# -*- coding: utf-8 -*-

###############################################################################
#
# GenerateAuthToken
# Generates an authentication token.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class GenerateAuthToken(Choreography):

    """
    Create a new instance of the GenerateAuthToken Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Zoho/CRM/GenerateAuthToken')


    def new_input_set(self):
        return GenerateAuthTokenInputSet()

    def _make_result_set(self, result, path):
        return GenerateAuthTokenResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GenerateAuthTokenChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the GenerateAuthToken
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class GenerateAuthTokenInputSet(InputSet):
        """
        Set the value of the Password input for this choreography. ((required, string) Your Zoho password.)
        """
        def set_Password(self, value):
            InputSet._set_input(self, 'Password', value)

        """
        Set the value of the Username input for this choreography. ((required, string) Your Zoho CRM username.)
        """
        def set_Username(self, value):
            InputSet._set_input(self, 'Username', value)


"""
A ResultSet with methods tailored to the values returned by the GenerateAuthToken choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class GenerateAuthTokenResultSet(ResultSet):
        """
        Retrieve the value for the "AuthenticationToken" output from this choreography execution. ((string) The authentication token returned from Zoho.)
        """
        def get_AuthenticationToken(self):
            return self._output.get('AuthenticationToken', None)

class GenerateAuthTokenChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GenerateAuthTokenResultSet(response, path)
