# -*- coding: utf-8 -*-

###############################################################################
#
# FullTextSearch
# Returns a list of Congressional Record documents in which the given phrase appears.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class FullTextSearch(Choreography):

    """
    Create a new instance of the FullTextSearch Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/SunlightLabs/CapitolWords/FullTextSearch')


    def new_input_set(self):
        return FullTextSearchInputSet()

    def _make_result_set(self, result, path):
        return FullTextSearchResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return FullTextSearchChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the FullTextSearch
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class FullTextSearchInputSet(InputSet):
        """
        Set the value of the APIKey input for this choreography. ((required, string) The API Key provided by Sunlight Labs.)
        """
        def set_APIKey(self, value):
            InputSet._set_input(self, 'APIKey', value)

        """
        Set the value of the BioguideID input for this choreography. ((optional, string) Limit results to the member of Congress with the given Bioguide ID. The Bioguide ID of any current or past congressonal member can be found at bioguide.congress.gov.)
        """
        def set_BioguideID(self, value):
            InputSet._set_input(self, 'BioguideID', value)

        """
        Set the value of the CRPages input for this choreography. ((optional, string) The pages in the Congressional Record to search.)
        """
        def set_CRPages(self, value):
            InputSet._set_input(self, 'CRPages', value)

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
        Set the value of the Page input for this choreography. ((optional, integer) The page of results to show. 100 shown at a time.)
        """
        def set_Page(self, value):
            InputSet._set_input(self, 'Page', value)

        """
        Set the value of the Party input for this choreography. ((optional, string) Limit results to members of congress from a given party. Valid values: R, D, I.)
        """
        def set_Party(self, value):
            InputSet._set_input(self, 'Party', value)

        """
        Set the value of the Phrase input for this choreography. ((required, string) A phrase to search the body of each Congressional Record document for. Either Phrase or Title inputs are required.)
        """
        def set_Phrase(self, value):
            InputSet._set_input(self, 'Phrase', value)

        """
        Set the value of the ResponseFormat input for this choreography. ((optional, string) Output formats inlcude json and xml. Defaults to json.)
        """
        def set_ResponseFormat(self, value):
            InputSet._set_input(self, 'ResponseFormat', value)

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
        Set the value of the Title input for this choreography. ((optional, integer) A phrase to search the title of each Congressional Record document for. Either Phrase or Title are required.)
        """
        def set_Title(self, value):
            InputSet._set_input(self, 'Title', value)


"""
A ResultSet with methods tailored to the values returned by the FullTextSearch choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class FullTextSearchResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((json) The response from CapitolWords.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class FullTextSearchChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return FullTextSearchResultSet(response, path)
