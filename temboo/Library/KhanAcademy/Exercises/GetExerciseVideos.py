# -*- coding: utf-8 -*-

###############################################################################
#
# GetExerciseVideos
# Retrieves all videos associated with a given exercise.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class GetExerciseVideos(Choreography):

    """
    Create a new instance of the GetExerciseVideos Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/KhanAcademy/Exercises/GetExerciseVideos')


    def new_input_set(self):
        return GetExerciseVideosInputSet()

    def _make_result_set(self, result, path):
        return GetExerciseVideosResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetExerciseVideosChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the GetExerciseVideos
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class GetExerciseVideosInputSet(InputSet):
        """
        Set the value of the ExerciseName input for this choreography. ((required, string) The name of the exercise to retrieve (e.g. logarithms_1))
        """
        def set_ExerciseName(self, value):
            InputSet._set_input(self, 'ExerciseName', value)


"""
A ResultSet with methods tailored to the values returned by the GetExerciseVideos choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class GetExerciseVideosResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((json) The response from Khan Academy.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class GetExerciseVideosChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetExerciseVideosResultSet(response, path)
