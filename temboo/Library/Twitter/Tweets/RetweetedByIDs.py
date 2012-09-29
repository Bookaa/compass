# -*- coding: utf-8 -*-

###############################################################################
#
# RetweetedByIDs
# Retrieves user IDs of up to 100 users who retweeted the status.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class RetweetedByIDs(Choreography):

    """
    Create a new instance of the RetweetedByIDs Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Twitter/Tweets/RetweetedByIDs')


    def new_input_set(self):
        return RetweetedByIDsInputSet()

    def _make_result_set(self, result, path):
        return RetweetedByIDsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return RetweetedByIDsChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the RetweetedByIDs
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class RetweetedByIDsInputSet(InputSet):
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
        Set the value of the Count input for this choreography. ((optional, integer) Specifies the number of ids to try and retrieve, up to a maximum of 100.)
        """
        def set_Count(self, value):
            InputSet._set_input(self, 'Count', value)

        """
        Set the value of the ID input for this choreography. ((required, integer) The numerical ID of the desired status.)
        """
        def set_ID(self, value):
            InputSet._set_input(self, 'ID', value)

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
        Set the value of the StringifyIDs input for this choreography. ((optional, boolean) Many programming environments will not consume Twitter's Tweet IDs due to their size. Set this option to 1 to have ids returned as strings instead.)
        """
        def set_StringifyIDs(self, value):
            InputSet._set_input(self, 'StringifyIDs', value)


"""
A ResultSet with methods tailored to the values returned by the RetweetedByIDs choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class RetweetedByIDsResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The response from Twitter.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class RetweetedByIDsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return RetweetedByIDsResultSet(response, path)
