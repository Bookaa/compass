# -*- coding: utf-8 -*-

###############################################################################
#
# ListLocations
# Returns a list of locations of companies matching the given query.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class ListLocations(Choreography):

    """
    Create a new instance of the ListLocations Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/CorpWatch/Lists/ListLocations')


    def new_input_set(self):
        return ListLocationsInputSet()

    def _make_result_set(self, result, path):
        return ListLocationsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ListLocationsChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the ListLocations
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class ListLocationsInputSet(InputSet):
        """
        Set the value of the APIKey input for this choreography. ((optional, string) The APIKey from CorpWatch if you have one.)
        """
        def set_APIKey(self, value):
            InputSet._set_input(self, 'APIKey', value)

        """
        Set the value of the Address input for this choreography. ((optional, string) Enter an address fragment to search for. This can be either a street address, city, or state/subregion.)
        """
        def set_Address(self, value):
            InputSet._set_input(self, 'Address', value)

        """
        Set the value of the CountryCode input for this choreography. ((optional, string) Enter an ISO-3166 formatted country code. )
        """
        def set_CountryCode(self, value):
            InputSet._set_input(self, 'CountryCode', value)

        """
        Set the value of the Index input for this choreography. ((optional, integer) Set the index number of the first result to be returned. The index of the first result is 0.)
        """
        def set_Index(self, value):
            InputSet._set_input(self, 'Index', value)

        """
        Set the value of the Limit input for this choreography. ((optional, integer) The number of results to be returned. Defaults to 100. Maximum is 5000.)
        """
        def set_Limit(self, value):
            InputSet._set_input(self, 'Limit', value)

        """
        Set the value of the MaxYear input for this choreography. ((optional, integer) Indicate desired year of the most recent appearance in SEC filing data (e.g. indicating 2007 will search for companies that ceased filing in 2007).)
        """
        def set_MaxYear(self, value):
            InputSet._set_input(self, 'MaxYear', value)

        """
        Set the value of the MinYear input for this choreography. ((optional, integer) Indicate desired year of the earliest appearance in SEC filing data (e.g. indicating 2004 will search for companies that started filing in 2004).)
        """
        def set_MinYear(self, value):
            InputSet._set_input(self, 'MinYear', value)

        """
        Set the value of the PostalCode input for this choreography. ((optional, integer) Enter a postal code to be searched.)
        """
        def set_PostalCode(self, value):
            InputSet._set_input(self, 'PostalCode', value)

        """
        Set the value of the ResponseType input for this choreography. ((optional, string) Specify json or xml for the type of response to be returned. Defaults to xml.)
        """
        def set_ResponseType(self, value):
            InputSet._set_input(self, 'ResponseType', value)

        """
        Set the value of the Type input for this choreography. ((optional, string) Indicates the origin of the location information found. Acceptable values: relation_loc, business, mailing, state_of_incorp. See documentation for more info.)
        """
        def set_Type(self, value):
            InputSet._set_input(self, 'Type', value)

        """
        Set the value of the Year input for this choreography. ((optional, integer) If a year is specified, only records for that year will be returned and the data in the company objects returned will be set appropriately for the request year. Defaults to most recent.)
        """
        def set_Year(self, value):
            InputSet._set_input(self, 'Year', value)


"""
A ResultSet with methods tailored to the values returned by the ListLocations choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class ListLocationsResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The response from CorpWatch.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class ListLocationsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ListLocationsResultSet(response, path)
