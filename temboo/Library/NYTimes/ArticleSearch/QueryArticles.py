# -*- coding: utf-8 -*-

###############################################################################
#
# QueryArticles
# Lets you query the Article Search API for New York Times articles.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class QueryArticles(Choreography):

    """
    Create a new instance of the QueryArticles Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/NYTimes/ArticleSearch/QueryArticles')


    def new_input_set(self):
        return QueryArticlesInputSet()

    def _make_result_set(self, result, path):
        return QueryArticlesResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return QueryArticlesChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the QueryArticles
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class QueryArticlesInputSet(InputSet):
        """
        Set the value of the APIKey input for this choreography. ((required, string) The API Key provided by NY Times.)
        """
        def set_APIKey(self, value):
            InputSet._set_input(self, 'APIKey', value)

        """
        Set the value of the BeginDate input for this choreography. ((optional, date) Sets the starting point (which is inclusive) of the range of publication dates to return. Must be used with EndDate.)
        """
        def set_BeginDate(self, value):
            InputSet._set_input(self, 'BeginDate', value)

        """
        Set the value of the EndDate input for this choreography. ((optional, date) Sets the end point (which is inclusive) of the range of publication dates to return. Must be used with BeginDate.)
        """
        def set_EndDate(self, value):
            InputSet._set_input(self, 'EndDate', value)

        """
        Set the value of the Facets input for this choreography. ((optional, string) A comma-delimited list of up to 5 facets. This indicates the sets of facet values to include in the response. See Choreo documentation for more information about accepted values for this input.)
        """
        def set_Facets(self, value):
            InputSet._set_input(self, 'Facets', value)

        """
        Set the value of the Fields input for this choreography. ((optional, string) A comma-delimited list of fields to return. These fields are returned by default: body, byline, date, title, and url.)
        """
        def set_Fields(self, value):
            InputSet._set_input(self, 'Fields', value)

        """
        Set the value of the Offset input for this choreography. ((optional, integer) This corresponds to which set of 10 results is returned. Used to page through results. Set to 0 to return records 0-9, set to 1 to return records 10-19, etc.)
        """
        def set_Offset(self, value):
            InputSet._set_input(self, 'Offset', value)

        """
        Set the value of the Query input for this choreography. ((required, string) Search keywords (optionally applied to specific fields) and/or facets. See Choreo documentation for syntax examples.)
        """
        def set_Query(self, value):
            InputSet._set_input(self, 'Query', value)

        """
        Set the value of the Rank input for this choreography. ((optional, string) Sets the order of the results. Accepted values are: newest (the defaults), oldest, or closest.)
        """
        def set_Rank(self, value):
            InputSet._set_input(self, 'Rank', value)


"""
A ResultSet with methods tailored to the values returned by the QueryArticles choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class QueryArticlesResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((json) The response from the NY Times API.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class QueryArticlesChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return QueryArticlesResultSet(response, path)
