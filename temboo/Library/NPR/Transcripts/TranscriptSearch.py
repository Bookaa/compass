# -*- coding: utf-8 -*-

###############################################################################
#
# TranscriptSearch
# Retrieves transcripts of NPR stories based on their unique story IDs.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class TranscriptSearch(Choreography):

    """
    Create a new instance of the TranscriptSearch Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/NPR/Transcripts/TranscriptSearch')


    def new_input_set(self):
        return TranscriptSearchInputSet()

    def _make_result_set(self, result, path):
        return TranscriptSearchResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return TranscriptSearchChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the TranscriptSearch
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class TranscriptSearchInputSet(InputSet):
        """
        Set the value of the APIKey input for this choreography. ((required, string) The API Key provided by NPR.)
        """
        def set_APIKey(self, value):
            InputSet._set_input(self, 'APIKey', value)

        """
        Set the value of the ID input for this choreography. ((required, integer) The story ID for which you want a transcript. You can find the story ID by first running an aprropriate StoryFinder Choreo.)
        """
        def set_ID(self, value):
            InputSet._set_input(self, 'ID', value)


"""
A ResultSet with methods tailored to the values returned by the TranscriptSearch choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class TranscriptSearchResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) )
        """
        def get_Response(self):
            return self._output.get('Response', None)

class TranscriptSearchChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return TranscriptSearchResultSet(response, path)
