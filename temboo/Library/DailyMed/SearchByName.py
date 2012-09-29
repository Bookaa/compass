# -*- coding: utf-8 -*-

###############################################################################
#
# SearchByName
# Returns a list of drugs in the DailyMed database associated with a given drug name.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class SearchByName(Choreography):

    """
    Create a new instance of the SearchByName Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/DailyMed/SearchByName')


    def new_input_set(self):
        return SearchByNameInputSet()

    def _make_result_set(self, result, path):
        return SearchByNameResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return SearchByNameChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the SearchByName
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class SearchByNameInputSet(InputSet):
        """
        Set the value of the DrugName input for this choreography. ((required, string) The name of the drug you want to find.)
        """
        def set_DrugName(self, value):
            InputSet._set_input(self, 'DrugName', value)

        """
        Set the value of the LabelType input for this choreography. ((optional, string) Filter results by a specified type. Acceptable values: rxonly, otc, human, human/rxonly, human/otc, animal. See documentation for more information.)
        """
        def set_LabelType(self, value):
            InputSet._set_input(self, 'LabelType', value)

        """
        Set the value of the OutputFormat input for this choreography. ((optional, string) Defaults to XML format when nothing is specified. Acceptable values: xml or json.)
        """
        def set_OutputFormat(self, value):
            InputSet._set_input(self, 'OutputFormat', value)


"""
A ResultSet with methods tailored to the values returned by the SearchByName choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class SearchByNameResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The response from DailyMed.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class SearchByNameChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return SearchByNameResultSet(response, path)
