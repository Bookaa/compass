# -*- coding: utf-8 -*-

###############################################################################
#
# FundingSourcesByID
# Retrieves the account information for the user associated with the given authorized access token.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class FundingSourcesByID(Choreography):

    """
    Create a new instance of the FundingSourcesByID Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Dwolla/FundingSources/FundingSourcesByID')


    def new_input_set(self):
        return FundingSourcesByIDInputSet()

    def _make_result_set(self, result, path):
        return FundingSourcesByIDResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return FundingSourcesByIDChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the FundingSourcesByID
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class FundingSourcesByIDInputSet(InputSet):
        """
        Set the value of the AccessToken input for this choreography. ((required, string) A valid OAuth token.)
        """
        def set_AccessToken(self, value):
            InputSet._set_input(self, 'AccessToken', value)

        """
        Set the value of the FundingID input for this choreography. ((required, string) Funding source identifier of the funding source being requested.)
        """
        def set_FundingID(self, value):
            InputSet._set_input(self, 'FundingID', value)


"""
A ResultSet with methods tailored to the values returned by the FundingSourcesByID choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class FundingSourcesByIDResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((json) The response from Dwolla.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class FundingSourcesByIDChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return FundingSourcesByIDResultSet(response, path)
