# -*- coding: utf-8 -*-

###############################################################################
#
# SearchAnonymous
# Allows anonymous users to search public forums.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class SearchAnonymous(Choreography):

    """
    Create a new instance of the SearchAnonymous Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Zendesk/Search/SearchAnonymous')


    def new_input_set(self):
        return SearchAnonymousInputSet()

    def _make_result_set(self, result, path):
        return SearchAnonymousResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return SearchAnonymousChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the SearchAnonymous
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class SearchAnonymousInputSet(InputSet):
        """
        Set the value of the Email input for this choreography. ((required, string) The email to authenticate the Zendesk account.)
        """
        def set_Email(self, value):
            InputSet._set_input(self, 'Email', value)

        """
        Set the value of the Password input for this choreography. ((required, string) The password matching the email to authenticate the Zendesk account.)
        """
        def set_Password(self, value):
            InputSet._set_input(self, 'Password', value)

        """
        Set the value of the Query input for this choreography. ((required, string) Perform a search across usernames or email addresses.)
        """
        def set_Query(self, value):
            InputSet._set_input(self, 'Query', value)

        """
        Set the value of the Server input for this choreography. ((required, string) The server URL associated with your Zendesk account. In many cases this looks like: temboo.zendesk.com but may also be customized: support.temboo.com)
        """
        def set_Server(self, value):
            InputSet._set_input(self, 'Server', value)

        """
        Set the value of the SortBy input for this choreography. ((optional, string) Acceptable values: updated_at, created_at, priority, status, ticket_type.)
        """
        def set_SortBy(self, value):
            InputSet._set_input(self, 'SortBy', value)

        """
        Set the value of the SortOrder input for this choreography. ((optional, string) Indicate either: relevance, asc (for ascending), desc (for descending). Defaults to relevance.)
        """
        def set_SortOrder(self, value):
            InputSet._set_input(self, 'SortOrder', value)


"""
A ResultSet with methods tailored to the values returned by the SearchAnonymous choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class SearchAnonymousResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((json) The response from Zendesk.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class SearchAnonymousChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return SearchAnonymousResultSet(response, path)
