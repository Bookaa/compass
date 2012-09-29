# -*- coding: utf-8 -*-

###############################################################################
#
# Query
# Returns the records available in the DailyMed database associated with a given drug.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class Query(Choreography):

    """
    Create a new instance of the Query Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/DailyMed/Query')


    def new_input_set(self):
        return QueryInputSet()

    def _make_result_set(self, result, path):
        return QueryResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return QueryChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the Query
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class QueryInputSet(InputSet):
        """
        Set the value of the Components input for this choreography. ((optional, string) Enter the DailyMed components you want returned as a comma delimited string. When left blank, the full DailyMed record is returned. See documentation for more information on components.)
        """
        def set_Components(self, value):
            InputSet._set_input(self, 'Components', value)

        """
        Set the value of the SetID input for this choreography. ((required, string) The unique ID assigned by DailyMed to each drug. You can find the SetID of a drug by first running the SearchByName or SearchByNDC Choreos.)
        """
        def set_SetID(self, value):
            InputSet._set_input(self, 'SetID', value)


"""
A ResultSet with methods tailored to the values returned by the Query choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class QueryResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response from DailyMed.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class QueryChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return QueryResultSet(response, path)
