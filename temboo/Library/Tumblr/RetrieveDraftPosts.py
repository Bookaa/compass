# -*- coding: utf-8 -*-

###############################################################################
#
# RetrieveDraftPosts
# Retrieves a list of queued posts for a specified Tumblr blog.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class RetrieveDraftPosts(Choreography):

    """
    Create a new instance of the RetrieveDraftPosts Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Tumblr/RetrieveDraftPosts')


    def new_input_set(self):
        return RetrieveDraftPostsInputSet()

    def _make_result_set(self, result, path):
        return RetrieveDraftPostsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return RetrieveDraftPostsChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the RetrieveDraftPosts
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class RetrieveDraftPostsInputSet(InputSet):
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
        Set the value of the BaseHostname input for this choreography. ((required, string) The standard or custom blog hostname (i.e. temboo.tumblr.com).)
        """
        def set_BaseHostname(self, value):
            InputSet._set_input(self, 'BaseHostname', value)

        """
        Set the value of the SecretKey input for this choreography. ((required, string) The Secret Key provided by Tumblr (AKA the OAuth Consumer Secret).)
        """
        def set_SecretKey(self, value):
            InputSet._set_input(self, 'SecretKey', value)


"""
A ResultSet with methods tailored to the values returned by the RetrieveDraftPosts choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class RetrieveDraftPostsResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response from Tumblr in XML format.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class RetrieveDraftPostsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return RetrieveDraftPostsResultSet(response, path)
