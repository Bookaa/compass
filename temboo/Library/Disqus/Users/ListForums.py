# -*- coding: utf-8 -*-

###############################################################################
#
# ListForums
# Retrieve a list of forums owned by the specified user.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class ListForums(Choreography):

    """
    Create a new instance of the ListForums Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Disqus/Users/ListForums')


    def new_input_set(self):
        return ListForumsInputSet()

    def _make_result_set(self, result, path):
        return ListForumsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ListForumsChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the ListForums
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class ListForumsInputSet(InputSet):
        """
        Set the value of the Cursor input for this choreography. ((optional, string) Default is set to null.)
        """
        def set_Cursor(self, value):
            InputSet._set_input(self, 'Cursor', value)

        """
        Set the value of the Limit input for this choreography. ((optional, integer) The number of records to return. Defaults to 25.)
        """
        def set_Limit(self, value):
            InputSet._set_input(self, 'Limit', value)

        """
        Set the value of the Order input for this choreography. ((optional, string) The sort order for the results. Valid vaues are: asc or desc. Default is set to: asc.)
        """
        def set_Order(self, value):
            InputSet._set_input(self, 'Order', value)

        """
        Set the value of the PublicKey input for this choreography. ((required, string) The Public Key provided by Disqus (AKA the Client ID).)
        """
        def set_PublicKey(self, value):
            InputSet._set_input(self, 'PublicKey', value)

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
        Set the value of the UserID input for this choreography. ((conditional, string) The Disqus User ID, for which active forum information will be retrieved.  If UserID is set, then Username must be null.)
        """
        def set_UserID(self, value):
            InputSet._set_input(self, 'UserID', value)

        """
        Set the value of the Username input for this choreography. ((conditional, string) A Disqus username.  If Username is being set, then UserID must be null.)
        """
        def set_Username(self, value):
            InputSet._set_input(self, 'Username', value)


"""
A ResultSet with methods tailored to the values returned by the ListForums choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class ListForumsResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The response from Disqus.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class ListForumsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ListForumsResultSet(response, path)
