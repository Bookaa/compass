# -*- coding: utf-8 -*-

###############################################################################
#
# GetLoadServingEntity
# Returns a Load Serving Entity with a given ID.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class GetLoadServingEntity(Choreography):

    """
    Create a new instance of the GetLoadServingEntity Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Genability/TariffData/GetLoadServingEntity')


    def new_input_set(self):
        return GetLoadServingEntityInputSet()

    def _make_result_set(self, result, path):
        return GetLoadServingEntityResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetLoadServingEntityChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the GetLoadServingEntity
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class GetLoadServingEntityInputSet(InputSet):
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
        Set the value of the LSEID input for this choreography. ((required, integer) The id of a particular Load Serving Entity to return.)
        """
        def set_LSEID(self, value):
            InputSet._set_input(self, 'LSEID', value)


"""
A ResultSet with methods tailored to the values returned by the GetLoadServingEntity choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class GetLoadServingEntityResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((json) The response from Genability.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class GetLoadServingEntityChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetLoadServingEntityResultSet(response, path)
