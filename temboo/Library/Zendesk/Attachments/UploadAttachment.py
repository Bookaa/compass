# -*- coding: utf-8 -*-

###############################################################################
#
# UploadAttachment
# Uploads a file to be used as an attachment to a ticket.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class UploadAttachment(Choreography):

    """
    Create a new instance of the UploadAttachment Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Zendesk/Attachments/UploadAttachment')


    def new_input_set(self):
        return UploadAttachmentInputSet()

    def _make_result_set(self, result, path):
        return UploadAttachmentResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return UploadAttachmentChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the UploadAttachment
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class UploadAttachmentInputSet(InputSet):
        """
        Set the value of the Email input for this choreography. ((required, string) The email address you use to login to your Zendesk account.)
        """
        def set_Email(self, value):
            InputSet._set_input(self, 'Email', value)

        """
        Set the value of the ExistingToken input for this choreography. ((optional, string) Allows you to pass in an existing token when uploading multiple attachments to associate with a ticket creation.)
        """
        def set_ExistingToken(self, value):
            InputSet._set_input(self, 'ExistingToken', value)

        """
        Set the value of the FileContents input for this choreography. ((required, string) The Base64 encoded file contents of the attachment you want to upload.)
        """
        def set_FileContents(self, value):
            InputSet._set_input(self, 'FileContents', value)

        """
        Set the value of the FileName input for this choreography. ((required, string) )
        """
        def set_FileName(self, value):
            InputSet._set_input(self, 'FileName', value)

        """
        Set the value of the Password input for this choreography. ((required, string) Your Zendesk password.)
        """
        def set_Password(self, value):
            InputSet._set_input(self, 'Password', value)

        """
        Set the value of the Server input for this choreography. ((required, string) Your Zendesk domain and subdomain (i.e. support.temboo.com or temboo.zendesk.com).)
        """
        def set_Server(self, value):
            InputSet._set_input(self, 'Server', value)

        """
        Set the value of the VaultFile input for this choreography. (The path to a vault file to upload. Can be used as an alternative to the FileContents input.)
        """


"""
A ResultSet with methods tailored to the values returned by the UploadAttachment choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class UploadAttachmentResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((json) The response from Zendesk.)
        """
        def get_Response(self):
            return self._output.get('Response', None)
        """
        Retrieve the value for the "Token" output from this choreography execution. ((string) The token returned from Zendesk for the upload. This can be passed to the ExistingToken input when associating  multiple attachments to the same upload token.)
        """
        def get_Token(self):
            return self._output.get('Token', None)

class UploadAttachmentChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return UploadAttachmentResultSet(response, path)
