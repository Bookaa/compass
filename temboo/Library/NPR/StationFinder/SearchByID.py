# -*- coding: utf-8 -*-

###############################################################################
#
# SearchByID
# Retrieves local NPR member stations based on their unique ID.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class SearchByID(Choreography):

    """
    Create a new instance of the SearchByID Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/NPR/StationFinder/SearchByID')


    def new_input_set(self):
        return SearchByIDInputSet()

    def _make_result_set(self, result, path):
        return SearchByIDResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return SearchByIDChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the SearchByID
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class SearchByIDInputSet(InputSet):
        """
        Set the value of the APIKey input for this choreography. ((required, string) The API Key provided by NPR.)
        """
        def set_APIKey(self, value):
            InputSet._set_input(self, 'APIKey', value)

        """
        Set the value of the ID input for this choreography. ((required, integer) The unique ID that NPR asociates with the organization.)
        """
        def set_ID(self, value):
            InputSet._set_input(self, 'ID', value)


"""
A ResultSet with methods tailored to the values returned by the SearchByID choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class SearchByIDResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) )
        """
        def get_Response(self):
            return self._output.get('Response', None)

class SearchByIDChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return SearchByIDResultSet(response, path)
