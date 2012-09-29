# -*- coding: utf-8 -*-

###############################################################################
#
# GetVideoExercises
# Retrieves all the exercises associated with a given video.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class GetVideoExercises(Choreography):

    """
    Create a new instance of the GetVideoExercises Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/KhanAcademy/Videos/GetVideoExercises')


    def new_input_set(self):
        return GetVideoExercisesInputSet()

    def _make_result_set(self, result, path):
        return GetVideoExercisesResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetVideoExercisesChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the GetVideoExercises
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class GetVideoExercisesInputSet(InputSet):
        """
        Set the value of the YouTubeID input for this choreography. ((required, string) The Youtube ID of the video for which you want data.)
        """
        def set_YouTubeID(self, value):
            InputSet._set_input(self, 'YouTubeID', value)


"""
A ResultSet with methods tailored to the values returned by the GetVideoExercises choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class GetVideoExercisesResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((json) The response from Khan Academy.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class GetVideoExercisesChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetVideoExercisesResultSet(response, path)
