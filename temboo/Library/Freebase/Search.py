# -*- coding: utf-8 -*-

###############################################################################
#
# Search
# Search the Freebase dataset.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class Search(Choreography):

    """
    Create a new instance of the Search Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Freebase/Search')


    def new_input_set(self):
        return SearchInputSet()

    def _make_result_set(self, result, path):
        return SearchResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return SearchChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the Search
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class SearchInputSet(InputSet):
        """
        Set the value of the APIKey input for this choreography. ((required, string) The API Key provided by Freebase.)
        """
        def set_APIKey(self, value):
            InputSet._set_input(self, 'APIKey', value)

        """
        Set the value of the Domain input for this choreography. ((optional, string) Enter a comma separated list of domain IDs.)
        """
        def set_Domain(self, value):
            InputSet._set_input(self, 'Domain', value)

        """
        Set the value of the EscapeHTMLResults input for this choreography. ((optional, boolean) Specify whether html results are to be escaped or not.  Default is set to: true.)
        """
        def set_EscapeHTMLResults(self, value):
            InputSet._set_input(self, 'EscapeHTMLResults', value)

        """
        Set the value of the Exact input for this choreography. ((optional, boolean) If set to true, the search query will match only the name and keys exactly. No normalization of any kind will be performed at indexing and query time.Default is set to: false.)
        """
        def set_Exact(self, value):
            InputSet._set_input(self, 'Exact', value)

        """
        Set the value of the Filter input for this choreography. ((optional, string) Specify an s-expression to filter search results. For more info, see: http://wiki.freebase.com/wiki/Search_Cookbook)
        """
        def set_Filter(self, value):
            InputSet._set_input(self, 'Filter', value)

        """
        Set the value of the Indent input for this choreography. ((optional, boolean) Specify whether the JSON results should be indented, or not. Enter true, or false. Default: false.)
        """
        def set_Indent(self, value):
            InputSet._set_input(self, 'Indent', value)

        """
        Set the value of the Language input for this choreography. ((optional, string) Specify the language in which the searches will be performed.  Default is set to English: /lang/en)
        """
        def set_Language(self, value):
            InputSet._set_input(self, 'Language', value)

        """
        Set the value of the Limit input for this choreography. ((optional, integer) Specify the number of results to be retrieved.  Default: 20.)
        """
        def set_Limit(self, value):
            InputSet._set_input(self, 'Limit', value)

        """
        Set the value of the MQLOutput input for this choreography. ((optional, string) Enter an MQL query to extract entity information.)
        """
        def set_MQLOutput(self, value):
            InputSet._set_input(self, 'MQLOutput', value)

        """
        Set the value of the Prefixed input for this choreography. ((optional, boolean) Specify whether or not search queries are to match results by name prefix. Default value: false.)
        """
        def set_Prefixed(self, value):
            InputSet._set_input(self, 'Prefixed', value)

        """
        Set the value of the Query input for this choreography. ((required, string) Enter a search query.)
        """
        def set_Query(self, value):
            InputSet._set_input(self, 'Query', value)

        """
        Set the value of the Start input for this choreography. ((optional, integer) Enter a value to page through results.  Default is set to 0.)
        """
        def set_Start(self, value):
            InputSet._set_input(self, 'Start', value)

        """
        Set the value of the Type input for this choreography. ((optional, string) Enter a comma-seperated list of type IDs.)
        """
        def set_Type(self, value):
            InputSet._set_input(self, 'Type', value)


"""
A ResultSet with methods tailored to the values returned by the Search choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class SearchResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The response from the Freebase Search API in JSON format.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class SearchChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return SearchResultSet(response, path)
