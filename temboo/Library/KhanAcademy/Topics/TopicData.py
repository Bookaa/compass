# -*- coding: utf-8 -*-

###############################################################################
#
# TopicData
# Retrieves topic data for a given topic, including an abbreviated list of all its sub-topics.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class TopicData(Choreography):

    """
    Create a new instance of the TopicData Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/KhanAcademy/Topics/TopicData')


    def new_input_set(self):
        return TopicDataInputSet()

    def _make_result_set(self, result, path):
        return TopicDataResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return TopicDataChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the TopicData
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class TopicDataInputSet(InputSet):
        """
        Set the value of the TopicID input for this choreography. ((required, string) The ID of the topic.)
        """
        def set_TopicID(self, value):
            InputSet._set_input(self, 'TopicID', value)


"""
A ResultSet with methods tailored to the values returned by the TopicData choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class TopicDataResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((json) The response from Khan Academy.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class TopicDataChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return TopicDataResultSet(response, path)
