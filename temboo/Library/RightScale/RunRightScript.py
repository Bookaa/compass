# -*- coding: utf-8 -*-

###############################################################################
#
# RunRightScript
# Executes a specified RightScript.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class RunRightScript(Choreography):

    """
    Create a new instance of the RunRightScript Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/RightScale/RunRightScript')


    def new_input_set(self):
        return RunRightScriptInputSet()

    def _make_result_set(self, result, path):
        return RunRightScriptResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return RunRightScriptChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the RunRightScript
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class RunRightScriptInputSet(InputSet):
        """
        Set the value of the AccountID input for this choreography. ((required, string) Enter a RighScale Account ID.)
        """
        def set_AccountID(self, value):
            InputSet._set_input(self, 'AccountID', value)

        """
        Set the value of the Password input for this choreography. ((required, string) Enter a RightScale account password.)
        """
        def set_Password(self, value):
            InputSet._set_input(self, 'Password', value)

        """
        Set the value of the RightScriptID input for this choreography. ((required, integer) The ID of the RightScript.)
        """
        def set_RightScriptID(self, value):
            InputSet._set_input(self, 'RightScriptID', value)

        """
        Set the value of the ServerID input for this choreography. ((required, integer) Enter the RightScale Server ID that is to be stopped.)
        """
        def set_ServerID(self, value):
            InputSet._set_input(self, 'ServerID', value)

        """
        Set the value of the Username input for this choreography. ((required, string) Enter a RightScale username.)
        """
        def set_Username(self, value):
            InputSet._set_input(self, 'Username', value)


"""
A ResultSet with methods tailored to the values returned by the RunRightScript choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class RunRightScriptResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response from Rightscale in XML format.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class RunRightScriptChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return RunRightScriptResultSet(response, path)
