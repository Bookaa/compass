# -*- coding: utf-8 -*-

###############################################################################
#
# SubscribeToThread
# Subscribe to a thread.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class SubscribeToThread(Choreography):

    """
    Create a new instance of the SubscribeToThread Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Disqus/Threads/SubscribeToThread')


    def new_input_set(self):
        return SubscribeToThreadInputSet()

    def _make_result_set(self, result, path):
        return SubscribeToThreadResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return SubscribeToThreadChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the SubscribeToThread
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class SubscribeToThreadInputSet(InputSet):
        """
        Set the value of the Email input for this choreography. ((optional, string) An email address to use when subscribing to the thread.)
        """
        def set_Email(self, value):
            InputSet._set_input(self, 'Email', value)

        """
        Set the value of the Forum input for this choreography. ((optional, integer) The forum ID of a thread that is to be subscribed to. Required if setting either ThreadByIdentification, or ThreadByLink.)
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
        Set the value of the ThreadID input for this choreography. ((conditional, integer) Enter an ID of a thread that is to be subscribed to. Required unless specifying ThreadIdentifier or ThreadLink. If using this parameter, ThreadIdentifier cannot be set.)
        """
        def set_ThreadID(self, value):
            InputSet._set_input(self, 'ThreadID', value)

        """
        Set the value of the ThreadIdentifier input for this choreography. ((conditional, string) The identifier for the thread that is to be subscribed to.  Note that a Forum must also be provided when using this parameter. If set, ThreadID and ThreadLink cannot be used.)
        """
        def set_ThreadIdentifier(self, value):
            InputSet._set_input(self, 'ThreadIdentifier', value)

        """
        Set the value of the ThreadLink input for this choreography. ((conditional, string) A link pointing to the thread that is to be subscribed to. Note that a Forum must also be provided when using this parameter. If set, ThreadID and ThreadIdentifier cannot be set.)
        """
        def set_ThreadLink(self, value):
            InputSet._set_input(self, 'ThreadLink', value)

        """
        Set the value of the VaultFile input for this choreography. ()
        """


"""
A ResultSet with methods tailored to the values returned by the SubscribeToThread choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class SubscribeToThreadResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((json) The response from Disqus.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class SubscribeToThreadChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return SubscribeToThreadResultSet(response, path)
