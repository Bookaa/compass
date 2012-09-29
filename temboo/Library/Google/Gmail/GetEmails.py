# -*- coding: utf-8 -*-

###############################################################################
#
# GetEmails
# Retrieves one or more email messages from a Gmail inbox.
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
        Choreography.__init__(self, temboo_session, '/Library/Google/Gmail/GetEmails')


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
        Set the value of the DeleteAfterRetrieval input for this choreography. ((optional, boolean) To delete messages after retrieval, set to 1. Defaults to 0 indicating that the messages will not be deleted after retrieval. Note that you will need to adjust Gmail settings to use this feature.)
        """
        def set_DeleteAfterRetrieval(self, value):
            InputSet._set_input(self, 'DeleteAfterRetrieval', value)

        """
        Set the value of the MaxMessages input for this choreography. ((optional, string) The max number of email messages to retrieve. Valid values are 1-100. Defaults to 100.)
        """
        def set_MaxMessages(self, value):
            InputSet._set_input(self, 'MaxMessages', value)

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
A ResultSet with methods tailored to the values returned by the GetEmails choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class GetEmailsResultSet(ResultSet):
        """
        Retrieve the value for the "Messages" output from this choreography execution. ((xml) A list of the email messages retrieved from Gmail. Each email message will contain the message body and message header fields.)
        """
        def get_Messages(self):
            return self._output.get('Messages', None)

class GetEmailsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetEmailsResultSet(response, path)
