# -*- coding: utf-8 -*-

###############################################################################
#
# AddressVerify
# Confirms whether a postal address and postal code match those of the specified PayPal account holder.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class AddressVerify(Choreography):

    """
    Create a new instance of the AddressVerify Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/PayPal/AddressVerify')


    def new_input_set(self):
        return AddressVerifyInputSet()

    def _make_result_set(self, result, path):
        return AddressVerifyResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return AddressVerifyChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the AddressVerify
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class AddressVerifyInputSet(InputSet):
        """
        Set the value of the Email input for this choreography. ((required, string) The email address of a PayPal member to verify.)
        """
        def set_Email(self, value):
            InputSet._set_input(self, 'Email', value)

        """
        Set the value of the Endpoint input for this choreography. ((optional, string) Set to api-3t.paypal.com when running in production. Defaults to api-3t.sandbox.paypal.com for sandbox testing.)
        """
        def set_Endpoint(self, value):
            InputSet._set_input(self, 'Endpoint', value)

        """
        Set the value of the Password input for this choreography. ((required, string) The API Password provided by PayPal.)
        """
        def set_Password(self, value):
            InputSet._set_input(self, 'Password', value)

        """
        Set the value of the PostalCode input for this choreography. ((required, string) The postal code to verify.)
        """
        def set_PostalCode(self, value):
            InputSet._set_input(self, 'PostalCode', value)

        """
        Set the value of the Signature input for this choreography. ((required, string) The API Signature provided by PayPal.)
        """
        def set_Signature(self, value):
            InputSet._set_input(self, 'Signature', value)

        """
        Set the value of the Street input for this choreography. ((required, string) The first line of the billing or shipping address to verify.)
        """
        def set_Street(self, value):
            InputSet._set_input(self, 'Street', value)

        """
        Set the value of the User input for this choreography. ((required, string) The API Username provided by PayPal.)
        """
        def set_User(self, value):
            InputSet._set_input(self, 'User', value)


"""
A ResultSet with methods tailored to the values returned by the AddressVerify choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class AddressVerifyResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((string) Response from PayPal formatted in name/value pairs.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class AddressVerifyChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return AddressVerifyResultSet(response, path)
