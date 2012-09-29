# -*- coding: utf-8 -*-

###############################################################################
#
# AddFavoriteActivity
# Adds a specified activity to a user's favorite activities list.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class AddFavoriteActivity(Choreography):

    """
    Create a new instance of the AddFavoriteActivity Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Fitbit/AddFavoriteActivity')


    def new_input_set(self):
        return AddFavoriteActivityInputSet()

    def _make_result_set(self, result, path):
        return AddFavoriteActivityResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return AddFavoriteActivityChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the AddFavoriteActivity
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class AddFavoriteActivityInputSet(InputSet):
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
        Set the value of the ActivityId input for this choreography. ((required, integer) The id of the activity you want to make a favorite.)
        """
        def set_ActivityId(self, value):
            InputSet._set_input(self, 'ActivityId', value)

        """
        Set the value of the ConsumerKey input for this choreography. ((required, string) The Consumer Key provided by Fitbit.)
        """
        def set_ConsumerKey(self, value):
            InputSet._set_input(self, 'ConsumerKey', value)

        """
        Set the value of the ConsumerSecret input for this choreography. ((required, string) The Consumer Secret provided by Fitbit.)
        """
        def set_ConsumerSecret(self, value):
            InputSet._set_input(self, 'ConsumerSecret', value)

        """
        Set the value of the Format input for this choreography. ((optional, string) The format that you want the response to be in: xml or json. Defaults to xml.)
        """
        def set_Format(self, value):
            InputSet._set_input(self, 'Format', value)

        """
        Set the value of the UserId input for this choreography. ((optional, string) The user's encoded id. Defaults to "-" (dash) which will return data for the user associated with the token credentials provided.)
        """
        def set_UserId(self, value):
            InputSet._set_input(self, 'UserId', value)


"""
A ResultSet with methods tailored to the values returned by the AddFavoriteActivity choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class AddFavoriteActivityResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The response from Fitbit.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class AddFavoriteActivityChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return AddFavoriteActivityResultSet(response, path)
