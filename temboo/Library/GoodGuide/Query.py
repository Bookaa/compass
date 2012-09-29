# -*- coding: utf-8 -*-

###############################################################################
#
# Query
# Queries the GoodGuide API by keyword and retrieves information on GoodGuide products.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class Query(Choreography):

    """
    Create a new instance of the Query Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/GoodGuide/Query')


    def new_input_set(self):
        return QueryInputSet()

    def _make_result_set(self, result, path):
        return QueryResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return QueryChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the Query
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class QueryInputSet(InputSet):
        """
        Set the value of the APIFormat input for this choreography. ((optional, string) The response type supplied by GoodGuides. Default is reference. Other acceptable inputs are simple and badge.)
        """
        def set_APIFormat(self, value):
            InputSet._set_input(self, 'APIFormat', value)

        """
        Set the value of the APIKey input for this choreography. ((required, string) The API KEy provided by GoodGuide.)
        """
        def set_APIKey(self, value):
            InputSet._set_input(self, 'APIKey', value)

        """
        Set the value of the Count input for this choreography. ((optional, integer) The number of entries to return. Default is 20. Up to 50 entries can be returned at once.)
        """
        def set_Count(self, value):
            InputSet._set_input(self, 'Count', value)

        """
        Set the value of the Query input for this choreography. ((required, string) A text string used in the keyword search. By default, queries return product data only. Use the EntityType input to query other types of entities.)
        """
        def set_Query(self, value):
            InputSet._set_input(self, 'Query', value)

        """
        Set the value of the SortBy input for this choreography. ((optional, string) Acceptable values: best_match (for keyword searches, this is the default); rating (the overall GoodGuide rating); and name (sorted alphabetically).)
        """
        def set_SortBy(self, value):
            InputSet._set_input(self, 'SortBy', value)

        """
        Set the value of the SortOrder input for this choreography. ((optional, string) Acceptable values: 'desc' to sort descending (default for sort_by=rating and sort_by is best_match); 'asc' to sort ascending (default for sort_by is name).)
        """
        def set_SortOrder(self, value):
            InputSet._set_input(self, 'SortOrder', value)


"""
A ResultSet with methods tailored to the values returned by the Query choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class QueryResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response from GoodGuide.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class QueryChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return QueryResultSet(response, path)
