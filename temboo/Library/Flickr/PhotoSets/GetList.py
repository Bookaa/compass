# -*- coding: utf-8 -*-

###############################################################################
#
# GetList
# Returns the photosets belonging to the specified user.
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
        Choreography.__init__(self, temboo_session, '/Library/Flickr/PhotoSets/GetList')


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
        Set the value of the Page input for this choreography. ((optional, integer) The page of results to get. Currently, if this is not provided, all sets are returned, but this behaviour may change in future.)
        """
        def set_Page(self, value):
            InputSet._set_input(self, 'Page', value)

        """
        Set the value of the PerPage input for this choreography. ((optional, integer) The number of sets to get per page. If paging is enabled, the maximum number of sets per page is 500.)
        """
        def set_PerPage(self, value):
            InputSet._set_input(self, 'PerPage', value)


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
