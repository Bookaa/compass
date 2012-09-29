# -*- coding: utf-8 -*-

###############################################################################
#
# ReverseGeocode
# Given a latitude and a longitude, this API operation searches for up to 20 places that can be used as a place_id when updating a status.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class ReverseGeocode(Choreography):

    """
    Create a new instance of the ReverseGeocode Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Twitter/PlacesAndGeo/ReverseGeocode')


    def new_input_set(self):
        return ReverseGeocodeInputSet()

    def _make_result_set(self, result, path):
        return ReverseGeocodeResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ReverseGeocodeChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the ReverseGeocode
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class ReverseGeocodeInputSet(InputSet):
        """
        Set the value of the Accuracy input for this choreography. ((optional, string) A hint on the "region" in which to search. If a number, then this is a radius in meters. You can also specify feet by using the ft suffix (i.e. 5ft).)
        """
        def set_Accuracy(self, value):
            InputSet._set_input(self, 'Accuracy', value)

        """
        Set the value of the Callback input for this choreography. ((optional, string) If supplied, the response will use the JSONP format with a callback of the given name.)
        """
        def set_Callback(self, value):
            InputSet._set_input(self, 'Callback', value)

        """
        Set the value of the Granularity input for this choreography. ((optional, string) This is the minimal granularity of place types to return and must be one of: poi, neighborhood, city, admin or country. Defaults to neighborhood.)
        """
        def set_Granularity(self, value):
            InputSet._set_input(self, 'Granularity', value)

        """
        Set the value of the Latitude input for this choreography. ((required, decimal) The latitude to search around.)
        """
        def set_Latitude(self, value):
            InputSet._set_input(self, 'Latitude', value)

        """
        Set the value of the Longitude input for this choreography. ((required, decimal) The longitude to search around.)
        """
        def set_Longitude(self, value):
            InputSet._set_input(self, 'Longitude', value)

        """
        Set the value of the MaxResults input for this choreography. ((optional, integer) The maximum number of results to return.)
        """
        def set_MaxResults(self, value):
            InputSet._set_input(self, 'MaxResults', value)

        """
        Set the value of the ResponseFormat input for this choreography. ((optional, string) Specify the format of the response from Twitter: json, or xml.  Default is set to json.)
        """
        def set_ResponseFormat(self, value):
            InputSet._set_input(self, 'ResponseFormat', value)


"""
A ResultSet with methods tailored to the values returned by the ReverseGeocode choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class ReverseGeocodeResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The response from Twitter.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class ReverseGeocodeChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ReverseGeocodeResultSet(response, path)
