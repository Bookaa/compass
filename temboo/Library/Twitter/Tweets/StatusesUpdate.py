# -*- coding: utf-8 -*-

###############################################################################
#
# StatusesUpdate
# Allows you to update your Twitter status (aka Tweet).
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class StatusesUpdate(Choreography):

    """
    Create a new instance of the StatusesUpdate Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Twitter/Tweets/StatusesUpdate')


    def new_input_set(self):
        return StatusesUpdateInputSet()

    def _make_result_set(self, result, path):
        return StatusesUpdateResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return StatusesUpdateChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the StatusesUpdate
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class StatusesUpdateInputSet(InputSet):
        """
        Set the value of the AccessTokenSecret input for this choreography. ((required, string) The Access Token Secret provided by Twitter or retrieved during the OAuth process.)
        """
        def set_AccessTokenSecret(self, value):
            InputSet._set_input(self, 'AccessTokenSecret', value)

        """
        Set the value of the AccessToken input for this choreography. ((required, string) The Access Token provided by Twitter or retrieved during the OAuth process.)
        """
        def set_AccessToken(self, value):
            InputSet._set_input(self, 'AccessToken', value)

        """
        Set the value of the ConsumerKey input for this choreography. ((required, string) The Consumer Key provided by Twitter.)
        """
        def set_ConsumerKey(self, value):
            InputSet._set_input(self, 'ConsumerKey', value)

        """
        Set the value of the ConsumerSecret input for this choreography. ((required, string) The Consumer Secret provided by Twitter.)
        """
        def set_ConsumerSecret(self, value):
            InputSet._set_input(self, 'ConsumerSecret', value)

        """
        Set the value of the ResponseFormat input for this choreography. ((optional, string) Specify the format of the response from Twitter: json, or xml.  Default is set to xml.)
        """
        def set_ResponseFormat(self, value):
            InputSet._set_input(self, 'ResponseFormat', value)

        """
        Set the value of the StatusUpdate input for this choreography. ((required, string) The text for your status update. 140-character limit.)
        """
        def set_StatusUpdate(self, value):
            InputSet._set_input(self, 'StatusUpdate', value)


"""
A ResultSet with methods tailored to the values returned by the StatusesUpdate choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class StatusesUpdateResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The response from Twitter.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class StatusesUpdateChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return StatusesUpdateResultSet(response, path)
