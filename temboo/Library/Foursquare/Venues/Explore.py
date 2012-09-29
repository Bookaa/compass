# -*- coding: utf-8 -*-

###############################################################################
#
# Explore
# Returns a list of recommended venues near the current location.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class Explore(Choreography):

    """
    Create a new instance of the Explore Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Foursquare/Venues/Explore')


    def new_input_set(self):
        return ExploreInputSet()

    def _make_result_set(self, result, path):
        return ExploreResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ExploreChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the Explore
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class ExploreInputSet(InputSet):
        """
        Set the value of the AccuracyOfCoordinates input for this choreography. ((optional, integer) Accuracy of latitude and longitude, in meters.)
        """
        def set_AccuracyOfCoordinates(self, value):
            InputSet._set_input(self, 'AccuracyOfCoordinates', value)

        """
        Set the value of the AltitudeAccuracy input for this choreography. ((optional, integer) Accuracy of the user's altitude, in meters.)
        """
        def set_AltitudeAccuracy(self, value):
            InputSet._set_input(self, 'AltitudeAccuracy', value)

        """
        Set the value of the Altitude input for this choreography. ((optional, integer) Altitude of the user's location, in meters.)
        """
        def set_Altitude(self, value):
            InputSet._set_input(self, 'Altitude', value)

        """
        Set the value of the ClientID input for this choreography. ((conditional, string) Your Foursquare client ID, obtained after registering at Foursquare. Required unless using the OauthToken input.)
        """
        def set_ClientID(self, value):
            InputSet._set_input(self, 'ClientID', value)

        """
        Set the value of the ClientSecret input for this choreography. ((conditional, string) Your Foursquare client secret, obtained after registering at Foursquare. Required unless using the OauthToken input.)
        """
        def set_ClientSecret(self, value):
            InputSet._set_input(self, 'ClientSecret', value)

        """
        Set the value of the Intent input for this choreography. ((optional, string) Limit results to venues when set to "specials".)
        """
        def set_Intent(self, value):
            InputSet._set_input(self, 'Intent', value)

        """
        Set the value of the Latitude input for this choreography. ((conditional, decimal) The latitude point of the user's location. Required unless the Near parameter is provided.)
        """
        def set_Latitude(self, value):
            InputSet._set_input(self, 'Latitude', value)

        """
        Set the value of the Limit input for this choreography. ((optional, integer) Number of results to retun, up to 50.)
        """
        def set_Limit(self, value):
            InputSet._set_input(self, 'Limit', value)

        """
        Set the value of the Longitude input for this choreography. ((conditional, decimal) The longitude point of the user's location. Required unless the Near parameter is provided.)
        """
        def set_Longitude(self, value):
            InputSet._set_input(self, 'Longitude', value)

        """
        Set the value of the Near input for this choreography. ((conditional, string) A string naming a place in the world. If the near string is not geocodable, returns a failed_geocode error. Required unless provided Latitude and Longitude.)
        """
        def set_Near(self, value):
            InputSet._set_input(self, 'Near', value)

        """
        Set the value of the Novelty input for this choreography. ((optional, string) Pass new or old to limit results to places the acting user hasn't been or has been, respectively. Omitting this parameter returns a mixture of both new and old.)
        """
        def set_Novelty(self, value):
            InputSet._set_input(self, 'Novelty', value)

        """
        Set the value of the OauthToken input for this choreography. ((conditional, string) The Foursquare API Oauth token string. Required unless specifying the ClientID and ClientSecret.)
        """
        def set_OauthToken(self, value):
            InputSet._set_input(self, 'OauthToken', value)

        """
        Set the value of the Query input for this choreography. ((optional, string) A search term to be applied against tips, category, etc. at a venue.)
        """
        def set_Query(self, value):
            InputSet._set_input(self, 'Query', value)

        """
        Set the value of the Radius input for this choreography. ((optional, integer) Radius to search within, in meters. If radius is not specified, a suggested radius will be used depending on the density of venues in the area.)
        """
        def set_Radius(self, value):
            InputSet._set_input(self, 'Radius', value)

        """
        Set the value of the ResponseFormat input for this choreography. ((optional, string) The format that response should be in. Can be set to xml or json. Defaults to json.)
        """
        def set_ResponseFormat(self, value):
            InputSet._set_input(self, 'ResponseFormat', value)

        """
        Set the value of the Section input for this choreography. ((optional, string) One of food, drinks, coffee, shops, arts, or outdoors. Choosing one of these limits results to venues with categories matching these terms.)
        """
        def set_Section(self, value):
            InputSet._set_input(self, 'Section', value)


"""
A ResultSet with methods tailored to the values returned by the Explore choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class ExploreResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The response from Foursquare. Corresponds to the ResponseFormat input. Defaults to JSON.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class ExploreChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ExploreResultSet(response, path)
