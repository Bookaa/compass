# -*- coding: utf-8 -*-

###############################################################################
#
# TopPhraseSources
# Returns the top sources of a given phrase, which can be sorted either by legislator, state, party, bioguide ID, volume, or chambers.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class TopPhraseSources(Choreography):

    """
    Create a new instance of the TopPhraseSources Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/SunlightLabs/CapitolWords/TopPhraseSources')


    def new_input_set(self):
        return TopPhraseSourcesInputSet()

    def _make_result_set(self, result, path):
        return TopPhraseSourcesResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return TopPhraseSourcesChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the TopPhraseSources
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class TopPhraseSourcesInputSet(InputSet):
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
        Set the value of the Entity input for this choreography. ((required, string) The type of entity for which to return top results. Acceptable inputs: legislator, state, party, bioguide_id, volume, chamber. So 'legislator' returns the top legislators who say the given phrase.)
        """
        def set_Entity(self, value):
            InputSet._set_input(self, 'Entity', value)

        """
        Set the value of the MinCount input for this choreography. ((optional, integer) Only returns results where mentions are at or above the supplied threshold.)
        """
        def set_MinCount(self, value):
            InputSet._set_input(self, 'MinCount', value)

        """
        Set the value of the Page input for this choreography. ((optional, integer) The page number to return.)
        """
        def set_Page(self, value):
            InputSet._set_input(self, 'Page', value)

        """
        Set the value of the Party input for this choreography. ((optional, string) Limit results to members of congress from a given party. Valid values: R, D, I.)
        """
        def set_Party(self, value):
            InputSet._set_input(self, 'Party', value)

        """
        Set the value of the PerPage input for this choreography. ((optional, integer) The number of results to return per page.)
        """
        def set_PerPage(self, value):
            InputSet._set_input(self, 'PerPage', value)

        """
        Set the value of the Phrase input for this choreography. ((required, string) The phrase to search for.)
        """
        def set_Phrase(self, value):
            InputSet._set_input(self, 'Phrase', value)

        """
        Set the value of the ResponseFormat input for this choreography. ((optional, string) Output formats inlcude json and xml. Defaults to json.)
        """
        def set_ResponseFormat(self, value):
            InputSet._set_input(self, 'ResponseFormat', value)

        """
        Set the value of the Sort input for this choreography. ((optional, string) The metric on which to sort top results. Acceptable inputs: tfidf or count. Defaults to tfidf.)
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
A ResultSet with methods tailored to the values returned by the TopPhraseSources choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class TopPhraseSourcesResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((json) The response from CapitolWords.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class TopPhraseSourcesChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return TopPhraseSourcesResultSet(response, path)
