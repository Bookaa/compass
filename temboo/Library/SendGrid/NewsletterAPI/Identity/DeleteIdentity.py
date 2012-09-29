# -*- coding: utf-8 -*-

###############################################################################
#
# DeleteIdentity
# Delete an Identity.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class DeleteIdentity(Choreography):

    """
    Create a new instance of the DeleteIdentity Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/SendGrid/NewsletterAPI/Identity/DeleteIdentity')


    def new_input_set(self):
        return DeleteIdentityInputSet()

    def _make_result_set(self, result, path):
        return DeleteIdentityResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return DeleteIdentityChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the DeleteIdentity
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class DeleteIdentityInputSet(InputSet):
        """
        Set the value of the Response input for this choreography. ((required, any) The response from SendGrid. The format corresponds to the ResponseFormat input. Default is json.)
        """
        def set_Response(self, value):
            InputSet._set_input(self, 'Response', value)

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
        Set the value of the Identity input for this choreography. ((required, string) Enter an identity to be removed from your account.)
        """
        def set_Identity(self, value):
            InputSet._set_input(self, 'Identity', value)

        """
        Set the value of the ResponseFormat input for this choreography. ((optional, string) Specify the format of the response from SendGrid: json, or xml.  Default is set to json.)
        """
        def set_ResponseFormat(self, value):
            InputSet._set_input(self, 'ResponseFormat', value)

        """
        Set the value of the VaultFile input for this choreography. ()
        """


"""
A ResultSet with methods tailored to the values returned by the DeleteIdentity choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class DeleteIdentityResultSet(ResultSet):
    pass

class DeleteIdentityChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return DeleteIdentityResultSet(response, path)
