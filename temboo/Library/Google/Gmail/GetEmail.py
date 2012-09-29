# -*- coding: utf-8 -*-

###############################################################################
#
# GetEmail
# Retrieves a single email message from a Gmail inbox.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class GetEmail(Choreography):

    """
    Create a new instance of the GetEmail Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Google/Gmail/GetEmail')


    def new_input_set(self):
        return GetEmailInputSet()

    def _make_result_set(self, result, path):
        return GetEmailResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetEmailChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the GetEmail
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class GetEmailInputSet(InputSet):
        """
        Set the value of the DeleteAfterRetrieval input for this choreography. ((optional, boolean) To delete the message after retrieval, set to 1. Defaults to 0 indicating that the message will not be deleted after retrieval. Note that you will need to adjust Gmail settings to use this feature.)
        """
        def set_DeleteAfterRetrieval(self, value):
            InputSet._set_input(self, 'DeleteAfterRetrieval', value)

        """
        Set the value of the Password input for this choreography. ((required, string) Your Gmail password.)
        """
        def set_Password(self, value):
            InputSet._set_input(self, 'Password', value)

        """
        Set the value of the SenderAddressFilter input for this choreography. ((optional, string) A string used to filter by a particular sender address.)
        """
        def set_SenderAddressFilter(self, value):
            InputSet._set_input(self, 'SenderAddressFilter', value)

        """
        Set the value of the SubjectFilter input for this choreography. ((optional, string) A string used to filter by subject.)
        """
        def set_SubjectFilter(self, value):
            InputSet._set_input(self, 'SubjectFilter', value)

        """
        Set the value of the Username input for this choreography. ((required, string) Your Gmail username. Provide the complete email address used for logging into Gmail.)
        """
        def set_Username(self, value):
            InputSet._set_input(self, 'Username', value)


"""
A ResultSet with methods tailored to the values returned by the GetEmail choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class GetEmailResultSet(ResultSet):
        """
        Retrieve the value for the "Attachment" output from this choreography execution. ((string) If the email has an attachment, the Base64 encoded contents of the attachment are returned in this output variable.)
        """
        def get_Attachment(self):
            return self._output.get('Attachment', None)
        """
        Retrieve the value for the "Message" output from this choreography execution. ((xml) The response from Gmail including the message body and message header fields.)
        """
        def get_Message(self):
            return self._output.get('Message', None)
        """
        Retrieve the value for the "MessageBody" output from this choreography execution. ((string) The message body of the email.)
        """
        def get_MessageBody(self):
            return self._output.get('MessageBody', None)
        """
        Retrieve the value for the "Sender" output from this choreography execution. ((string) The sender email address.)
        """
        def get_Sender(self):
            return self._output.get('Sender', None)
        """
        Retrieve the value for the "Subject" output from this choreography execution. ((string) The subject of the email.)
        """
        def get_Subject(self):
            return self._output.get('Subject', None)

class GetEmailChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetEmailResultSet(response, path)
