# -*- coding: utf-8 -*-

###############################################################################
#
# Basic
# Retrieves the Dwolla account information for the user associated with the specified consumer credentials and Dwolla account identifier.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class Basic(Choreography):

    """
    Create a new instance of the Basic Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Dwolla/Users/Basic')


    def new_input_set(self):
        return BasicInputSet()

    def _make_result_set(self, result, path):
        return BasicResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return BasicChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the Basic
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class BasicInputSet(InputSet):
        """
        Set the value of the AccountIdentifier input for this choreography. ((required, string) Dwolla account identifier or email address of the Dwolla account.)
        """
        def set_AccountIdentifier(self, value):
            InputSet._set_input(self, 'AccountIdentifier', value)

        """
        Set the value of the ClientID input for this choreography. ((required, string) The Client ID provided by Dwolla (AKA the Consumer Key).)
        """
        def set_ClientID(self, value):
            InputSet._set_input(self, 'ClientID', value)

        """
        Set the value of the ClientSecret input for this choreography. ((required, string) The Client Secret provided by Dwolla (AKA the Consumer Secret).)
        """
        def set_ClientSecret(self, value):
            InputSet._set_input(self, 'ClientSecret', value)


"""
A ResultSet with methods tailored to the values returned by the Basic choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class BasicResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((json) The response from Dwolla.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class BasicChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return BasicResultSet(response, path)
