# -*- coding: utf-8 -*-

###############################################################################
#
# ListIssuesForRepo
# List all issues for a specified repository.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class ListIssuesForRepo(Choreography):

    """
    Create a new instance of the ListIssuesForRepo Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/GitHub/IssuesAPI/Issues/ListIssuesForRepo')


    def new_input_set(self):
        return ListIssuesForRepoInputSet()

    def _make_result_set(self, result, path):
        return ListIssuesForRepoResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ListIssuesForRepoChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the ListIssuesForRepo
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class ListIssuesForRepoInputSet(InputSet):
        """
        Set the value of the AccessToken input for this choreography. ((required, string) The Access Token retrieved during the OAuth process.)
        """
        def set_AccessToken(self, value):
            InputSet._set_input(self, 'AccessToken', value)

        """
        Set the value of the Assignee input for this choreography. ((required, string) Can be set to a username, "none" for issues with no assinged user, or * for issues with any assigned user.)
        """
        def set_Assignee(self, value):
            InputSet._set_input(self, 'Assignee', value)

        """
        Set the value of the Direction input for this choreography. ((optional, string) The direction of the sort order. Valid values are: asc or desc (the default).)
        """
        def set_Direction(self, value):
            InputSet._set_input(self, 'Direction', value)

        """
        Set the value of the Labels input for this choreography. ((optional, string) A comma separated list of label names (i.e. bug, ui, etc).)
        """
        def set_Labels(self, value):
            InputSet._set_input(self, 'Labels', value)

        """
        Set the value of the Mentioned input for this choreography. ((optional, string) A Github username that is mentioned.)
        """
        def set_Mentioned(self, value):
            InputSet._set_input(self, 'Mentioned', value)

        """
        Set the value of the Milestone input for this choreography. ((required, string) Can be set to a milestone number, "none" for issues with no milestone, or * for issues with any milestone.)
        """
        def set_Milestone(self, value):
            InputSet._set_input(self, 'Milestone', value)

        """
        Set the value of the Page input for this choreography. ((optional, integer) Indicates the page index that you want to retrieve. This is used to page through many results. Defaults to 1.)
        """
        def set_Page(self, value):
            InputSet._set_input(self, 'Page', value)

        """
        Set the value of the Repo input for this choreography. ((required, string) The name of the repo.)
        """
        def set_Repo(self, value):
            InputSet._set_input(self, 'Repo', value)

        """
        Set the value of the Since input for this choreography. ((optional, date) A timestamp in ISO 8601 format (YYYY-MM-DDTHH:MM:SSZ). Returns issues since this date.)
        """
        def set_Since(self, value):
            InputSet._set_input(self, 'Since', value)

        """
        Set the value of the Sort input for this choreography. ((optional, string) Indicates how the issues will be sorted in the response. Valid sort options are: created (the default), updated, comments.)
        """
        def set_Sort(self, value):
            InputSet._set_input(self, 'Sort', value)

        """
        Set the value of the State input for this choreography. ((optional, string) Returns issues with a particular state: open (the default) or closed.)
        """
        def set_State(self, value):
            InputSet._set_input(self, 'State', value)

        """
        Set the value of the User input for this choreography. ((required, string) A GitHub username.)
        """
        def set_User(self, value):
            InputSet._set_input(self, 'User', value)


"""
A ResultSet with methods tailored to the values returned by the ListIssuesForRepo choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class ListIssuesForRepoResultSet(ResultSet):
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

class ListIssuesForRepoChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ListIssuesForRepoResultSet(response, path)
