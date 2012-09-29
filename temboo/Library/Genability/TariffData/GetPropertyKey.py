# -*- coding: utf-8 -*-

###############################################################################
#
# GetPropertyKey
# Returns an individual Property Key using a given key name.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class GetPropertyKey(Choreography):

    """
    Create a new instance of the GetPropertyKey Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Genability/TariffData/GetPropertyKey')


    def new_input_set(self):
        return GetPropertyKeyInputSet()

    def _make_result_set(self, result, path):
        return GetPropertyKeyResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetPropertyKeyChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the GetPropertyKey
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class GetPropertyKeyInputSet(InputSet):
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
        Set the value of the KeyName input for this choreography. ((required, string) The key name for the property key you want to return.)
        """
        def set_KeyName(self, value):
            InputSet._set_input(self, 'KeyName', value)


"""
A ResultSet with methods tailored to the values returned by the GetPropertyKey choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class GetPropertyKeyResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((json) The response from Genability.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class GetPropertyKeyChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetPropertyKeyResultSet(response, path)
