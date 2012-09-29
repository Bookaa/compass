# -*- coding: utf-8 -*-

###############################################################################
#
# CreateAnonymousPost
# Creates an anonymous post.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class CreateAnonymousPost(Choreography):

    """
    Create a new instance of the CreateAnonymousPost Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Disqus/Posts/CreateAnonymousPost')


    def new_input_set(self):
        return CreateAnonymousPostInputSet()

    def _make_result_set(self, result, path):
        return CreateAnonymousPostResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CreateAnonymousPostChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the CreateAnonymousPost
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class CreateAnonymousPostInputSet(InputSet):
        """
        Set the value of the AuthorEmail input for this choreography. ((required, string) The email address of the post author.)
        """
        def set_AuthorEmail(self, value):
            InputSet._set_input(self, 'AuthorEmail', value)

        """
        Set the value of the AuthorName input for this choreography. ((optional, string) The name of the post author.)
        """
        def set_AuthorName(self, value):
            InputSet._set_input(self, 'AuthorName', value)

        """
        Set the value of the AuthorURL input for this choreography. ((optional, string) The URL of the author's Disqus profile.)
        """
        def set_AuthorURL(self, value):
            InputSet._set_input(self, 'AuthorURL', value)

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
A ResultSet with methods tailored to the values returned by the CreateAnonymousPost choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class CreateAnonymousPostResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((json) The response from Disqus.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class CreateAnonymousPostChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return CreateAnonymousPostResultSet(response, path)
