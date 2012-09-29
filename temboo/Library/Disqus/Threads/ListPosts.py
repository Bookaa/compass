# -*- coding: utf-8 -*-

###############################################################################
#
# ListPosts
# Retrieve a list of posts within a thread.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class ListPosts(Choreography):

    """
    Create a new instance of the ListPosts Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Disqus/Threads/ListPosts')


    def new_input_set(self):
        return ListPostsInputSet()

    def _make_result_set(self, result, path):
        return ListPostsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ListPostsChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the ListPosts
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class ListPostsInputSet(InputSet):
        """
        Set the value of the Cursor input for this choreography. ((optional, string) Default is set to null.)
        """
        def set_Cursor(self, value):
            InputSet._set_input(self, 'Cursor', value)

        """
        Set the value of the Forum input for this choreography. ((optional, integer) A Disqus forum ID (AKA a short name). If null, threads from all forums moderated by the authenticating user will be retrieved.)
        """
        def set_Forum(self, value):
            InputSet._set_input(self, 'Forum', value)

        """
        Set the value of the Include input for this choreography. ((optional, string) Specify a post status parameter to filter results by. Valid parameters include: unapproved, approved, spam, deleted, flagged.  Default is set to: approved.)
        """
        def set_Include(self, value):
            InputSet._set_input(self, 'Include', value)

        """
        Set the value of the Limit input for this choreography. ((optional, integer) The number of records to return. Maximum value is 100.  Defaults to 25.)
        """
        def set_Limit(self, value):
            InputSet._set_input(self, 'Limit', value)

        """
        Set the value of the Order input for this choreography. ((optional, string) The sort order of the results. Valid values are: asc or desc. Default is set to: asc.)
        """
        def set_Order(self, value):
            InputSet._set_input(self, 'Order', value)

        """
        Set the value of the PublicKey input for this choreography. ((required, string) The Public Key provided by Disqus (AKA the Client ID).)
        """
        def set_PublicKey(self, value):
            InputSet._set_input(self, 'PublicKey', value)

        """
        Set the value of the Query input for this choreography. ((optional, string) A search string to limit results.)
        """
        def set_Query(self, value):
            InputSet._set_input(self, 'Query', value)

        """
        Set the value of the Related input for this choreography. ((optional, string) Specify a related thread or forum that are to be included in the response.  Valid entries include: forum.)
        """
        def set_Related(self, value):
            InputSet._set_input(self, 'Related', value)

        """
        Set the value of the ResponseFormat input for this choreography. ((optional, string) The format that the response should be in. Valid values are: json (the default), jsonp, or rss.)
        """
        def set_ResponseFormat(self, value):
            InputSet._set_input(self, 'ResponseFormat', value)

        """
        Set the value of the Since input for this choreography. ((optional, integer) A Unix timestamp (or ISO datetime standard) to obtain results from. Default is set to null.)
        """
        def set_Since(self, value):
            InputSet._set_input(self, 'Since', value)

        """
        Set the value of the ThreadID input for this choreography. ((conditional, string) A Thread ID to narrow post search results. Required unless specifying ThreadIdentifier or ThreadLink.)
        """
        def set_ThreadID(self, value):
            InputSet._set_input(self, 'ThreadID', value)

        """
        Set the value of the ThreadIdentifier input for this choreography. ((optional, string) An identifier to retrieve associated thread details. Note that a Forum must also be provided when using this parameter. If set, ThreadID and ThreadLink cannot be used.)
        """
        def set_ThreadIdentifier(self, value):
            InputSet._set_input(self, 'ThreadIdentifier', value)

        """
        Set the value of the ThreadLink input for this choreography. ((optional, string) A link pointing to the thread that is to be retrieved. Note that a Forum must also be provided when using this parameter. If set, ThreadID and ThreadIdentifier cannot be set.)
        """
        def set_ThreadLink(self, value):
            InputSet._set_input(self, 'ThreadLink', value)


"""
A ResultSet with methods tailored to the values returned by the ListPosts choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class ListPostsResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The response from Disqus.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class ListPostsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ListPostsResultSet(response, path)
