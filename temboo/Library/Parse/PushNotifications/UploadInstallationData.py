# -*- coding: utf-8 -*-

###############################################################################
#
# UploadInstallationData
# Creates an installation object on Parse.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class UploadInstallationData(Choreography):

    """
    Create a new instance of the UploadInstallationData Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Parse/PushNotifications/UploadInstallationData')


    def new_input_set(self):
        return UploadInstallationDataInputSet()

    def _make_result_set(self, result, path):
        return UploadInstallationDataResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return UploadInstallationDataChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the UploadInstallationData
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class UploadInstallationDataInputSet(InputSet):
        """
        Set the value of the Installation input for this choreography. ((required, json) A JSON string containing the installation data. See documentation for syntax examples.)
        """
        def set_Installation(self, value):
            InputSet._set_input(self, 'Installation', value)

        """
        Set the value of the ApplicationID input for this choreography. ((required, string) The Application ID provided by Parse.)
        """
        def set_ApplicationID(self, value):
            InputSet._set_input(self, 'ApplicationID', value)

        """
        Set the value of the RESTAPIKey input for this choreography. ((required, string) The REST API Key provided by Parse.)
        """
        def set_RESTAPIKey(self, value):
            InputSet._set_input(self, 'RESTAPIKey', value)


"""
A ResultSet with methods tailored to the values returned by the UploadInstallationData choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class UploadInstallationDataResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((json) The response from Parse.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class UploadInstallationDataChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return UploadInstallationDataResultSet(response, path)
