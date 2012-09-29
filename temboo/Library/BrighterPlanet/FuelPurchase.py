# -*- coding: utf-8 -*-

###############################################################################
#
# FuelPurchase
# Returns information about the carbon emissions from using a wide variety of fuel types.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class FuelPurchase(Choreography):

    """
    Create a new instance of the FuelPurchase Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/BrighterPlanet/FuelPurchase')


    def new_input_set(self):
        return FuelPurchaseInputSet()

    def _make_result_set(self, result, path):
        return FuelPurchaseResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return FuelPurchaseChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the FuelPurchase
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class FuelPurchaseInputSet(InputSet):
        """
        Set the value of the APIKey input for this choreography. ((required, string) The API Key provided by Brighter Planet.)
        """
        def set_APIKey(self, value):
            InputSet._set_input(self, 'APIKey', value)

        """
        Set the value of the Cost input for this choreography. ((optional, decimal) The cost of the fuel purchase.)
        """
        def set_Cost(self, value):
            InputSet._set_input(self, 'Cost', value)

        """
        Set the value of the Date input for this choreography. ((optional, date) The date of the fuel purchase in YYYY-MM-DD format.)
        """
        def set_Date(self, value):
            InputSet._set_input(self, 'Date', value)

        """
        Set the value of the FuelType input for this choreography. ((optional, string) The fuel type purchases (i.e. Asphalt and Road Oil, Aviation Gasoline, Commercial Coal, Commercial Natural Gas, or Motor Gasoline))
        """
        def set_FuelType(self, value):
            InputSet._set_input(self, 'FuelType', value)

        """
        Set the value of the PADD input for this choreography. ((optional, string) A code for the Petroleum administration for defense districts (1A, 1B, 1C, 2, or 3).)
        """
        def set_PADD(self, value):
            InputSet._set_input(self, 'PADD', value)

        """
        Set the value of the Price input for this choreography. ((optional, string) The price of the fuel.)
        """
        def set_Price(self, value):
            InputSet._set_input(self, 'Price', value)

        """
        Set the value of the ResponseFormat input for this choreography. ((optional, string) Specify your desired response format. Accepted values are xml and json (the default).)
        """
        def set_ResponseFormat(self, value):
            InputSet._set_input(self, 'ResponseFormat', value)

        """
        Set the value of the State input for this choreography. ((optional, string) A postal abbreviation for the state where the fuel was purchased.)
        """
        def set_State(self, value):
            InputSet._set_input(self, 'State', value)

        """
        Set the value of the Timeframe input for this choreography. ((optional, string) A date range specified in the following format: 2008-01-01/2008-07-09)
        """
        def set_Timeframe(self, value):
            InputSet._set_input(self, 'Timeframe', value)

        """
        Set the value of the Volume input for this choreography. ((optional, decimal) The amount of fuel purchased.)
        """
        def set_Volume(self, value):
            InputSet._set_input(self, 'Volume', value)

        """
        Set the value of the ZipCode input for this choreography. ((optional, string) The postal code for the area where the fuel was purchased.)
        """
        def set_ZipCode(self, value):
            InputSet._set_input(self, 'ZipCode', value)


"""
A ResultSet with methods tailored to the values returned by the FuelPurchase choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class FuelPurchaseResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The response from Brighter Planet.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class FuelPurchaseChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return FuelPurchaseResultSet(response, path)
