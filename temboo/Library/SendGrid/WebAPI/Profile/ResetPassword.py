# -*- coding: utf-8 -*-

###############################################################################
#
# ResetPassword
# Reset a SendGrid account password.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class ResetPassword(Choreography):

    """
    Create a new instance of the ResetPassword Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/SendGrid/WebAPI/Profile/ResetPassword')


    def new_input_set(self):
        return ResetPasswordInputSet()

    def _make_result_set(self, result, path):
        return ResetPasswordResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ResetPasswordChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the ResetPassword
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class ResetPasswordInputSet(InputSet):
        """
        Set the value of the APIKey input for this choreography. ((required, string) Enter a SendGrid API Key.)
        """
        def set_APIKey(self, value):
            InputSet._set_input(self, 'APIKey', value)

        """
        Set the value of the APIUser input for this choreography. ((required, string) Enter a SendGrid username.)
        """
        def set_APIUser(self, value):
            InputSet._set_input(self, 'APIUser', value)

        """
        Set the value of the ConfirmPassword input for this choreography. ((required, string) Re-enter the new account password.  Must match the string entered in the Password variable.  Minumum password length is 6 characters.)
        """
        def set_ConfirmPassword(self, value):
            InputSet._set_input(self, 'ConfirmPassword', value)

        """
        Set the value of the Password input for this choreography. ((required, string) Enter a new account password of 6 characters or more.)
        """
        def set_Password(self, value):
            InputSet._set_input(self, 'Password', value)

        """
        Set the value of the ResponseFormat input for this choreography. ((optional, string) Specify the format of the response from SendGrid: json, or xml.  Default is set to json.)
        """
        def set_ResponseFormat(self, value):
            InputSet._set_input(self, 'ResponseFormat', value)

        """
        Set the value of the VaultFile input for this choreography. ()
        """


"""
A ResultSet with methods tailored to the values returned by the ResetPassword choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class ResetPasswordResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The response from SendGrid. The format corresponds to the ResponseFormat input. Default is json.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class ResetPasswordChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ResetPasswordResultSet(response, path)
