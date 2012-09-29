# -*- coding: utf-8 -*-

###############################################################################
#
# SetupApp
# Sets up a previously activated app.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class SetupApp(Choreography):

    """
    Create a new instance of the SetupApp Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/SendGrid/WebAPI/FilterCommands/SetupApp')


    def new_input_set(self):
        return SetupAppInputSet()

    def _make_result_set(self, result, path):
        return SetupAppResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return SetupAppChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the SetupApp
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class SetupAppInputSet(InputSet):
        """
        Set the value of the APIKey input for this choreography. ((required, string) Enter a SendGrid API Key.)
        """
        def set_APIKey(self, value):
            InputSet._set_input(self, 'APIKey', value)

        """
        Set the value of the APIUser input for this choreography. ((required, string) Enter a SendGrid username.)
        """
        def set_APIUser(self, value):
            InputSet._set_input(self, 'APIUser', value)

        """
        Set the value of the AppName input for this choreography. ((required, string) Enter the name of the app to be activated.  A list of available apps can be obtained by running the ListAvailableApps Choreo.)
        """
        def set_AppName(self, value):
            InputSet._set_input(self, 'AppName', value)

        """
        Set the value of the Password input for this choreography. ((required, string) Enter the password for the app that is being setup.  For example, if setting up a Twitter app, enter a valid Twitter account password.)
        """
        def set_Password(self, value):
            InputSet._set_input(self, 'Password', value)

        """
        Set the value of the ResponseFormat input for this choreography. ((optional, string) Specify the format of the response from SendGrid: json, or xml.  Default is set to json.)
        """
        def set_ResponseFormat(self, value):
            InputSet._set_input(self, 'ResponseFormat', value)

        """
        Set the value of the Username input for this choreography. ((required, string) Enter the username for the app that is being setup. For example, if setting up a Twitter app, enter a valid Twitter account username.)
        """
        def set_Username(self, value):
            InputSet._set_input(self, 'Username', value)

        """
        Set the value of the VaultFile input for this choreography. ()
        """


"""
A ResultSet with methods tailored to the values returned by the SetupApp choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class SetupAppResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The response from SendGrid. The format corresponds to the ResponseFormat input. Default is json.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class SetupAppChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return SetupAppResultSet(response, path)
