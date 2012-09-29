# -*- coding: utf-8 -*-

###############################################################################
#
# GetTopicVideos
# Retreievs a list of all videos for a given topic.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class GetTopicVideos(Choreography):

    """
    Create a new instance of the GetTopicVideos Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/KhanAcademy/Topics/GetTopicVideos')


    def new_input_set(self):
        return GetTopicVideosInputSet()

    def _make_result_set(self, result, path):
        return GetTopicVideosResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetTopicVideosChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the GetTopicVideos
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class GetTopicVideosInputSet(InputSet):
        """
        Set the value of the TopicID input for this choreography. ((required, string) The ID of the topic.)
        """
        def set_TopicID(self, value):
            InputSet._set_input(self, 'TopicID', value)


"""
A ResultSet with methods tailored to the values returned by the GetTopicVideos choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class GetTopicVideosResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((json) The response from Khan Academy.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class GetTopicVideosChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetTopicVideosResultSet(response, path)
