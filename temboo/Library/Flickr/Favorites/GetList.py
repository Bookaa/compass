# -*- coding: utf-8 -*-

###############################################################################
#
# GetList
# Returns a list of the user's favorite photos.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class GetList(Choreography):

    """
    Create a new instance of the GetList Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Flickr/Favorites/GetList')


    def new_input_set(self):
        return GetListInputSet()

    def _make_result_set(self, result, path):
        return GetListResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetListChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the GetList
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class GetListInputSet(InputSet):
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
        Set the value of the Extras input for this choreography. ((optional, string) A comma-delimited list of extra information to fetch for each returned record. See Choreo documentation for accepted values.)
        """
        def set_Extras(self, value):
            InputSet._set_input(self, 'Extras', value)

        """
        Set the value of the MaxFaveDate input for this choreography. ((optional, date) Maximum date that a photo was favorited on. The date should be in the form of a unix timestamp.)
        """
        def set_MaxFaveDate(self, value):
            InputSet._set_input(self, 'MaxFaveDate', value)

        """
        Set the value of the MinFaveDate input for this choreography. ((optional, date) Minimum date that a photo was favorited on. The date should be in the form of a unix timestamp.)
        """
        def set_MinFaveDate(self, value):
            InputSet._set_input(self, 'MinFaveDate', value)

        """
        Set the value of the Page input for this choreography. ((optional, integer) The page of results to return. Used for paging through many results.)
        """
        def set_Page(self, value):
            InputSet._set_input(self, 'Page', value)

        """
        Set the value of the PerPage input for this choreography. ((optional, integer) The number of photos to return per page. Defaults to 100.)
        """
        def set_PerPage(self, value):
            InputSet._set_input(self, 'PerPage', value)

        """
        Set the value of the UserId input for this choreography. ((required, string) The NSID of the user to fetch the favorites list for. If this argument is omitted, the favorites list for the calling user is returned.)
        """
        def set_UserId(self, value):
            InputSet._set_input(self, 'UserId', value)


"""
A ResultSet with methods tailored to the values returned by the GetList choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class GetListResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response from Flickr.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class GetListChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetListResultSet(response, path)
