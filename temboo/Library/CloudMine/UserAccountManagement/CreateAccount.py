# -*- coding: utf-8 -*-

###############################################################################
#
# CreateAccount
# Creates a user account with a given username and password.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class CreateAccount(Choreography):

    """
    Create a new instance of the CreateAccount Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/CloudMine/UserAccountManagement/CreateAccount')


    def new_input_set(self):
        return CreateAccountInputSet()

    def _make_result_set(self, result, path):
        return CreateAccountResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CreateAccountChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the CreateAccount
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class CreateAccountInputSet(InputSet):
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
        Set the value of the Latitude input for this choreography. ((optional, decimal) The latitude coordinate of the user's location. If provide, Longitude is also required.)
        """
        def set_Latitude(self, value):
            InputSet._set_input(self, 'Latitude', value)

        """
        Set the value of the Longitude input for this choreography. ((optional, decimal) The longitude coordinate of the user's location. If provide, Latitude is also required.)
        """
        def set_Longitude(self, value):
            InputSet._set_input(self, 'Longitude', value)

        """
        Set the value of the Name input for this choreography. ((optional, string) A name to associated with the user profile information.)
        """
        def set_Name(self, value):
            InputSet._set_input(self, 'Name', value)

        """
        Set the value of the Password input for this choreography. ((required, string) The password for the account that is being created.)
        """
        def set_Password(self, value):
            InputSet._set_input(self, 'Password', value)

        """
        Set the value of the Username input for this choreography. ((required, string) The username for the account that is being created.)
        """
        def set_Username(self, value):
            InputSet._set_input(self, 'Username', value)


"""
A ResultSet with methods tailored to the values returned by the CreateAccount choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class CreateAccountResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((json) The response from CloudMine.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class CreateAccountChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return CreateAccountResultSet(response, path)
