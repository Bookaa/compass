# -*- coding: utf-8 -*-

###############################################################################
#
# GetListUserPopular
# Retrieves the popular tags for a given user (or the currently logged in user).
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class GetListUserPopular(Choreography):

    """
    Create a new instance of the GetListUserPopular Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Flickr/Tags/GetListUserPopular')


    def new_input_set(self):
        return GetListUserPopularInputSet()

    def _make_result_set(self, result, path):
        return GetListUserPopularResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetListUserPopularChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the GetListUserPopular
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class GetListUserPopularInputSet(InputSet):
        """
        Set the value of the APIKey input for this choreography. ((required, string) The API Key provided by Flickr (AKA the OAuth Consumer Key).)
        """
        def set_APIKey(self, value):
            InputSet._set_input(self, 'APIKey', value)

        """
        Set the value of the APISecret input for this choreography. ((required, string) The API Secret provided by Flickr (AKA the OAuth Consumer Secret).)
        """
        def set_APISecret(self, value):
            InputSet._set_input(self, 'APISecret', value)

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
        Set the value of the Count input for this choreography. ((optional, integer) Number of popular tags to return. defaults to 10 when this argument is not present.)
        """
        def set_Count(self, value):
            InputSet._set_input(self, 'Count', value)

        """
        Set the value of the UserId input for this choreography. ((optional, integer) The NSID of the user to fetch the tag list for. If not provided, the authenticated user is assumed.)
        """
        def set_UserId(self, value):
            InputSet._set_input(self, 'UserId', value)


"""
A ResultSet with methods tailored to the values returned by the GetListUserPopular choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class GetListUserPopularResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response from Flickr.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class GetListUserPopularChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetListUserPopularResultSet(response, path)
