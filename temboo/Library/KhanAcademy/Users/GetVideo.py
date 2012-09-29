# -*- coding: utf-8 -*-

###############################################################################
#
# GetVideo
# Retrieves user data about a specific video, such as amount of video watched, points received, etc.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class GetVideo(Choreography):

    """
    Create a new instance of the GetVideo Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/KhanAcademy/Users/GetVideo')


    def new_input_set(self):
        return GetVideoInputSet()

    def _make_result_set(self, result, path):
        return GetVideoResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetVideoChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the GetVideo
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class GetVideoInputSet(InputSet):
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
        Set the value of the YouTubeID input for this choreography. ((required, string) The YouTube ID of the video for which you want to retrieve information.)
        """
        def set_YouTubeID(self, value):
            InputSet._set_input(self, 'YouTubeID', value)


"""
A ResultSet with methods tailored to the values returned by the GetVideo choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class GetVideoResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((json) The response from Khan Academy.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class GetVideoChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetVideoResultSet(response, path)
