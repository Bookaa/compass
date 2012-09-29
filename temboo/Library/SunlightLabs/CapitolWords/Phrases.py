# -*- coding: utf-8 -*-

###############################################################################
#
# Phrases
# Returns a list of the top phrases in the Congressional Record, which are searchable by day, month, state, or legislator.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class Phrases(Choreography):

    """
    Create a new instance of the Phrases Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/SunlightLabs/CapitolWords/Phrases')


    def new_input_set(self):
        return PhrasesInputSet()

    def _make_result_set(self, result, path):
        return PhrasesResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return PhrasesChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the Phrases
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class PhrasesInputSet(InputSet):
        """
        Set the value of the APIKey input for this choreography. ((required, string) The API Key provided by Sunlight Labs.)
        """
        def set_APIKey(self, value):
            InputSet._set_input(self, 'APIKey', value)

        """
        Set the value of the Chamber input for this choreography. ((optional, string) Limit results to a particular chamber. Valid values: house, senate, extensions.)
        """
        def set_Chamber(self, value):
            InputSet._set_input(self, 'Chamber', value)

        """
        Set the value of the Date input for this choreography. ((optional, string) Show results for only the given date. Format: YYYY-MM-DD)
        """
        def set_Date(self, value):
            InputSet._set_input(self, 'Date', value)

        """
        Set the value of the EndDate input for this choreography. ((optional, string) Limit results to those on or before the given date. Format: YYYY-MM-DD.)
        """
        def set_EndDate(self, value):
            InputSet._set_input(self, 'EndDate', value)

        """
        Set the value of the EntityType input for this choreography. ((required, string) The entity type to get top phrases for. Acceptable values: date, month, state, legislator.)
        """
        def set_EntityType(self, value):
            InputSet._set_input(self, 'EntityType', value)

        """
        Set the value of the EntityValue input for this choreography. ((required, string) The value of the entity to get top phrases for. Acceptable formats as follows for each EntityType: (date) 2011-11-09, (month) 201111, (state) NY. For the legislator EntityType, enter Bioguide ID here.)
        """
        def set_EntityValue(self, value):
            InputSet._set_input(self, 'EntityValue', value)

        """
        Set the value of the Length input for this choreography. ((optional, integer) The length of the phrase, in words, to search for (up to 5).)
        """
        def set_Length(self, value):
            InputSet._set_input(self, 'Length', value)

        """
        Set the value of the Page input for this choreography. ((optional, integer) The page of results to show. 100 results are shown at a time. To see more results use the page parameter.)
        """
        def set_Page(self, value):
            InputSet._set_input(self, 'Page', value)

        """
        Set the value of the Party input for this choreography. ((optional, string) Limit results to members of congress from a given party. Valid values: R, D, I.)
        """
        def set_Party(self, value):
            InputSet._set_input(self, 'Party', value)

        """
        Set the value of the ResponseFormat input for this choreography. ((optional, string) Output formats inlcude json and xml. Defaults to json.)
        """
        def set_ResponseFormat(self, value):
            InputSet._set_input(self, 'ResponseFormat', value)

        """
        Set the value of the Sort input for this choreography. ((optional, string) The metric and direction to sort by. Acceptable values: tfidf asc (default), tfidf desc, count asc, count desc.)
        """
        def set_Sort(self, value):
            InputSet._set_input(self, 'Sort', value)

        """
        Set the value of the StartDate input for this choreography. ((optional, string) Limit results to those on or after the given date. Format: YYYY-MM-DD)
        """
        def set_StartDate(self, value):
            InputSet._set_input(self, 'StartDate', value)

        """
        Set the value of the State input for this choreography. ((optional, string) Limit results to members from a particular state. Format: 2-letter state abbreviation (e.g. MD, RI, NY))
        """
        def set_State(self, value):
            InputSet._set_input(self, 'State', value)


"""
A ResultSet with methods tailored to the values returned by the Phrases choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class PhrasesResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((json) The response from CapitolWords.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class PhrasesChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return PhrasesResultSet(response, path)
