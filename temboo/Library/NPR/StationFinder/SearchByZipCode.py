# -*- coding: utf-8 -*-

###############################################################################
#
# SearchByZipCode
# Retrieves local NPR member stations based on zip code.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class SearchByZipCode(Choreography):

    """
    Create a new instance of the SearchByZipCode Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/NPR/StationFinder/SearchByZipCode')


    def new_input_set(self):
        return SearchByZipCodeInputSet()

    def _make_result_set(self, result, path):
        return SearchByZipCodeResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return SearchByZipCodeChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the SearchByZipCode
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class SearchByZipCodeInputSet(InputSet):
        """
        Set the value of the APIKey input for this choreography. ((required, string) The API Key provided by NPR.)
        """
        def set_APIKey(self, value):
            InputSet._set_input(self, 'APIKey', value)

        """
        Set the value of the Zip input for this choreography. ((required, string) Enter a five-digit zip code.)
        """
        def set_Zip(self, value):
            InputSet._set_input(self, 'Zip', value)


"""
A ResultSet with methods tailored to the values returned by the SearchByZipCode choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class SearchByZipCodeResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) )
        """
        def get_Response(self):
            return self._output.get('Response', None)

class SearchByZipCodeChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return SearchByZipCodeResultSet(response, path)
