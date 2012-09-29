# -*- coding: utf-8 -*-

###############################################################################
#
# ListStarredGists
# Returns a list of starred gists for the authenticated user.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class ListStarredGists(Choreography):

    """
    Create a new instance of the ListStarredGists Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/GitHub/GistsAPI/Gists/ListStarredGists')


    def new_input_set(self):
        return ListStarredGistsInputSet()

    def _make_result_set(self, result, path):
        return ListStarredGistsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ListStarredGistsChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the ListStarredGists
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class ListStarredGistsInputSet(InputSet):
        """
        Set the value of the AccessToken input for this choreography. ((required, string) The Access Token retrieved during the OAuth process.)
        """
        def set_AccessToken(self, value):
            InputSet._set_input(self, 'AccessToken', value)

        """
        Set the value of the Page input for this choreography. ((optional, integer) Indicates the page index that you want to retrieve. This is used to page through many results. Defaults to 1.)
        """
        def set_Page(self, value):
            InputSet._set_input(self, 'Page', value)


"""
A ResultSet with methods tailored to the values returned by the ListStarredGists choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class ListStarredGistsResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((json) The response from GitHub.)
        """
        def get_Response(self):
            return self._output.get('Response', None)
        """
        Retrieve the value for the "LastPage" output from this choreography execution. ((integer) If multiple pages are available for the response, this contains the last available page.)
        """
        def get_LastPage(self):
            return self._output.get('LastPage', None)
        """
        Retrieve the value for the "Limit" output from this choreography execution. ((integer) The available rate limit for your account. This is returned in the GitHub response header.)
        """
        def get_Limit(self):
            return self._output.get('Limit', None)
        """
        Retrieve the value for the "NextPage" output from this choreography execution. ((integer) If multiple pages are available for the response, this contains the next page that you should retrieve.)
        """
        def get_NextPage(self):
            return self._output.get('NextPage', None)
        """
        Retrieve the value for the "Remaining" output from this choreography execution. ((integer) The remaining number of API requests available to you. This is returned in the GitHub response header.)
        """
        def get_Remaining(self):
            return self._output.get('Remaining', None)

class ListStarredGistsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ListStarredGistsResultSet(response, path)
