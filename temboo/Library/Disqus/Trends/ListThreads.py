# -*- coding: utf-8 -*-

###############################################################################
#
# ListThreads
# Returns a list of trending threads.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class ListThreads(Choreography):

    """
    Create a new instance of the ListThreads Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Disqus/Trends/ListThreads')


    def new_input_set(self):
        return ListThreadsInputSet()

    def _make_result_set(self, result, path):
        return ListThreadsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ListThreadsChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the ListThreads
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class ListThreadsInputSet(InputSet):
        """
        Set the value of the AccessToken input for this choreography. ((optional, string) A valid OAuth 2.0 access token.)
        """
        def set_AccessToken(self, value):
            InputSet._set_input(self, 'AccessToken', value)

        """
        Set the value of the Callback input for this choreography. ((optional, string) The name of a callback function to wrap the respone in. Used when setting ResponseFormat to "jsonp".)
        """
        def set_Callback(self, value):
            InputSet._set_input(self, 'Callback', value)

        """
        Set the value of the Forum input for this choreography. ((optional, string) Allows you to look up a forum by ID (aka the short name).)
        """
        def set_Forum(self, value):
            InputSet._set_input(self, 'Forum', value)

        """
        Set the value of the Limit input for this choreography. ((optional, integer) The number of records to return. Defaults to 10.)
        """
        def set_Limit(self, value):
            InputSet._set_input(self, 'Limit', value)

        """
        Set the value of the PublicKey input for this choreography. ((required, string) The Public Key provided by Disqus (AKA the The Client ID).)
        """
        def set_PublicKey(self, value):
            InputSet._set_input(self, 'PublicKey', value)

        """
        Set the value of the Related input for this choreography. ((optional, string) Indicates the relations to include with your response. Valid values are: forum, author, category.)
        """
        def set_Related(self, value):
            InputSet._set_input(self, 'Related', value)

        """
        Set the value of the ResponseFormat input for this choreography. ((optional, string) The format that the response should be in. Valid values are: json (the default), jsonp, or rss.)
        """
        def set_ResponseFormat(self, value):
            InputSet._set_input(self, 'ResponseFormat', value)


"""
A ResultSet with methods tailored to the values returned by the ListThreads choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class ListThreadsResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The response from Disqus.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class ListThreadsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ListThreadsResultSet(response, path)
