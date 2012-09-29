# -*- coding: utf-8 -*-

###############################################################################
#
# PostDetails
# Obtain information about a post.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class PostDetails(Choreography):

    """
    Create a new instance of the PostDetails Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Disqus/Posts/PostDetails')


    def new_input_set(self):
        return PostDetailsInputSet()

    def _make_result_set(self, result, path):
        return PostDetailsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return PostDetailsChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the PostDetails
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class PostDetailsInputSet(InputSet):
        """
        Set the value of the AccessToken input for this choreography. ((optional, string) A valid OAuth 2.0 access token.)
        """
        def set_AccessToken(self, value):
            InputSet._set_input(self, 'AccessToken', value)

        """
        Set the value of the PostID input for this choreography. ((required, integer) The post ID for which information will be returned.)
        """
        def set_PostID(self, value):
            InputSet._set_input(self, 'PostID', value)

        """
        Set the value of the PublicKey input for this choreography. ((required, string) The Public Key provided by Disqus (AKA the Client ID).)
        """
        def set_PublicKey(self, value):
            InputSet._set_input(self, 'PublicKey', value)

        """
        Set the value of the Related input for this choreography. ((optional, string) Specify a related thread or forum that are to be included in the response.  Valid entries include: thread, or forum.)
        """
        def set_Related(self, value):
            InputSet._set_input(self, 'Related', value)

        """
        Set the value of the ResponseFormat input for this choreography. ((optional, string) The format that the response should be in. Valid values are: json (the default) and jsonp.)
        """
        def set_ResponseFormat(self, value):
            InputSet._set_input(self, 'ResponseFormat', value)

        """
        Set the value of the VaultFile input for this choreography. ()
        """


"""
A ResultSet with methods tailored to the values returned by the PostDetails choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class PostDetailsResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((json) The response from Disqus.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class PostDetailsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return PostDetailsResultSet(response, path)
