# -*- coding: utf-8 -*-

###############################################################################
#
# SearchLocations
# Searches for locations by geographic coordinates. 
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class SearchLocations(Choreography):

    """
    Create a new instance of the SearchLocations Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Instagram/SearchLocations')


    def new_input_set(self):
        return SearchLocationsInputSet()

    def _make_result_set(self, result, path):
        return SearchLocationsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return SearchLocationsChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the SearchLocations
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class SearchLocationsInputSet(InputSet):
        """
        Set the value of the AccessToken input for this choreography. ((conditional, string) The access token retrieved during the Oauth 2.0 process. Required unless you provide the ClientID.)
        """
        def set_AccessToken(self, value):
            InputSet._set_input(self, 'AccessToken', value)

        """
        Set the value of the ClientID input for this choreography. ((conditional, string) The Client ID provided by Instagram after registering your application. Required unless you provide the AccessToken.)
        """
        def set_ClientID(self, value):
            InputSet._set_input(self, 'ClientID', value)

        """
        Set the value of the Distance input for this choreography. ((optional, integer) The distance to search. Default is 1000m (distance=1000), max distance is 5000.)
        """
        def set_Distance(self, value):
            InputSet._set_input(self, 'Distance', value)

        """
        Set the value of the FoursquareID input for this choreography. ((conditional, string) Returns a location mapped off of a foursquare v2 api location id. If used, you are not required to provide values for Latitude or Longitude.)
        """
        def set_FoursquareID(self, value):
            InputSet._set_input(self, 'FoursquareID', value)

        """
        Set the value of the Latitude input for this choreography. ((conditional, decimal) Latitude of the center search coordinate. If used, Longitude is required.)
        """
        def set_Latitude(self, value):
            InputSet._set_input(self, 'Latitude', value)

        """
        Set the value of the Longitude input for this choreography. ((conditional, decimal) Longitude of the center search coordinate. If used, Latitude is required.)
        """
        def set_Longitude(self, value):
            InputSet._set_input(self, 'Longitude', value)


"""
A ResultSet with methods tailored to the values returned by the SearchLocations choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class SearchLocationsResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((json) The response from Instagram.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class SearchLocationsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return SearchLocationsResultSet(response, path)
