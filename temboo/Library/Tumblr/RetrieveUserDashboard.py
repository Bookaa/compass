# -*- coding: utf-8 -*-

###############################################################################
#
# RetrieveUserDashboard
# Retrieves the dashboard of the user that corresponds to the OAuth credentials provided.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class RetrieveUserDashboard(Choreography):

    """
    Create a new instance of the RetrieveUserDashboard Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Tumblr/RetrieveUserDashboard')


    def new_input_set(self):
        return RetrieveUserDashboardInputSet()

    def _make_result_set(self, result, path):
        return RetrieveUserDashboardResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return RetrieveUserDashboardChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the RetrieveUserDashboard
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class RetrieveUserDashboardInputSet(InputSet):
        """
        Set the value of the APIKey input for this choreography. ((required, string) The API Key provided by Tumblr (AKA the OAuth Consumer Key).)
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
        Set the value of the Limit input for this choreography. ((optional, integer) The number of results to return: 1 - 20. Defaults to 20.)
        """
        def set_Limit(self, value):
            InputSet._set_input(self, 'Limit', value)

        """
        Set the value of the NotesInfo input for this choreography. ((optional, boolean) Indicates whether to return notes information. Specify 1(true) or 0 (false). Defaults to 0.)
        """
        def set_NotesInfo(self, value):
            InputSet._set_input(self, 'NotesInfo', value)

        """
        Set the value of the Offset input for this choreography. ((optional, integer) The result to start at. Defaults to 0.)
        """
        def set_Offset(self, value):
            InputSet._set_input(self, 'Offset', value)

        """
        Set the value of the ReblogInfo input for this choreography. ((optional, boolean) Indicates whether to return reblog information. Specify 1(true) or 0 (false). Defaults to 0.)
        """
        def set_ReblogInfo(self, value):
            InputSet._set_input(self, 'ReblogInfo', value)

        """
        Set the value of the SecretKey input for this choreography. ((required, string) The Secret Key provided by Tumblr (AKA the OAuth Consumer Secret).)
        """
        def set_SecretKey(self, value):
            InputSet._set_input(self, 'SecretKey', value)

        """
        Set the value of the SinceId input for this choreography. ((optional, integer) Return posts that have appeared after this ID. Used to page through results.)
        """
        def set_SinceId(self, value):
            InputSet._set_input(self, 'SinceId', value)

        """
        Set the value of the Type input for this choreography. ((optional, string) The type of post to return. Specify one of the following:  text, photo, quote, link, chat, audio, video, answer.)
        """
        def set_Type(self, value):
            InputSet._set_input(self, 'Type', value)


"""
A ResultSet with methods tailored to the values returned by the RetrieveUserDashboard choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class RetrieveUserDashboardResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response from Tumblr in XML format.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class RetrieveUserDashboardChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return RetrieveUserDashboardResultSet(response, path)
