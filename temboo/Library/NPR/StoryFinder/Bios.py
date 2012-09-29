# -*- coding: utf-8 -*-

###############################################################################
#
# Bios
# Retrieves a list of NPR personalities and corresponding IDs. Also used to look up the IDs of specific NPR personalities by specifying them as an optional parameter.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class Bios(Choreography):

    """
    Create a new instance of the Bios Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/NPR/StoryFinder/Bios')


    def new_input_set(self):
        return BiosInputSet()

    def _make_result_set(self, result, path):
        return BiosResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return BiosChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the Bios
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class BiosInputSet(InputSet):
        """
        Set the value of the Personality input for this choreography. ((optional, string) The specific name or an NPR personality to return. Multiple names can be specified separated by commas (i.e. Andrei Codrescu,Allison Keyes). Personality IDs are returned when this input is used.)
        """
        def set_Personality(self, value):
            InputSet._set_input(self, 'Personality', value)

        """
        Set the value of the ResponseFormat input for this choreography. ((optional, string) The format that you want the response to be in. Set to json or xml (the default). Note that when specifying Personality, only xml is returned.)
        """
        def set_ResponseFormat(self, value):
            InputSet._set_input(self, 'ResponseFormat', value)

        """
        Set the value of the StoryCountAll input for this choreography. ((optional, integer) Returns only items with at least this number of associated stories.)
        """
        def set_StoryCountAll(self, value):
            InputSet._set_input(self, 'StoryCountAll', value)

        """
        Set the value of the StoryCountMonth input for this choreography. ((optional, integer) Returns only items with at least this number of associated stories published in the last month.)
        """
        def set_StoryCountMonth(self, value):
            InputSet._set_input(self, 'StoryCountMonth', value)

        """
        Set the value of the StoryCountToday input for this choreography. ((optional, integer) Returns only items with at least this number of associated stories published today.)
        """
        def set_StoryCountToday(self, value):
            InputSet._set_input(self, 'StoryCountToday', value)


"""
A ResultSet with methods tailored to the values returned by the Bios choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class BiosResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The response from NPR.)
        """
        def get_Response(self):
            return self._output.get('Response', None)
        """
        Retrieve the value for the "Id" output from this choreography execution. ((integer) The ID of the personality specified. This is only returned when the Personality input is specified. When personalities are specified, this will be a list of IDs separated by commas.)
        """
        def get_Id(self):
            return self._output.get('Id', None)

class BiosChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return BiosResultSet(response, path)
