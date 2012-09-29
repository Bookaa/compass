# -*- coding: utf-8 -*-

###############################################################################
#
# GetTariffs
# Returns a list of Tariff objects based a specified search criteria.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class GetTariffs(Choreography):

    """
    Create a new instance of the GetTariffs Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Genability/TariffData/GetTariffs')


    def new_input_set(self):
        return GetTariffsInputSet()

    def _make_result_set(self, result, path):
        return GetTariffsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetTariffsChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the GetTariffs
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class GetTariffsInputSet(InputSet):
        """
        Set the value of the AccountID input for this choreography. ((optional, string) The unique ID of the Account to find tariffs for. Values passed in will override those from the Account.)
        """
        def set_AccountID(self, value):
            InputSet._set_input(self, 'AccountID', value)

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
        Set the value of the CustomerClasses input for this choreography. ((optional, string) Returns only these customer classes. Valid values are: RESIDENTIAL, GENERAL.)
        """
        def set_CustomerClasses(self, value):
            InputSet._set_input(self, 'CustomerClasses', value)

        """
        Set the value of the EffectiveOn input for this choreography. ((optional, date) Returns only tariffs that are effective on this date.)
        """
        def set_EffectiveOn(self, value):
            InputSet._set_input(self, 'EffectiveOn', value)

        """
        Set the value of the EndsWith input for this choreography. ((optional, string) When true, the search will only return results that end with the specified search string. Otherwise, any match of the search string will be returned as a result.)
        """
        def set_EndsWith(self, value):
            InputSet._set_input(self, 'EndsWith', value)

        """
        Set the value of the FromDateTime input for this choreography. ((optional, date) Returns only tariffs that are effective on or after this date.)
        """
        def set_FromDateTime(self, value):
            InputSet._set_input(self, 'FromDateTime', value)

        """
        Set the value of the IsRegex input for this choreography. ((optional, boolean) When true, the provided search string will be regarded as a regular expression and the search will return results matching the regular expression.)
        """
        def set_IsRegex(self, value):
            InputSet._set_input(self, 'IsRegex', value)

        """
        Set the value of the LSEID input for this choreography. ((optional, integer) Filter tariffs for a specific LSE.)
        """
        def set_LSEID(self, value):
            InputSet._set_input(self, 'LSEID', value)

        """
        Set the value of the PageCount input for this choreography. ((optional, integer) The number of results to return. Defaults to 25.)
        """
        def set_PageCount(self, value):
            InputSet._set_input(self, 'PageCount', value)

        """
        Set the value of the PageStart input for this choreography. ((optional, integer) The page number to begin the result set from. Defaults to 1.)
        """
        def set_PageStart(self, value):
            InputSet._set_input(self, 'PageStart', value)

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
        Set the value of the SearchOn input for this choreography. ((optional, string) Comma separated list of fields to query on. When searchOn is specified, the text provided in the search string field will be searched within these fields.)
        """
        def set_SearchOn(self, value):
            InputSet._set_input(self, 'SearchOn', value)

        """
        Set the value of the Search input for this choreography. ((optional, string) The string of text to search on. This can also be a regular expression, in which case you should set the 'isRegex' flag to true.)
        """
        def set_Search(self, value):
            InputSet._set_input(self, 'Search', value)

        """
        Set the value of the SortOn input for this choreography. ((optional, string) Comma separated list of fields to sort on.)
        """
        def set_SortOn(self, value):
            InputSet._set_input(self, 'SortOn', value)

        """
        Set the value of the SortOrder input for this choreography. ((optional, string) Comma separated list of ordering. Possible values are 'ASC' and 'DESC'. Default is 'ASC'. This list corresponds to the field list used in the SortOn input.)
        """
        def set_SortOrder(self, value):
            InputSet._set_input(self, 'SortOrder', value)

        """
        Set the value of the StartsWith input for this choreography. ((optional, boolean) When true, the search will only return results that begin with the specified search string. Otherwise, any match of the search string will be returned as a result.)
        """
        def set_StartsWith(self, value):
            InputSet._set_input(self, 'StartsWith', value)

        """
        Set the value of the TariffTypes input for this choreography. ((optional, string) Returns only these tariff types. Valid values are: DEFAULT, ALTERNATIVE, OPTIONAL_EXTRA, RIDER.)
        """
        def set_TariffTypes(self, value):
            InputSet._set_input(self, 'TariffTypes', value)

        """
        Set the value of the ToDateTime input for this choreography. ((optional, date) Returns only tariffs that are effective on or before this date.)
        """
        def set_ToDateTime(self, value):
            InputSet._set_input(self, 'ToDateTime', value)

        """
        Set the value of the ZipCode input for this choreography. ((optional, string) Return tariffs for a given zip or post code.)
        """
        def set_ZipCode(self, value):
            InputSet._set_input(self, 'ZipCode', value)


"""
A ResultSet with methods tailored to the values returned by the GetTariffs choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class GetTariffsResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((json) The response from Genability.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class GetTariffsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetTariffsResultSet(response, path)
