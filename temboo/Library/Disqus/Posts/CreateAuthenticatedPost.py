# -*- coding: utf-8 -*-

###############################################################################
#
# CreateAuthenticatedPost
# Create a new post for the authenticated user.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class CreateAuthenticatedPost(Choreography):

    """
    Create a new instance of the CreateAuthenticatedPost Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Disqus/Posts/CreateAuthenticatedPost')


    def new_input_set(self):
        return CreateAuthenticatedPostInputSet()

    def _make_result_set(self, result, path):
        return CreateAuthenticatedPostResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CreateAuthenticatedPostChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the CreateAuthenticatedPost
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class CreateAuthenticatedPostInputSet(InputSet):
        """
        Set the value of the AccessToken input for this choreography. ((required, string) A valid OAuth 2.0 access token.)
        """
        def set_AccessToken(self, value):
            InputSet._set_input(self, 'AccessToken', value)

        """
        Set the value of the Date input for this choreography. ((optional, string) The date of the post, either in Unix timestamp format, or ISO datetime standard. You must be a moderator to do this.)
        """
        def set_Date(self, value):
            InputSet._set_input(self, 'Date', value)

        """
        Set the value of the IPAddress input for this choreography. ((optional, string) The author's IP address. You must be a moderator to do this.)
        """
        def set_IPAddress(self, value):
            InputSet._set_input(self, 'IPAddress', value)

        """
        Set the value of the ParentPost input for this choreography. ((conditional, string) The ID of a parent post to which the new post will be responding to. Either ParentPost, or Thread must be set, or both.)
        """
        def set_ParentPost(self, value):
            InputSet._set_input(self, 'ParentPost', value)

        """
        Set the value of the PostContent input for this choreography. ((required, string) The text of this post.)
        """
        def set_PostContent(self, value):
            InputSet._set_input(self, 'PostContent', value)

        """
        Set the value of the PostState input for this choreography. ((optional, string) Specify the state of the post (comment). Available options include: unapproved, approved, spam, killed. You must be a moderator to do this. If set, pre-approval validation will be skipped.)
        """
        def set_PostState(self, value):
            InputSet._set_input(self, 'PostState', value)

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
        Set the value of the Thread input for this choreography. ((conditional, string) The thread ID to attach the new post to. Either ParentPost, or Thread must be set, or both.)
        """
        def set_Thread(self, value):
            InputSet._set_input(self, 'Thread', value)

        """
        Set the value of the VaultFile input for this choreography. ()
        """


"""
A ResultSet with methods tailored to the values returned by the CreateAuthenticatedPost choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class CreateAuthenticatedPostResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((json) The response from Disqus.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class CreateAuthenticatedPostChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return CreateAuthenticatedPostResultSet(response, path)
