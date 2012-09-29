# -*- coding: utf-8 -*-

###############################################################################
#
# GetListByID
# Retrieves a list of NPR categories from a specified list type ID.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class GetListByID(Choreography):

    """
    Create a new instance of the GetListByID Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/NPR/StoryFinder/GetListByID')


    def new_input_set(self):
        return GetListByIDInputSet()

    def _make_result_set(self, result, path):
        return GetListByIDResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetListByIDChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the GetListByID
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class GetListByIDInputSet(InputSet):
        """
        Set the value of the ChildrenOf input for this choreography. ((optional, integer) Returns only items which are assigned to the given topic ID. For example, if Id=3006 and ChildrenOf=1008 only recent series which are assigned to "Arts & Life" are returned.)
        """
        def set_ChildrenOf(self, value):
            InputSet._set_input(self, 'ChildrenOf', value)

        """
        Set the value of the HideChildren input for this choreography. ((optional, boolean) If set to "1", returns only topics which are not subtopics of another topic.)
        """
        def set_HideChildren(self, value):
            InputSet._set_input(self, 'HideChildren', value)

        """
        Set the value of the Id input for this choreography. ((required, integer) The id of the list type you want to retrieve. For example, the list type id for Music Genres is 3218).)
        """
        def set_Id(self, value):
            InputSet._set_input(self, 'Id', value)

        """
        Set the value of the ResponseFormat input for this choreography. ((optional, string) The format that you want the response to be in. Set to json or xml (the default).)
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
A ResultSet with methods tailored to the values returned by the GetListByID choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class GetListByIDResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response from NPR.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class GetListByIDChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetListByIDResultSet(response, path)
