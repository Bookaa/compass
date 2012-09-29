# -*- coding: utf-8 -*-

###############################################################################
#
# AutomobileTrip
# Returns information about the carbon footprint of driving an automobile.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class AutomobileTrip(Choreography):

    """
    Create a new instance of the AutomobileTrip Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/BrighterPlanet/AutomobileTrip')


    def new_input_set(self):
        return AutomobileTripInputSet()

    def _make_result_set(self, result, path):
        return AutomobileTripResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return AutomobileTripChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the AutomobileTrip
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class AutomobileTripInputSet(InputSet):
        """
        Set the value of the APIKey input for this choreography. ((required, string) The API Key provided by Brighter Planet.)
        """
        def set_APIKey(self, value):
            InputSet._set_input(self, 'APIKey', value)

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
        Set the value of the Date input for this choreography. ((optional, string) Automobile trip date in YYYY-MM-DD format.)
        """
        def set_Date(self, value):
            InputSet._set_input(self, 'Date', value)

        """
        Set the value of the Destination input for this choreography. ((optional, string) Enter the name of a destination.)
        """
        def set_Destination(self, value):
            InputSet._set_input(self, 'Destination', value)

        """
        Set the value of the Distance input for this choreography. ((optional, decimal) Distance traveled in kilometres.)
        """
        def set_Distance(self, value):
            InputSet._set_input(self, 'Distance', value)

        """
        Set the value of the Duration input for this choreography. ((optional, decimal) Duration of trip in total seconds.)
        """
        def set_Duration(self, value):
            InputSet._set_input(self, 'Duration', value)

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
        Set the value of the SizeClass input for this choreography. ((optional, string) Automobile size class (e.g. midsize car, large van).)
        """
        def set_SizeClass(self, value):
            InputSet._set_input(self, 'SizeClass', value)

        """
        Set the value of the Speed input for this choreography. ((optional, decimal) Enter the speed during the trip in kilometres per hour.)
        """
        def set_Speed(self, value):
            InputSet._set_input(self, 'Speed', value)

        """
        Set the value of the Urbanity input for this choreography. ((optional, boolean) Enter whether the trip is in an urban area.)
        """
        def set_Urbanity(self, value):
            InputSet._set_input(self, 'Urbanity', value)

        """
        Set the value of the Year input for this choreography. ((optional, integer) Year that automobile was manufactured.)
        """
        def set_Year(self, value):
            InputSet._set_input(self, 'Year', value)


"""
A ResultSet with methods tailored to the values returned by the AutomobileTrip choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class AutomobileTripResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The response from Brighter Planet.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class AutomobileTripChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return AutomobileTripResultSet(response, path)
