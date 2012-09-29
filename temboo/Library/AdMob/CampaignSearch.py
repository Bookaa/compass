# -*- coding: utf-8 -*-

###############################################################################
#
# CampaignSearch
# Search for ad campaigns using IDs.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class CampaignSearch(Choreography):

    """
    Create a new instance of the CampaignSearch Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/AdMob/CampaignSearch')


    def new_input_set(self):
        return CampaignSearchInputSet()

    def _make_result_set(self, result, path):
        return CampaignSearchResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CampaignSearchChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the CampaignSearch
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class CampaignSearchInputSet(InputSet):
        """
        Set the value of the CampaignID input for this choreography. ((optional, string) Search for ad campaigns using this ID.)
        """
        def set_CampaignID(self, value):
            InputSet._set_input(self, 'CampaignID', value)

        """
        Set the value of the ClientKey input for this choreography. ((required, string) The Client Key provided by AdMob.)
        """
        def set_ClientKey(self, value):
            InputSet._set_input(self, 'ClientKey', value)

        """
        Set the value of the Email input for this choreography. ((conditional, string) Your AdMob username. Required unless providing a valid Token input.)
        """
        def set_Email(self, value):
            InputSet._set_input(self, 'Email', value)

        """
        Set the value of the IncludeDeleted input for this choreography. ((optional, boolean) If set to 1, ad groups that have been deleted will be included in the search result.)
        """
        def set_IncludeDeleted(self, value):
            InputSet._set_input(self, 'IncludeDeleted', value)

        """
        Set the value of the Password input for this choreography. ((conditional, string) Your Admob password. Required unless providing a valid Token input.)
        """
        def set_Password(self, value):
            InputSet._set_input(self, 'Password', value)

        """
        Set the value of the ResponseFormat input for this choreography. ((optional, string) The format that your want the response to be in. Accepted values are: xml (the default) and json.)
        """
        def set_ResponseFormat(self, value):
            InputSet._set_input(self, 'ResponseFormat', value)

        """
        Set the value of the Token input for this choreography. ((conditional, string) If provided, the Choreo will use the token to authenticate. If the token is expired or not provided, the Choreo will relogin and retrieve a new token when Email and Password are supplied.)
        """
        def set_Token(self, value):
            InputSet._set_input(self, 'Token', value)


"""
A ResultSet with methods tailored to the values returned by the CampaignSearch choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class CampaignSearchResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The response from AdMob. Corresponds to the ResponseFormat input. Defaults to xml.)
        """
        def get_Response(self):
            return self._output.get('Response', None)
        """
        Retrieve the value for the "Token" output from this choreography execution. ((conditional, string) If provided, the Choreo will use the token to authenticate. If the token is expired or not provided, the Choreo will relogin and retrieve a new token when Email and Password are supplied.)
        """
        def get_Token(self):
            return self._output.get('Token', None)

class CampaignSearchChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return CampaignSearchResultSet(response, path)
