# -*- coding: utf-8 -*-

###############################################################################
#
# CompoundSearch
# Returns a list of companies according to several search parameters such as industry, location, date range, company name, etc.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class CompoundSearch(Choreography):

    """
    Create a new instance of the CompoundSearch Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/CorpWatch/Search/CompoundSearch')


    def new_input_set(self):
        return CompoundSearchInputSet()

    def _make_result_set(self, result, path):
        return CompoundSearchResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CompoundSearchChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the CompoundSearch
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class CompoundSearchInputSet(InputSet):
        """
        Set the value of the APIKey input for this choreography. ((optional, string) The APIKey from CorpWatch if you have one.)
        """
        def set_APIKey(self, value):
            InputSet._set_input(self, 'APIKey', value)

        """
        Set the value of the Address input for this choreography. ((optional, string) Specific fragment of an address to be searched, such as "empire" or "Main Street.")
        """
        def set_Address(self, value):
            InputSet._set_input(self, 'Address', value)

        """
        Set the value of the CountryCode input for this choreography. ((optional, string) Two-letter country code (e.g. VI for Virgin Islands).)
        """
        def set_CountryCode(self, value):
            InputSet._set_input(self, 'CountryCode', value)

        """
        Set the value of the Index input for this choreography. ((optional, integer) Set the index number of the first result to be returned. The index of the first result is 0.)
        """
        def set_Index(self, value):
            InputSet._set_input(self, 'Index', value)

        """
        Set the value of the IndustryCode input for this choreography. ((optional, integer) Standard Industrial Classification (SIC) code.)
        """
        def set_IndustryCode(self, value):
            InputSet._set_input(self, 'IndustryCode', value)

        """
        Set the value of the IndustrySector input for this choreography. ((optional, integer) Standard Industrial Classification (SIC) sector code.)
        """
        def set_IndustrySector(self, value):
            InputSet._set_input(self, 'IndustrySector', value)

        """
        Set the value of the Limit input for this choreography. ((optional, integer) The number of results to be returned. Defaults to 100. Maximum is 5000.)
        """
        def set_Limit(self, value):
            InputSet._set_input(self, 'Limit', value)

        """
        Set the value of the Match input for this choreography. ((optional, integer) By default search terms match against complete words. Use 1 to return cases where the search string matches anywhere in the Name or Address field. Performance is significantly affected when enabled.)
        """
        def set_Match(self, value):
            InputSet._set_input(self, 'Match', value)

        """
        Set the value of the MaxYear input for this choreography. ((optional, integer) Indicate desired year of the most recent appearance in SEC filing data (e.g. indicating 2007 will search for companies that ceased filing in 2007).)
        """
        def set_MaxYear(self, value):
            InputSet._set_input(self, 'MaxYear', value)

        """
        Set the value of the MinYear input for this choreography. ((optional, integer) Indicate desired year of the most recent appearance in SEC filing data (e.g. indicating 2007 will search for companies that ceased filing in 2007).)
        """
        def set_MinYear(self, value):
            InputSet._set_input(self, 'MinYear', value)

        """
        Set the value of the Name input for this choreography. ((optional, string) Company name to search. Words in the search query must match to full words in the name. See documentation for more details.)
        """
        def set_Name(self, value):
            InputSet._set_input(self, 'Name', value)

        """
        Set the value of the NumChildren input for this choreography. ((optional, integer) Limit results to those with a specified number of listed subsidiaries, or "children." (Only immediate relationships are counted.)
        """
        def set_NumChildren(self, value):
            InputSet._set_input(self, 'NumChildren', value)

        """
        Set the value of the NumParents input for this choreography. ((optional, integer) Limit results to those with a specified number of listed parent companies (only immediate relationships are counted).)
        """
        def set_NumParents(self, value):
            InputSet._set_input(self, 'NumParents', value)

        """
        Set the value of the ResponseType input for this choreography. ((optional, string) Specify json or xml for the type of response to be returned. Defaults to xml.)
        """
        def set_ResponseType(self, value):
            InputSet._set_input(self, 'ResponseType', value)

        """
        Set the value of the SourceType input for this choreography. ((optional, string) Indicate "filers" to restrict results to those of companies that appeared as a filer on SEC documents, or "relationships" for companies that only appear as subsidiaries on filings.)
        """
        def set_SourceType(self, value):
            InputSet._set_input(self, 'SourceType', value)

        """
        Set the value of the SubdivisionCode input for this choreography. ((optional, string) Two-letter abbreviation for the subdivision of the area to be searched (e.g. "OR" for Oregon when CountryCode is set to "US").)
        """
        def set_SubdivisionCode(self, value):
            InputSet._set_input(self, 'SubdivisionCode', value)

        """
        Set the value of the TopParent input for this choreography. ((optional, integer) Limit results by he CWID of the highest-level owning parent of a family of corprorations (or Top Parent). Most company records contain a field for top_parent_id.)
        """
        def set_TopParent(self, value):
            InputSet._set_input(self, 'TopParent', value)

        """
        Set the value of the Year input for this choreography. ((optional, integer) If a year is specified, only records for that year will be returned and the data in the company objects returned will be set appropriately for the request year. Defaults to most recent.)
        """
        def set_Year(self, value):
            InputSet._set_input(self, 'Year', value)


"""
A ResultSet with methods tailored to the values returned by the CompoundSearch choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class CompoundSearchResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The response from CorpWatch.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class CompoundSearchChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return CompoundSearchResultSet(response, path)
