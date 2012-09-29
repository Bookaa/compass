# -*- coding: utf-8 -*-

###############################################################################
#
# DeleteEmailAddress
# Delete an email address from the spam reports list.

#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class DeleteEmailAddress(Choreography):

    """
    Create a new instance of the DeleteEmailAddress Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/SendGrid/WebAPI/SpamReports/DeleteEmailAddress')


    def new_input_set(self):
        return DeleteEmailAddressInputSet()

    def _make_result_set(self, result, path):
        return DeleteEmailAddressResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return DeleteEmailAddressChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the DeleteEmailAddress
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class DeleteEmailAddressInputSet(InputSet):
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
        Set the value of the Email input for this choreography. ((optional, string) Enter a specific email address to be deleted from the spam report list.)
        """
        def set_Email(self, value):
            InputSet._set_input(self, 'Email', value)

        """
        Set the value of the ResponseFormat input for this choreography. ((optional, string) Specify the format of the response from SendGrid: json, or xml.  Default is set to json.)
        """
        def set_ResponseFormat(self, value):
            InputSet._set_input(self, 'ResponseFormat', value)

        """
        Set the value of the VaultFile input for this choreography. ()
        """


"""
A ResultSet with methods tailored to the values returned by the DeleteEmailAddress choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class DeleteEmailAddressResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The response from SendGrid. The format corresponds to the ResponseFormat input. Default is json.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class DeleteEmailAddressChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return DeleteEmailAddressResultSet(response, path)
