# -*- coding: utf-8 -*-

###############################################################################
#
# ListThreadReactions
# Retrieve a list of reactions for a given thread.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class ListThreadReactions(Choreography):

    """
    Create a new instance of the ListThreadReactions Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Disqus/Threads/ListThreadReactions')


    def new_input_set(self):
        return ListThreadReactionsInputSet()

    def _make_result_set(self, result, path):
        return ListThreadReactionsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ListThreadReactionsChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the ListThreadReactions
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class ListThreadReactionsInputSet(InputSet):
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
        Set the value of the Limit input for this choreography. ((optional, integer) The number of records to return. Maximum value is 100.  Defaults to 25.)
        """
        def set_Limit(self, value):
            InputSet._set_input(self, 'Limit', value)

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
        Set the value of the ThreadID input for this choreography. ((conditional, string) The ID of the Thread to list reactions for. Required unless specifying ThreadIdentifier or ThreadLink.)
        """
        def set_ThreadID(self, value):
            InputSet._set_input(self, 'ThreadID', value)

        """
        Set the value of the ThreadIdentifier input for this choreography. ((conditional, string) An identifier for which thread reactions will be retrieved.  Note that a Forum must also be provided when using this parameter. If set, ThreadID and ThreadLink cannot be used.)
        """
        def set_ThreadIdentifier(self, value):
            InputSet._set_input(self, 'ThreadIdentifier', value)

        """
        Set the value of the ThreadLink input for this choreography. ((conditional, string) A link pointing to the thread that is to be retrieved. Note that a Forum must also be provided when using this parameter. If set, ThreadID and ThreadIdentifier cannot be set.)
        """
        def set_ThreadLink(self, value):
            InputSet._set_input(self, 'ThreadLink', value)


"""
A ResultSet with methods tailored to the values returned by the ListThreadReactions choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class ListThreadReactionsResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The response from Disqus.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class ListThreadReactionsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ListThreadReactionsResultSet(response, path)
