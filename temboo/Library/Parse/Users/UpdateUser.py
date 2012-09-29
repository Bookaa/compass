# -*- coding: utf-8 -*-

###############################################################################
#
# UpdateUser
# Updates information for an existing user.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class UpdateUser(Choreography):

    """
    Create a new instance of the UpdateUser Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Parse/Users/UpdateUser')


    def new_input_set(self):
        return UpdateUserInputSet()

    def _make_result_set(self, result, path):
        return UpdateUserResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return UpdateUserChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the UpdateUser
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class UpdateUserInputSet(InputSet):
        """
        Set the value of the UserInformation input for this choreography. ((required, json) A JSON string containing the user information to update.)
        """
        def set_UserInformation(self, value):
            InputSet._set_input(self, 'UserInformation', value)

        """
        Set the value of the ApplicationID input for this choreography. ((required, string) The Application ID provided by Parse.)
        """
        def set_ApplicationID(self, value):
            InputSet._set_input(self, 'ApplicationID', value)

        """
        Set the value of the ObjectID input for this choreography. ((required, string) The ID of the user to update.)
        """
        def set_ObjectID(self, value):
            InputSet._set_input(self, 'ObjectID', value)

        """
        Set the value of the RESTAPIKey input for this choreography. ((required, string) The REST API Key provided by Parse.)
        """
        def set_RESTAPIKey(self, value):
            InputSet._set_input(self, 'RESTAPIKey', value)

        """
        Set the value of the SessionToken input for this choreography. ((required, string) A valid Session Token. Note that Session Tokens can be retrieved by the Login and SignUp Choreos.)
        """
        def set_SessionToken(self, value):
            InputSet._set_input(self, 'SessionToken', value)


"""
A ResultSet with methods tailored to the values returned by the UpdateUser choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class UpdateUserResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((json) The response from Parse.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class UpdateUserChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return UpdateUserResultSet(response, path)
