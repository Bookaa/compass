# -*- coding: utf-8 -*-

###############################################################################
#
# GetFriendsByID
# Retrieves a list of numeric IDs for every user the specified user is following.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class GetFriendsByID(Choreography):

    """
    Create a new instance of the GetFriendsByID Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Twitter/FriendsAndFollowers/GetFriendsByID')


    def new_input_set(self):
        return GetFriendsByIDInputSet()

    def _make_result_set(self, result, path):
        return GetFriendsByIDResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetFriendsByIDChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the GetFriendsByID
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class GetFriendsByIDInputSet(InputSet):
        """
        Set the value of the AccessTokenSecret input for this choreography. ((conditional, string) The Access Token Secret provided by Twitter or retrieved during the OAuth process.)
        """
        def set_AccessTokenSecret(self, value):
            InputSet._set_input(self, 'AccessTokenSecret', value)

        """
        Set the value of the AccessToken input for this choreography. ((conditional, string) The Access Token provided by Twitter or retrieved during the OAuth process.)
        """
        def set_AccessToken(self, value):
            InputSet._set_input(self, 'AccessToken', value)

        """
        Set the value of the ConsumerKey input for this choreography. ((conditional, string) The Consumer Key provided by Twitter.)
        """
        def set_ConsumerKey(self, value):
            InputSet._set_input(self, 'ConsumerKey', value)

        """
        Set the value of the ConsumerSecret input for this choreography. ((conditional, string) The Consumer Secret provided by Twitter.)
        """
        def set_ConsumerSecret(self, value):
            InputSet._set_input(self, 'ConsumerSecret', value)

        """
        Set the value of the ResponseFormat input for this choreography. ((optional, string) Specify the format of the response from Twitter: json, or xml.  Default is set to xml.)
        """
        def set_ResponseFormat(self, value):
            InputSet._set_input(self, 'ResponseFormat', value)

        """
        Set the value of the ScreenName input for this choreography. ((conditional, string) Used to retrieve the followers of another Twitter user. Required if UserId isn't specified.)
        """
        def set_ScreenName(self, value):
            InputSet._set_input(self, 'ScreenName', value)

        """
        Set the value of the UserID input for this choreography. ((conditional, integer) Used to retrieve the followers of another Twitter user. Required if ScreenName isn't specified.)
        """
        def set_UserID(self, value):
            InputSet._set_input(self, 'UserID', value)


"""
A ResultSet with methods tailored to the values returned by the GetFriendsByID choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class GetFriendsByIDResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The response from Twitter.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class GetFriendsByIDChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetFriendsByIDResultSet(response, path)
