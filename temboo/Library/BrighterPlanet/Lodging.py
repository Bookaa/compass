# -*- coding: utf-8 -*-

###############################################################################
#
# Lodging
# Returns the the footprint of a guest's hotel stay.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class Lodging(Choreography):

    """
    Create a new instance of the Lodging Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/BrighterPlanet/Lodging')


    def new_input_set(self):
        return LodgingInputSet()

    def _make_result_set(self, result, path):
        return LodgingResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return LodgingChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the Lodging
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class LodgingInputSet(InputSet):
        """
        Set the value of the ACCoverage input for this choreography. ((optional, decimal) A numeric value representing the AC coverage of the lodging establishment.)
        """
        def set_ACCoverage(self, value):
            InputSet._set_input(self, 'ACCoverage', value)

        """
        Set the value of the APIKey input for this choreography. ((required, string) The API Key provided by Brighter Planet.)
        """
        def set_APIKey(self, value):
            InputSet._set_input(self, 'APIKey', value)

        """
        Set the value of the City input for this choreography. ((optional, string) The city of the establishment.)
        """
        def set_City(self, value):
            InputSet._set_input(self, 'City', value)

        """
        Set the value of the Compliance input for this choreography. ((optional, string) Comply with one or more protocols:  Greenhouse Gas Protocol Scope 3 (ghg_protocol_scope_3), ISO 14064-1 (iso), and The Climate Registry (tcr).)
        """
        def set_Compliance(self, value):
            InputSet._set_input(self, 'Compliance', value)

        """
        Set the value of the ConstructionYear input for this choreography. ((optional, integer) The year that the establishment was constructed.)
        """
        def set_ConstructionYear(self, value):
            InputSet._set_input(self, 'ConstructionYear', value)

        """
        Set the value of the Country input for this choreography. ((optional, string) The ISO 3166 country code associated with the establishment.)
        """
        def set_Country(self, value):
            InputSet._set_input(self, 'Country', value)

        """
        Set the value of the Date input for this choreography. ((optional, date) The date of the stay at the establishment in YYYY-MM-DD format.)
        """
        def set_Date(self, value):
            InputSet._set_input(self, 'Date', value)

        """
        Set the value of the Duration input for this choreography. ((optional, integer) The amount of time spent at the establishment in seconds.)
        """
        def set_Duration(self, value):
            InputSet._set_input(self, 'Duration', value)

        """
        Set the value of the Floors input for this choreography. ((optional, integer) The number of floors at the establishment.)
        """
        def set_Floors(self, value):
            InputSet._set_input(self, 'Floors', value)

        """
        Set the value of the HotTubs input for this choreography. ((optional, integer) The number of hot tubs that the establishment has.)
        """
        def set_HotTubs(self, value):
            InputSet._set_input(self, 'HotTubs', value)

        """
        Set the value of the IndoorPools input for this choreography. ((optional, integer) The number of indoor pools that the establishment has.)
        """
        def set_IndoorPools(self, value):
            InputSet._set_input(self, 'IndoorPools', value)

        """
        Set the value of the LodgingClass input for this choreography. ((optional, string) The lodging class (i.e. Hotel, Inn, or Motel).)
        """
        def set_LodgingClass(self, value):
            InputSet._set_input(self, 'LodgingClass', value)

        """
        Set the value of the OutdoorPools input for this choreography. ((optional, integer) The number of outdoor pools that the establishment has.)
        """
        def set_OutdoorPools(self, value):
            InputSet._set_input(self, 'OutdoorPools', value)

        """
        Set the value of the PropertyRooms input for this choreography. ((optional, integer) The number of rooms on the property.)
        """
        def set_PropertyRooms(self, value):
            InputSet._set_input(self, 'PropertyRooms', value)

        """
        Set the value of the Property input for this choreography. ((optional, integer) A property id (or northstart_id) associated with the establishment.)
        """
        def set_Property(self, value):
            InputSet._set_input(self, 'Property', value)

        """
        Set the value of the ResponseFormat input for this choreography. ((optional, string) Specify your desired response format. Accepted values are xml and json (the default).)
        """
        def set_ResponseFormat(self, value):
            InputSet._set_input(self, 'ResponseFormat', value)

        """
        Set the value of the Rooms input for this choreography. ((optional, integer) The number of rooms.)
        """
        def set_Rooms(self, value):
            InputSet._set_input(self, 'Rooms', value)

        """
        Set the value of the State input for this choreography. ((optional, string) The postal abbreviation for the state that the establishment is in.)
        """
        def set_State(self, value):
            InputSet._set_input(self, 'State', value)

        """
        Set the value of the Timeframe input for this choreography. ((optional, string) A date range specified in the following format: 2008-01-01/2008-07-09)
        """
        def set_Timeframe(self, value):
            InputSet._set_input(self, 'Timeframe', value)

        """
        Set the value of the ZipCode input for this choreography. ((optional, string) The postal code associated with the establishment.)
        """
        def set_ZipCode(self, value):
            InputSet._set_input(self, 'ZipCode', value)


"""
A ResultSet with methods tailored to the values returned by the Lodging choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class LodgingResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The response from Brighter Planet.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class LodgingChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return LodgingResultSet(response, path)
