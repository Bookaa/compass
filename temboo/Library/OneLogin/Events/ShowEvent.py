# -*- coding: utf-8 -*-

###############################################################################
#
# ShowEvent
# Retrieves information for a single event.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class ShowEvent(Choreography):

    """
    Create a new instance of the ShowEvent Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/OneLogin/Events/ShowEvent')


    def new_input_set(self):
        return ShowEventInputSet()

    def _make_result_set(self, result, path):
        return ShowEventResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ShowEventChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the ShowEvent
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class ShowEventInputSet(InputSet):
        """
        Set the value of the APIKey input for this choreography. ((required, string) The API Key provided by OneLogin.)
        """
        def set_APIKey(self, value):
            InputSet._set_input(self, 'APIKey', value)

        """
        Set the value of the ID input for this choreography. ((required, integer) The id the event you want to return.)
        """
        def set_ID(self, value):
            InputSet._set_input(self, 'ID', value)


"""
A ResultSet with methods tailored to the values returned by the ShowEvent choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class ShowEventResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response from OneLogin.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class ShowEventChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ShowEventResultSet(response, path)
