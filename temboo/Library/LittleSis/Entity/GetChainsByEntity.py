# -*- coding: utf-8 -*-

###############################################################################
#
# GetChainsByEntity
# Retrieves a chain of connections between two Entities (person or organization) in LittleSis.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class GetChainsByEntity(Choreography):

    """
    Create a new instance of the GetChainsByEntity Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/LittleSis/Entity/GetChainsByEntity')


    def new_input_set(self):
        return GetChainsByEntityInputSet()

    def _make_result_set(self, result, path):
        return GetChainsByEntityResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetChainsByEntityChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the GetChainsByEntity
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class GetChainsByEntityInputSet(InputSet):
        """
        Set the value of the APIKey input for this choreography. ((required, string) The API Key obtained from LittleSis.org.)
        """
        def set_APIKey(self, value):
            InputSet._set_input(self, 'APIKey', value)

        """
        Set the value of the CategoryID input for this choreography. ((optional, integer) Limit the relationships to specific categories by specifying the category number.)
        """
        def set_CategoryID(self, value):
            InputSet._set_input(self, 'CategoryID', value)

        """
        Set the value of the EntityIDs input for this choreography. ((required, integer) The EntityIDs of the two entities for which a relationship chain is to be returned, separated by a semicolon (e.g. 14629;2 ).)
        """
        def set_EntityIDs(self, value):
            InputSet._set_input(self, 'EntityIDs', value)

        """
        Set the value of the Page input for this choreography. ((optional, string) Specifies which of the found chain to expand in detail. Default is 1.)
        """
        def set_Page(self, value):
            InputSet._set_input(self, 'Page', value)

        """
        Set the value of the ResponseFormat input for this choreography. ((optional, string) Format of the response returned by LittleSis.org. Acceptable inputs: xml or json. Defaults to xml)
        """
        def set_ResponseFormat(self, value):
            InputSet._set_input(self, 'ResponseFormat', value)


"""
A ResultSet with methods tailored to the values returned by the GetChainsByEntity choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class GetChainsByEntityResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The response from LittleSis.org.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class GetChainsByEntityChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetChainsByEntityResultSet(response, path)
