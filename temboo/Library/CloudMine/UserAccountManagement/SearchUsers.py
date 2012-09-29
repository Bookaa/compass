# -*- coding: utf-8 -*-

###############################################################################
#
# SearchUsers
# Allows you to search for users using CloudMine's search query language syntax.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class SearchUsers(Choreography):

    """
    Create a new instance of the SearchUsers Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/CloudMine/UserAccountManagement/SearchUsers')


    def new_input_set(self):
        return SearchUsersInputSet()

    def _make_result_set(self, result, path):
        return SearchUsersResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return SearchUsersChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the SearchUsers
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class SearchUsersInputSet(InputSet):
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
        Set the value of the Query input for this choreography. ((required, string) Search query for which users to retrieve.)
        """
        def set_Query(self, value):
            InputSet._set_input(self, 'Query', value)

        """
        Set the value of the SessionToken input for this choreography. ((required, string) The session token for an existing user (returned by the AccountLogin Choreo).)
        """
        def set_SessionToken(self, value):
            InputSet._set_input(self, 'SessionToken', value)


"""
A ResultSet with methods tailored to the values returned by the SearchUsers choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class SearchUsersResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((json) The response from CloudMine.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class SearchUsersChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return SearchUsersResultSet(response, path)
