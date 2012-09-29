# -*- coding: utf-8 -*-

###############################################################################
#
# RetrieveObject
# Retrieves a given object.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class RetrieveObject(Choreography):

    """
    Create a new instance of the RetrieveObject Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Parse/Objects/RetrieveObject')


    def new_input_set(self):
        return RetrieveObjectInputSet()

    def _make_result_set(self, result, path):
        return RetrieveObjectResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return RetrieveObjectChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the RetrieveObject
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class RetrieveObjectInputSet(InputSet):
        """
        Set the value of the ObjectID input for this choreography. ((required, json) The ID of the object to retrieve.)
        """
        def set_ObjectID(self, value):
            InputSet._set_input(self, 'ObjectID', value)

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
        Set the value of the RESTAPIKey input for this choreography. ((required, string) The REST API Key provided by Parse.)
        """
        def set_RESTAPIKey(self, value):
            InputSet._set_input(self, 'RESTAPIKey', value)


"""
A ResultSet with methods tailored to the values returned by the RetrieveObject choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class RetrieveObjectResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((json) The response from Parse.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class RetrieveObjectChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return RetrieveObjectResultSet(response, path)
