# -*- coding: utf-8 -*-

###############################################################################
#
# GetRecommendations
# Retrieves a list of catalog title recommendations for a subscriber.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class GetRecommendations(Choreography):

    """
    Create a new instance of the GetRecommendations Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Netflix/GetRecommendations')


    def new_input_set(self):
        return GetRecommendationsInputSet()

    def _make_result_set(self, result, path):
        return GetRecommendationsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetRecommendationsChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the GetRecommendations
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class GetRecommendationsInputSet(InputSet):
        """
        Set the value of the APIKey input for this choreography. ((required, string) The API Key provided by Netflix (AKA the OAuth Consumer Key).)
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
        Set the value of the MaxResults input for this choreography. ((optional, integer) Set this to the maximum number of results to return. This number cannot be greater than 500. If you do not specify max_results, the default value is 25)
        """
        def set_MaxResults(self, value):
            InputSet._set_input(self, 'MaxResults', value)

        """
        Set the value of the SharedSecret input for this choreography. ((required, string) The Shared Secret provided by Netflix (AKA the OAuth Consumer Secret).)
        """
        def set_SharedSecret(self, value):
            InputSet._set_input(self, 'SharedSecret', value)

        """
        Set the value of the StartIndex input for this choreography. ((optional, integer) The offset number of the results from the query.)
        """
        def set_StartIndex(self, value):
            InputSet._set_input(self, 'StartIndex', value)

        """
        Set the value of the UserID input for this choreography. ((required, string) The ID associated with the user whose recommendations you want to retrieve.)
        """
        def set_UserID(self, value):
            InputSet._set_input(self, 'UserID', value)


"""
A ResultSet with methods tailored to the values returned by the GetRecommendations choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class GetRecommendationsResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response from Netflix.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class GetRecommendationsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetRecommendationsResultSet(response, path)
