# -*- coding: utf-8 -*-

###############################################################################
#
# CreateIdentity
# Create a new identity.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class CreateIdentity(Choreography):

    """
    Create a new instance of the CreateIdentity Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/SendGrid/NewsletterAPI/Identity/CreateIdentity')


    def new_input_set(self):
        return CreateIdentityInputSet()

    def _make_result_set(self, result, path):
        return CreateIdentityResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CreateIdentityChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the CreateIdentity
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class CreateIdentityInputSet(InputSet):
        """
        Set the value of the APIKey input for this choreography. ((required, string) Enter a SendGrid API Key.)
        """
        def set_APIKey(self, value):
            InputSet._set_input(self, 'APIKey', value)

        """
        Set the value of the APIUser input for this choreography. ((required, string) Enter a SendGrid username.)
        """
        def set_APIUser(self, value):
            InputSet._set_input(self, 'APIUser', value)

        """
        Set the value of the Address input for this choreography. ((required, string) Specify the physical address to be used for this Identity.)
        """
        def set_Address(self, value):
            InputSet._set_input(self, 'Address', value)

        """
        Set the value of the City input for this choreography. ((required, string) Enter the city for this Identity.)
        """
        def set_City(self, value):
            InputSet._set_input(self, 'City', value)

        """
        Set the value of the Country input for this choreography. ((required, string) Enter a country to be associated with this Identity.)
        """
        def set_Country(self, value):
            InputSet._set_input(self, 'Country', value)

        """
        Set the value of the Email input for this choreography. ((required, string) Enter an email address to be used for this identity.)
        """
        def set_Email(self, value):
            InputSet._set_input(self, 'Email', value)

        """
        Set the value of the Identity input for this choreography. ((required, string) Enter a name for this identity.)
        """
        def set_Identity(self, value):
            InputSet._set_input(self, 'Identity', value)

        """
        Set the value of the Name input for this choreography. ((required, string) Enter the name to be associated with this identity.)
        """
        def set_Name(self, value):
            InputSet._set_input(self, 'Name', value)

        """
        Set the value of the ReplyTo input for this choreography. ((required, string) Enter an email address to be used in the Reply-To field.)
        """
        def set_ReplyTo(self, value):
            InputSet._set_input(self, 'ReplyTo', value)

        """
        Set the value of the ResponseFormat input for this choreography. ((optional, string) Specify the format of the response from SendGrid: json, or xml.  Default is set to json.)
        """
        def set_ResponseFormat(self, value):
            InputSet._set_input(self, 'ResponseFormat', value)

        """
        Set the value of the State input for this choreography. ((required, string) Enter the state to be associated with this Identity.)
        """
        def set_State(self, value):
            InputSet._set_input(self, 'State', value)

        """
        Set the value of the Zip input for this choreography. ((required, integer) Enter the zip code associated with this Identity.)
        """
        def set_Zip(self, value):
            InputSet._set_input(self, 'Zip', value)

        """
        Set the value of the VaultFile input for this choreography. ()
        """


"""
A ResultSet with methods tailored to the values returned by the CreateIdentity choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class CreateIdentityResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The response from SendGrid. The format corresponds to the ResponseFormat input. Default is json.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class CreateIdentityChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return CreateIdentityResultSet(response, path)
