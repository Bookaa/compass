# -*- coding: utf-8 -*-

###############################################################################
#
# GetContext
# Returns next and previous favorites for a photo in a user's favorites.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class GetContext(Choreography):

    """
    Create a new instance of the GetContext Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Flickr/Favorites/GetContext')


    def new_input_set(self):
        return GetContextInputSet()

    def _make_result_set(self, result, path):
        return GetContextResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetContextChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the GetContext
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class GetContextInputSet(InputSet):
        """
        Set the value of the APIKey input for this choreography. ((required, string) The API Key provided by Flickr (AKA the OAuth Consumer Key).)
        """
        def set_APIKey(self, value):
            InputSet._set_input(self, 'APIKey', value)

        """
        Set the value of the PhotoId input for this choreography. ((required, integer) The id of the photo to fetch the context for.)
        """
        def set_PhotoId(self, value):
            InputSet._set_input(self, 'PhotoId', value)

        """
        Set the value of the UserId input for this choreography. ((conditional, string) The user who counts the photo as a favorite.)
        """
        def set_UserId(self, value):
            InputSet._set_input(self, 'UserId', value)


"""
A ResultSet with methods tailored to the values returned by the GetContext choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class GetContextResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response from Flickr.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class GetContextChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetContextResultSet(response, path)
