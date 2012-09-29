# -*- coding: utf-8 -*-

###############################################################################
#
# RestorePost
# Restore a deleted post.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class RestorePost(Choreography):

    """
    Create a new instance of the RestorePost Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Disqus/Posts/RestorePost')


    def new_input_set(self):
        return RestorePostInputSet()

    def _make_result_set(self, result, path):
        return RestorePostResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return RestorePostChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the RestorePost
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class RestorePostInputSet(InputSet):
        """
        Set the value of the AccessToken input for this choreography. ((required, string) A valid OAuth 2.0 access token.)
        """
        def set_AccessToken(self, value):
            InputSet._set_input(self, 'AccessToken', value)

        """
        Set the value of the PostID input for this choreography. ((required, integer) The post ID which is to be restored (undeleted).)
        """
        def set_PostID(self, value):
            InputSet._set_input(self, 'PostID', value)

        """
        Set the value of the PublicKey input for this choreography. ((required, string) The Public Key provided by Disqus (AKA the Client ID).)
        """
        def set_PublicKey(self, value):
            InputSet._set_input(self, 'PublicKey', value)

        """
        Set the value of the ResponseFormat input for this choreography. ((optional, string) The format that the response should be in. Valid values are: json (the default) and jsonp.)
        """
        def set_ResponseFormat(self, value):
            InputSet._set_input(self, 'ResponseFormat', value)

        """
        Set the value of the VaultFile input for this choreography. ()
        """


"""
A ResultSet with methods tailored to the values returned by the RestorePost choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class RestorePostResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((json) The response from Disqus.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class RestorePostChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return RestorePostResultSet(response, path)
