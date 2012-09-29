# -*- coding: utf-8 -*-

###############################################################################
#
# GetByCoordinates
# Returns all legislators that currently represent an area (district or state) that contains a given Geo point. 
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class GetByCoordinates(Choreography):

    """
    Create a new instance of the GetByCoordinates Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/SunlightLabs/Congress/Legislator/GetByCoordinates')


    def new_input_set(self):
        return GetByCoordinatesInputSet()

    def _make_result_set(self, result, path):
        return GetByCoordinatesResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetByCoordinatesChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the GetByCoordinates
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class GetByCoordinatesInputSet(InputSet):
        """
        Set the value of the APIKey input for this choreography. ((required, string) The API Key provided by Sunlight Labs.)
        """
        def set_APIKey(self, value):
            InputSet._set_input(self, 'APIKey', value)

        """
        Set the value of the Latitude input for this choreography. ((required, decimal) The latitude coordinate of the area that a legislator represents.)
        """
        def set_Latitude(self, value):
            InputSet._set_input(self, 'Latitude', value)

        """
        Set the value of the Longitude input for this choreography. ((required, decimal) The longitude coordinate of the area that a legislator represents.)
        """
        def set_Longitude(self, value):
            InputSet._set_input(self, 'Longitude', value)

        """
        Set the value of the ResponseFormat input for this choreography. ((optional, string) The format that the response should be in. Valid values are: json (the default) and xml.)
        """
        def set_ResponseFormat(self, value):
            InputSet._set_input(self, 'ResponseFormat', value)


"""
A ResultSet with methods tailored to the values returned by the GetByCoordinates choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class GetByCoordinatesResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The response from the Sunlight Congress API.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class GetByCoordinatesChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetByCoordinatesResultSet(response, path)
