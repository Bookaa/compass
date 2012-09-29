# -*- coding: utf-8 -*-

###############################################################################
#
# GetUserConnections
# Returns a list of connections associated with the profile of the current user.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class GetUserConnections(Choreography):

    """
    Create a new instance of the GetUserConnections Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/LinkedIn/PeopleAndConnections/GetUserConnections')


    def new_input_set(self):
        return GetUserConnectionsInputSet()

    def _make_result_set(self, result, path):
        return GetUserConnectionsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetUserConnectionsChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the GetUserConnections
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class GetUserConnectionsInputSet(InputSet):
        """
        Set the value of the APIKey input for this choreography. ((required, string) The API Key provided by LinkedIn (AKA the OAuth Consumer Key).)
        """
        def set_APIKey(self, value):
            InputSet._set_input(self, 'APIKey', value)

        """
        Set the value of the AccessTokenSecret input for this choreography. ((required, string) The Access Token Secret retrieved during the OAuth process.)
        """
        def set_AccessTokenSecret(self, value):
            InputSet._set_input(self, 'AccessTokenSecret', value)

        """
        Set the value of the AccessToken input for this choreography. ((required, string) The Access Token retrieved during the OAuth process.)
        """
        def set_AccessToken(self, value):
            InputSet._set_input(self, 'AccessToken', value)

        """
        Set the value of the SecretKey input for this choreography. ((required, string) The Secret Key provided by LinkedIn (AKA the OAuth Consumer Secret).)
        """
        def set_SecretKey(self, value):
            InputSet._set_input(self, 'SecretKey', value)


"""
A ResultSet with methods tailored to the values returned by the GetUserConnections choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class GetUserConnectionsResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response from LinkedIn in XML format.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class GetUserConnectionsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetUserConnectionsResultSet(response, path)
