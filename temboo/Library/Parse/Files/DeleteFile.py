# -*- coding: utf-8 -*-

###############################################################################
#
# DeleteFile
# Deletes a file stored on Parse.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class DeleteFile(Choreography):

    """
    Create a new instance of the DeleteFile Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Parse/Files/DeleteFile')


    def new_input_set(self):
        return DeleteFileInputSet()

    def _make_result_set(self, result, path):
        return DeleteFileResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return DeleteFileChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the DeleteFile
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class DeleteFileInputSet(InputSet):
        """
        Set the value of the FileName input for this choreography. ((required, json) The name of the file to delete. Note that this is the name generated and returned by Parse after uploading the file.)
        """
        def set_FileName(self, value):
            InputSet._set_input(self, 'FileName', value)

        """
        Set the value of the ApplicationID input for this choreography. ((required, string) The Application ID provided by Parse.)
        """
        def set_ApplicationID(self, value):
            InputSet._set_input(self, 'ApplicationID', value)

        """
        Set the value of the MasterKey input for this choreography. ((required, string) The Master Key provided by Parse.)
        """
        def set_MasterKey(self, value):
            InputSet._set_input(self, 'MasterKey', value)


"""
A ResultSet with methods tailored to the values returned by the DeleteFile choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class DeleteFileResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((json) The response from Parse.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class DeleteFileChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return DeleteFileResultSet(response, path)
