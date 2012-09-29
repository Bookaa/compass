# -*- coding: utf-8 -*-

###############################################################################
#
# GetReferences
# Retrieves references for the data included in any record obtained from LittleSis.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class GetReferences(Choreography):

    """
    Create a new instance of the GetReferences Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/LittleSis/Reference/GetReferences')


    def new_input_set(self):
        return GetReferencesInputSet()

    def _make_result_set(self, result, path):
        return GetReferencesResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetReferencesChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the GetReferences
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class GetReferencesInputSet(InputSet):
        """
        Set the value of the APIKey input for this choreography. ((required, string) The API Key obtained from LittleSis.org.)
        """
        def set_APIKey(self, value):
            InputSet._set_input(self, 'APIKey', value)

        """
        Set the value of the ID input for this choreography. ((required, decimal) The ID of the record for which you want references. This can be either an entity or a relationship ID.)
        """
        def set_ID(self, value):
            InputSet._set_input(self, 'ID', value)

        """
        Set the value of the RecordType input for this choreography. ((required, string) Specify type of record for which you want to obtain references: entity (for a person or an institution record) or relationship (for a relationship record).)
        """
        def set_RecordType(self, value):
            InputSet._set_input(self, 'RecordType', value)

        """
        Set the value of the ResponseFormat input for this choreography. ((optional, string) Format of the response returned by LittleSis.org. Acceptable inputs: xml or json. Defaults to xml)
        """
        def set_ResponseFormat(self, value):
            InputSet._set_input(self, 'ResponseFormat', value)


"""
A ResultSet with methods tailored to the values returned by the GetReferences choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class GetReferencesResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The response from LittleSis.org.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class GetReferencesChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetReferencesResultSet(response, path)
