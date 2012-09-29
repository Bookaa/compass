# -*- coding: utf-8 -*-

###############################################################################
#
# SearchByNDC
# Returns a list of drugs in the DailyMed database associated with a given National Drug Code (NDC).
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class SearchByNDC(Choreography):

    """
    Create a new instance of the SearchByNDC Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/DailyMed/SearchByNDC')


    def new_input_set(self):
        return SearchByNDCInputSet()

    def _make_result_set(self, result, path):
        return SearchByNDCResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return SearchByNDCChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the SearchByNDC
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class SearchByNDCInputSet(InputSet):
        """
        Set the value of the NDC input for this choreography. ((required, string) National Drug Code. This is a unique 10-digit numeric identifier assigned to each medication by the Food and Drug Administration (FDA).)
        """
        def set_NDC(self, value):
            InputSet._set_input(self, 'NDC', value)

        """
        Set the value of the OutputFormat input for this choreography. ((optional, string) Defaults to XML format when nothing is specified. Acceptable values: xml or json.)
        """
        def set_OutputFormat(self, value):
            InputSet._set_input(self, 'OutputFormat', value)


"""
A ResultSet with methods tailored to the values returned by the SearchByNDC choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class SearchByNDCResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The response from DailyMed.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class SearchByNDCChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return SearchByNDCResultSet(response, path)
