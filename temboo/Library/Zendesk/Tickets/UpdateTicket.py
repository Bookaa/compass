# -*- coding: utf-8 -*-

###############################################################################
#
# UpdateTicket
# Updates an existing ticket.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class UpdateTicket(Choreography):

    """
    Create a new instance of the UpdateTicket Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Zendesk/Tickets/UpdateTicket')


    def new_input_set(self):
        return UpdateTicketInputSet()

    def _make_result_set(self, result, path):
        return UpdateTicketResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return UpdateTicketChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the UpdateTicket
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class UpdateTicketInputSet(InputSet):
        """
        Set the value of the Comment input for this choreography. ((conditional, string) The text for a ticket comment.)
        """
        def set_Comment(self, value):
            InputSet._set_input(self, 'Comment', value)

        """
        Set the value of the Email input for this choreography. ((required, string) The email address you use to login to your Zendesk account.)
        """
        def set_Email(self, value):
            InputSet._set_input(self, 'Email', value)

        """
        Set the value of the Metadata input for this choreography. ((optional, json) Ticket metadata formatted in JSON. See docs for more information on the input format.)
        """
        def set_Metadata(self, value):
            InputSet._set_input(self, 'Metadata', value)

        """
        Set the value of the Password input for this choreography. ((required, string) Your Zendesk password.)
        """
        def set_Password(self, value):
            InputSet._set_input(self, 'Password', value)

        """
        Set the value of the Public input for this choreography. ((optional, boolean) A flag indicating if this update is public or not. Defaults to "true")
        """
        def set_Public(self, value):
            InputSet._set_input(self, 'Public', value)

        """
        Set the value of the Server input for this choreography. ((required, string) Your Zendesk domain and subdomain (i.e. temboocare.zendesk.com).)
        """
        def set_Server(self, value):
            InputSet._set_input(self, 'Server', value)

        """
        Set the value of the Status input for this choreography. ((conditional, string) The status of the ticket (i.e. solved, pending, open).)
        """
        def set_Status(self, value):
            InputSet._set_input(self, 'Status', value)

        """
        Set the value of the TicketData input for this choreography. ((optional, json) A JSON string containing the ticket information. This can be used as an alternative to the serialized ticket inputs in case you need to update tickets that have custom fields.)
        """
        def set_TicketData(self, value):
            InputSet._set_input(self, 'TicketData', value)

        """
        Set the value of the TicketID input for this choreography. ((required, integer) The id of the ticket being updated.)
        """
        def set_TicketID(self, value):
            InputSet._set_input(self, 'TicketID', value)

        """
        Set the value of the Token input for this choreography. ((optional, string) The token associated with an upload to attach to this ticket. Note that tokens can be retrieved by running the UploadFile Choreo.)
        """
        def set_Token(self, value):
            InputSet._set_input(self, 'Token', value)


"""
A ResultSet with methods tailored to the values returned by the UpdateTicket choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class UpdateTicketResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((json) The response from Zendesk.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class UpdateTicketChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return UpdateTicketResultSet(response, path)
