# -*- coding: utf-8 -*-

###############################################################################
#
# GetExerciseFollowUp
# Retrieves all exercises which have the specified exercise as a prerequisite.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class GetExerciseFollowUp(Choreography):

    """
    Create a new instance of the GetExerciseFollowUp Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/KhanAcademy/Exercises/GetExerciseFollowUp')


    def new_input_set(self):
        return GetExerciseFollowUpInputSet()

    def _make_result_set(self, result, path):
        return GetExerciseFollowUpResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetExerciseFollowUpChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the GetExerciseFollowUp
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class GetExerciseFollowUpInputSet(InputSet):
        """
        Set the value of the ExerciseName input for this choreography. ((required, string) The name of the exercise to retrieve (e.g. logarithms_1))
        """
        def set_ExerciseName(self, value):
            InputSet._set_input(self, 'ExerciseName', value)


"""
A ResultSet with methods tailored to the values returned by the GetExerciseFollowUp choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class GetExerciseFollowUpResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((json) The response from Khan Academy.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class GetExerciseFollowUpChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetExerciseFollowUpResultSet(response, path)
