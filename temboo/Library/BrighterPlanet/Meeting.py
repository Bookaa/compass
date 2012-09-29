# -*- coding: utf-8 -*-

###############################################################################
#
# Meeting
# Returns facility operations emissions analysis for corporate and cultural events.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class Meeting(Choreography):

    """
    Create a new instance of the Meeting Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/BrighterPlanet/Meeting')


    def new_input_set(self):
        return MeetingInputSet()

    def _make_result_set(self, result, path):
        return MeetingResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return MeetingChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the Meeting
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class MeetingInputSet(InputSet):
        """
        Set the value of the APIKey input for this choreography. ((required, string) The API Key provided by Brighter Planet.)
        """
        def set_APIKey(self, value):
            InputSet._set_input(self, 'APIKey', value)

        """
        Set the value of the Area input for this choreography. ((optional, integer) Area of event venue in square meters.)
        """
        def set_Area(self, value):
            InputSet._set_input(self, 'Area', value)

        """
        Set the value of the Date input for this choreography. ((optional, string) Date of event in YYYY-MM-DD format.)
        """
        def set_Date(self, value):
            InputSet._set_input(self, 'Date', value)

        """
        Set the value of the Duration input for this choreography. ((optional, integer) Event duration in total seconds.)
        """
        def set_Duration(self, value):
            InputSet._set_input(self, 'Duration', value)

        """
        Set the value of the ResponseFormat input for this choreography. ((optional, string) Specify your desired response format. Accepted values are xml and json (the default).)
        """
        def set_ResponseFormat(self, value):
            InputSet._set_input(self, 'ResponseFormat', value)

        """
        Set the value of the State input for this choreography. ((optional, string) Two-letter postal abbreviation for the state in which the meeting takes place (e.g. NY).)
        """
        def set_State(self, value):
            InputSet._set_input(self, 'State', value)

        """
        Set the value of the Zip input for this choreography. ((optional, integer) Five digit zip code in which the meeting takes place.)
        """
        def set_Zip(self, value):
            InputSet._set_input(self, 'Zip', value)


"""
A ResultSet with methods tailored to the values returned by the Meeting choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class MeetingResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The response from Brighter Planet.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class MeetingChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return MeetingResultSet(response, path)
