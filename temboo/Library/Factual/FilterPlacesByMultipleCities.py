# -*- coding: utf-8 -*-

###############################################################################
#
# FilterPlacesByMultipleCities
# Restrict a query to a specified city.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class FilterPlacesByMultipleCities(Choreography):

    """
    Create a new instance of the FilterPlacesByMultipleCities Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Factual/FilterPlacesByMultipleCities')


    def new_input_set(self):
        return FilterPlacesByMultipleCitiesInputSet()

    def _make_result_set(self, result, path):
        return FilterPlacesByMultipleCitiesResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return FilterPlacesByMultipleCitiesChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the FilterPlacesByMultipleCities
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class FilterPlacesByMultipleCitiesInputSet(InputSet):
        """
        Set the value of the APIKey input for this choreography. ((required, string) The API Key provided by Factual (AKA the OAuth Consumer Key).)
        """
        def set_APIKey(self, value):
            InputSet._set_input(self, 'APIKey', value)

        """
        Set the value of the APISecret input for this choreography. ((required, string) The API Secret provided by Factual (AKA the OAuth Consumer Secret).)
        """
        def set_APISecret(self, value):
            InputSet._set_input(self, 'APISecret', value)

        """
        Set the value of the Cities input for this choreography. ((required, string) Enter a list of cities to filter results. Use the following comma-separated format: "New York", "Ithaca", "Albany")
        """
        def set_Cities(self, value):
            InputSet._set_input(self, 'Cities', value)

        """
        Set the value of the Query input for this choreography. ((optional, string) A search string (i.e. Starbucks).)
        """
        def set_Query(self, value):
            InputSet._set_input(self, 'Query', value)


"""
A ResultSet with methods tailored to the values returned by the FilterPlacesByMultipleCities choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class FilterPlacesByMultipleCitiesResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((json) The response from Factual.)
        """
        def get_Response(self):
            return self._output.get('Response', None)
        """
        Retrieve the value for the "JSON" output from this choreography execution. ()
        """
        def get_JSON(self):
            return self._output.get('JSON', None)

class FilterPlacesByMultipleCitiesChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return FilterPlacesByMultipleCitiesResultSet(response, path)
