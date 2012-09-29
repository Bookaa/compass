# -*- coding: utf-8 -*-

###############################################################################
#
# GetTimeOfUseGroupIntervals
# Returns all the Intervals for a Time of Use Group within a given date range.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class GetTimeOfUseGroupIntervals(Choreography):

    """
    Create a new instance of the GetTimeOfUseGroupIntervals Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Genability/TariffData/GetTimeOfUseGroupIntervals')


    def new_input_set(self):
        return GetTimeOfUseGroupIntervalsInputSet()

    def _make_result_set(self, result, path):
        return GetTimeOfUseGroupIntervalsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetTimeOfUseGroupIntervalsChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the GetTimeOfUseGroupIntervals
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class GetTimeOfUseGroupIntervalsInputSet(InputSet):
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
        Set the value of the FromDateTime input for this choreography. ((optional, date) The starting date and time of the requested Intervals (in ISO 8601 format). Defaults to current date if not specified.)
        """
        def set_FromDateTime(self, value):
            InputSet._set_input(self, 'FromDateTime', value)

        """
        Set the value of the LSEID input for this choreography. ((required, integer) Used to retrieve a TOU Group for a specific LSE.)
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
        Set the value of the TOUGroupID input for this choreography. ((required, integer) Used to retrieve a TOU Group by its ID.)
        """
        def set_TOUGroupID(self, value):
            InputSet._set_input(self, 'TOUGroupID', value)

        """
        Set the value of the ToDateTime input for this choreography. ((optional, date) The ending date and time of the requested Intervals (in ISO 8601 format). If not specified, defaults to one week ahead of the current date.)
        """
        def set_ToDateTime(self, value):
            InputSet._set_input(self, 'ToDateTime', value)


"""
A ResultSet with methods tailored to the values returned by the GetTimeOfUseGroupIntervals choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class GetTimeOfUseGroupIntervalsResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((json) The response from Genability.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class GetTimeOfUseGroupIntervalsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetTimeOfUseGroupIntervalsResultSet(response, path)
