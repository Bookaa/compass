# -*- coding: utf-8 -*-

###############################################################################
#
# Send
# Use this method to send funds to a destination user, from the user associated with the authorized access token.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class Send(Choreography):

    """
    Create a new instance of the Send Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Dwolla/Transactions/Send')


    def new_input_set(self):
        return SendInputSet()

    def _make_result_set(self, result, path):
        return SendResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return SendChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the Send
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class SendInputSet(InputSet):
        """
        Set the value of the AccessToken input for this choreography. ((required, string) A valid OAuth token.)
        """
        def set_AccessToken(self, value):
            InputSet._set_input(self, 'AccessToken', value)

        """
        Set the value of the Amount input for this choreography. ((required, decimal) Amount of funds to transfer to the destination user.)
        """
        def set_Amount(self, value):
            InputSet._set_input(self, 'Amount', value)

        """
        Set the value of the AssumeCosts input for this choreography. ((required, boolean) Set to true if the user will assume the Dwolla fee. Set to false if the destination user will assume the Dwolla fee. Does not affect facilitator fees. Defaults to false.)
        """
        def set_AssumeCosts(self, value):
            InputSet._set_input(self, 'AssumeCosts', value)

        """
        Set the value of the DestinationId input for this choreography. ((required, string) Identification of the user to send funds to. Must be the Dwolla identifier, Facebook identifier, Twitter identifier, phone number, or email address.)
        """
        def set_DestinationId(self, value):
            InputSet._set_input(self, 'DestinationId', value)

        """
        Set the value of the DestinationType input for this choreography. ((optional, string) Type of destination user. Defaults to Dwolla. Can be Dwolla, Facebook, Twitter, Email, or Phone.)
        """
        def set_DestinationType(self, value):
            InputSet._set_input(self, 'DestinationType', value)

        """
        Set the value of the FacillitatorAmount input for this choreography. ((required, string) Amount of the facilitator fee to override. Only applicable if the facilitator fee feature is enabled. If set to 0, facilitator fee is disabled for transaction. Cannot exceed 25% of the 'amount'.)
        """
        def set_FacillitatorAmount(self, value):
            InputSet._set_input(self, 'FacillitatorAmount', value)

        """
        Set the value of the FundsSource input for this choreography. ((required, string) Id of funding source to send funds from. Defaults to Balance.  Balance sourced transfers process immediately. Non-balanced sourced transfers may process immediately or take up to five business days.)
        """
        def set_FundsSource(self, value):
            InputSet._set_input(self, 'FundsSource', value)

        """
        Set the value of the Notes input for this choreography. ((required, multiline) Note to attach to the transaction. Limited to 250 characters.)
        """
        def set_Notes(self, value):
            InputSet._set_input(self, 'Notes', value)

        """
        Set the value of the Pin input for this choreography. ((required, integer) User's PIN associated with their account)
        """
        def set_Pin(self, value):
            InputSet._set_input(self, 'Pin', value)


"""
A ResultSet with methods tailored to the values returned by the Send choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class SendResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((json) The response from Dwolla.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class SendChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return SendResultSet(response, path)
