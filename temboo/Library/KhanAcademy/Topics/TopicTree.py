# -*- coding: utf-8 -*-

###############################################################################
#
# TopicTree
# Retrieves the hierarchical organization of all topics in the Khan Academy library.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class TopicTree(Choreography):

    """
    Create a new instance of the TopicTree Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/KhanAcademy/Topics/TopicTree')


    def new_input_set(self):
        return TopicTreeInputSet()

    def _make_result_set(self, result, path):
        return TopicTreeResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return TopicTreeChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the TopicTree
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class TopicTreeInputSet(InputSet):
    pass

"""
A ResultSet with methods tailored to the values returned by the TopicTree choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class TopicTreeResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((json) The response from Khan Academy.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class TopicTreeChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return TopicTreeResultSet(response, path)
