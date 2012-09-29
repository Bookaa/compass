# -*- coding: utf-8 -*-

###############################################################################
#
# ChemicalSearch
# Retrieves information about specific chemicals released by EPA-regulated facilities.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class ChemicalSearch(Choreography):

    """
    Create a new instance of the ChemicalSearch Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/EnviroFacts/ChemicalSearch')


    def new_input_set(self):
        return ChemicalSearchInputSet()

    def _make_result_set(self, result, path):
        return ChemicalSearchResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ChemicalSearchChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the ChemicalSearch
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class ChemicalSearchInputSet(InputSet):
        """
        Set the value of the ChemicalID input for this choreography. ((required, string) EPA ID number of a chemical. Chemical IDs from a given facility can be found by first running the ChemActivityByFacility or ToxinReleaseByFacility Choreos.)
        """
        def set_ChemicalID(self, value):
            InputSet._set_input(self, 'ChemicalID', value)


"""
A ResultSet with methods tailored to the values returned by the ChemicalSearch choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class ChemicalSearchResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response from EnviroFacts.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class ChemicalSearchChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ChemicalSearchResultSet(response, path)
