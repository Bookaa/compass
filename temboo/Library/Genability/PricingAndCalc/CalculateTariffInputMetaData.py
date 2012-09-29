# -*- coding: utf-8 -*-

###############################################################################
#
# CalculateTariffInputMetaData
# Retrieve inputs required to run a calculation for the specified tariff, within a specified period of time.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class CalculateTariffInputMetaData(Choreography):

    """
    Create a new instance of the CalculateTariffInputMetaData Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Genability/PricingAndCalc/CalculateTariffInputMetaData')


    def new_input_set(self):
        return CalculateTariffInputMetaDataInputSet()

    def _make_result_set(self, result, path):
        return CalculateTariffInputMetaDataResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CalculateTariffInputMetaDataChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the CalculateTariffInputMetaData
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class CalculateTariffInputMetaDataInputSet(InputSet):
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
        Set the value of the BillingPeriod input for this choreography. ((optional, string) Enter: true, or false, to specify whether results retireved should be based on a billing period, or not.  Default is set to: false.)
        """
        def set_BillingPeriod(self, value):
            InputSet._set_input(self, 'BillingPeriod', value)

        """
        Set the value of the CityLimits input for this choreography. ((optional, string) Specify whether electricity pricing information should be restricted to city limits, or not.  Example input value: Inside.)
        """
        def set_CityLimits(self, value):
            InputSet._set_input(self, 'CityLimits', value)

        """
        Set the value of the ConnectionType input for this choreography. ((optional, string) Enter a connection type.  For example: Primary.)
        """
        def set_ConnectionType(self, value):
            InputSet._set_input(self, 'ConnectionType', value)

        """
        Set the value of the FromDateTime input for this choreography. ((required, string) Enter the date and time of the requested start of the price query. Must be in ISO 8601 format.  Example: 2012-06-12T00:00:00.0-0700)
        """
        def set_FromDateTime(self, value):
            InputSet._set_input(self, 'FromDateTime', value)

        """
        Set the value of the GroupBy input for this choreography. ((optional, string) Specify how calculation details are displayed.  For example retrieved details can be grouped by month, or year. Options include: Daily, Weekly, Month, Year.)
        """
        def set_GroupBy(self, value):
            InputSet._set_input(self, 'GroupBy', value)

        """
        Set the value of the KeyName input for this choreography. ((optional, string) Enter an applicability value.  If an error is returned, indicating the need for an extra applicability parameter, use this variable to set the parameter name.  For example: territoryID.)
        """
        def set_KeyName(self, value):
            InputSet._set_input(self, 'KeyName', value)

        """
        Set the value of the KeyValue input for this choreography. ((conditional, string) Enter the value for the specified KeyName variable. For example if KeyName is set to territoryID, you could provide 3385 for the KeyValue input.)
        """
        def set_KeyValue(self, value):
            InputSet._set_input(self, 'KeyValue', value)

        """
        Set the value of the MasterTariffID input for this choreography. ((required, string) Enter a Genability tariff ID.)
        """
        def set_MasterTariffID(self, value):
            InputSet._set_input(self, 'MasterTariffID', value)

        """
        Set the value of the ToDateTime input for this choreography. ((required, string) Enter the date and time of the requested start of the price query. Must be in ISO 8601 format.  Example: 2012-06-12T00:00:00.0-0700)
        """
        def set_ToDateTime(self, value):
            InputSet._set_input(self, 'ToDateTime', value)


"""
A ResultSet with methods tailored to the values returned by the CalculateTariffInputMetaData choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class CalculateTariffInputMetaDataResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((json) The response from Genability.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class CalculateTariffInputMetaDataChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return CalculateTariffInputMetaDataResultSet(response, path)
