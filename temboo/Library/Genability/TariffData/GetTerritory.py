# -*- coding: utf-8 -*-

###############################################################################
#
# GetTerritory
# Returns a an individual Territory objects with a given id.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class GetTerritory(Choreography):

    """
    Create a new instance of the GetTerritory Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Genability/TariffData/GetTerritory')


    def new_input_set(self):
        return GetTerritoryInputSet()

    def _make_result_set(self, result, path):
        return GetTerritoryResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetTerritoryChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the GetTerritory
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class GetTerritoryInputSet(InputSet):
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
        Set the value of the PopulateItems input for this choreography. ((optional, boolean) If set to "true", returns a list of territory items for each territory in the result set.)
        """
        def set_PopulateItems(self, value):
            InputSet._set_input(self, 'PopulateItems', value)

        """
        Set the value of the TerritoryID input for this choreography. ((required, integer) The id for the territory to retrieve. This can be retrieved in the output of the GetTerritories Choreo.)
        """
        def set_TerritoryID(self, value):
            InputSet._set_input(self, 'TerritoryID', value)


"""
A ResultSet with methods tailored to the values returned by the GetTerritory choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class GetTerritoryResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((json) The response from Genability.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class GetTerritoryChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetTerritoryResultSet(response, path)
