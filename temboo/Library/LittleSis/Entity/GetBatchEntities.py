# -*- coding: utf-8 -*-

###############################################################################
#
# GetBatchEntities
# Retrieves the LittleSis record for a given Entity (person or organization) by its ID.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class GetBatchEntities(Choreography):

    """
    Create a new instance of the GetBatchEntities Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/LittleSis/Entity/GetBatchEntities')


    def new_input_set(self):
        return GetBatchEntitiesInputSet()

    def _make_result_set(self, result, path):
        return GetBatchEntitiesResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetBatchEntitiesChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the GetBatchEntities
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class GetBatchEntitiesInputSet(InputSet):
        """
        Set the value of the APIKey input for this choreography. ((required, string) The API Key obtained from LittleSis.org.)
        """
        def set_APIKey(self, value):
            InputSet._set_input(self, 'APIKey', value)

        """
        Set the value of the Details input for this choreography. ((optional, integer) Indicate 1 to retrieve detailed information associated with each record retrieved Otherwise, only a basic record will be returned.)
        """
        def set_Details(self, value):
            InputSet._set_input(self, 'Details', value)

        """
        Set the value of the EntityIDs input for this choreography. ((required, string) A comma delimited string of the IDs of the Entities to retrieve.)
        """
        def set_EntityIDs(self, value):
            InputSet._set_input(self, 'EntityIDs', value)

        """
        Set the value of the ResponseFormat input for this choreography. ((optional, string) Format of the response returned by LittleSis.org. Acceptable inputs: xml or json. Defaults to xml)
        """
        def set_ResponseFormat(self, value):
            InputSet._set_input(self, 'ResponseFormat', value)


"""
A ResultSet with methods tailored to the values returned by the GetBatchEntities choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class GetBatchEntitiesResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The response from LittleSis.org.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class GetBatchEntitiesChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetBatchEntitiesResultSet(response, path)
