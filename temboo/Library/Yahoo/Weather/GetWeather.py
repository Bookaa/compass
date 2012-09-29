# -*- coding: utf-8 -*-

###############################################################################
#
# GetWeather
# Retrieves the Yahoo! Weather RSS Feed for any specified location.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class GetWeather(Choreography):

    """
    Create a new instance of the GetWeather Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Yahoo/Weather/GetWeather')


    def new_input_set(self):
        return GetWeatherInputSet()

    def _make_result_set(self, result, path):
        return GetWeatherResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetWeatherChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the GetWeather
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class GetWeatherInputSet(InputSet):
        """
        Set the value of the Units input for this choreography. ((optional, string) The unit of temperature in the response. Acceptable inputs: f for Fahrenheit or c for Celcius. Defaults to f. When c is specified, all units measurements returned are changed to metric.)
        """
        def set_Units(self, value):
            InputSet._set_input(self, 'Units', value)

        """
        Set the value of the WOEID input for this choreography. ((required, integer) Where On Earth ID for the desired location. This unique integer can be found by first running the GetWeatherByCoordinates Choreo.)
        """
        def set_WOEID(self, value):
            InputSet._set_input(self, 'WOEID', value)


"""
A ResultSet with methods tailored to the values returned by the GetWeather choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class GetWeatherResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The response from Yahoo! Weather.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class GetWeatherChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetWeatherResultSet(response, path)
