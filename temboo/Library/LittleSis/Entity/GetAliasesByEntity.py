# -*- coding: utf-8 -*-

###############################################################################
#
# GetAliasesByEntity
# Retrieves the aliases associated with each LittleSis Entity (person or organization).
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class GetAliasesByEntity(Choreography):

    """
    Create a new instance of the GetAliasesByEntity Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/LittleSis/Entity/GetAliasesByEntity')


    def new_input_set(self):
        return GetAliasesByEntityInputSet()

    def _make_result_set(self, result, path):
        return GetAliasesByEntityResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetAliasesByEntityChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the GetAliasesByEntity
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class GetAliasesByEntityInputSet(InputSet):
        """
        Set the value of the APIKey input for this choreography. ((required, string) The API Key obtained from LittleSis.org.)
        """
        def set_APIKey(self, value):
            InputSet._set_input(self, 'APIKey', value)

        """
        Set the value of the EntityID input for this choreography. ((required, integer) The ID of the Entity (person or organization) for which aliases are to be retrieved.)
        """
        def set_EntityID(self, value):
            InputSet._set_input(self, 'EntityID', value)

        """
        Set the value of the ResponseFormat input for this choreography. ((optional, string) Format of the response returned by LittleSis.org. Acceptable inputs: xml or json. Defaults to xml)
        """
        def set_ResponseFormat(self, value):
            InputSet._set_input(self, 'ResponseFormat', value)


"""
A ResultSet with methods tailored to the values returned by the GetAliasesByEntity choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class GetAliasesByEntityResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The response from LittleSis.org.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class GetAliasesByEntityChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetAliasesByEntityResultSet(response, path)
