# -*- coding: utf-8 -*-

###############################################################################
#
# EditIdentity
# Edit a newsletter identity.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class EditIdentity(Choreography):

    """
    Create a new instance of the EditIdentity Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/SendGrid/NewsletterAPI/Identity/EditIdentity')


    def new_input_set(self):
        return EditIdentityInputSet()

    def _make_result_set(self, result, path):
        return EditIdentityResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return EditIdentityChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the EditIdentity
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class EditIdentityInputSet(InputSet):
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
        Set the value of the Address input for this choreography. ((required, string) Specify a new physical address to be used for this Identity.)
        """
        def set_Address(self, value):
            InputSet._set_input(self, 'Address', value)

        """
        Set the value of the City input for this choreography. ((required, string) Enter the new city for this Identity.)
        """
        def set_City(self, value):
            InputSet._set_input(self, 'City', value)

        """
        Set the value of the Country input for this choreography. ((required, string) Enter a new country to be associated with this Identity.)
        """
        def set_Country(self, value):
            InputSet._set_input(self, 'Country', value)

        """
        Set the value of the Email input for this choreography. ((required, string) Enter an email address to be used for this identity.)
        """
        def set_Email(self, value):
            InputSet._set_input(self, 'Email', value)

        """
        Set the value of the Identity input for this choreography. ((required, string) Enter an identity that is to be edited.)
        """
        def set_Identity(self, value):
            InputSet._set_input(self, 'Identity', value)

        """
        Set the value of the Name input for this choreography. ((required, string) Enter the new name to be associated with this identity.)
        """
        def set_Name(self, value):
            InputSet._set_input(self, 'Name', value)

        """
        Set the value of the NewIdentity input for this choreography. ((optional, string) Enter a new name for this identity.)
        """
        def set_NewIdentity(self, value):
            InputSet._set_input(self, 'NewIdentity', value)

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
        Set the value of the Zip input for this choreography. ((required, integer) Enter a new zip code associated with this Identity.)
        """
        def set_Zip(self, value):
            InputSet._set_input(self, 'Zip', value)

        """
        Set the value of the VaultFile input for this choreography. ()
        """


"""
A ResultSet with methods tailored to the values returned by the EditIdentity choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class EditIdentityResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The response from SendGrid. The format corresponds to the ResponseFormat input. Default is json.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class EditIdentityChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return EditIdentityResultSet(response, path)
