# -*- coding: utf-8 -*-

###############################################################################
#
# FriendshipsExist
# Tests for the existence of friendship between two users.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class FriendshipsExist(Choreography):

    """
    Create a new instance of the FriendshipsExist Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Twitter/FriendsAndFollowers/FriendshipsExist')


    def new_input_set(self):
        return FriendshipsExistInputSet()

    def _make_result_set(self, result, path):
        return FriendshipsExistResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return FriendshipsExistChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the FriendshipsExist
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class FriendshipsExistInputSet(InputSet):
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
        Set the value of the ScreenName1 input for this choreography. ((conditional, string) The screen_name of the user you are checking the relationship from. Required unless specifying UserIds instead.)
        """
        def set_ScreenName1(self, value):
            InputSet._set_input(self, 'ScreenName1', value)

        """
        Set the value of the ScreenName2 input for this choreography. ((conditional, string) The screen_name of the user you are checking the relationship to. Required unless specifying UserIds instead.)
        """
        def set_ScreenName2(self, value):
            InputSet._set_input(self, 'ScreenName2', value)

        """
        Set the value of the UserID1 input for this choreography. ((conditional, integer) The ID of the user you are checking the relationship from. Required unless specifying ScreenNames instead.)
        """
        def set_UserID1(self, value):
            InputSet._set_input(self, 'UserID1', value)

        """
        Set the value of the UserID2 input for this choreography. ((conditional, integer) The ID of the user you are checking the relationship to. Required unless specifying ScreenNames instead.)
        """
        def set_UserID2(self, value):
            InputSet._set_input(self, 'UserID2', value)


"""
A ResultSet with methods tailored to the values returned by the FriendshipsExist choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class FriendshipsExistResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The response from Twitter.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class FriendshipsExistChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return FriendshipsExistResultSet(response, path)
