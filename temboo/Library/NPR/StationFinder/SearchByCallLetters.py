# -*- coding: utf-8 -*-

###############################################################################
#
# SearchByCallLetters
# Retrieves local NPR member stations based on uniquely identifying call letters.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class SearchByCallLetters(Choreography):

    """
    Create a new instance of the SearchByCallLetters Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/NPR/StationFinder/SearchByCallLetters')


    def new_input_set(self):
        return SearchByCallLettersInputSet()

    def _make_result_set(self, result, path):
        return SearchByCallLettersResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return SearchByCallLettersChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the SearchByCallLetters
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class SearchByCallLettersInputSet(InputSet):
        """
        Set the value of the APIKey input for this choreography. ((required, string) The API Key provided by NPR.)
        """
        def set_APIKey(self, value):
            InputSet._set_input(self, 'APIKey', value)

        """
        Set the value of the Band input for this choreography. ((optional, string) Enter AM or FM.)
        """
        def set_Band(self, value):
            InputSet._set_input(self, 'Band', value)

        """
        Set the value of the CallLetters input for this choreography. ((required, string) Enter the unique identifier associated with a station.)
        """
        def set_CallLetters(self, value):
            InputSet._set_input(self, 'CallLetters', value)


"""
A ResultSet with methods tailored to the values returned by the SearchByCallLetters choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class SearchByCallLettersResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) )
        """
        def get_Response(self):
            return self._output.get('Response', None)

class SearchByCallLettersChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return SearchByCallLettersResultSet(response, path)
