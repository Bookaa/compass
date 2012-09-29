# -*- coding: utf-8 -*-

###############################################################################
#
# GetUserVideos
# Retrieves data about all videos watched by a specific user.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class GetUserVideos(Choreography):

    """
    Create a new instance of the GetUserVideos Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/KhanAcademy/Users/GetUserVideos')


    def new_input_set(self):
        return GetUserVideosInputSet()

    def _make_result_set(self, result, path):
        return GetUserVideosResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetUserVideosChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the GetUserVideos
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class GetUserVideosInputSet(InputSet):
        """
        Set the value of the ConsumerKey input for this choreography. ((required, string) The Consumer Key provided by Khan Academy.)
        """
        def set_ConsumerKey(self, value):
            InputSet._set_input(self, 'ConsumerKey', value)

        """
        Set the value of the ConsumerSecret input for this choreography. ((required, string) The OAuth Consumer Secret provided by Khan Academy.)
        """
        def set_ConsumerSecret(self, value):
            InputSet._set_input(self, 'ConsumerSecret', value)

        """
        Set the value of the Email input for this choreography. ((optional, string) The email address (coach or student ID) of user. If not provided, defaults to currently logged in user.)
        """
        def set_Email(self, value):
            InputSet._set_input(self, 'Email', value)

        """
        Set the value of the EndTime input for this choreography. ((optional, string) The date/time to end searching for logs in UTC format: YYYY-mm-ddTHH:MM:SS (e.g., 2011-10-18T02:41:53).)
        """
        def set_EndTime(self, value):
            InputSet._set_input(self, 'EndTime', value)

        """
        Set the value of the OAuthTokenSecret input for this choreography. ((required, string) The OAuth Token Secret retrieved during the OAuth process.)
        """
        def set_OAuthTokenSecret(self, value):
            InputSet._set_input(self, 'OAuthTokenSecret', value)

        """
        Set the value of the OAuthToken input for this choreography. ((required, string) The OAuth Token retrieved during the OAuth process.)
        """
        def set_OAuthToken(self, value):
            InputSet._set_input(self, 'OAuthToken', value)

        """
        Set the value of the StartTime input for this choreography. ((optional, string) The date/time to start searching for logs in UTC format: YYYY-mm-ddTHH:MM:SS (e.g., 2011-10-18T02:41:53).)
        """
        def set_StartTime(self, value):
            InputSet._set_input(self, 'StartTime', value)


"""
A ResultSet with methods tailored to the values returned by the GetUserVideos choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class GetUserVideosResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((json) The response from Khan Academy.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class GetUserVideosChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetUserVideosResultSet(response, path)
