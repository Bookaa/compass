# -*- coding: utf-8 -*-

###############################################################################
#
# RunNewPriceCalculation
# Calculate electricity costs based on a POSTed calculation criteria. 
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class RunNewPriceCalculation(Choreography):

    """
    Create a new instance of the RunNewPriceCalculation Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Genability/PricingAndCalc/RunNewPriceCalculation')


    def new_input_set(self):
        return RunNewPriceCalculationInputSet()

    def _make_result_set(self, result, path):
        return RunNewPriceCalculationResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return RunNewPriceCalculationChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the RunNewPriceCalculation
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class RunNewPriceCalculationInputSet(InputSet):
        """
        Set the value of the POSTData input for this choreography. ((required, json) Enter the POST payload in JSON format.)
        """
        def set_POSTData(self, value):
            InputSet._set_input(self, 'POSTData', value)

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
        Set the value of the MasterTariffID input for this choreography. ((required, string) Enter a Genability tariff ID.)
        """
        def set_MasterTariffID(self, value):
            InputSet._set_input(self, 'MasterTariffID', value)


"""
A ResultSet with methods tailored to the values returned by the RunNewPriceCalculation choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class RunNewPriceCalculationResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((json) The response from Genability.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class RunNewPriceCalculationChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return RunNewPriceCalculationResultSet(response, path)
