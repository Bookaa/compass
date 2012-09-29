# -*- coding: utf-8 -*-

###############################################################################
#
# UserContacts
# Retrieves the information for contacts for the user assoicated with the authorized access token.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class UserContacts(Choreography):

    """
    Create a new instance of the UserContacts Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Dwolla/Contacts/UserContacts')


    def new_input_set(self):
        return UserContactsInputSet()

    def _make_result_set(self, result, path):
        return UserContactsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return UserContactsChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the UserContacts
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class UserContactsInputSet(InputSet):
        """
        Set the value of the AccessToken input for this choreography. ((required, string) A valid OAuth token.)
        """
        def set_AccessToken(self, value):
            InputSet._set_input(self, 'AccessToken', value)

        """
        Set the value of the Limit input for this choreography. ((optional, integer) Number of contacts to retrieve. Defaults to 10. Can be between 1 and 200 contacts.)
        """
        def set_Limit(self, value):
            InputSet._set_input(self, 'Limit', value)

        """
        Set the value of the Search input for this choreography. ((optional, string) Search term used to search the contacts.)
        """
        def set_Search(self, value):
            InputSet._set_input(self, 'Search', value)

        """
        Set the value of the Types input for this choreography. ((optional, string) Type of accounts to retrieve, in the form of a comma-separated list (e.g. "Facebook,Dwolla"))
        """
        def set_Types(self, value):
            InputSet._set_input(self, 'Types', value)


"""
A ResultSet with methods tailored to the values returned by the UserContacts choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class UserContactsResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((json) The response from Dwolla.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class UserContactsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return UserContactsResultSet(response, path)
