# -*- coding: utf-8 -*-

###############################################################################
#
# Stats
# Retrieves the account information for the user associated with the given authorized access token.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class Stats(Choreography):

    """
    Create a new instance of the Stats Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Dwolla/Transactions/Stats')


    def new_input_set(self):
        return StatsInputSet()

    def _make_result_set(self, result, path):
        return StatsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return StatsChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the Stats
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class StatsInputSet(InputSet):
        """
        Set the value of the AccessToken input for this choreography. ((required, string) A valid OAuth token.)
        """
        def set_AccessToken(self, value):
            InputSet._set_input(self, 'AccessToken', value)

        """
        Set the value of the EndDate input for this choreography. ((optional, string) Ending date and time to for which to process transactions stats. Defaults to current date and time in UTC.)
        """
        def set_EndDate(self, value):
            InputSet._set_input(self, 'EndDate', value)

        """
        Set the value of the StartDate input for this choreography. ((optional, string) Starting date and time to for which to process transactions stats. Defaults to 0300 of the current day in UTC.)
        """
        def set_StartDate(self, value):
            InputSet._set_input(self, 'StartDate', value)

        """
        Set the value of the Types input for this choreography. ((optional, string) Types of status to retrieve. Must be comma delimited. Options are TransactionsCount and TransactionsTotal. Defaults to include all stats.)
        """
        def set_Types(self, value):
            InputSet._set_input(self, 'Types', value)


"""
A ResultSet with methods tailored to the values returned by the Stats choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class StatsResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((json) The response from Dwolla.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class StatsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return StatsResultSet(response, path)
