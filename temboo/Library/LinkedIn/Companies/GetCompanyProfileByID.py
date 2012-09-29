# -*- coding: utf-8 -*-

###############################################################################
#
# GetCompanyProfileByID
# Retrieve a company profile by ID.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class GetCompanyProfileByID(Choreography):

    """
    Create a new instance of the GetCompanyProfileByID Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/LinkedIn/Companies/GetCompanyProfileByID')


    def new_input_set(self):
        return GetCompanyProfileByIDInputSet()

    def _make_result_set(self, result, path):
        return GetCompanyProfileByIDResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetCompanyProfileByIDChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the GetCompanyProfileByID
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class GetCompanyProfileByIDInputSet(InputSet):
        """
        Set the value of the APIKey input for this choreography. ((required, string) The API Key provided by LinkedIn (AKA the OAuth Consumer Key).)
        """
        def set_APIKey(self, value):
            InputSet._set_input(self, 'APIKey', value)

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
        Set the value of the CompanyID input for this choreography. ((required, integer) A LinkedIn assigned ID associated with the company that you want to retrieve.)
        """
        def set_CompanyID(self, value):
            InputSet._set_input(self, 'CompanyID', value)

        """
        Set the value of the SecretKey input for this choreography. ((required, string) The Secret Key provided by LinkedIn (AKA the OAuth Consumer Secret).)
        """
        def set_SecretKey(self, value):
            InputSet._set_input(self, 'SecretKey', value)


"""
A ResultSet with methods tailored to the values returned by the GetCompanyProfileByID choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class GetCompanyProfileByIDResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response from LinkedIn in XML format.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class GetCompanyProfileByIDChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetCompanyProfileByIDResultSet(response, path)
