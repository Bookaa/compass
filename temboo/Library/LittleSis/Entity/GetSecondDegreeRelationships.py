# -*- coding: utf-8 -*-

###############################################################################
#
# GetSecondDegreeRelationships
# Retrieves a list of all the Entities (people or organizations) that are two-degrees removed by Relationships from the given Entity.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class GetSecondDegreeRelationships(Choreography):

    """
    Create a new instance of the GetSecondDegreeRelationships Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/LittleSis/Entity/GetSecondDegreeRelationships')


    def new_input_set(self):
        return GetSecondDegreeRelationshipsInputSet()

    def _make_result_set(self, result, path):
        return GetSecondDegreeRelationshipsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetSecondDegreeRelationshipsChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the GetSecondDegreeRelationships
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class GetSecondDegreeRelationshipsInputSet(InputSet):
        """
        Set the value of the APIKey input for this choreography. ((required, string) The API Key obtained from LittleSis.org.)
        """
        def set_APIKey(self, value):
            InputSet._set_input(self, 'APIKey', value)

        """
        Set the value of the Category1 input for this choreography. ((optional, string) Comma delimited list of Category IDs. Restricts the categories of Relationships that the given Entity and all first degree Entities returned should be connected through.)
        """
        def set_Category1(self, value):
            InputSet._set_input(self, 'Category1', value)

        """
        Set the value of the Category2 input for this choreography. ((optional, string) Comma delimited list of Category IDs. Restricts the categories of Relationships that the given Entity and all second degree Entities returned should be connected through.)
        """
        def set_Category2(self, value):
            InputSet._set_input(self, 'Category2', value)

        """
        Set the value of the EntityID input for this choreography. ((required, integer) The ID of the person or organization for which records are to be returned.)
        """
        def set_EntityID(self, value):
            InputSet._set_input(self, 'EntityID', value)

        """
        Set the value of the Number input for this choreography. ((optional, integer) Specifies what number of results to show. Used in conjunction with Page parameter, a Number of 20 and a Page of 6 will show results 100-120. Defaults to 20.)
        """
        def set_Number(self, value):
            InputSet._set_input(self, 'Number', value)

        """
        Set the value of the Order1 input for this choreography. ((optional, integer) Specifies the order of the Entities returned in the first degree Relationship. Acceptable values: 1 or 2. See documentation for more on Relationship order.)
        """
        def set_Order1(self, value):
            InputSet._set_input(self, 'Order1', value)

        """
        Set the value of the Order2 input for this choreography. ((optional, integer) Specifies the order of the first degree Entity in the second degree Relationship. Acceptable values: 1 or 2. See documentation for more on Relationship order.)
        """
        def set_Order2(self, value):
            InputSet._set_input(self, 'Order2', value)

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
A ResultSet with methods tailored to the values returned by the GetSecondDegreeRelationships choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class GetSecondDegreeRelationshipsResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The response from LittleSis.org.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class GetSecondDegreeRelationshipsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetSecondDegreeRelationshipsResultSet(response, path)
