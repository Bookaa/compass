# -*- coding: utf-8 -*-

###############################################################################
#
# StatusesDestroy
# Deletes a specified status.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class StatusesDestroy(Choreography):

    """
    Create a new instance of the StatusesDestroy Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Twitter/Tweets/StatusesDestroy')


    def new_input_set(self):
        return StatusesDestroyInputSet()

    def _make_result_set(self, result, path):
        return StatusesDestroyResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return StatusesDestroyChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the StatusesDestroy
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class StatusesDestroyInputSet(InputSet):
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
        Set the value of the ID input for this choreography. ((required, integer) The numerical ID of the desired status.)
        """
        def set_ID(self, value):
            InputSet._set_input(self, 'ID', value)

        """
        Set the value of the IncludeEntities input for this choreography. ((optional, boolean) When set to either true, t or 1, each tweet will include a node called "entities". This node offers a variety of metadata about the tweet.)
        """
        def set_IncludeEntities(self, value):
            InputSet._set_input(self, 'IncludeEntities', value)

        """
        Set the value of the ResponseFormat input for this choreography. ((optional, string) Specify the format of the response from Twitter: json, or xml.  Default is set to xml.)
        """
        def set_ResponseFormat(self, value):
            InputSet._set_input(self, 'ResponseFormat', value)

        """
        Set the value of the TrimUser input for this choreography. ((optional, boolean) When set to either true, t or 1, each tweet returned in a timeline will include a user object including only the status authors numerical ID.)
        """
        def set_TrimUser(self, value):
            InputSet._set_input(self, 'TrimUser', value)


"""
A ResultSet with methods tailored to the values returned by the StatusesDestroy choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class StatusesDestroyResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The response from Twitter.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class StatusesDestroyChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return StatusesDestroyResultSet(response, path)
