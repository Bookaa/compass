# -*- coding: utf-8 -*-

###############################################################################
#
# GetWeatherByAddress
# Retrieves the Yahoo Weather RSS Feed for any specified location by address.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class GetWeatherByAddress(Choreography):

    """
    Create a new instance of the GetWeatherByAddress Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Yahoo/Weather/GetWeatherByAddress')


    def new_input_set(self):
        return GetWeatherByAddressInputSet()

    def _make_result_set(self, result, path):
        return GetWeatherByAddressResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetWeatherByAddressChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the GetWeatherByAddress
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class GetWeatherByAddressInputSet(InputSet):
        """
        Set the value of the Address input for this choreography. ((required, string) The address to be searched.)
        """
        def set_Address(self, value):
            InputSet._set_input(self, 'Address', value)

        """
        Set the value of the AppID input for this choreography. ((required, string) The App ID provided by Yahoo!)
        """
        def set_AppID(self, value):
            InputSet._set_input(self, 'AppID', value)

        """
        Set the value of the Units input for this choreography. ((optional, string) The unit of temperature in the response. Acceptable inputs: f for Fahrenheit or c for Celcius. Defaults to f. When c is specified, all units measurements returned are changed to metric.)
        """
        def set_Units(self, value):
            InputSet._set_input(self, 'Units', value)


"""
A ResultSet with methods tailored to the values returned by the GetWeatherByAddress choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class GetWeatherByAddressResultSet(ResultSet):
        """
        Retrieve the value for the "AddressFile" output from this choreography execution. (The address file returned by Yahoo! GeoCode.)
        """
        def get_AddressFile(self):
            return self._output.get('AddressFile', None)
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

class GetWeatherByAddressChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetWeatherByAddressResultSet(response, path)
