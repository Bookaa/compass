# -*- coding: utf-8 -*-

###############################################################################
#
# Find
# Returns a list of place IDs for a query string.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class Find(Choreography):

    """
    Create a new instance of the Find Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Flickr/Places/Find')


    def new_input_set(self):
        return FindInputSet()

    def _make_result_set(self, result, path):
        return FindResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return FindChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the Find
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class FindInputSet(InputSet):
        """
        Set the value of the APIKey input for this choreography. ((required, string) The API Key provided by Flickr (AKA the OAuth Consumer Key).)
        """
        def set_APIKey(self, value):
            InputSet._set_input(self, 'APIKey', value)

        """
        Set the value of the APISecret input for this choreography. ((conditional, string) The API Secret provided by Flickr (AKA the OAuth Consumer Secret).)
        """
        def set_APISecret(self, value):
            InputSet._set_input(self, 'APISecret', value)

        """
        Set the value of the AccessTokenSecret input for this choreography. ((conditional, string) The Access Token Secret retrieved during the OAuth process.)
        """
        def set_AccessTokenSecret(self, value):
            InputSet._set_input(self, 'AccessTokenSecret', value)

        """
        Set the value of the AccessToken input for this choreography. ((conditional, string) The Access Token retrieved during the OAuth process.)
        """
        def set_AccessToken(self, value):
            InputSet._set_input(self, 'AccessToken', value)

        """
        Set the value of the Query input for this choreography. ((required, string) The query string to use for place ID lookups.)
        """
        def set_Query(self, value):
            InputSet._set_input(self, 'Query', value)


"""
A ResultSet with methods tailored to the values returned by the Find choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class FindResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response from Flickr.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class FindChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return FindResultSet(response, path)
