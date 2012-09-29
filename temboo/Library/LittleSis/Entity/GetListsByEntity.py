# -*- coding: utf-8 -*-

###############################################################################
#
# GetListsByEntity
# Retrieves a list of Lists in LittleSis the given Entity (person or organization) belongs to.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class GetListsByEntity(Choreography):

    """
    Create a new instance of the GetListsByEntity Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/LittleSis/Entity/GetListsByEntity')


    def new_input_set(self):
        return GetListsByEntityInputSet()

    def _make_result_set(self, result, path):
        return GetListsByEntityResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetListsByEntityChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the GetListsByEntity
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class GetListsByEntityInputSet(InputSet):
        """
        Set the value of the APIKey input for this choreography. ((required, string) The API Key obtained from LittleSis.org.)
        """
        def set_APIKey(self, value):
            InputSet._set_input(self, 'APIKey', value)

        """
        Set the value of the EntityID input for this choreography. ((required, integer) The ID of the record to be returned.)
        """
        def set_EntityID(self, value):
            InputSet._set_input(self, 'EntityID', value)

        """
        Set the value of the ResponseFormat input for this choreography. ((optional, string) Format of the response returned by LittleSis.org. Acceptable inputs: xml or json. Defaults to xml)
        """
        def set_ResponseFormat(self, value):
            InputSet._set_input(self, 'ResponseFormat', value)


"""
A ResultSet with methods tailored to the values returned by the GetListsByEntity choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class GetListsByEntityResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The response from LittleSis.org.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class GetListsByEntityChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetListsByEntityResultSet(response, path)
