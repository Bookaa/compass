# -*- coding: utf-8 -*-

###############################################################################
#
# DeleteInstallation
# Deletes an installation object.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class DeleteInstallation(Choreography):

    """
    Create a new instance of the DeleteInstallation Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Parse/PushNotifications/DeleteInstallation')


    def new_input_set(self):
        return DeleteInstallationInputSet()

    def _make_result_set(self, result, path):
        return DeleteInstallationResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return DeleteInstallationChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the DeleteInstallation
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class DeleteInstallationInputSet(InputSet):
        """
        Set the value of the ObjectID input for this choreography. ((required, string) The ID of the installation to retrieve.)
        """
        def set_ObjectID(self, value):
            InputSet._set_input(self, 'ObjectID', value)

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
A ResultSet with methods tailored to the values returned by the DeleteInstallation choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class DeleteInstallationResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((json) The response from Parse.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class DeleteInstallationChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return DeleteInstallationResultSet(response, path)
