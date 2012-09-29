# -*- coding: utf-8 -*-

###############################################################################
#
# GetEntity
# Retrieves the LittleSis record for a given Entity (person or organization) by its ID.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class GetEntity(Choreography):

    """
    Create a new instance of the GetEntity Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/LittleSis/Entity/GetEntity')


    def new_input_set(self):
        return GetEntityInputSet()

    def _make_result_set(self, result, path):
        return GetEntityResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetEntityChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the GetEntity
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class GetEntityInputSet(InputSet):
        """
        Set the value of the APIKey input for this choreography. ((required, string) The API Key obtained from LittleSis.org.)
        """
        def set_APIKey(self, value):
            InputSet._set_input(self, 'APIKey', value)

        """
        Set the value of the Details input for this choreography. ((optional, string) Indicate "details" to retrieve detailed information associated with this record, including aliases. Otherwise, only a basic record will be returned.)
        """
        def set_Details(self, value):
            InputSet._set_input(self, 'Details', value)

        """
        Set the value of the EntityID input for this choreography. ((required, integer) The EntityID of the person or organization record to be returned.)
        """
        def set_EntityID(self, value):
            InputSet._set_input(self, 'EntityID', value)

        """
        Set the value of the ResponseFormat input for this choreography. ((optional, string) Format of the response returned by LittleSis.org. Acceptable inputs: xml or json. Defaults to xml)
        """
        def set_ResponseFormat(self, value):
            InputSet._set_input(self, 'ResponseFormat', value)


"""
A ResultSet with methods tailored to the values returned by the GetEntity choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class GetEntityResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The response from LittleSis.org.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class GetEntityChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetEntityResultSet(response, path)
