# -*- coding: utf-8 -*-

###############################################################################
#
# GetExercise
# Retrieves the specified exercise.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class GetExercise(Choreography):

    """
    Create a new instance of the GetExercise Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/KhanAcademy/Exercises/GetExercise')


    def new_input_set(self):
        return GetExerciseInputSet()

    def _make_result_set(self, result, path):
        return GetExerciseResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetExerciseChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the GetExercise
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class GetExerciseInputSet(InputSet):
        """
        Set the value of the ExerciseName input for this choreography. ((required, string) The name of the exercise to retrieve (e.g. logarithms_1))
        """
        def set_ExerciseName(self, value):
            InputSet._set_input(self, 'ExerciseName', value)


"""
A ResultSet with methods tailored to the values returned by the GetExercise choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class GetExerciseResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((json) The response from Khan Academy.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class GetExerciseChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetExerciseResultSet(response, path)
