# -*- coding: utf-8 -*-

###############################################################################
#
# PhotosForLocation
# Return a list of the user's photos for a specified location.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class PhotosForLocation(Choreography):

    """
    Create a new instance of the PhotosForLocation Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Flickr/Geo/PhotosForLocation')


    def new_input_set(self):
        return PhotosForLocationInputSet()

    def _make_result_set(self, result, path):
        return PhotosForLocationResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return PhotosForLocationChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the PhotosForLocation
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class PhotosForLocationInputSet(InputSet):
        """
        Set the value of the APIKey input for this choreography. ((required, string) The API Key provided by Flickr (AKA the OAuth Consumer Key).)
        """
        def set_APIKey(self, value):
            InputSet._set_input(self, 'APIKey', value)

        """
        Set the value of the APISecret input for this choreography. ((required, string) The API Secret provided by Flickr (AKA the OAuth Consumer Secret).)
        """
        def set_APISecret(self, value):
            InputSet._set_input(self, 'APISecret', value)

        """
        Set the value of the AccessTokenSecret input for this choreography. ((required, string) The Access Token Secret retrieved during the OAuth process.)
        """
        def set_AccessTokenSecret(self, value):
            InputSet._set_input(self, 'AccessTokenSecret', value)

        """
        Set the value of the AccessToken input for this choreography. ((required, string) The Access Token retrieved during the OAuth process.)
        """
        def set_AccessToken(self, value):
            InputSet._set_input(self, 'AccessToken', value)

        """
        Set the value of the Accuracy input for this choreography. ((optional, integer) Recorded accuracy level of the location information. Current range is 1-16. Defaults to 16 if not specified.)
        """
        def set_Accuracy(self, value):
            InputSet._set_input(self, 'Accuracy', value)

        """
        Set the value of the Extras input for this choreography. ((optional, string) A comma-delimited list of extra information to retrieve for each returned record. See Choreo documentation for accepted values.)
        """
        def set_Extras(self, value):
            InputSet._set_input(self, 'Extras', value)

        """
        Set the value of the Latitude input for this choreography. ((required, decimal) The latitude whose valid range is -90 to 90. Anything more than 6 decimal places will be truncated.)
        """
        def set_Latitude(self, value):
            InputSet._set_input(self, 'Latitude', value)

        """
        Set the value of the Longitude input for this choreography. ((required, decimal) The longitude whose valid range is -180 to 180. Anything more than 6 decimal places will be truncated.)
        """
        def set_Longitude(self, value):
            InputSet._set_input(self, 'Longitude', value)

        """
        Set the value of the Page input for this choreography. ((optional, integer) The page of results to return. Used for paging through many results. Defaults to 1.)
        """
        def set_Page(self, value):
            InputSet._set_input(self, 'Page', value)

        """
        Set the value of the PerPage input for this choreography. ((optional, integer) Number of photos to return per page. If this argument is omitted, it defaults to 100. The maximum allowed value is 500.)
        """
        def set_PerPage(self, value):
            InputSet._set_input(self, 'PerPage', value)


"""
A ResultSet with methods tailored to the values returned by the PhotosForLocation choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class PhotosForLocationResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response from Flickr.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class PhotosForLocationChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return PhotosForLocationResultSet(response, path)
