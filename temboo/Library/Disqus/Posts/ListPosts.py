# -*- coding: utf-8 -*-

###############################################################################
#
# ListPosts
# Retrieve a list of posts ordered by date of creation.
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
        Choreography.__init__(self, temboo_session, '/Library/Disqus/Posts/ListPosts')


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
        Set the value of the AccessToken input for this choreography. ((optional, string) A valid OAuth 2.0 access token.)
        """
        def set_AccessToken(self, value):
            InputSet._set_input(self, 'AccessToken', value)

        """
        Set the value of the Category input for this choreography. ((optional, integer) Specify a category ID for which posts wil be retrieved.)
        """
        def set_Category(self, value):
            InputSet._set_input(self, 'Category', value)

        """
        Set the value of the Cursor input for this choreography. ((optional, string) Default is set to null.)
        """
        def set_Cursor(self, value):
            InputSet._set_input(self, 'Cursor', value)

        """
        Set the value of the Forum input for this choreography. ((optional, string) A Disqus forum name to display all posts contained in that specified forum.  If null, posts from all forums moderated by the authenticating user will be retrieved.)
        """
        def set_Forum(self, value):
            InputSet._set_input(self, 'Forum', value)

        """
        Set the value of the Include input for this choreography. ((optional, string) A post status parameter to filter results by. Valid parameters include: unapproved, approved, spam, deleted, flagged, highlighted.  Default is set to: approved.)
        """
        def set_Include(self, value):
            InputSet._set_input(self, 'Include', value)

        """
        Set the value of the Limit input for this choreography. ((optional, integer) The number of records to return. Defaults to 25.)
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
        Set the value of the Query input for this choreography. ((optional, string) A search string to retrieve posts mathching the query.  Default is set to null.)
        """
        def set_Query(self, value):
            InputSet._set_input(self, 'Query', value)

        """
        Set the value of the Related input for this choreography. ((optional, string) Specify a related thread or forum that are to be included in the response.  Valid entries include: thread, or forum.)
        """
        def set_Related(self, value):
            InputSet._set_input(self, 'Related', value)

        """
        Set the value of the ResponseFormat input for this choreography. ((optional, string) The format that the response should be in. Valid values are: json (the default), jsonp, or rss.)
        """
        def set_ResponseFormat(self, value):
            InputSet._set_input(self, 'ResponseFormat', value)

        """
        Set the value of the SinceID input for this choreography. ((optional, integer) A Unix timestamp (or ISO datetime standard) to obtain results from. Default is set to null.)
        """
        def set_SinceID(self, value):
            InputSet._set_input(self, 'SinceID', value)

        """
        Set the value of the ThreadID input for this choreography. ((optional, string) The Thread ID to narrow post search results.)
        """
        def set_ThreadID(self, value):
            InputSet._set_input(self, 'ThreadID', value)


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
