# -*- coding: utf-8 -*-

###############################################################################
#
# GeoSearch
# Searches for places that can be attached to a statuses/update using a latitude and a longitude pair, an IP address, or a name.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class GeoSearch(Choreography):

    """
    Create a new instance of the GeoSearch Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Twitter/PlacesAndGeo/GeoSearch')


    def new_input_set(self):
        return GeoSearchInputSet()

    def _make_result_set(self, result, path):
        return GeoSearchResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GeoSearchChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the GeoSearch
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class GeoSearchInputSet(InputSet):
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
        Set the value of the ContainedWithin input for this choreography. ((optional, string) This is the place_id which you would like to restrict the search results to. This id can be retrieved with the GetPlaceInformation Choreo.)
        """
        def set_ContainedWithin(self, value):
            InputSet._set_input(self, 'ContainedWithin', value)

        """
        Set the value of the Granularity input for this choreography. ((optional, string) This is the minimal granularity of place types to return and must be one of: poi, neighborhood, city, admin or country. Defaults to neighborhood.)
        """
        def set_Granularity(self, value):
            InputSet._set_input(self, 'Granularity', value)

        """
        Set the value of the IP input for this choreography. ((conditional, string) An IP address. Used when attempting to fix geolocation based off of the user's IP address. You must provide Latitude and Longitude, IP, or Query.)
        """
        def set_IP(self, value):
            InputSet._set_input(self, 'IP', value)

        """
        Set the value of the Latitude input for this choreography. ((conditional, decimal) The latitude to search around. You must provide Latitude and Longitude, IP, or Query.)
        """
        def set_Latitude(self, value):
            InputSet._set_input(self, 'Latitude', value)

        """
        Set the value of the Longitude input for this choreography. ((conditional, decimal) The longitude to search around. You must provide Latitude and Longitude, IP, or Query.)
        """
        def set_Longitude(self, value):
            InputSet._set_input(self, 'Longitude', value)

        """
        Set the value of the MaxResults input for this choreography. ((optional, integer) The maximum number of results to return.)
        """
        def set_MaxResults(self, value):
            InputSet._set_input(self, 'MaxResults', value)

        """
        Set the value of the Query input for this choreography. ((conditional, string) Free-form text to match against while executing a geo-based query. You must provide Latitude and Longitude, IP, or Query.)
        """
        def set_Query(self, value):
            InputSet._set_input(self, 'Query', value)

        """
        Set the value of the ResponseFormat input for this choreography. ((optional, string) Specify the format of the response from Twitter: json, or xml.  Default is set to json.)
        """
        def set_ResponseFormat(self, value):
            InputSet._set_input(self, 'ResponseFormat', value)


"""
A ResultSet with methods tailored to the values returned by the GeoSearch choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class GeoSearchResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The response from Twitter.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class GeoSearchChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GeoSearchResultSet(response, path)
