# -*- coding: utf-8 -*-

###############################################################################
#
# CreateTicketNewRequester
# Creates a new ticket as well as a new requester account.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class CreateTicketNewRequester(Choreography):

    """
    Create a new instance of the CreateTicketNewRequester Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Zendesk/Tickets/CreateTicketNewRequester')


    def new_input_set(self):
        return CreateTicketNewRequesterInputSet()

    def _make_result_set(self, result, path):
        return CreateTicketNewRequesterResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CreateTicketNewRequesterChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the CreateTicketNewRequester
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class CreateTicketNewRequesterInputSet(InputSet):
        """
        Set the value of the Comment input for this choreography. ((required, string) The comment for the ticket that is being created.)
        """
        def set_Comment(self, value):
            InputSet._set_input(self, 'Comment', value)

        """
        Set the value of the Email input for this choreography. ((required, string) The email address you use to login to your Zendesk account.)
        """
        def set_Email(self, value):
            InputSet._set_input(self, 'Email', value)

        """
        Set the value of the LocaleID input for this choreography. ((required, integer) LocaleID for the new requester. Indicate 1 for English, 8 for Deutsch, etc.)
        """
        def set_LocaleID(self, value):
            InputSet._set_input(self, 'LocaleID', value)

        """
        Set the value of the Name input for this choreography. ((required, string) Name of new requester.)
        """
        def set_Name(self, value):
            InputSet._set_input(self, 'Name', value)

        """
        Set the value of the Password input for this choreography. ((required, string) Your Zendesk password.)
        """
        def set_Password(self, value):
            InputSet._set_input(self, 'Password', value)

        """
        Set the value of the RequesterEmail input for this choreography. ((required, string) Email of new requester.)
        """
        def set_RequesterEmail(self, value):
            InputSet._set_input(self, 'RequesterEmail', value)

        """
        Set the value of the Server input for this choreography. ((required, string) Your Zendesk domain and subdomain (i.e. temboocare.zendesk.com).)
        """
        def set_Server(self, value):
            InputSet._set_input(self, 'Server', value)

        """
        Set the value of the Subject input for this choreography. ((required, string) The subject for the ticket that is being created.)
        """
        def set_Subject(self, value):
            InputSet._set_input(self, 'Subject', value)

        """
        Set the value of the Token input for this choreography. ((optional, string) The token associated with an upload to attach to this ticket. Note that tokens can be retrieved by running the UploadFile Choreo.)
        """
        def set_Token(self, value):
            InputSet._set_input(self, 'Token', value)


"""
A ResultSet with methods tailored to the values returned by the CreateTicketNewRequester choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class CreateTicketNewRequesterResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((json) The response from Zendesk.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class CreateTicketNewRequesterChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return CreateTicketNewRequesterResultSet(response, path)
