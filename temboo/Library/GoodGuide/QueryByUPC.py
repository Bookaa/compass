# -*- coding: utf-8 -*-

###############################################################################
#
# QueryByUPC
# Retrieves information about products based on the product's UPC code.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class QueryByUPC(Choreography):

    """
    Create a new instance of the QueryByUPC Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/GoodGuide/QueryByUPC')


    def new_input_set(self):
        return QueryByUPCInputSet()

    def _make_result_set(self, result, path):
        return QueryByUPCResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return QueryByUPCChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the QueryByUPC
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class QueryByUPCInputSet(InputSet):
        """
        Set the value of the APIFormat input for this choreography. ((optional, string) The response type supplied by GoodGuides. Default is simple. Other acceptable inputs are reference and badge.)
        """
        def set_APIFormat(self, value):
            InputSet._set_input(self, 'APIFormat', value)

        """
        Set the value of the APIKey input for this choreography. ((required, string) The API KEy provided by GoodGuide.)
        """
        def set_APIKey(self, value):
            InputSet._set_input(self, 'APIKey', value)

        """
        Set the value of the UPC input for this choreography. ((required, string) The UPC number of the product. This consists of 12 numerical barcode digits uniquely assigned to most products sold in North America.)
        """
        def set_UPC(self, value):
            InputSet._set_input(self, 'UPC', value)


"""
A ResultSet with methods tailored to the values returned by the QueryByUPC choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class QueryByUPCResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response from GoodGuide.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class QueryByUPCChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return QueryByUPCResultSet(response, path)
