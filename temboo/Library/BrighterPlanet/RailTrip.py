# -*- coding: utf-8 -*-

###############################################################################
#
# RailTrip
# Returns information about the carbon footprint of a passenger's train travel.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class RailTrip(Choreography):

    """
    Create a new instance of the RailTrip Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/BrighterPlanet/RailTrip')


    def new_input_set(self):
        return RailTripInputSet()

    def _make_result_set(self, result, path):
        return RailTripResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return RailTripChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the RailTrip
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class RailTripInputSet(InputSet):
        """
        Set the value of the APIKey input for this choreography. ((required, string) The API Key provided by Brighter Planet.)
        """
        def set_APIKey(self, value):
            InputSet._set_input(self, 'APIKey', value)

        """
        Set the value of the Compliance input for this choreography. ((optional, string) Comply with one or more protocols:  Greenhouse Gas Protocol Scope 3 (ghg_protocol_scope_3), ISO 14064-1 (iso), and The Climate Registry (tcr).)
        """
        def set_Compliance(self, value):
            InputSet._set_input(self, 'Compliance', value)

        """
        Set the value of the Country input for this choreography. ((optional, string) A country code associated with the rail trip (in ISO 3166 format).)
        """
        def set_Country(self, value):
            InputSet._set_input(self, 'Country', value)

        """
        Set the value of the Date input for this choreography. ((optional, date) The date of the rail trip in YYYY-MM-DD format.)
        """
        def set_Date(self, value):
            InputSet._set_input(self, 'Date', value)

        """
        Set the value of the Destination input for this choreography. ((optional, string) The destination of the rail trip.)
        """
        def set_Destination(self, value):
            InputSet._set_input(self, 'Destination', value)

        """
        Set the value of the Distance input for this choreography. ((optional, decimal) The distance of the rail trip in kilometres.)
        """
        def set_Distance(self, value):
            InputSet._set_input(self, 'Distance', value)

        """
        Set the value of the Duration input for this choreography. ((optional, decimal) The duration of the rail trip in seconds.)
        """
        def set_Duration(self, value):
            InputSet._set_input(self, 'Duration', value)

        """
        Set the value of the Origin input for this choreography. ((optional, string) The origin of the rail trip.)
        """
        def set_Origin(self, value):
            InputSet._set_input(self, 'Origin', value)

        """
        Set the value of the RailClass input for this choreography. ((optional, string) The rail class associated with the rail trip (i.e. commuter, heavy, highspeed, intercity, light).)
        """
        def set_RailClass(self, value):
            InputSet._set_input(self, 'RailClass', value)

        """
        Set the value of the RailCompany input for this choreography. ((optional, string) The rail company associated with the rail trip (i.e. AMTRAK).)
        """
        def set_RailCompany(self, value):
            InputSet._set_input(self, 'RailCompany', value)

        """
        Set the value of the RailTraction input for this choreography. ((optional, string) The rail traction associated with the rail trip (i.e. diesel, electric).)
        """
        def set_RailTraction(self, value):
            InputSet._set_input(self, 'RailTraction', value)

        """
        Set the value of the ResponseFormat input for this choreography. ((optional, string) Specify your desired response format. Accepted values are xml and json (the default).)
        """
        def set_ResponseFormat(self, value):
            InputSet._set_input(self, 'ResponseFormat', value)

        """
        Set the value of the Timeframe input for this choreography. ((optional, string) A date range specified in the following format: 2008-01-01/2008-07-09)
        """
        def set_Timeframe(self, value):
            InputSet._set_input(self, 'Timeframe', value)


"""
A ResultSet with methods tailored to the values returned by the RailTrip choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class RailTripResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The response from Brighter Planet.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class RailTripChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return RailTripResultSet(response, path)
