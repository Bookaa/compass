# -*- coding: utf-8 -*-

###############################################################################
#
# GetEmails
# Retrieves one or more email messages from a specified mail account.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class GetEmails(Choreography):

    """
    Create a new instance of the GetEmails Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Temboo/Email/GetEmails')


    def new_input_set(self):
        return GetEmailsInputSet()

    def _make_result_set(self, result, path):
        return GetEmailsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetEmailsChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the GetEmails
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class GetEmailsInputSet(InputSet):
        """
        Set the value of the DeleteAfterRetrieval input for this choreography. ((optional, boolean) To delete messages after retrieval, set to 1. Defaults to 0 indicating that the messages will not be deleted after retrieval.)
        """
        def set_DeleteAfterRetrieval(self, value):
            InputSet._set_input(self, 'DeleteAfterRetrieval', value)

        """
        Set the value of the MailboxFolder input for this choreography. ((optional, string) The folder name to retrieve emails from. This is only used when the Protocol input is set to imap. The default value is "Inbox".)
        """
        def set_MailboxFolder(self, value):
            InputSet._set_input(self, 'MailboxFolder', value)

        """
        Set the value of the MaxMessages input for this choreography. ((optional, string) The max number of email messages to retrieve. Valid values are 1-100. Defaults to 100.)
        """
        def set_MaxMessages(self, value):
            InputSet._set_input(self, 'MaxMessages', value)

        """
        Set the value of the Password input for this choreography. ((required, string) The password for the email account.)
        """
        def set_Password(self, value):
            InputSet._set_input(self, 'Password', value)

        """
        Set the value of the Port input for this choreography. ((required, integer) Specify the port number.)
        """
        def set_Port(self, value):
            InputSet._set_input(self, 'Port', value)

        """
        Set the value of the Protocol input for this choreography. ((required, string) Specify the protocol. Valid values are: pop or imap.)
        """
        def set_Protocol(self, value):
            InputSet._set_input(self, 'Protocol', value)

        """
        Set the value of the SenderAddressFilter input for this choreography. ((optional, string) A string used to filter by a particular sender address.)
        """
        def set_SenderAddressFilter(self, value):
            InputSet._set_input(self, 'SenderAddressFilter', value)

        """
        Set the value of the Server input for this choreography. ((required, string) The name or IP address of the email server.)
        """
        def set_Server(self, value):
            InputSet._set_input(self, 'Server', value)

        """
        Set the value of the SubjectFilter input for this choreography. ((optional, string) A string used to filter by subject.)
        """
        def set_SubjectFilter(self, value):
            InputSet._set_input(self, 'SubjectFilter', value)

        """
        Set the value of the UseSSL input for this choreography. ((optional, boolean) Set to 1 to use SSL. Defaults to 1 (true).)
        """
        def set_UseSSL(self, value):
            InputSet._set_input(self, 'UseSSL', value)

        """
        Set the value of the Username input for this choreography. ((required, string) The username for the email account.)
        """
        def set_Username(self, value):
            InputSet._set_input(self, 'Username', value)


"""
A ResultSet with methods tailored to the values returned by the GetEmails choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class GetEmailsResultSet(ResultSet):
        """
        Retrieve the value for the "Messages" output from this choreography execution. ((xml) A list of the email messages retrieved from the mail server. Each email message will contain the message body and message header fields.)
        """
        def get_Messages(self):
            return self._output.get('Messages', None)

class GetEmailsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetEmailsResultSet(response, path)
