# -*- coding: utf-8 -*-

###############################################################################
#
# UnsubscribeFromThread
# Unsubscribe from a thread.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class UnsubscribeFromThread(Choreography):

    """
    Create a new instance of the UnsubscribeFromThread Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Disqus/Threads/UnsubscribeFromThread')


    def new_input_set(self):
        return UnsubscribeFromThreadInputSet()

    def _make_result_set(self, result, path):
        return UnsubscribeFromThreadResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return UnsubscribeFromThreadChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the UnsubscribeFromThread
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class UnsubscribeFromThreadInputSet(InputSet):
        """
        Set the value of the Email input for this choreography. ((optional, string) The email address that will be unsubsribed from the thread.)
        """
        def set_Email(self, value):
            InputSet._set_input(self, 'Email', value)

        """
        Set the value of the Forum input for this choreography. ((optional, integer) The forum ID of a thread that is to be unsubscribed from. Required if setting either ThreadByIdentification, or ThreadByLink.)
        """
        def set_Forum(self, value):
            InputSet._set_input(self, 'Forum', value)

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
        Set the value of the ThreadID input for this choreography. ((conditional, integer) The ID of a thread that is to be unsubscribed from. Required unless specifying the ThreadIdentifier or ThreadLink. If using this parameter, ThreadIdentifier cannot be set.)
        """
        def set_ThreadID(self, value):
            InputSet._set_input(self, 'ThreadID', value)

        """
        Set the value of the ThreadIdentifier input for this choreography. ((optional, string) The identifier for the thread that is to be unsubscribed from.  Note that a Forum must also be provided when using this parameter. If set, ThreadID and ThreadLink cannot be used.)
        """
        def set_ThreadIdentifier(self, value):
            InputSet._set_input(self, 'ThreadIdentifier', value)

        """
        Set the value of the ThreadLink input for this choreography. ((optional, string) A link pointing to the thread that is to be unsubscribed from. Note that a Forum must also be provided when using this parameter. If set, ThreadID and ThreadIdentifier cannot be set.)
        """
        def set_ThreadLink(self, value):
            InputSet._set_input(self, 'ThreadLink', value)

        """
        Set the value of the VaultFile input for this choreography. ()
        """


"""
A ResultSet with methods tailored to the values returned by the UnsubscribeFromThread choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class UnsubscribeFromThreadResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((json) The response from Disqus.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class UnsubscribeFromThreadChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return UnsubscribeFromThreadResultSet(response, path)
