# -*- coding: utf-8 -*-

###############################################################################
#
# Purchase
# Returns lifecycle emissions for any good or service. 
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class Purchase(Choreography):

    """
    Create a new instance of the Purchase Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/BrighterPlanet/Purchase')


    def new_input_set(self):
        return PurchaseInputSet()

    def _make_result_set(self, result, path):
        return PurchaseResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return PurchaseChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the Purchase
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class PurchaseInputSet(InputSet):
        """
        Set the value of the APIKey input for this choreography. ((required, string) The API Key provided by Brighter Planet.)
        """
        def set_APIKey(self, value):
            InputSet._set_input(self, 'APIKey', value)

        """
        Set the value of the Cost input for this choreography. ((optional, decimal) The cost associated with the purchase.)
        """
        def set_Cost(self, value):
            InputSet._set_input(self, 'Cost', value)

        """
        Set the value of the Date input for this choreography. ((optional, date) The date of the purchase in YYYY-MM-DD format.)
        """
        def set_Date(self, value):
            InputSet._set_input(self, 'Date', value)

        """
        Set the value of the Industry input for this choreography. ((optional, integer) An industry code (NAICS CODE) corresponding to the industry to return results for. For example, the id for Audio and Video Equipment Manufacturing is 334310.)
        """
        def set_Industry(self, value):
            InputSet._set_input(self, 'Industry', value)

        """
        Set the value of the MerchantCategory input for this choreography. ((optional, string) The id for a merchant category.)
        """
        def set_MerchantCategory(self, value):
            InputSet._set_input(self, 'MerchantCategory', value)

        """
        Set the value of the Merchant input for this choreography. ((optional, integer) An id corresponding to a merchant that you want to return data for.)
        """
        def set_Merchant(self, value):
            InputSet._set_input(self, 'Merchant', value)

        """
        Set the value of the PurchaseAmount input for this choreography. ((optional, decimal) The purchase amount.)
        """
        def set_PurchaseAmount(self, value):
            InputSet._set_input(self, 'PurchaseAmount', value)

        """
        Set the value of the ResponseFormat input for this choreography. ((optional, string) Specify your desired response format. Accepted values are xml and json (the default).)
        """
        def set_ResponseFormat(self, value):
            InputSet._set_input(self, 'ResponseFormat', value)

        """
        Set the value of the SicIndustry input for this choreography. ((optional, integer) A Sic Industry id (i.e. 0111 is the code for Wheat, 0112 is the code for Rice, etc).)
        """
        def set_SicIndustry(self, value):
            InputSet._set_input(self, 'SicIndustry', value)

        """
        Set the value of the Tax input for this choreography. ((optional, decimal) The tax amount for the purchase.)
        """
        def set_Tax(self, value):
            InputSet._set_input(self, 'Tax', value)

        """
        Set the value of the Timeframe input for this choreography. ((optional, string) A date range specified in the following format: 2008-01-01/2008-07-09)
        """
        def set_Timeframe(self, value):
            InputSet._set_input(self, 'Timeframe', value)


"""
A ResultSet with methods tailored to the values returned by the Purchase choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class PurchaseResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The response from Brighter Planet.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class PurchaseChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return PurchaseResultSet(response, path)
