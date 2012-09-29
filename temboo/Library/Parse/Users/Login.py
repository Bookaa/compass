# -*- coding: utf-8 -*-

###############################################################################
#
# Login
# Allows your application to authenticate a given user; returns user information, user-provided fields, and a session token.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class Login(Choreography):

    """
    Create a new instance of the Login Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Parse/Users/Login')


    def new_input_set(self):
        return LoginInputSet()

    def _make_result_set(self, result, path):
        return LoginResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return LoginChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the Login
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class LoginInputSet(InputSet):
        """
        Set the value of the ApplicationID input for this choreography. ((required, string) The Application ID provided by Parse.)
        """
        def set_ApplicationID(self, value):
            InputSet._set_input(self, 'ApplicationID', value)

        """
        Set the value of the Password input for this choreography. ((required, string) The password for the user that is loggin in.)
        """
        def set_Password(self, value):
            InputSet._set_input(self, 'Password', value)

        """
        Set the value of the RESTAPIKey input for this choreography. ((required, string) The REST API Key provided by Parse.)
        """
        def set_RESTAPIKey(self, value):
            InputSet._set_input(self, 'RESTAPIKey', value)

        """
        Set the value of the Username input for this choreography. ((required, string) The username for the user that is authenticating.)
        """
        def set_Username(self, value):
            InputSet._set_input(self, 'Username', value)


"""
A ResultSet with methods tailored to the values returned by the Login choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class LoginResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((json) The response from Parse.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class LoginChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return LoginResultSet(response, path)
