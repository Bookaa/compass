# -*- coding: utf-8 -*-

###############################################################################
#
# GetMetricsForZipCode
# Returns a place object and associated facts and metrics with a given zip code.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class GetMetricsForZipCode(Choreography):

    """
    Create a new instance of the GetMetricsForZipCode Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Genability/TariffData/GetMetricsForZipCode')


    def new_input_set(self):
        return GetMetricsForZipCodeInputSet()

    def _make_result_set(self, result, path):
        return GetMetricsForZipCodeResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetMetricsForZipCodeChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the GetMetricsForZipCode
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class GetMetricsForZipCodeInputSet(InputSet):
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
        Set the value of the ZipCode input for this choreography. ((optional, string) )
        """
        def set_ZipCode(self, value):
            InputSet._set_input(self, 'ZipCode', value)


"""
A ResultSet with methods tailored to the values returned by the GetMetricsForZipCode choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class GetMetricsForZipCodeResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((json) The response from Genability.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class GetMetricsForZipCodeChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetMetricsForZipCodeResultSet(response, path)
