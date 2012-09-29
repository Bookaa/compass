# -*- coding: utf-8 -*-

###############################################################################
#
# SearchByCity
# Retrieves local NPR member stations based on zip code.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class SearchByCity(Choreography):

    """
    Create a new instance of the SearchByCity Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/NPR/StationFinder/SearchByCity')


    def new_input_set(self):
        return SearchByCityInputSet()

    def _make_result_set(self, result, path):
        return SearchByCityResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return SearchByCityChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the SearchByCity
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class SearchByCityInputSet(InputSet):
        """
        Set the value of the APIKey input for this choreography. ((required, string) The API Key provided by NPR.)
        """
        def set_APIKey(self, value):
            InputSet._set_input(self, 'APIKey', value)

        """
        Set the value of the City input for this choreography. ((required, string) Enter the city name. When searching by city, the state parameter must also be specified.)
        """
        def set_City(self, value):
            InputSet._set_input(self, 'City', value)

        """
        Set the value of the State input for this choreography. ((required, string) Enter the state. The city parameter must also be specified.)
        """
        def set_State(self, value):
            InputSet._set_input(self, 'State', value)


"""
A ResultSet with methods tailored to the values returned by the SearchByCity choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class SearchByCityResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) )
        """
        def get_Response(self):
            return self._output.get('Response', None)

class SearchByCityChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return SearchByCityResultSet(response, path)
