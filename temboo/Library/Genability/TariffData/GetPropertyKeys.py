# -*- coding: utf-8 -*-

###############################################################################
#
# GetPropertyKeys
# Returns a list of Property Keys based on a specified search criteria.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class GetPropertyKeys(Choreography):

    """
    Create a new instance of the GetPropertyKeys Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Genability/TariffData/GetPropertyKeys')


    def new_input_set(self):
        return GetPropertyKeysInputSet()

    def _make_result_set(self, result, path):
        return GetPropertyKeysResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetPropertyKeysChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the GetPropertyKeys
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class GetPropertyKeysInputSet(InputSet):
        """
        Set the value of the AppID input for this choreography. ((conditional, string) The App ID provided by Genability.)
        """
        def set_AppID(self, value):
            InputSet._set_input(self, 'AppID', value)

        """
        Set the value of the AppKey input for this choreography. ((required, string) The App Key provided by Genability.)
        """
        def set_AppKey(self, value):
            InputSet._set_input(self, 'AppKey', value)

        """
        Set the value of the EntityID input for this choreography. ((optional, string) Filters the result so that only Properties that belong to this EntityID are returned. When specified, EntityType must also be specified.)
        """
        def set_EntityID(self, value):
            InputSet._set_input(self, 'EntityID', value)

        """
        Set the value of the EntityType input for this choreography. ((optional, string) Filters the result so that only Properties that belong to this EntityType are returned. When specified, EntityID must also be specified.)
        """
        def set_EntityType(self, value):
            InputSet._set_input(self, 'EntityType', value)

        """
        Set the value of the PageCount input for this choreography. ((optional, integer) The number of results to return. Defaults to 25.)
        """
        def set_PageCount(self, value):
            InputSet._set_input(self, 'PageCount', value)

        """
        Set the value of the PageStart input for this choreography. ((optional, integer) The page number to begin the result set from. Defaults to 1.)
        """
        def set_PageStart(self, value):
            InputSet._set_input(self, 'PageStart', value)


"""
A ResultSet with methods tailored to the values returned by the GetPropertyKeys choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class GetPropertyKeysResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((json) The response from Genability.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class GetPropertyKeysChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetPropertyKeysResultSet(response, path)
