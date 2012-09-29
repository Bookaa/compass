# -*- coding: utf-8 -*-

###############################################################################
#
# LinkNewUser
# Allows your application to sign up and login users by linking them to other services such as Twitter or Facebook.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class LinkNewUser(Choreography):

    """
    Create a new instance of the LinkNewUser Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Parse/Users/LinkNewUser')


    def new_input_set(self):
        return LinkNewUserInputSet()

    def _make_result_set(self, result, path):
        return LinkNewUserResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return LinkNewUserChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the LinkNewUser
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class LinkNewUserInputSet(InputSet):
        """
        Set the value of the AuthData input for this choreography. ((required, json) A JSON string containing the authentication data of the user you want to link with another service. See documentation for more formatting details.)
        """
        def set_AuthData(self, value):
            InputSet._set_input(self, 'AuthData', value)

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
A ResultSet with methods tailored to the values returned by the LinkNewUser choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class LinkNewUserResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((json) The response from Parse.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class LinkNewUserChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return LinkNewUserResultSet(response, path)
