# -*- coding: utf-8 -*-

###############################################################################
#
# GetDirectMessages
# Retrieves the 20 most recent direct messages sent to the authenticating user.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class GetDirectMessages(Choreography):

    """
    Create a new instance of the GetDirectMessages Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Twitter/DirectMessages/GetDirectMessages')


    def new_input_set(self):
        return GetDirectMessagesInputSet()

    def _make_result_set(self, result, path):
        return GetDirectMessagesResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetDirectMessagesChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the GetDirectMessages
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class GetDirectMessagesInputSet(InputSet):
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
        Set the value of the Count input for this choreography. ((optional, integer) Specifies the number of records to retrieve up to a maximum of 200.)
        """
        def set_Count(self, value):
            InputSet._set_input(self, 'Count', value)

        """
        Set the value of the IncludeEntities input for this choreography. ((optional, boolean) An advanced option for returning more verbose metadata. When set to either true, t or 1, each tweet will include a node called "entities".)
        """
        def set_IncludeEntities(self, value):
            InputSet._set_input(self, 'IncludeEntities', value)

        """
        Set the value of the MaxID input for this choreography. ((optional, integer) Returns results with an ID less than (older than) or equal to the specified ID.)
        """
        def set_MaxID(self, value):
            InputSet._set_input(self, 'MaxID', value)

        """
        Set the value of the Page input for this choreography. ((optional, integer) Specifies the page of results to retrieve.)
        """
        def set_Page(self, value):
            InputSet._set_input(self, 'Page', value)

        """
        Set the value of the ResponseFormat input for this choreography. ((optional, string) Specify the format of the response from Twitter: json, or xml.  Default is set to xml.)
        """
        def set_ResponseFormat(self, value):
            InputSet._set_input(self, 'ResponseFormat', value)

        """
        Set the value of the SinceID input for this choreography. ((optional, integer) Returns results with an ID greater than (more recent than) the specified ID.)
        """
        def set_SinceID(self, value):
            InputSet._set_input(self, 'SinceID', value)

        """
        Set the value of the SkipStatus input for this choreography. ((optional, boolean) When set to either true, t or 1 statuses will not be included in the returned user objects.)
        """
        def set_SkipStatus(self, value):
            InputSet._set_input(self, 'SkipStatus', value)


"""
A ResultSet with methods tailored to the values returned by the GetDirectMessages choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class GetDirectMessagesResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The response from Twitter.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class GetDirectMessagesChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetDirectMessagesResultSet(response, path)
