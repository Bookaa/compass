# -*- coding: utf-8 -*-

###############################################################################
#
# UpdateObject
# Updates an existing object.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class UpdateObject(Choreography):

    """
    Create a new instance of the UpdateObject Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Parse/Objects/UpdateObject')


    def new_input_set(self):
        return UpdateObjectInputSet()

    def _make_result_set(self, result, path):
        return UpdateObjectResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return UpdateObjectChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the UpdateObject
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class UpdateObjectInputSet(InputSet):
        """
        Set the value of the ObjectContents input for this choreography. ((required, json) A JSON string containing the object contents.)
        """
        def set_ObjectContents(self, value):
            InputSet._set_input(self, 'ObjectContents', value)

        """
        Set the value of the ApplicationID input for this choreography. ((required, string) The Application ID provided by Parse.)
        """
        def set_ApplicationID(self, value):
            InputSet._set_input(self, 'ApplicationID', value)

        """
        Set the value of the ClassName input for this choreography. ((required, string) The class name for the object being created.)
        """
        def set_ClassName(self, value):
            InputSet._set_input(self, 'ClassName', value)

        """
        Set the value of the ObjectID input for this choreography. ((required, string) The ID of the object to update.)
        """
        def set_ObjectID(self, value):
            InputSet._set_input(self, 'ObjectID', value)

        """
        Set the value of the RESTAPIKey input for this choreography. ((required, string) The REST API Key provided by Parse.)
        """
        def set_RESTAPIKey(self, value):
            InputSet._set_input(self, 'RESTAPIKey', value)


"""
A ResultSet with methods tailored to the values returned by the UpdateObject choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class UpdateObjectResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((json) The response from Parse.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class UpdateObjectChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return UpdateObjectResultSet(response, path)
