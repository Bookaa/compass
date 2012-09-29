# -*- coding: utf-8 -*-

###############################################################################
#
# ApplyMacroToAllTickets
# Applies a given macro to all applicable tickets.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class ApplyMacroToAllTickets(Choreography):

    """
    Create a new instance of the ApplyMacroToAllTickets Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Zendesk/Macros/ApplyMacroToAllTickets')


    def new_input_set(self):
        return ApplyMacroToAllTicketsInputSet()

    def _make_result_set(self, result, path):
        return ApplyMacroToAllTicketsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ApplyMacroToAllTicketsChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the ApplyMacroToAllTickets
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class ApplyMacroToAllTicketsInputSet(InputSet):
        """
        Set the value of the Email input for this choreography. ((required, string) The email to authenticate the Zendesk account.)
        """
        def set_Email(self, value):
            InputSet._set_input(self, 'Email', value)

        """
        Set the value of the MacroID input for this choreography. ((required, integer) The ID of the macro to apply.)
        """
        def set_MacroID(self, value):
            InputSet._set_input(self, 'MacroID', value)

        """
        Set the value of the Password input for this choreography. ((required, string) The password matching the email to authenticate the Zendesk account.)
        """
        def set_Password(self, value):
            InputSet._set_input(self, 'Password', value)

        """
        Set the value of the Server input for this choreography. ((required, string) The server URL associated with your Zendesk account. In many cases this looks like: temboo.zendesk.com but may also be customized: support.temboo.com)
        """
        def set_Server(self, value):
            InputSet._set_input(self, 'Server', value)


"""
A ResultSet with methods tailored to the values returned by the ApplyMacroToAllTickets choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class ApplyMacroToAllTicketsResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((json) The response from Zendesk.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class ApplyMacroToAllTicketsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ApplyMacroToAllTicketsResultSet(response, path)
