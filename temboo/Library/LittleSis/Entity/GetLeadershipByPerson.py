# -*- coding: utf-8 -*-

###############################################################################
#
# GetLeadershipByPerson
# Retrieves a list of organizations of which a given person is an executive or board member.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class GetLeadershipByPerson(Choreography):

    """
    Create a new instance of the GetLeadershipByPerson Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/LittleSis/Entity/GetLeadershipByPerson')


    def new_input_set(self):
        return GetLeadershipByPersonInputSet()

    def _make_result_set(self, result, path):
        return GetLeadershipByPersonResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetLeadershipByPersonChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the GetLeadershipByPerson
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class GetLeadershipByPersonInputSet(InputSet):
        """
        Set the value of the APIKey input for this choreography. ((required, string) The API Key obtained from LittleSis.org.)
        """
        def set_APIKey(self, value):
            InputSet._set_input(self, 'APIKey', value)

        """
        Set the value of the Current input for this choreography. ((optional, integer) Set to 1 to limit the relationships returned to only past relationships. Set to 0 to limit relationships returned to only current relationships. Defaults to all.)
        """
        def set_Current(self, value):
            InputSet._set_input(self, 'Current', value)

        """
        Set the value of the EntityID input for this choreography. ((required, integer) The ID of the person.)
        """
        def set_EntityID(self, value):
            InputSet._set_input(self, 'EntityID', value)

        """
        Set the value of the ResponseFormat input for this choreography. ((optional, string) Format of the response returned by LittleSis.org. Acceptable inputs: xml or json. Defaults to xml)
        """
        def set_ResponseFormat(self, value):
            InputSet._set_input(self, 'ResponseFormat', value)

        """
        Set the value of the Type input for this choreography. ((optional, string) Limits results to organizations of the specified type, e.g. "PublicCompany.")
        """
        def set_Type(self, value):
            InputSet._set_input(self, 'Type', value)


"""
A ResultSet with methods tailored to the values returned by the GetLeadershipByPerson choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class GetLeadershipByPersonResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The response from LittleSis.org.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class GetLeadershipByPersonChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetLeadershipByPersonResultSet(response, path)
