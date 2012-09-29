# -*- coding: utf-8 -*-

###############################################################################
#
# GetPlaceInformation
# Returns all the information about a known place.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class GetPlaceInformation(Choreography):

    """
    Create a new instance of the GetPlaceInformation Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Twitter/PlacesAndGeo/GetPlaceInformation')


    def new_input_set(self):
        return GetPlaceInformationInputSet()

    def _make_result_set(self, result, path):
        return GetPlaceInformationResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetPlaceInformationChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the GetPlaceInformation
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class GetPlaceInformationInputSet(InputSet):
        """
        Set the value of the PlaceId input for this choreography. ((required, string) An id that corresponds to a place in the world. These IDs can be retrieved from the ReverseGeocode Choreo.)
        """
        def set_PlaceId(self, value):
            InputSet._set_input(self, 'PlaceId', value)

        """
        Set the value of the ResponseFormat input for this choreography. ((optional, string) Specify the format of the response from Twitter: json, or xml.  Default is set to json.)
        """
        def set_ResponseFormat(self, value):
            InputSet._set_input(self, 'ResponseFormat', value)


"""
A ResultSet with methods tailored to the values returned by the GetPlaceInformation choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class GetPlaceInformationResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The response from Twitter.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class GetPlaceInformationChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetPlaceInformationResultSet(response, path)
