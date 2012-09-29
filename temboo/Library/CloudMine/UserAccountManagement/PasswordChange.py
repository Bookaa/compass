# -*- coding: utf-8 -*-

###############################################################################
#
# PasswordChange
# Updates a user's password.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class PasswordChange(Choreography):

    """
    Create a new instance of the PasswordChange Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/CloudMine/UserAccountManagement/PasswordChange')


    def new_input_set(self):
        return PasswordChangeInputSet()

    def _make_result_set(self, result, path):
        return PasswordChangeResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return PasswordChangeChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the PasswordChange
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class PasswordChangeInputSet(InputSet):
        """
        Set the value of the APIKey input for this choreography. ((required, string) The API Key provided by CloudMine after registering your app.)
        """
        def set_APIKey(self, value):
            InputSet._set_input(self, 'APIKey', value)

        """
        Set the value of the ApplicationIdentifier input for this choreography. ((required, string) The application identifier provided by CloudMine after registering your app.)
        """
        def set_ApplicationIdentifier(self, value):
            InputSet._set_input(self, 'ApplicationIdentifier', value)

        """
        Set the value of the NewPassword input for this choreography. ((required, string) The user's new password.)
        """
        def set_NewPassword(self, value):
            InputSet._set_input(self, 'NewPassword', value)

        """
        Set the value of the Password input for this choreography. ((required, string) The password for the user that needs to authenticate.)
        """
        def set_Password(self, value):
            InputSet._set_input(self, 'Password', value)

        """
        Set the value of the Username input for this choreography. ((required, string) The username for the user that needs to authenticate.)
        """
        def set_Username(self, value):
            InputSet._set_input(self, 'Username', value)


"""
A ResultSet with methods tailored to the values returned by the PasswordChange choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class PasswordChangeResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((json) The response from CloudMine.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class PasswordChangeChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return PasswordChangeResultSet(response, path)
