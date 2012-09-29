# -*- coding: utf-8 -*-

###############################################################################
#
# GetCompanyProfileByEmailDomain
# Retrieve a company profile by email domain.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class GetCompanyProfileByEmailDomain(Choreography):

    """
    Create a new instance of the GetCompanyProfileByEmailDomain Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/LinkedIn/Companies/GetCompanyProfileByEmailDomain')


    def new_input_set(self):
        return GetCompanyProfileByEmailDomainInputSet()

    def _make_result_set(self, result, path):
        return GetCompanyProfileByEmailDomainResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetCompanyProfileByEmailDomainChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the GetCompanyProfileByEmailDomain
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class GetCompanyProfileByEmailDomainInputSet(InputSet):
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
        Set the value of the EmailDomain input for this choreography. ((required, string) An email domain used to search for a company (i.e. apple.com).)
        """
        def set_EmailDomain(self, value):
            InputSet._set_input(self, 'EmailDomain', value)

        """
        Set the value of the SecretKey input for this choreography. ((required, string) The Secret Key provided by LinkedIn (AKA the OAuth Consumer Secret).)
        """
        def set_SecretKey(self, value):
            InputSet._set_input(self, 'SecretKey', value)


"""
A ResultSet with methods tailored to the values returned by the GetCompanyProfileByEmailDomain choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class GetCompanyProfileByEmailDomainResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response from LinkedIn in XML format.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class GetCompanyProfileByEmailDomainChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetCompanyProfileByEmailDomainResultSet(response, path)
