# -*- coding: utf-8 -*-

###############################################################################
#
# UploadFile
# Uploads a file to Parse.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class UploadFile(Choreography):

    """
    Create a new instance of the UploadFile Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Parse/Files/UploadFile')


    def new_input_set(self):
        return UploadFileInputSet()

    def _make_result_set(self, result, path):
        return UploadFileResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return UploadFileChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the UploadFile
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class UploadFileInputSet(InputSet):
        """
        Set the value of the FileContents input for this choreography. ((conditional, string) The Base64-encoded contents of the file you want to upload.)
        """
        def set_FileContents(self, value):
            InputSet._set_input(self, 'FileContents', value)

        """
        Set the value of the ApplicationID input for this choreography. ((required, string) The Application ID provided by Parse.)
        """
        def set_ApplicationID(self, value):
            InputSet._set_input(self, 'ApplicationID', value)

        """
        Set the value of the ContentType input for this choreography. ((required, string) The content type of the file that is being uploaded (i.e. text/plain, image/jpeg, etc).)
        """
        def set_ContentType(self, value):
            InputSet._set_input(self, 'ContentType', value)

        """
        Set the value of the FileName input for this choreography. ((required, string) The name of the file you are uploading to Parse.)
        """
        def set_FileName(self, value):
            InputSet._set_input(self, 'FileName', value)

        """
        Set the value of the RESTAPIKey input for this choreography. ((required, string) The REST API Key provided by Parse.)
        """
        def set_RESTAPIKey(self, value):
            InputSet._set_input(self, 'RESTAPIKey', value)

        """
        Set the value of the VaultFile input for this choreography. (A path to a vault file to upload. Can be used as an alternative to the FileContents input.)
        """


"""
A ResultSet with methods tailored to the values returned by the UploadFile choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class UploadFileResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((json) The response from Parse.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class UploadFileChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return UploadFileResultSet(response, path)
