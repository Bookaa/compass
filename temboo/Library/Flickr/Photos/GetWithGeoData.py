# -*- coding: utf-8 -*-

###############################################################################
#
# GetWithGeoData
# Returns a list of your geo-tagged photos.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class GetWithGeoData(Choreography):

    """
    Create a new instance of the GetWithGeoData Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Flickr/Photos/GetWithGeoData')


    def new_input_set(self):
        return GetWithGeoDataInputSet()

    def _make_result_set(self, result, path):
        return GetWithGeoDataResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetWithGeoDataChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the GetWithGeoData
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class GetWithGeoDataInputSet(InputSet):
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
        Set the value of the Extras input for this choreography. ((optional, string) A comma-delimited list of extra information to retrieve for each returned record. See Choreo documentation for accepted values.)
        """
        def set_Extras(self, value):
            InputSet._set_input(self, 'Extras', value)

        """
        Set the value of the MaxTakenDate input for this choreography. ((optional, date) Photos with an taken date less than or equal to this value will be returned. The date should be in the form of a mysql datetime.)
        """
        def set_MaxTakenDate(self, value):
            InputSet._set_input(self, 'MaxTakenDate', value)

        """
        Set the value of the MaxUploadDate input for this choreography. ((optional, date) Photos with an upload date less than or equal to this value will be returned. The date should be in the form of a unix timestamp.)
        """
        def set_MaxUploadDate(self, value):
            InputSet._set_input(self, 'MaxUploadDate', value)

        """
        Set the value of the Media input for this choreography. ((optional, string) Filter results by media type. Possible values are all (default), photos or videos.)
        """
        def set_Media(self, value):
            InputSet._set_input(self, 'Media', value)

        """
        Set the value of the MinTakenDate input for this choreography. ((optional, date) Photos with an taken date greater than or equal to this value will be returned. The date should be in the form of a mysql datetime.)
        """
        def set_MinTakenDate(self, value):
            InputSet._set_input(self, 'MinTakenDate', value)

        """
        Set the value of the MinUploadDate input for this choreography. ((optional, date) Photos with an upload date greater than or equal to this value will be returned. The date should be in the form of a unix timestamp.)
        """
        def set_MinUploadDate(self, value):
            InputSet._set_input(self, 'MinUploadDate', value)

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
        Set the value of the PrivacyFilter input for this choreography. ((optional, integer) Valid values are: 1 (public photos), 2 (private photos visible to friends), 3 (private photos visible to family), 4 (private photos visible to friends and family), 5 (completely private photos).)
        """
        def set_PrivacyFilter(self, value):
            InputSet._set_input(self, 'PrivacyFilter', value)

        """
        Set the value of the Sort input for this choreography. ((optional, any) The sort order. Deafults to date-posted-desc. Accepted values are: date-posted-asc, date-posted-desc, date-taken-asc, date-taken-desc, interestingness-desc, and interestingness-asc.)
        """
        def set_Sort(self, value):
            InputSet._set_input(self, 'Sort', value)


"""
A ResultSet with methods tailored to the values returned by the GetWithGeoData choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class GetWithGeoDataResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response from Flickr.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class GetWithGeoDataChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetWithGeoDataResultSet(response, path)
