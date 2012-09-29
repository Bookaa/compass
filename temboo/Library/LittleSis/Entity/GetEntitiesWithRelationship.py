# -*- coding: utf-8 -*-

###############################################################################
#
# GetEntitiesWithRelationship
# Retrieves a list of Entities (person or organization) to which a known relationship exists in LittleSis for any Entity.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class GetEntitiesWithRelationship(Choreography):

    """
    Create a new instance of the GetEntitiesWithRelationship Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/LittleSis/Entity/GetEntitiesWithRelationship')


    def new_input_set(self):
        return GetEntitiesWithRelationshipInputSet()

    def _make_result_set(self, result, path):
        return GetEntitiesWithRelationshipResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetEntitiesWithRelationshipChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the GetEntitiesWithRelationship
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class GetEntitiesWithRelationshipInputSet(InputSet):
        """
        Set the value of the APIKey input for this choreography. ((required, string) The API Key obtained from LittleSis.org.)
        """
        def set_APIKey(self, value):
            InputSet._set_input(self, 'APIKey', value)

        """
        Set the value of the CategoryIDs input for this choreography. ((optional, string) Comma delimited list of category IDs of the categories to which the resulting Entities should belong.)
        """
        def set_CategoryIDs(self, value):
            InputSet._set_input(self, 'CategoryIDs', value)

        """
        Set the value of the Current input for this choreography. ((optional, integer) Set to 1 to limit the relationships returned to only past relationships. Set to 0 to limit relationships returned to only current relationships. Defaults to all.)
        """
        def set_Current(self, value):
            InputSet._set_input(self, 'Current', value)

        """
        Set the value of the EntityID input for this choreography. ((required, integer) The ID of the person or organization fro which a record is to be returned.)
        """
        def set_EntityID(self, value):
            InputSet._set_input(self, 'EntityID', value)

        """
        Set the value of the Number input for this choreography. ((optional, integer) Specifies what number of results to show. Used in conjunction with Page parameter, a Number of 20 and a Page of 6 will show results 100-120.)
        """
        def set_Number(self, value):
            InputSet._set_input(self, 'Number', value)

        """
        Set the value of the Order input for this choreography. ((optional, integer) Specifies what order the given entity must have in the relationship.)
        """
        def set_Order(self, value):
            InputSet._set_input(self, 'Order', value)

        """
        Set the value of the Page input for this choreography. ((optional, integer) Specifies what page of results to show. Used in conjunction with Number parameter. A number of 20 and a Page of 6 will show results 100-120.)
        """
        def set_Page(self, value):
            InputSet._set_input(self, 'Page', value)

        """
        Set the value of the ResponseFormat input for this choreography. ((optional, string) Format of the response returned by LittleSis.org. Acceptable inputs: xml or json. Defaults to xml)
        """
        def set_ResponseFormat(self, value):
            InputSet._set_input(self, 'ResponseFormat', value)

        """
        Set the value of the SortBy input for this choreography. ((optional, string) Defaults to sorting by entity, which returns a list of relationships grouped by related entity. Specify another sort order for the results. Acceptable inputs: category or relationship.)
        """
        def set_SortBy(self, value):
            InputSet._set_input(self, 'SortBy', value)


"""
A ResultSet with methods tailored to the values returned by the GetEntitiesWithRelationship choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class GetEntitiesWithRelationshipResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The response from LittleSis.org.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class GetEntitiesWithRelationshipChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetEntitiesWithRelationshipResultSet(response, path)
