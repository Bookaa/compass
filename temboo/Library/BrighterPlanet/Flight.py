# -*- coding: utf-8 -*-

###############################################################################
#
# Flight
# Returns information about the carbon footprint of a passenger's air travel.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class Flight(Choreography):

    """
    Create a new instance of the Flight Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/BrighterPlanet/Flight')


    def new_input_set(self):
        return FlightInputSet()

    def _make_result_set(self, result, path):
        return FlightResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return FlightChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the Flight
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class FlightInputSet(InputSet):
        """
        Set the value of the APIKey input for this choreography. ((required, string) The API Key provided by Brighter Planet.)
        """
        def set_APIKey(self, value):
            InputSet._set_input(self, 'APIKey', value)

        """
        Set the value of the Aircraft input for this choreography. ((optional, string) The ICAO code associated with the aircraft.)
        """
        def set_Aircraft(self, value):
            InputSet._set_input(self, 'Aircraft', value)

        """
        Set the value of the Airline input for this choreography. ((optional, string) The name of the airline used (i.e. Continental, Delta, etc).)
        """
        def set_Airline(self, value):
            InputSet._set_input(self, 'Airline', value)

        """
        Set the value of the Compliance input for this choreography. ((optional, string) Comply with one or more protocols:  Greenhouse Gas Protocol Scope 3 (ghg_protocol_scope_3), ISO 14064-1 (iso), and The Climate Registry (tcr).)
        """
        def set_Compliance(self, value):
            InputSet._set_input(self, 'Compliance', value)

        """
        Set the value of the Date input for this choreography. ((optional, date) The date of the trip in YYYY-MM-DD format.)
        """
        def set_Date(self, value):
            InputSet._set_input(self, 'Date', value)

        """
        Set the value of the DestinationAirport input for this choreography. ((optional, string) The airport code for the destination (i.e. LGA, JFK, etc.).)
        """
        def set_DestinationAirport(self, value):
            InputSet._set_input(self, 'DestinationAirport', value)

        """
        Set the value of the DistanceClass input for this choreography. ((optional, string) The distance class associated it the air travel (i.e. long haul, short haul).)
        """
        def set_DistanceClass(self, value):
            InputSet._set_input(self, 'DistanceClass', value)

        """
        Set the value of the DistanceEstimate input for this choreography. ((optional, decimal) A estimate of the distance of the travel in kilometres.)
        """
        def set_DistanceEstimate(self, value):
            InputSet._set_input(self, 'DistanceEstimate', value)

        """
        Set the value of the Fuel input for this choreography. ((optional, string) The type of fuel used in the aircraft (i.e. Aviation Gasoline, Biodiesel).)
        """
        def set_Fuel(self, value):
            InputSet._set_input(self, 'Fuel', value)

        """
        Set the value of the OriginAirport input for this choreography. ((optional, string) The airport code for the origin (i.e. LGA, JFK, etc.).)
        """
        def set_OriginAirport(self, value):
            InputSet._set_input(self, 'OriginAirport', value)

        """
        Set the value of the ResponseFormat input for this choreography. ((optional, string) Specify your desired response format. Accepted values are xml and json (the default).)
        """
        def set_ResponseFormat(self, value):
            InputSet._set_input(self, 'ResponseFormat', value)

        """
        Set the value of the Seats input for this choreography. ((optional, integer) The number of seats.)
        """
        def set_Seats(self, value):
            InputSet._set_input(self, 'Seats', value)

        """
        Set the value of the Timeframe input for this choreography. ((optional, string) A date range specified in the following format: 2008-01-01/2008-07-09)
        """
        def set_Timeframe(self, value):
            InputSet._set_input(self, 'Timeframe', value)

        """
        Set the value of the Trips input for this choreography. ((optional, string) The number of trips to calculate information for.)
        """
        def set_Trips(self, value):
            InputSet._set_input(self, 'Trips', value)


"""
A ResultSet with methods tailored to the values returned by the Flight choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class FlightResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The response from Brighter Planet.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class FlightChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return FlightResultSet(response, path)
