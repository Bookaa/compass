# -*- coding: utf-8 -*-

###############################################################################
#
# GetDistrictsByZip
# Returns all districts that overlap the area for a given zip code.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class GetDistrictsByZip(Choreography):

    """
    Create a new instance of the GetDistrictsByZip Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/SunlightLabs/Congress/District/GetDistrictsByZip')


    def new_input_set(self):
        return GetDistrictsByZipInputSet()

    def _make_result_set(self, result, path):
        return GetDistrictsByZipResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetDistrictsByZipChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the GetDistrictsByZip
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class GetDistrictsByZipInputSet(InputSet):
        """
        Set the value of the APIKey input for this choreography. ((required, string) The API Key provided by Sunlight Labs.)
        """
        def set_APIKey(self, value):
            InputSet._set_input(self, 'APIKey', value)

        """
        Set the value of the ResponseFormat input for this choreography. ((optional, string) The format that the response should be in. Valid values are: json (the default) and xml.)
        """
        def set_ResponseFormat(self, value):
            InputSet._set_input(self, 'ResponseFormat', value)

        """
        Set the value of the Zip input for this choreography. ((required, string) The zip code for the districts to return.)
        """
        def set_Zip(self, value):
            InputSet._set_input(self, 'Zip', value)


"""
A ResultSet with methods tailored to the values returned by the GetDistrictsByZip choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class GetDistrictsByZipResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The response from the Sunlight Congress API.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class GetDistrictsByZipChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetDistrictsByZipResultSet(response, path)
