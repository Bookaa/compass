# -*- coding: utf-8 -*-

###############################################################################
#
# GetTopicExercises
# Retrieves a list of all exercises for a given topic.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class GetTopicExercises(Choreography):

    """
    Create a new instance of the GetTopicExercises Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/KhanAcademy/Topics/GetTopicExercises')


    def new_input_set(self):
        return GetTopicExercisesInputSet()

    def _make_result_set(self, result, path):
        return GetTopicExercisesResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetTopicExercisesChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the GetTopicExercises
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class GetTopicExercisesInputSet(InputSet):
        """
        Set the value of the TopicID input for this choreography. ((required, string) The ID of the topic.)
        """
        def set_TopicID(self, value):
            InputSet._set_input(self, 'TopicID', value)


"""
A ResultSet with methods tailored to the values returned by the GetTopicExercises choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class GetTopicExercisesResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((json) The response from Khan Academy.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class GetTopicExercisesChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetTopicExercisesResultSet(response, path)
