# -*- coding: utf-8 -*-

###############################################################################
#
# UnfollowUser
# List posts made by a user.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class UnfollowUser(Choreography):

    """
    Create a new instance of the UnfollowUser Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Disqus/Users/UnfollowUser')


    def new_input_set(self):
        return UnfollowUserInputSet()

    def _make_result_set(self, result, path):
        return UnfollowUserResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return UnfollowUserChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the UnfollowUser
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class UnfollowUserInputSet(InputSet):
        """
        Set the value of the AccessToken input for this choreography. ((required, string) A valid OAuth 2.0 access token.)
        """
        def set_AccessToken(self, value):
            InputSet._set_input(self, 'AccessToken', value)

        """
        Set the value of the PublicKey input for this choreography. ((required, string) The Public Key provided by Disqus (AKA the Client ID).)
        """
        def set_PublicKey(self, value):
            InputSet._set_input(self, 'PublicKey', value)

        """
        Set the value of the ResponseFormat input for this choreography. ((optional, string) The format that the response should be in. Valid values are: json (the default), jsonp, or rss.)
        """
        def set_ResponseFormat(self, value):
            InputSet._set_input(self, 'ResponseFormat', value)

        """
        Set the value of the UserID input for this choreography. ((conditional, string) The User ID that is to be unfollowed. If UserID is set, then Username must be null.)
        """
        def set_UserID(self, value):
            InputSet._set_input(self, 'UserID', value)

        """
        Set the value of the Username input for this choreography. ((conditional, string) A Disqus username.  If Username is being set, then UserID must be null.)
        """
        def set_Username(self, value):
            InputSet._set_input(self, 'Username', value)


"""
A ResultSet with methods tailored to the values returned by the UnfollowUser choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class UnfollowUserResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The response from Disqus.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class UnfollowUserChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return UnfollowUserResultSet(response, path)
