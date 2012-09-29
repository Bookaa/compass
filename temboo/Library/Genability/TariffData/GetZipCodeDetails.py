# -*- coding: utf-8 -*-

###############################################################################
#
# GetZipCodeDetails
# Returns the details for a given zip code.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class GetZipCodeDetails(Choreography):

    """
    Create a new instance of the GetZipCodeDetails Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Genability/TariffData/GetZipCodeDetails')


    def new_input_set(self):
        return GetZipCodeDetailsInputSet()

    def _make_result_set(self, result, path):
        return GetZipCodeDetailsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetZipCodeDetailsChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the GetZipCodeDetails
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class GetZipCodeDetailsInputSet(InputSet):
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
        Set the value of the ZipCode input for this choreography. ((optional, string) A zip code to search with.)
        """
        def set_ZipCode(self, value):
            InputSet._set_input(self, 'ZipCode', value)


"""
A ResultSet with methods tailored to the values returned by the GetZipCodeDetails choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class GetZipCodeDetailsResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((json) The response from Genability.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class GetZipCodeDetailsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetZipCodeDetailsResultSet(response, path)
