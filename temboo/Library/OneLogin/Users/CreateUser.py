# -*- coding: utf-8 -*-

###############################################################################
#
# CreateUser
# Creates a new user.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class CreateUser(Choreography):

    """
    Create a new instance of the CreateUser Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/OneLogin/Users/CreateUser')


    def new_input_set(self):
        return CreateUserInputSet()

    def _make_result_set(self, result, path):
        return CreateUserResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CreateUserChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the CreateUser
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class CreateUserInputSet(InputSet):
        """
        Set the value of the APIKey input for this choreography. ((required, string) The API Key provided by OneLogin.)
        """
        def set_APIKey(self, value):
            InputSet._set_input(self, 'APIKey', value)

        """
        Set the value of the Address input for this choreography. ((conditional, string) The street address for the new account.)
        """
        def set_Address(self, value):
            InputSet._set_input(self, 'Address', value)

        """
        Set the value of the Email input for this choreography. ((conditional, string) The email address for the new user.)
        """
        def set_Email(self, value):
            InputSet._set_input(self, 'Email', value)

        """
        Set the value of the FirstName input for this choreography. ((conditional, string) The first name of the new user.)
        """
        def set_FirstName(self, value):
            InputSet._set_input(self, 'FirstName', value)

        """
        Set the value of the GroupID input for this choreography. ((optional, string) The group id associated with the new user.)
        """
        def set_GroupID(self, value):
            InputSet._set_input(self, 'GroupID', value)

        """
        Set the value of the LastName input for this choreography. ((conditional, string) The last name of the new user.)
        """
        def set_LastName(self, value):
            InputSet._set_input(self, 'LastName', value)

        """
        Set the value of the OpenIDName input for this choreography. ((conditional, string) The open id name.)
        """
        def set_OpenIDName(self, value):
            InputSet._set_input(self, 'OpenIDName', value)

        """
        Set the value of the Phone input for this choreography. ((conditional, string) The phone number of the new user.)
        """
        def set_Phone(self, value):
            InputSet._set_input(self, 'Phone', value)


"""
A ResultSet with methods tailored to the values returned by the CreateUser choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class CreateUserResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response from OneLogin.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class CreateUserChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return CreateUserResultSet(response, path)
