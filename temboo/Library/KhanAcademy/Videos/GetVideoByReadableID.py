# -*- coding: utf-8 -*-

###############################################################################
#
# GetVideoByReadableID
# Retrieves video data for a given video according to its readable ID.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class GetVideoByReadableID(Choreography):

    """
    Create a new instance of the GetVideoByReadableID Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/KhanAcademy/Videos/GetVideoByReadableID')


    def new_input_set(self):
        return GetVideoByReadableIDInputSet()

    def _make_result_set(self, result, path):
        return GetVideoByReadableIDResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetVideoByReadableIDChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the GetVideoByReadableID
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class GetVideoByReadableIDInputSet(InputSet):
        """
        Set the value of the ReadableID input for this choreography. ((required, string) The ReadableID of the video fro which you want to retrieve information (e.g. adding-subtracting-negative-numbers).)
        """
        def set_ReadableID(self, value):
            InputSet._set_input(self, 'ReadableID', value)


"""
A ResultSet with methods tailored to the values returned by the GetVideoByReadableID choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class GetVideoByReadableIDResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((json) The response from Khan Academy.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class GetVideoByReadableIDChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetVideoByReadableIDResultSet(response, path)
