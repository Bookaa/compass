# -*- coding: utf-8 -*-

###############################################################################
#
# QueryByID
# Retrieves information about products based on a GoodGuide product ID.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class QueryByID(Choreography):

    """
    Create a new instance of the QueryByID Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/GoodGuide/QueryByID')


    def new_input_set(self):
        return QueryByIDInputSet()

    def _make_result_set(self, result, path):
        return QueryByIDResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return QueryByIDChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the QueryByID
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class QueryByIDInputSet(InputSet):
        """
        Set the value of the APIFormat input for this choreography. ((optional, string) The response type supplied by GoodGuide. Default is simple. Other acceptable inputs are reference and badge.)
        """
        def set_APIFormat(self, value):
            InputSet._set_input(self, 'APIFormat', value)

        """
        Set the value of the APIKey input for this choreography. ((required, string) The API KEy provided by GoodGuide.)
        """
        def set_APIKey(self, value):
            InputSet._set_input(self, 'APIKey', value)

        """
        Set the value of the ID input for this choreography. ((required, string) GoodGuide ID number of product.)
        """
        def set_ID(self, value):
            InputSet._set_input(self, 'ID', value)


"""
A ResultSet with methods tailored to the values returned by the QueryByID choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class QueryByIDResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response from GoodGuide.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class QueryByIDChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return QueryByIDResultSet(response, path)
