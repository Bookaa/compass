# -*- coding: utf-8 -*-

###############################################################################
#
# ByID
# Retrieves the account information about the specified transaction by Transaction ID.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class ByID(Choreography):

    """
    Create a new instance of the ByID Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Dwolla/Transactions/ByID')


    def new_input_set(self):
        return ByIDInputSet()

    def _make_result_set(self, result, path):
        return ByIDResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ByIDChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the ByID
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class ByIDInputSet(InputSet):
        """
        Set the value of the AccessToken input for this choreography. ((required, string) A valid OAuth token.)
        """
        def set_AccessToken(self, value):
            InputSet._set_input(self, 'AccessToken', value)

        """
        Set the value of the TransactionID input for this choreography. ((required, integer) Transaction identifier of the transaction being requested.)
        """
        def set_TransactionID(self, value):
            InputSet._set_input(self, 'TransactionID', value)


"""
A ResultSet with methods tailored to the values returned by the ByID choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class ByIDResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((json) The response from Dwolla.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class ByIDChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ByIDResultSet(response, path)
