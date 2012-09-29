# -*- coding: utf-8 -*-

###############################################################################
#
# EntityTypes
# Retrieves a list of the types of Entities (people or organizations) in LittleSis, along with TypeIDs.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class EntityTypes(Choreography):

    """
    Create a new instance of the EntityTypes Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/LittleSis/Entity/EntityTypes')


    def new_input_set(self):
        return EntityTypesInputSet()

    def _make_result_set(self, result, path):
        return EntityTypesResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return EntityTypesChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the EntityTypes
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class EntityTypesInputSet(InputSet):
        """
        Set the value of the ResponseFormat input for this choreography. ((optional, string) The format of the response from LittleSis.org. Acceptable inputs: xml or json. Defautls to xml.)
        """
        def set_ResponseFormat(self, value):
            InputSet._set_input(self, 'ResponseFormat', value)


"""
A ResultSet with methods tailored to the values returned by the EntityTypes choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class EntityTypesResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The response from LittleSis.org.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class EntityTypesChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return EntityTypesResultSet(response, path)
