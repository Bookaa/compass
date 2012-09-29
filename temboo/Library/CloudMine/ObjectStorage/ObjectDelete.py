# -*- coding: utf-8 -*-

###############################################################################
#
# ObjectDelete
# Deletes one or more specified keys.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class ObjectDelete(Choreography):

    """
    Create a new instance of the ObjectDelete Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/CloudMine/ObjectStorage/ObjectDelete')


    def new_input_set(self):
        return ObjectDeleteInputSet()

    def _make_result_set(self, result, path):
        return ObjectDeleteResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ObjectDeleteChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the ObjectDelete
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class ObjectDeleteInputSet(InputSet):
        """
        Set the value of the APIKey input for this choreography. ((required, string) The API Key provided by CloudMine after registering your app.)
        """
        def set_APIKey(self, value):
            InputSet._set_input(self, 'APIKey', value)

        """
        Set the value of the All input for this choreography. ((conditional, boolean) Indicates that all keys should be deleted if the Keys input is left empty. Set to "true" to delete all keys.)
        """
        def set_All(self, value):
            InputSet._set_input(self, 'All', value)

        """
        Set the value of the ApplicationIdentifier input for this choreography. ((required, string) The application identifier provided by CloudMine after registering your app.)
        """
        def set_ApplicationIdentifier(self, value):
            InputSet._set_input(self, 'ApplicationIdentifier', value)

        """
        Set the value of the Keys input for this choreography. ((conditional, string) A comma separated list of keys to delete. Required unless specifying "true" for the All parameter.)
        """
        def set_Keys(self, value):
            InputSet._set_input(self, 'Keys', value)

        """
        Set the value of the SessionToken input for this choreography. ((conditional, string) The session token for an existing user (returned by the AccountLogin Choreo). This is only required if your app is performing this operation on behalf of another user.)
        """
        def set_SessionToken(self, value):
            InputSet._set_input(self, 'SessionToken', value)


"""
A ResultSet with methods tailored to the values returned by the ObjectDelete choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class ObjectDeleteResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((json) The response from CloudMine.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class ObjectDeleteChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ObjectDeleteResultSet(response, path)
