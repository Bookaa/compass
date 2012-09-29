# -*- coding: utf-8 -*-

###############################################################################
#
# AssociateWithObject
# Allows you to associate a previously uploaded file with Parse objects.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class AssociateWithObject(Choreography):

    """
    Create a new instance of the AssociateWithObject Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Parse/Files/AssociateWithObject')


    def new_input_set(self):
        return AssociateWithObjectInputSet()

    def _make_result_set(self, result, path):
        return AssociateWithObjectResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return AssociateWithObjectChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the AssociateWithObject
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class AssociateWithObjectInputSet(InputSet):
        """
        Set the value of the Association input for this choreography. ((required, json) A JSON string containing the file information that is to be associated with the Parse object. See documentation for formatting examples.)
        """
        def set_Association(self, value):
            InputSet._set_input(self, 'Association', value)

        """
        Set the value of the ApplicationID input for this choreography. ((required, string) The Application ID provided by Parse.)
        """
        def set_ApplicationID(self, value):
            InputSet._set_input(self, 'ApplicationID', value)

        """
        Set the value of the ClassName input for this choreography. ((required, string) The name of the class that a file is being associated with.)
        """
        def set_ClassName(self, value):
            InputSet._set_input(self, 'ClassName', value)

        """
        Set the value of the RESTAPIKey input for this choreography. ((required, string) The REST API Key provided by Parse.)
        """
        def set_RESTAPIKey(self, value):
            InputSet._set_input(self, 'RESTAPIKey', value)


"""
A ResultSet with methods tailored to the values returned by the AssociateWithObject choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class AssociateWithObjectResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((json) The response from Parse.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class AssociateWithObjectChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return AssociateWithObjectResultSet(response, path)
