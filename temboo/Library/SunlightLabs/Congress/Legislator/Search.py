# -*- coding: utf-8 -*-

###############################################################################
#
# Search
# Provides a fuzzy-matching text search of the legislators.
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
        Choreography.__init__(self, temboo_session, '/Library/SunlightLabs/Congress/Legislator/Search')


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
        Set the value of the APIKey input for this choreography. ((required, string) The API Key provided by Sunlight Labs.)
        """
        def set_APIKey(self, value):
            InputSet._set_input(self, 'APIKey', value)

        """
        Set the value of the AllLegislators input for this choreography. ((optional, boolean) A boolean flag indicating to search for all legislators even when they are no longer in office.)
        """
        def set_AllLegislators(self, value):
            InputSet._set_input(self, 'AllLegislators', value)

        """
        Set the value of the Name input for this choreography. ((required, string) A name to search for.)
        """
        def set_Name(self, value):
            InputSet._set_input(self, 'Name', value)

        """
        Set the value of the ResponseFormat input for this choreography. ((optional, string) The format that the response should be in. Valid values are: json (the default) and xml.)
        """
        def set_ResponseFormat(self, value):
            InputSet._set_input(self, 'ResponseFormat', value)


"""
A ResultSet with methods tailored to the values returned by the Search choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class SearchResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The response from the Sunlight Congress API.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class SearchChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return SearchResultSet(response, path)
