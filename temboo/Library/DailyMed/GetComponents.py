# -*- coding: utf-8 -*-

###############################################################################
#
# GetComponents
# Returns imprint data associated with a given National Drug Code (NDC) in the DailyMed database.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class GetComponents(Choreography):

    """
    Create a new instance of the GetComponents Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/DailyMed/GetComponents')


    def new_input_set(self):
        return GetComponentsInputSet()

    def _make_result_set(self, result, path):
        return GetComponentsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetComponentsChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the GetComponents
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class GetComponentsInputSet(InputSet):
        """
        Set the value of the SetID input for this choreography. ((required, string) The unique ID assigned by DailyMed to each drug. You can find the SetID of a drug by first running the SearchByName or SearchByNDC Choreos.)
        """
        def set_SetID(self, value):
            InputSet._set_input(self, 'SetID', value)


"""
A ResultSet with methods tailored to the values returned by the GetComponents choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class GetComponentsResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response from DailyMed.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class GetComponentsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetComponentsResultSet(response, path)
