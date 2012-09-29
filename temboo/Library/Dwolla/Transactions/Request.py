# -*- coding: utf-8 -*-

###############################################################################
#
# Request
# Use this method to request funds from a source user, originating from the user associated with the authorized access token.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class Request(Choreography):

    """
    Create a new instance of the Request Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Dwolla/Transactions/Request')


    def new_input_set(self):
        return RequestInputSet()

    def _make_result_set(self, result, path):
        return RequestResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return RequestChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the Request
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class RequestInputSet(InputSet):
        """
        Set the value of the AccessToken input for this choreography. ((required, string) A valid OAuth token.)
        """
        def set_AccessToken(self, value):
            InputSet._set_input(self, 'AccessToken', value)

        """
        Set the value of the Amount input for this choreography. ((required, decimal) Amount of funds to request from the source user.)
        """
        def set_Amount(self, value):
            InputSet._set_input(self, 'Amount', value)

        """
        Set the value of the FacillitatorAmount input for this choreography. ((optional, decimal) Amount of the facilitator fee to override. Only applicable if the facilitator fee feature is enabled. If set to 0, facilitator fee is disabled for transaction. Cannot exceed 25% of the 'amount'.)
        """
        def set_FacillitatorAmount(self, value):
            InputSet._set_input(self, 'FacillitatorAmount', value)

        """
        Set the value of the Notes input for this choreography. ((optional, multiline) Note to attach to the transaction. Limited to 250 characters.)
        """
        def set_Notes(self, value):
            InputSet._set_input(self, 'Notes', value)

        """
        Set the value of the Pin input for this choreography. ((required, integer) User's PIN associated with their account.)
        """
        def set_Pin(self, value):
            InputSet._set_input(self, 'Pin', value)

        """
        Set the value of the SourceID input for this choreography. ((required, string) Identification of the user to request funds from. Must be the Dwolla identifier, Facebook identifier, Twitter screename, phone number, or email address.)
        """
        def set_SourceID(self, value):
            InputSet._set_input(self, 'SourceID', value)

        """
        Set the value of the SourceType input for this choreography. ((optional, string) Type of destination user. Defaults to Dwolla. Can be Dwolla, Facebook, Twitter, Email, or Phone.)
        """
        def set_SourceType(self, value):
            InputSet._set_input(self, 'SourceType', value)


"""
A ResultSet with methods tailored to the values returned by the Request choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class RequestResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((json) The response from Dwolla.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class RequestChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return RequestResultSet(response, path)
