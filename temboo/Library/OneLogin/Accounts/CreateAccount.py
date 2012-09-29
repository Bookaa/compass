# -*- coding: utf-8 -*-

###############################################################################
#
# CreateAccount
# Creates a new account.
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
        Choreography.__init__(self, temboo_session, '/Library/OneLogin/Accounts/CreateAccount')


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
        Set the value of the APIKey input for this choreography. ((required, string) The API Key provided by OneLogin.)
        """
        def set_APIKey(self, value):
            InputSet._set_input(self, 'APIKey', value)

        """
        Set the value of the AccountName input for this choreography. ((required, string) The account name.)
        """
        def set_AccountName(self, value):
            InputSet._set_input(self, 'AccountName', value)

        """
        Set the value of the Address input for this choreography. ((optional, string) The street address for the new account.)
        """
        def set_Address(self, value):
            InputSet._set_input(self, 'Address', value)

        """
        Set the value of the City input for this choreography. ((optional, string) The city associated with the address.)
        """
        def set_City(self, value):
            InputSet._set_input(self, 'City', value)

        """
        Set the value of the Country input for this choreography. ((optional, string) The country associated with the address of the new account.)
        """
        def set_Country(self, value):
            InputSet._set_input(self, 'Country', value)

        """
        Set the value of the Email input for this choreography. ((required, string) The email address for the new account.)
        """
        def set_Email(self, value):
            InputSet._set_input(self, 'Email', value)

        """
        Set the value of the FirstName input for this choreography. ((required, string) The first name on the new account.)
        """
        def set_FirstName(self, value):
            InputSet._set_input(self, 'FirstName', value)

        """
        Set the value of the LastName input for this choreography. ((required, string) The last name on the new account.)
        """
        def set_LastName(self, value):
            InputSet._set_input(self, 'LastName', value)

        """
        Set the value of the Phone input for this choreography. ((optional, string) The phone number for the new account.)
        """
        def set_Phone(self, value):
            InputSet._set_input(self, 'Phone', value)

        """
        Set the value of the Plan input for this choreography. ((required, string) Indicates which plan the new account has (i.e. enterprise).)
        """
        def set_Plan(self, value):
            InputSet._set_input(self, 'Plan', value)

        """
        Set the value of the State input for this choreography. ((optional, string) The state associated with the address of the new account.)
        """
        def set_State(self, value):
            InputSet._set_input(self, 'State', value)

        """
        Set the value of the Zip input for this choreography. ((optional, string) The postal code associated with the address of the new account.)
        """
        def set_Zip(self, value):
            InputSet._set_input(self, 'Zip', value)


"""
A ResultSet with methods tailored to the values returned by the CreateAccount choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class CreateAccountResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response from OneLogin.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class CreateAccountChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return CreateAccountResultSet(response, path)
