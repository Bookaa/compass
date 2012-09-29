# -*- coding: utf-8 -*-

###############################################################################
#
# GetPrice
# Retrieves the consumption price of a specified Tariff over a given date range.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class GetPrice(Choreography):

    """
    Create a new instance of the GetPrice Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Genability/PricingAndCalc/GetPrice')


    def new_input_set(self):
        return GetPriceInputSet()

    def _make_result_set(self, result, path):
        return GetPriceResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetPriceChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the GetPrice
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class GetPriceInputSet(InputSet):
        """
        Set the value of the AccountID input for this choreography. ((optional, string) Enter a Genability ID for an account. More info on Accounts is available here: http://developer.genability.com/documentation/api-reference/account-api/account)
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
        Set the value of the MasterTariffID input for this choreography. ((optional, string) Enter a Genability tariff ID. Not required, if AccountID is specified.)
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
        Set the value of the ProfileID input for this choreography. ((optional, string) Enter a Genability ID of a profile. This ID can be passed instead of consumptionAmount or demandAmount.)
        """
        def set_ProfileID(self, value):
            InputSet._set_input(self, 'ProfileID', value)

        """
        Set the value of the ProviderAccountID input for this choreography. ((optional, string) Specify a unique ID for an Account. Same as AccountId, however your unique ID can be used instead of the Genability Account ID.)
        """
        def set_ProviderAccountID(self, value):
            InputSet._set_input(self, 'ProviderAccountID', value)

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
A ResultSet with methods tailored to the values returned by the GetPrice choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class GetPriceResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((json) The response from Genability.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class GetPriceChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetPriceResultSet(response, path)
