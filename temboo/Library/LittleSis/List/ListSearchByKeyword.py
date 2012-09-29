# -*- coding: utf-8 -*-

###############################################################################
#
# ListSearchByKeyword
# Retrieves the name and description fields of Lists available in LittleSis that match a keyword search.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class ListSearchByKeyword(Choreography):

    """
    Create a new instance of the ListSearchByKeyword Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/LittleSis/List/ListSearchByKeyword')


    def new_input_set(self):
        return ListSearchByKeywordInputSet()

    def _make_result_set(self, result, path):
        return ListSearchByKeywordResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ListSearchByKeywordChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the ListSearchByKeyword
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class ListSearchByKeywordInputSet(InputSet):
        """
        Set the value of the APIKey input for this choreography. ((required, string) The API Key obtained from LittleSis.org.)
        """
        def set_APIKey(self, value):
            InputSet._set_input(self, 'APIKey', value)

        """
        Set the value of the Keywords input for this choreography. ((required, string) Enter search text.)
        """
        def set_Keywords(self, value):
            InputSet._set_input(self, 'Keywords', value)

        """
        Set the value of the ResponseFormat input for this choreography. ((optional, string) Format of the response returned by LittleSis.org. Acceptable inputs: xml or json. Defaults to xml)
        """
        def set_ResponseFormat(self, value):
            InputSet._set_input(self, 'ResponseFormat', value)


"""
A ResultSet with methods tailored to the values returned by the ListSearchByKeyword choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class ListSearchByKeywordResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The response from LittleSis.org.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class ListSearchByKeywordChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ListSearchByKeywordResultSet(response, path)
