# -*- coding: utf-8 -*-

###############################################################################
#
# SignUp
# Allows your application to sign up a new user.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class SignUp(Choreography):

    """
    Create a new instance of the SignUp Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Parse/Users/SignUp')


    def new_input_set(self):
        return SignUpInputSet()

    def _make_result_set(self, result, path):
        return SignUpResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return SignUpChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the SignUp
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class SignUpInputSet(InputSet):
        """
        Set the value of the User input for this choreography. ((required, json) A JSON string containing the new user information.)
        """
        def set_User(self, value):
            InputSet._set_input(self, 'User', value)

        """
        Set the value of the ApplicationID input for this choreography. ((required, string) The Application ID provided by Parse.)
        """
        def set_ApplicationID(self, value):
            InputSet._set_input(self, 'ApplicationID', value)

        """
        Set the value of the RESTAPIKey input for this choreography. ((required, string) The REST API Key provided by Parse.)
        """
        def set_RESTAPIKey(self, value):
            InputSet._set_input(self, 'RESTAPIKey', value)


"""
A ResultSet with methods tailored to the values returned by the SignUp choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class SignUpResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((json) The response from Parse.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class SignUpChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return SignUpResultSet(response, path)
