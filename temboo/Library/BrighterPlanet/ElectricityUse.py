# -*- coding: utf-8 -*-

###############################################################################
#
# ElectricityUse
# Returns information about the carbon footprint of using electricity from the US public grid.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class ElectricityUse(Choreography):

    """
    Create a new instance of the ElectricityUse Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/BrighterPlanet/ElectricityUse')


    def new_input_set(self):
        return ElectricityUseInputSet()

    def _make_result_set(self, result, path):
        return ElectricityUseResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ElectricityUseChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the ElectricityUse
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class ElectricityUseInputSet(InputSet):
        """
        Set the value of the APIKey input for this choreography. ((required, string) The API Key provided by Brighter Planet.)
        """
        def set_APIKey(self, value):
            InputSet._set_input(self, 'APIKey', value)

        """
        Set the value of the Country input for this choreography. ((optional, string) An iso_3166 country code.)
        """
        def set_Country(self, value):
            InputSet._set_input(self, 'Country', value)

        """
        Set the value of the Date input for this choreography. ((optional, date) The date of the electricity use in YYYY-MM-DD format.)
        """
        def set_Date(self, value):
            InputSet._set_input(self, 'Date', value)

        """
        Set the value of the Energy input for this choreography. ((optional, decimal) The amount of engery in kilowatt hours.)
        """
        def set_Energy(self, value):
            InputSet._set_input(self, 'Energy', value)

        """
        Set the value of the ResponseFormat input for this choreography. ((optional, string) Specify your desired response format. Accepted values are xml and json (the default).)
        """
        def set_ResponseFormat(self, value):
            InputSet._set_input(self, 'ResponseFormat', value)

        """
        Set the value of the State input for this choreography. ((optional, string) A postal abbreviation for the state to return electricity information for.)
        """
        def set_State(self, value):
            InputSet._set_input(self, 'State', value)

        """
        Set the value of the Timeframe input for this choreography. ((optional, string) A date range specified in the following format: 2008-01-01/2008-07-09)
        """
        def set_Timeframe(self, value):
            InputSet._set_input(self, 'Timeframe', value)

        """
        Set the value of the ZipCode input for this choreography. ((optional, string) The postal code for the area to retrieve electricity information for.)
        """
        def set_ZipCode(self, value):
            InputSet._set_input(self, 'ZipCode', value)


"""
A ResultSet with methods tailored to the values returned by the ElectricityUse choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class ElectricityUseResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The response from Brighter Planet.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class ElectricityUseChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ElectricityUseResultSet(response, path)
