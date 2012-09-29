# -*- coding: utf-8 -*-

###############################################################################
#
# Shipment
# Returns information about the carbon footprint of shipping packages.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class Shipment(Choreography):

    """
    Create a new instance of the Shipment Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/BrighterPlanet/Shipment')


    def new_input_set(self):
        return ShipmentInputSet()

    def _make_result_set(self, result, path):
        return ShipmentResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ShipmentChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the Shipment
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class ShipmentInputSet(InputSet):
        """
        Set the value of the APIKey input for this choreography. ((required, string) The API Key provided by Brighter Planet.)
        """
        def set_APIKey(self, value):
            InputSet._set_input(self, 'APIKey', value)

        """
        Set the value of the Carrier input for this choreography. ((optional, string) The carrier used for the shipment. Valid values are: FedEx, UPS, or USPS.)
        """
        def set_Carrier(self, value):
            InputSet._set_input(self, 'Carrier', value)

        """
        Set the value of the DestinationZipCode input for this choreography. ((optional, string) The postal code of the destination address.)
        """
        def set_DestinationZipCode(self, value):
            InputSet._set_input(self, 'DestinationZipCode', value)

        """
        Set the value of the Destination input for this choreography. ((optional, string) The destination of the shipment.)
        """
        def set_Destination(self, value):
            InputSet._set_input(self, 'Destination', value)

        """
        Set the value of the Distance input for this choreography. ((optional, decimal) The distance from the shipment origin to the shipment destination.)
        """
        def set_Distance(self, value):
            InputSet._set_input(self, 'Distance', value)

        """
        Set the value of the Mode input for this choreography. ((optional, string) The mode or method of shipment. Valid values are: air, courier, or ground.)
        """
        def set_Mode(self, value):
            InputSet._set_input(self, 'Mode', value)

        """
        Set the value of the OriginZipCode input for this choreography. ((optional, string) The postal code of the origin address.)
        """
        def set_OriginZipCode(self, value):
            InputSet._set_input(self, 'OriginZipCode', value)

        """
        Set the value of the Origin input for this choreography. ((optional, string) The origin of the shipment.)
        """
        def set_Origin(self, value):
            InputSet._set_input(self, 'Origin', value)

        """
        Set the value of the PackageCount input for this choreography. ((optional, integer) The number of packages in the shipment.)
        """
        def set_PackageCount(self, value):
            InputSet._set_input(self, 'PackageCount', value)

        """
        Set the value of the ResponseFormat input for this choreography. ((optional, string) Specify your desired response format. Accepted values are xml and json (the default).)
        """
        def set_ResponseFormat(self, value):
            InputSet._set_input(self, 'ResponseFormat', value)

        """
        Set the value of the Weight input for this choreography. ((optional, decimal) The weight of the shipment in kilograms.)
        """
        def set_Weight(self, value):
            InputSet._set_input(self, 'Weight', value)


"""
A ResultSet with methods tailored to the values returned by the Shipment choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class ShipmentResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The response from Brighter Planet.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class ShipmentChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ShipmentResultSet(response, path)
