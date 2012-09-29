# -*- coding: utf-8 -*-

###############################################################################
#
# GetBatchRelationships
# Retrieves information about a batch of relationships in LittleSis according to the relationship IDs provided.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class GetBatchRelationships(Choreography):

    """
    Create a new instance of the GetBatchRelationships Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/LittleSis/Relationship/GetBatchRelationships')


    def new_input_set(self):
        return GetBatchRelationshipsInputSet()

    def _make_result_set(self, result, path):
        return GetBatchRelationshipsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetBatchRelationshipsChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the GetBatchRelationships
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class GetBatchRelationshipsInputSet(InputSet):
        """
        Set the value of the APIKey input for this choreography. ((required, string) The API Key obtained from LittleSis.org.)
        """
        def set_APIKey(self, value):
            InputSet._set_input(self, 'APIKey', value)

        """
        Set the value of the Details input for this choreography. ((optional, integer) Indicate 1 to include details for each relationship record returned. Otherwise, only a basic record will be returned.)
        """
        def set_Details(self, value):
            InputSet._set_input(self, 'Details', value)

        """
        Set the value of the RelationshipIDs input for this choreography. ((required, string) The IDs of the relationship records to be returned as a comma delimited string.)
        """
        def set_RelationshipIDs(self, value):
            InputSet._set_input(self, 'RelationshipIDs', value)

        """
        Set the value of the ResponseFormat input for this choreography. ((optional, string) Format of the response returned by LittleSis.org. Acceptable inputs: xml or json. Defaults to xml)
        """
        def set_ResponseFormat(self, value):
            InputSet._set_input(self, 'ResponseFormat', value)


"""
A ResultSet with methods tailored to the values returned by the GetBatchRelationships choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class GetBatchRelationshipsResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The response from LittleSis.org.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class GetBatchRelationshipsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetBatchRelationshipsResultSet(response, path)
