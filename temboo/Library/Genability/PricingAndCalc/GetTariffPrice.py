# -*- coding: utf-8 -*-

###############################################################################
#
# GetTariffPrice
# Retrieve summarized rates of a specified electricity tariff, in addition to changes in rates over a specified time span.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class GetTariffPrice(Choreography):

    """
    Create a new instance of the GetTariffPrice Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Genability/PricingAndCalc/GetTariffPrice')


    def new_input_set(self):
        return GetTariffPriceInputSet()

    def _make_result_set(self, result, path):
        return GetTariffPriceResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetTariffPriceChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the GetTariffPrice
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class GetTariffPriceInputSet(InputSet):
        """
        Set the value of the AccountID input for this choreography. ((optional, string) Enter a Genability ID for an account. This is optional if MasterTariffID is set.)
        """
        def set_AccountID(self, value):
            InputSet._set_input(self, 'AccountID', value)

        """
        Set the value of the AppID input for this choreography. ((required, string) The App ID provided by Genability.)
        """
        def set_AppID(self, value):
            InputSet._set_input(self, 'AppID', value)

        """
        Set the value of the AppKey input for this choreography. ((required, string) The App Key provided by Genability.)
        """
        def set_AppKey(self, value):
            InputSet._set_input(self, 'AppKey', value)

        """
        Set the value of the ConsumptionAmount input for this choreography. ((optional, decimal) Specify a monthly consumption in kWh. By default the highest banded level of consumption is used.)
        """
        def set_ConsumptionAmount(self, value):
            InputSet._set_input(self, 'ConsumptionAmount', value)

        """
        Set the value of the DemandAmount input for this choreography. ((optional, decimal) Specify a monthly demand in kWh. By default the highest banded level of demand is used.)
        """
        def set_DemandAmount(self, value):
            InputSet._set_input(self, 'DemandAmount', value)

        """
        Set the value of the FromDateTime input for this choreography. ((required, string) Enter the date and time of the requested start of the price query. Must be in ISO 8601 format.  Example: 2012-06-12T00:00:00.0-0700)
        """
        def set_FromDateTime(self, value):
            InputSet._set_input(self, 'FromDateTime', value)

        """
        Set the value of the MasterTariffID input for this choreography. ((optional, string) Enter a Genability tariff ID. This variable is not required, if AccountID is set.)
        """
        def set_MasterTariffID(self, value):
            InputSet._set_input(self, 'MasterTariffID', value)

        """
        Set the value of the PageCount input for this choreography. ((optional, integer) Specify the number of results to be returned. Defailt is set to: 25.)
        """
        def set_PageCount(self, value):
            InputSet._set_input(self, 'PageCount', value)

        """
        Set the value of the PageStart input for this choreography. ((optional, integer) Enter the page number to start to display results from. If unspecified, the first page of results will be returned.)
        """
        def set_PageStart(self, value):
            InputSet._set_input(self, 'PageStart', value)

        """
        Set the value of the TerritoryID input for this choreography. ((optional, string) Return rate changes for the specified Territory.)
        """
        def set_TerritoryID(self, value):
            InputSet._set_input(self, 'TerritoryID', value)

        """
        Set the value of the ToDateTime input for this choreography. ((optional, string) Enter the date and time of the requested start of the price query. Must be in ISO 8601 format.  Example: 2012-06-12T00:00:00.0-0700)
        """
        def set_ToDateTime(self, value):
            InputSet._set_input(self, 'ToDateTime', value)


"""
A ResultSet with methods tailored to the values returned by the GetTariffPrice choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class GetTariffPriceResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((json) The response from Genability.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class GetTariffPriceChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetTariffPriceResultSet(response, path)
