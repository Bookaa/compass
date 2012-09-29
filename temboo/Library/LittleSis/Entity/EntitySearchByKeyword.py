# -*- coding: utf-8 -*-

###############################################################################
#
# EntitySearchByKeyword
# Retrieves Entities (people or organizations) in LittleSis that match a given keyword search.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class EntitySearchByKeyword(Choreography):

    """
    Create a new instance of the EntitySearchByKeyword Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/LittleSis/Entity/EntitySearchByKeyword')


    def new_input_set(self):
        return EntitySearchByKeywordInputSet()

    def _make_result_set(self, result, path):
        return EntitySearchByKeywordResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return EntitySearchByKeywordChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the EntitySearchByKeyword
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class EntitySearchByKeywordInputSet(InputSet):
        """
        Set the value of the APIKey input for this choreography. ((required, string) The API Key obtained from LittleSis.org.)
        """
        def set_APIKey(self, value):
            InputSet._set_input(self, 'APIKey', value)

        """
        Set the value of the Keywords input for this choreography. ((required, string) Enter search text.)
        """
        def set_Keywords(self, value):
            InputSet._set_input(self, 'Keywords', value)

        """
        Set the value of the Number input for this choreography. ((optional, integer) Specifies what number of results to show. Used in conjunction with Page parameter, a Number of 20 and a Page of 6 will show results 100-120.)
        """
        def set_Number(self, value):
            InputSet._set_input(self, 'Number', value)

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
        Set the value of the SearchAll input for this choreography. ((optional, integer) Enter 1 to search a record's description and summary fields. When not specified, only the name and aliases fields of each record will be searched.)
        """
        def set_SearchAll(self, value):
            InputSet._set_input(self, 'SearchAll', value)

        """
        Set the value of the TypeIDs input for this choreography. ((optional, string) You can specify a TypeIDs value to limit the search results to only those of a given type. Obtain all possible types and type ID's by first running the GetTypes Choreo.)
        """
        def set_TypeIDs(self, value):
            InputSet._set_input(self, 'TypeIDs', value)


"""
A ResultSet with methods tailored to the values returned by the EntitySearchByKeyword choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class EntitySearchByKeywordResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The response from LittleSis.org.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class EntitySearchByKeywordChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return EntitySearchByKeywordResultSet(response, path)
