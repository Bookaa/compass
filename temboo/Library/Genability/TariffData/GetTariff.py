# -*- coding: utf-8 -*-

###############################################################################
#
# GetTariff
# Returns an individual Tariff object with a given id.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class GetTariff(Choreography):

    """
    Create a new instance of the GetTariff Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Genability/TariffData/GetTariff')


    def new_input_set(self):
        return GetTariffInputSet()

    def _make_result_set(self, result, path):
        return GetTariffResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetTariffChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the GetTariff
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class GetTariffInputSet(InputSet):
        """
        Set the value of the AppID input for this choreography. ((conditional, string) The App ID provided by Genability.)
        """
        def set_AppID(self, value):
            InputSet._set_input(self, 'AppID', value)

        """
        Set the value of the AppKey input for this choreography. ((required, string) The App Key provided by Genability.)
        """
        def set_AppKey(self, value):
            InputSet._set_input(self, 'AppKey', value)

        """
        Set the value of the MasterTariffID input for this choreography. ((required, integer) The master tariff id. This can be retrieved in the output of the GetTariffs Choreo.)
        """
        def set_MasterTariffID(self, value):
            InputSet._set_input(self, 'MasterTariffID', value)

        """
        Set the value of the PopulateProperties input for this choreography. ((optional, boolean) Set to "true" to populate the properties for the returned Tariffs.)
        """
        def set_PopulateProperties(self, value):
            InputSet._set_input(self, 'PopulateProperties', value)

        """
        Set the value of the PopulateRates input for this choreography. ((optional, boolean) Set to "true" to populate the rate details for the returned Tariffs.)
        """
        def set_PopulateRates(self, value):
            InputSet._set_input(self, 'PopulateRates', value)


"""
A ResultSet with methods tailored to the values returned by the GetTariff choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class GetTariffResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((json) The response from Genability.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class GetTariffChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetTariffResultSet(response, path)
