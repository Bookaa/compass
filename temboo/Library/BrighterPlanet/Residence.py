# -*- coding: utf-8 -*-

###############################################################################
#
# Residence
# Returns information about the annual carbon footprint of a home.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class Residence(Choreography):

    """
    Create a new instance of the Residence Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/BrighterPlanet/Residence')


    def new_input_set(self):
        return ResidenceInputSet()

    def _make_result_set(self, result, path):
        return ResidenceResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ResidenceChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the Residence
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class ResidenceInputSet(InputSet):
        """
        Set the value of the APIKey input for this choreography. ((required, string) The API Key provided by Brighter Planet.)
        """
        def set_APIKey(self, value):
            InputSet._set_input(self, 'APIKey', value)

        """
        Set the value of the Acquisition input for this choreography. ((optional, date) Date of acquisition in YYYY-MM-DD format.)
        """
        def set_Acquisition(self, value):
            InputSet._set_input(self, 'Acquisition', value)

        """
        Set the value of the AirConditionerUse input for this choreography. ((optional, string) The frequency of air conditioner use. Accepted values are: "Not used at all", "Turned on just about all summer", "Turned on only a few days or nights when really needed", or "Turned on quite a bit")
        """
        def set_AirConditionerUse(self, value):
            InputSet._set_input(self, 'AirConditionerUse', value)

        """
        Set the value of the AnnualCoalVolumeEstimate input for this choreography. ((optional, decimal) An estimate for amount of coal used annually.)
        """
        def set_AnnualCoalVolumeEstimate(self, value):
            InputSet._set_input(self, 'AnnualCoalVolumeEstimate', value)

        """
        Set the value of the AnnualFuelOilCost input for this choreography. ((optional, decimal) Annual cost of oil fuel in dollars.)
        """
        def set_AnnualFuelOilCost(self, value):
            InputSet._set_input(self, 'AnnualFuelOilCost', value)

        """
        Set the value of the AnnualFuelOilVolumeEstimate input for this choreography. ((optional, decimal) An estimate for the volume oil used annually.)
        """
        def set_AnnualFuelOilVolumeEstimate(self, value):
            InputSet._set_input(self, 'AnnualFuelOilVolumeEstimate', value)

        """
        Set the value of the AnnualPropaneCost input for this choreography. ((optional, decimal) The annual cost of propane annually in dollars.)
        """
        def set_AnnualPropaneCost(self, value):
            InputSet._set_input(self, 'AnnualPropaneCost', value)

        """
        Set the value of the AnnualPropaneVolumeEstimate input for this choreography. ((optional, decimal) An estimate of the amount of propane used annually in litres.)
        """
        def set_AnnualPropaneVolumeEstimate(self, value):
            InputSet._set_input(self, 'AnnualPropaneVolumeEstimate', value)

        """
        Set the value of the AnnualWoodVolumeEstimate input for this choreography. ((optional, decimal) An estimate of the amount of wood used for heating annually (in Joulses).)
        """
        def set_AnnualWoodVolumeEstimate(self, value):
            InputSet._set_input(self, 'AnnualWoodVolumeEstimate', value)

        """
        Set the value of the Bathrooms input for this choreography. ((optional, decimal) The amount of bathrooms in the residence.)
        """
        def set_Bathrooms(self, value):
            InputSet._set_input(self, 'Bathrooms', value)

        """
        Set the value of the Bedrooms input for this choreography. ((optional, decimal) The number of bedrooms in the residence.)
        """
        def set_Bedrooms(self, value):
            InputSet._set_input(self, 'Bedrooms', value)

        """
        Set the value of the ClothesMachineUse input for this choreography. ((optional, string) The number laundry loads per week. Valid values are: "1 load or less each week", "10 to 15 loads", "2 to 4 loads", "5 to 9 loads", "More than 15 loads")
        """
        def set_ClothesMachineUse(self, value):
            InputSet._set_input(self, 'ClothesMachineUse', value)

        """
        Set the value of the ConstructionYear input for this choreography. ((optional, integer) The year the residence was constructed.)
        """
        def set_ConstructionYear(self, value):
            InputSet._set_input(self, 'ConstructionYear', value)

        """
        Set the value of the DishwasherUse input for this choreography. ((optional, string) Number of times the dishwasher is used per week. Valid values: "2 or 3 times a week", "4 to 6 times a week", "At least once each day", "Less than once each week", "Once each week".)
        """
        def set_DishwasherUse(self, value):
            InputSet._set_input(self, 'DishwasherUse', value)

        """
        Set the value of the Floors input for this choreography. ((optional, integer) The number of floors.)
        """
        def set_Floors(self, value):
            InputSet._set_input(self, 'Floors', value)

        """
        Set the value of the FloorspaceEstimate input for this choreography. ((optional, decimal) An estimate of the amount of floorspace that the residence has.)
        """
        def set_FloorspaceEstimate(self, value):
            InputSet._set_input(self, 'FloorspaceEstimate', value)

        """
        Set the value of the FreezerCount input for this choreography. ((optional, integer) The number of freezers in the residence.)
        """
        def set_FreezerCount(self, value):
            InputSet._set_input(self, 'FreezerCount', value)

        """
        Set the value of the FullBathrooms input for this choreography. ((optional, integer) The number of full bathrooms in the residence.)
        """
        def set_FullBathrooms(self, value):
            InputSet._set_input(self, 'FullBathrooms', value)

        """
        Set the value of the GreenElectricty input for this choreography. ((optional, decimal) The amount green electricity that the residence uses.)
        """
        def set_GreenElectricty(self, value):
            InputSet._set_input(self, 'GreenElectricty', value)

        """
        Set the value of the HalfBathrooms input for this choreography. ((optional, integer) The number of half bathrooms in the residence.)
        """
        def set_HalfBathrooms(self, value):
            InputSet._set_input(self, 'HalfBathrooms', value)

        """
        Set the value of the LightingEfficiency input for this choreography. ((optional, decimal) A numeric value representing the lighting efficiency of the residence.)
        """
        def set_LightingEfficiency(self, value):
            InputSet._set_input(self, 'LightingEfficiency', value)

        """
        Set the value of the MonthlyElectricityCost input for this choreography. ((optional, decimal) The montly cost of electricity for the residence.)
        """
        def set_MonthlyElectricityCost(self, value):
            InputSet._set_input(self, 'MonthlyElectricityCost', value)

        """
        Set the value of the MonthlyElectricityUseEstimate input for this choreography. ((optional, decimal) An estimate for the amount of electricity used monthly in kilowatt hours.)
        """
        def set_MonthlyElectricityUseEstimate(self, value):
            InputSet._set_input(self, 'MonthlyElectricityUseEstimate', value)

        """
        Set the value of the MonthlyNaturalGasCost input for this choreography. ((optional, decimal) The monthly cost of natural gas for the residence.)
        """
        def set_MonthlyNaturalGasCost(self, value):
            InputSet._set_input(self, 'MonthlyNaturalGasCost', value)

        """
        Set the value of the MonthlyNaturalGasVolumeEstimate input for this choreography. ((optional, decimal) An estimate of the amount of natural gas used monthly.)
        """
        def set_MonthlyNaturalGasVolumeEstimate(self, value):
            InputSet._set_input(self, 'MonthlyNaturalGasVolumeEstimate', value)

        """
        Set the value of the Occupation input for this choreography. ((optional, decimal) Refers to the percentage of time a residence is occupied during a year. Defaults to 0.937.)
        """
        def set_Occupation(self, value):
            InputSet._set_input(self, 'Occupation', value)

        """
        Set the value of the Ownership input for this choreography. ((optional, boolean) Indicates whether the residence is owned or rented. Set to "true" if you own the residence.)
        """
        def set_Ownership(self, value):
            InputSet._set_input(self, 'Ownership', value)

        """
        Set the value of the RefrigeratorCount input for this choreography. ((optional, integer) The number of refrigerators in the residence.)
        """
        def set_RefrigeratorCount(self, value):
            InputSet._set_input(self, 'RefrigeratorCount', value)

        """
        Set the value of the ResidentialClass input for this choreography. ((optional, string) Valid values: "Apartment in a building with 5 or more units", "Apartment in a house or a building with 2-4 units", "Mobile home", "Single-family attached house", or "Single-family detached house".)
        """
        def set_ResidentialClass(self, value):
            InputSet._set_input(self, 'ResidentialClass', value)

        """
        Set the value of the Residents input for this choreography. ((optional, integer) The number of people living in the residence.)
        """
        def set_Residents(self, value):
            InputSet._set_input(self, 'Residents', value)

        """
        Set the value of the ResponseFormat input for this choreography. ((optional, string) Specify your desired response format. Accepted values are xml and json (the default).)
        """
        def set_ResponseFormat(self, value):
            InputSet._set_input(self, 'ResponseFormat', value)

        """
        Set the value of the Retirement input for this choreography. ((optional, date) A date of retirement.)
        """
        def set_Retirement(self, value):
            InputSet._set_input(self, 'Retirement', value)

        """
        Set the value of the Timeframe input for this choreography. ((optional, string) A date range specified in the following format: 2008-01-01/2008-07-09)
        """
        def set_Timeframe(self, value):
            InputSet._set_input(self, 'Timeframe', value)

        """
        Set the value of the Urbanity input for this choreography. ((optional, string) Can be set to: City, Rural, Suburbs, or Town.)
        """
        def set_Urbanity(self, value):
            InputSet._set_input(self, 'Urbanity', value)

        """
        Set the value of the ZipCode input for this choreography. ((optional, string) The postal code of the residence.)
        """
        def set_ZipCode(self, value):
            InputSet._set_input(self, 'ZipCode', value)


"""
A ResultSet with methods tailored to the values returned by the Residence choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class ResidenceResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The response from Brighter Planet.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class ResidenceChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ResidenceResultSet(response, path)
