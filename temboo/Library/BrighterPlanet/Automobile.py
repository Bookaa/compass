# -*- coding: utf-8 -*-

###############################################################################
#
# Automobile
# Returns greenhouse gas modeling for passenger vehicles operated over periods of time.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class Automobile(Choreography):

    """
    Create a new instance of the Automobile Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/BrighterPlanet/Automobile')


    def new_input_set(self):
        return AutomobileInputSet()

    def _make_result_set(self, result, path):
        return AutomobileResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return AutomobileChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the Automobile
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class AutomobileInputSet(InputSet):
        """
        Set the value of the APIKey input for this choreography. ((required, string) The API Key provided by Brighter Planet.)
        """
        def set_APIKey(self, value):
            InputSet._set_input(self, 'APIKey', value)

        """
        Set the value of the Acquisition input for this choreography. ((optional, string) Date automobile was acquired in YYYY-MM-DD format.)
        """
        def set_Acquisition(self, value):
            InputSet._set_input(self, 'Acquisition', value)

        """
        Set the value of the AnnualDistance input for this choreography. ((optional, decimal) Annual distance traveled in kilometres.)
        """
        def set_AnnualDistance(self, value):
            InputSet._set_input(self, 'AnnualDistance', value)

        """
        Set the value of the AnnualFuelUse input for this choreography. ((optional, decimal) Total fuel used in one year in litres.)
        """
        def set_AnnualFuelUse(self, value):
            InputSet._set_input(self, 'AnnualFuelUse', value)

        """
        Set the value of the AutomobileFuel input for this choreography. ((optional, string) Fuel used by automobile (e.g. regular gasoline).)
        """
        def set_AutomobileFuel(self, value):
            InputSet._set_input(self, 'AutomobileFuel', value)

        """
        Set the value of the Country input for this choreography. ((optional, string) ISO code of the country. Defaults to 3166.)
        """
        def set_Country(self, value):
            InputSet._set_input(self, 'Country', value)

        """
        Set the value of the DailyDistance input for this choreography. ((optional, decimal) Daily distance traveled on average in kilometres.)
        """
        def set_DailyDistance(self, value):
            InputSet._set_input(self, 'DailyDistance', value)

        """
        Set the value of the DailyDuration input for this choreography. ((optional, integer) Average amount of time used daily in seconds.)
        """
        def set_DailyDuration(self, value):
            InputSet._set_input(self, 'DailyDuration', value)

        """
        Set the value of the FuelEfficiency input for this choreography. ((optional, decimal) The automobile's fuel efficiency in kilometres per litre.)
        """
        def set_FuelEfficiency(self, value):
            InputSet._set_input(self, 'FuelEfficiency', value)

        """
        Set the value of the FuelUse input for this choreography. ((optional, decimal) Amount of fuel used in litres.)
        """
        def set_FuelUse(self, value):
            InputSet._set_input(self, 'FuelUse', value)

        """
        Set the value of the Hybridity input for this choreography. ((optional, boolean) Enter whether the automobile is a hybrid.)
        """
        def set_Hybridity(self, value):
            InputSet._set_input(self, 'Hybridity', value)

        """
        Set the value of the Make input for this choreography. ((optional, string) Automobile make (e.g. Honda).)
        """
        def set_Make(self, value):
            InputSet._set_input(self, 'Make', value)

        """
        Set the value of the Model input for this choreography. ((optional, string) Model of automobile (e.g. Civic, Accord).)
        """
        def set_Model(self, value):
            InputSet._set_input(self, 'Model', value)

        """
        Set the value of the ResponseFormat input for this choreography. ((optional, string) Specify your desired response format. Accepted values are xml and json (the default).)
        """
        def set_ResponseFormat(self, value):
            InputSet._set_input(self, 'ResponseFormat', value)

        """
        Set the value of the Retirement input for this choreography. ((optional, string) Date automobile is retired from use in YYYY-MM-DD format.)
        """
        def set_Retirement(self, value):
            InputSet._set_input(self, 'Retirement', value)

        """
        Set the value of the SizeClass input for this choreography. ((optional, string) Automobile size class (e.g. midsize car, large van).)
        """
        def set_SizeClass(self, value):
            InputSet._set_input(self, 'SizeClass', value)

        """
        Set the value of the Speed input for this choreography. ((optional, decimal) Enter average speed when in use in kilometres per hour.)
        """
        def set_Speed(self, value):
            InputSet._set_input(self, 'Speed', value)

        """
        Set the value of the Urbanity input for this choreography. ((optional, boolean) Enter whether the trip is in an urban area.)
        """
        def set_Urbanity(self, value):
            InputSet._set_input(self, 'Urbanity', value)

        """
        Set the value of the WeeklyDistance input for this choreography. ((optional, integer) Enter average weekly distance automobile travels in kilometres.)
        """
        def set_WeeklyDistance(self, value):
            InputSet._set_input(self, 'WeeklyDistance', value)

        """
        Set the value of the Year input for this choreography. ((optional, integer) Year that automobile was manufactured.)
        """
        def set_Year(self, value):
            InputSet._set_input(self, 'Year', value)


"""
A ResultSet with methods tailored to the values returned by the Automobile choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class AutomobileResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The response from Brighter Planet.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class AutomobileChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return AutomobileResultSet(response, path)
