# -*- coding: utf-8 -*-

###############################################################################
#
# ListAllUsers
# Retrieves a list of all existing users.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class ListAllUsers(Choreography):

    """
    Create a new instance of the ListAllUsers Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Zendesk/Users/ListAllUsers')


    def new_input_set(self):
        return ListAllUsersInputSet()

    def _make_result_set(self, result, path):
        return ListAllUsersResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ListAllUsersChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the ListAllUsers
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class ListAllUsersInputSet(InputSet):
        """
        Set the value of the Email input for this choreography. ((required, string) The email to authenticate the Zendesk account.)
        """
        def set_Email(self, value):
            InputSet._set_input(self, 'Email', value)

        """
        Set the value of the Number input for this choreography. ((optional, integer) The number of results to return per page. Maximum is 100 and default is 100.)
        """
        def set_Number(self, value):
            InputSet._set_input(self, 'Number', value)

        """
        Set the value of the Page input for this choreography. ((optional, integer) The page number of the results to be returned. Used together with the Number parameter to paginate a large set of results.)
        """
        def set_Page(self, value):
            InputSet._set_input(self, 'Page', value)

        """
        Set the value of the Password input for this choreography. ((required, string) The password matching the email to authenticate the Zendesk account.)
        """
        def set_Password(self, value):
            InputSet._set_input(self, 'Password', value)

        """
        Set the value of the Server input for this choreography. ((required, string) The server URL associated with your Zendesk account. In many cases this looks like: temboo.zendesk.com but may also be customized: support.temboo.com)
        """
        def set_Server(self, value):
            InputSet._set_input(self, 'Server', value)


"""
A ResultSet with methods tailored to the values returned by the ListAllUsers choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class ListAllUsersResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((json) The response from Zendesk.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class ListAllUsersChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ListAllUsersResultSet(response, path)
