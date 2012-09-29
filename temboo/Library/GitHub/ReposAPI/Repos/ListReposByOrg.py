# -*- coding: utf-8 -*-

###############################################################################
#
# ListReposByOrg
# Retrieces a list of repositories for the specified organization.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class ListReposByOrg(Choreography):

    """
    Create a new instance of the ListReposByOrg Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/GitHub/ReposAPI/Repos/ListReposByOrg')


    def new_input_set(self):
        return ListReposByOrgInputSet()

    def _make_result_set(self, result, path):
        return ListReposByOrgResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ListReposByOrgChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the ListReposByOrg
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class ListReposByOrgInputSet(InputSet):
        """
        Set the value of the AccessToken input for this choreography. ((conditional, string) The Access Token retrieved during the OAuth process. Required when accessing a protected resource.)
        """
        def set_AccessToken(self, value):
            InputSet._set_input(self, 'AccessToken', value)

        """
        Set the value of the Org input for this choreography. ((required, string) The name of the organization.)
        """
        def set_Org(self, value):
            InputSet._set_input(self, 'Org', value)

        """
        Set the value of the Page input for this choreography. ((optional, integer) Indicates the page index that you want to retrieve. This is used to page through many results. Defaults to 1.)
        """
        def set_Page(self, value):
            InputSet._set_input(self, 'Page', value)

        """
        Set the value of the Type input for this choreography. ((optional, string) The type of repos to return. Valid values are: all (the default), public, member, or private.)
        """
        def set_Type(self, value):
            InputSet._set_input(self, 'Type', value)


"""
A ResultSet with methods tailored to the values returned by the ListReposByOrg choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class ListReposByOrgResultSet(ResultSet):
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

class ListReposByOrgChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ListReposByOrgResultSet(response, path)
