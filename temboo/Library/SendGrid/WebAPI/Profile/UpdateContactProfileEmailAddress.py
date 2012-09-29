# -*- coding: utf-8 -*-

###############################################################################
#
# UpdateContactProfileEmailAddress
# Update an account username.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class UpdateContactProfileEmailAddress(Choreography):

    """
    Create a new instance of the UpdateContactProfileEmailAddress Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/SendGrid/WebAPI/Profile/UpdateContactProfileEmailAddress')


    def new_input_set(self):
        return UpdateContactProfileEmailAddressInputSet()

    def _make_result_set(self, result, path):
        return UpdateContactProfileEmailAddressResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return UpdateContactProfileEmailAddressChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the UpdateContactProfileEmailAddress
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class UpdateContactProfileEmailAddressInputSet(InputSet):
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
        Set the value of the NewEmailAddress input for this choreography. ((required, string) Enter a valid email address, not exceeding 100 characters. This address will be used for all future communication with SendGrid. A confirmation email will be sent to validate the change of address.)
        """
        def set_NewEmailAddress(self, value):
            InputSet._set_input(self, 'NewEmailAddress', value)

        """
        Set the value of the ResponseFormat input for this choreography. ((optional, string) Specify the format of the response from SendGrid: json, or xml.  Default is set to json.)
        """
        def set_ResponseFormat(self, value):
            InputSet._set_input(self, 'ResponseFormat', value)

        """
        Set the value of the VaultFile input for this choreography. ()
        """


"""
A ResultSet with methods tailored to the values returned by the UpdateContactProfileEmailAddress choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class UpdateContactProfileEmailAddressResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The response from SendGrid. The format corresponds to the ResponseFormat input. Default is json.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class UpdateContactProfileEmailAddressChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return UpdateContactProfileEmailAddressResultSet(response, path)
