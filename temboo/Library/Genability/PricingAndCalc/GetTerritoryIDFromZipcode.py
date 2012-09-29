# -*- coding: utf-8 -*-

###############################################################################
#
# GetTerritoryIDFromZipcode
# Get a territoryID, by using a consumer's zipcode, LSE ID and master tariff ID.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class GetTerritoryIDFromZipcode(Choreography):

    """
    Create a new instance of the GetTerritoryIDFromZipcode Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Genability/PricingAndCalc/GetTerritoryIDFromZipcode')


    def new_input_set(self):
        return GetTerritoryIDFromZipcodeInputSet()

    def _make_result_set(self, result, path):
        return GetTerritoryIDFromZipcodeResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetTerritoryIDFromZipcodeChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the GetTerritoryIDFromZipcode
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class GetTerritoryIDFromZipcodeInputSet(InputSet):
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
        Set the value of the LSEID input for this choreography. ((required, string) Enter an LSE ID.)
        """
        def set_LSEID(self, value):
            InputSet._set_input(self, 'LSEID', value)

        """
        Set the value of the MasterTariffID input for this choreography. ((required, string) Enter a Genability tariff ID.)
        """
        def set_MasterTariffID(self, value):
            InputSet._set_input(self, 'MasterTariffID', value)

        """
        Set the value of the Zipcode input for this choreography. ((required, integer) Enter a Zipcode for which a territory ID is to be retrieved.)
        """
        def set_Zipcode(self, value):
            InputSet._set_input(self, 'Zipcode', value)


"""
A ResultSet with methods tailored to the values returned by the GetTerritoryIDFromZipcode choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class GetTerritoryIDFromZipcodeResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((json) The response from Genability.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class GetTerritoryIDFromZipcodeChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetTerritoryIDFromZipcodeResultSet(response, path)
