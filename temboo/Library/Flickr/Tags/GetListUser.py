# -*- coding: utf-8 -*-

###############################################################################
#
# GetListUser
# Retrieves the tag list for a given user (or the currently logged in user).
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class GetListUser(Choreography):

    """
    Create a new instance of the GetListUser Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Flickr/Tags/GetListUser')


    def new_input_set(self):
        return GetListUserInputSet()

    def _make_result_set(self, result, path):
        return GetListUserResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetListUserChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the GetListUser
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class GetListUserInputSet(InputSet):
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
        Set the value of the UserId input for this choreography. ((optional, integer) The NSID of the user to fetch the tag list for. If not provided, the authenticated user is assumed.)
        """
        def set_UserId(self, value):
            InputSet._set_input(self, 'UserId', value)


"""
A ResultSet with methods tailored to the values returned by the GetListUser choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class GetListUserResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response from Flickr.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class GetListUserChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetListUserResultSet(response, path)
