# -*- coding: utf-8 -*-

###############################################################################
#
# GetList
# Retrieves information about a List in LittleSis according to its ID.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class GetList(Choreography):

    """
    Create a new instance of the GetList Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/LittleSis/List/GetList')


    def new_input_set(self):
        return GetListInputSet()

    def _make_result_set(self, result, path):
        return GetListResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetListChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the GetList
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class GetListInputSet(InputSet):
        """
        Set the value of the APIKey input for this choreography. ((required, string) The API Key obtained from LittleSis.org.)
        """
        def set_APIKey(self, value):
            InputSet._set_input(self, 'APIKey', value)

        """
        Set the value of the Entities input for this choreography. ((optional, string) Indicate "entities" to retrieve records of the entities that belong to the list. Otherwise, only a basic record about the list will be returned.)
        """
        def set_Entities(self, value):
            InputSet._set_input(self, 'Entities', value)

        """
        Set the value of the ListID input for this choreography. ((required, integer) The ID of the list record to be returned.)
        """
        def set_ListID(self, value):
            InputSet._set_input(self, 'ListID', value)

        """
        Set the value of the Number input for this choreography. ((optional, integer) Specifies what number of results to show. Used in conjunction with Page parameter, a Nnumber of 20 and a Page of 6 will show results 100-120.)
        """
        def set_Number(self, value):
            InputSet._set_input(self, 'Number', value)

        """
        Set the value of the Page input for this choreography. ((optional, integer) Specifies what page of results to show. Used in conjunction with Number parameter. A number of 20 and a Page of 6 will show results 100-120.)
        """
        def set_Page(self, value):
            InputSet._set_input(self, 'Page', value)

        """
        Set the value of the ResponseFormat input for this choreography. ((optional, string) Format of the response returned by LittleSis.org. Acceptable inputs: xml or json. Defaults to xml)
        """
        def set_ResponseFormat(self, value):
            InputSet._set_input(self, 'ResponseFormat', value)

        """
        Set the value of the TypeID input for this choreography. ((optional, integer) When the Entities parameter is activated, you can specify type IDs limiting the entities returned to those having the specified types (as a comma-delimited list).)
        """
        def set_TypeID(self, value):
            InputSet._set_input(self, 'TypeID', value)


"""
A ResultSet with methods tailored to the values returned by the GetList choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class GetListResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The response from LittleSis.org.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class GetListChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetListResultSet(response, path)
