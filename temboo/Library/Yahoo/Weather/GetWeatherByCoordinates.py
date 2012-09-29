# -*- coding: utf-8 -*-

###############################################################################
#
# GetWeatherByCoordinates
# Retrieves the Yahoo Weather RSS Feed for any specified location by geo-coordinates.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class GetWeatherByCoordinates(Choreography):

    """
    Create a new instance of the GetWeatherByCoordinates Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Yahoo/Weather/GetWeatherByCoordinates')


    def new_input_set(self):
        return GetWeatherByCoordinatesInputSet()

    def _make_result_set(self, result, path):
        return GetWeatherByCoordinatesResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetWeatherByCoordinatesChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the GetWeatherByCoordinates
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class GetWeatherByCoordinatesInputSet(InputSet):
        """
        Set the value of the AppID input for this choreography. ((required, string) The App ID provided by Yahoo!)
        """
        def set_AppID(self, value):
            InputSet._set_input(self, 'AppID', value)

        """
        Set the value of the Lattitude input for this choreography. ((required, decimal) The lattitude coordinate of the location you want to search.)
        """
        def set_Lattitude(self, value):
            InputSet._set_input(self, 'Lattitude', value)

        """
        Set the value of the Longitude input for this choreography. ((required, decimal) The longitude coordinate of the location you want to search.)
        """
        def set_Longitude(self, value):
            InputSet._set_input(self, 'Longitude', value)

        """
        Set the value of the Units input for this choreography. ((optional, string) The unit of temperature in the response. Acceptable inputs: f for Fahrenheit or c for Celcius. Defaults to f. When c is specified, all units measurements returned are changed to metric.)
        """
        def set_Units(self, value):
            InputSet._set_input(self, 'Units', value)


"""
A ResultSet with methods tailored to the values returned by the GetWeatherByCoordinates choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class GetWeatherByCoordinatesResultSet(ResultSet):
        """
        Retrieve the value for the "Address" output from this choreography execution. (The address of the location corresponding to the coordinates.)
        """
        def get_Address(self):
            return self._output.get('Address', None)
        """
        Retrieve the value for the "Response" output from this choreography execution. (The response from Yahoo Weather.)
        """
        def get_Response(self):
            return self._output.get('Response', None)
        """
        Retrieve the value for the "WOEID" output from this choreography execution. ((integer) The unigue Where On Earth ID of the location.)
        """
        def get_WOEID(self):
            return self._output.get('WOEID', None)

class GetWeatherByCoordinatesChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetWeatherByCoordinatesResultSet(response, path)
