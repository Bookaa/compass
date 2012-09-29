# -*- coding: utf-8 -*-

###############################################################################
#
# Series
# Retrieves a list of NPR series titles and corresponding IDs. Also used to look up the IDs of specific NPR series by specifying those as an optional parameter.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class Series(Choreography):

    """
    Create a new instance of the Series Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/NPR/StoryFinder/Series')


    def new_input_set(self):
        return SeriesInputSet()

    def _make_result_set(self, result, path):
        return SeriesResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return SeriesChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the Series
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class SeriesInputSet(InputSet):
        """
        Set the value of the ResponseFormat input for this choreography. ((optional, string) The format that you want the response to be in. Set to json or xml (the default). Note that when specifying Series, only xml is returned.)
        """
        def set_ResponseFormat(self, value):
            InputSet._set_input(self, 'ResponseFormat', value)

        """
        Set the value of the Series input for this choreography. ((optional, string) The specific series title to return. Multiple titles can be specified separated by commas (i.e. Life in Berlin,Climate Connections). Series IDs are returned when this input is used.)
        """
        def set_Series(self, value):
            InputSet._set_input(self, 'Series', value)

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
A ResultSet with methods tailored to the values returned by the Series choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class SeriesResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The response from NPR.)
        """
        def get_Response(self):
            return self._output.get('Response', None)
        """
        Retrieve the value for the "Id" output from this choreography execution. ((integer) The ID of the series. This is only returned when the Series input is specified. When multiple series are specified, this will be a list of IDs separated by commas.)
        """
        def get_Id(self):
            return self._output.get('Id', None)

class SeriesChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return SeriesResultSet(response, path)
