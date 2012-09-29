# -*- coding: utf-8 -*-

###############################################################################
#
# Dates
# Returns the popularity of a given phrase in the Congressional Record over time.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class Dates(Choreography):

    """
    Create a new instance of the Dates Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/SunlightLabs/CapitolWords/Dates')


    def new_input_set(self):
        return DatesInputSet()

    def _make_result_set(self, result, path):
        return DatesResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return DatesChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the Dates
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class DatesInputSet(InputSet):
        """
        Set the value of the APIKey input for this choreography. ((required, string) The API Key provided by Sunlight Labs.)
        """
        def set_APIKey(self, value):
            InputSet._set_input(self, 'APIKey', value)

        """
        Set the value of the BioguideID input for this choreography. ((optional, string) Limit results to the member of Congress with the given Bioguide ID. The Bioguide ID of any current or past congressional member can be found at bioguide.congress.gov.)
        """
        def set_BioguideID(self, value):
            InputSet._set_input(self, 'BioguideID', value)

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
        Set the value of the Granularity input for this choreography. ((optional, string) The length of time covered by each result. Valid values: year, month, day. Defaults to day.)
        """
        def set_Granularity(self, value):
            InputSet._set_input(self, 'Granularity', value)

        """
        Set the value of the MinCount input for this choreography. ((optional, boolean) Only returns results where mentions are at or above the supplied threshold.)
        """
        def set_MinCount(self, value):
            InputSet._set_input(self, 'MinCount', value)

        """
        Set the value of the Party input for this choreography. ((optional, string) Limit results to members of congress from a given party. Valid values: R, D, I.)
        """
        def set_Party(self, value):
            InputSet._set_input(self, 'Party', value)

        """
        Set the value of the Percentages input for this choreography. ((optional, string) Include the percentage of mentions versus total words in the result objects. Valid values: true, false. Defaults to false.)
        """
        def set_Percentages(self, value):
            InputSet._set_input(self, 'Percentages', value)

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
A ResultSet with methods tailored to the values returned by the Dates choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class DatesResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((json) The response from CapitolWords.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class DatesChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return DatesResultSet(response, path)
