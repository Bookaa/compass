# -*- coding: utf-8 -*-

###############################################################################
#
# Listing
# Retrieves a list of transactions for the user associated with the authorized access token.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class Listing(Choreography):

    """
    Create a new instance of the Listing Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Dwolla/Transactions/Listing')


    def new_input_set(self):
        return ListingInputSet()

    def _make_result_set(self, result, path):
        return ListingResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ListingChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the Listing
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class ListingInputSet(InputSet):
        """
        Set the value of the AccessToken input for this choreography. ((required, string) A valid OAuth token.)
        """
        def set_AccessToken(self, value):
            InputSet._set_input(self, 'AccessToken', value)

        """
        Set the value of the Limit input for this choreography. ((optional, integer) Number of transactions to retrieve. Defaults to 10. Can be between 1 and 200 transactions.)
        """
        def set_Limit(self, value):
            InputSet._set_input(self, 'Limit', value)

        """
        Set the value of the SinceDate input for this choreography. ((optional, string) Earliest date and time for which to retrieve transactions. Defaults to 7 days prior to current date and time in UTC.)
        """
        def set_SinceDate(self, value):
            InputSet._set_input(self, 'SinceDate', value)

        """
        Set the value of the Skip input for this choreography. ((optional, integer) Number of transactions to skip. Defaults to 0.)
        """
        def set_Skip(self, value):
            InputSet._set_input(self, 'Skip', value)

        """
        Set the value of the Types input for this choreography. ((optional, string) Transaction types to retrieve. Must be delimited by a '|'. Options are money_sent, money_received, deposit, withdrawal, and fee. Defaults to include all transaction types.)
        """
        def set_Types(self, value):
            InputSet._set_input(self, 'Types', value)


"""
A ResultSet with methods tailored to the values returned by the Listing choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class ListingResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((json) The response from Dwolla.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class ListingChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ListingResultSet(response, path)
