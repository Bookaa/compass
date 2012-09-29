# -*- coding: utf-8 -*-

###############################################################################
#
# PasswordReset
# Allows a user to request a password reset email.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class PasswordReset(Choreography):

    """
    Create a new instance of the PasswordReset Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Parse/Users/PasswordReset')


    def new_input_set(self):
        return PasswordResetInputSet()

    def _make_result_set(self, result, path):
        return PasswordResetResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return PasswordResetChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the PasswordReset
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class PasswordResetInputSet(InputSet):
        """
        Set the value of the EmailAddress input for this choreography. ((required, json) The email address for the user who wishes to reset their password.)
        """
        def set_EmailAddress(self, value):
            InputSet._set_input(self, 'EmailAddress', value)

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
A ResultSet with methods tailored to the values returned by the PasswordReset choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class PasswordResetResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((json) The response from Parse.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class PasswordResetChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return PasswordResetResultSet(response, path)
