# -*- coding: utf-8 -*-

###############################################################################
#
# UpdateFile
# Updates the content of an existing Google document.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class UpdateFile(Choreography):

    """
    Create a new instance of the UpdateFile Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Google/Documents/UpdateFile')


    def new_input_set(self):
        return UpdateFileInputSet()

    def _make_result_set(self, result, path):
        return UpdateFileResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return UpdateFileChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the UpdateFile
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class UpdateFileInputSet(InputSet):
        """
        Set the value of the FileContents input for this choreography. ((conditional, string) The base64-encoded contents of the file you want to update.)
        """
        def set_FileContents(self, value):
            InputSet._set_input(self, 'FileContents', value)

        """
        Set the value of the ContentType input for this choreography. ((required, string) Enter the content type for the file. Currently, the supported content types are: application/pdf, application/rtf, application/msword, application/vnd.ms-excel, text/plain, and text/csv.)
        """
        def set_ContentType(self, value):
            InputSet._set_input(self, 'ContentType', value)

        """
        Set the value of the Password input for this choreography. ((required, string) The password for your Google account.)
        """
        def set_Password(self, value):
            InputSet._set_input(self, 'Password', value)

        """
        Set the value of the Title input for this choreography. ((required, string) The title of the document that you want to update.)
        """
        def set_Title(self, value):
            InputSet._set_input(self, 'Title', value)

        """
        Set the value of the Username input for this choreography. ((required, string) The email address for your Google account.)
        """
        def set_Username(self, value):
            InputSet._set_input(self, 'Username', value)

        """
        Set the value of the VaultFile input for this choreography. (The path to the Vault file to upload. This can be used as an alternative to the FileContents input.)
        """


"""
A ResultSet with methods tailored to the values returned by the UpdateFile choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class UpdateFileResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response from the Google Documents API.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class UpdateFileChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return UpdateFileResultSet(response, path)
