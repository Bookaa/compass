# -*- coding: utf-8 -*-

###############################################################################
#
# ListAll
# Retrieves a list of all accounts.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class ListAll(Choreography):

    """
    Create a new instance of the ListAll Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/OneLogin/Accounts/ListAll')


    def new_input_set(self):
        return ListAllInputSet()

    def _make_result_set(self, result, path):
        return ListAllResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ListAllChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the ListAll
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class ListAllInputSet(InputSet):
        """
        Set the value of the APIKey input for this choreography. ((required, string) The API Key provided by OneLogin.)
        """
        def set_APIKey(self, value):
            InputSet._set_input(self, 'APIKey', value)


"""
A ResultSet with methods tailored to the values returned by the ListAll choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class ListAllResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response from OneLogin.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class ListAllChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ListAllResultSet(response, path)
