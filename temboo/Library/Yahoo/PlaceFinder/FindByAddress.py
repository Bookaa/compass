# -*- coding: utf-8 -*-

###############################################################################
#
# FindByAddress
# Retrieves complete geocoding information for a location by specifying an address or partial address.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class FindByAddress(Choreography):

    """
    Create a new instance of the FindByAddress Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Yahoo/PlaceFinder/FindByAddress')


    def new_input_set(self):
        return FindByAddressInputSet()

    def _make_result_set(self, result, path):
        return FindByAddressResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return FindByAddressChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the FindByAddress
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class FindByAddressInputSet(InputSet):
        """
        Set the value of the Address input for this choreography. ((required, string) The address to be searched.)
        """
        def set_Address(self, value):
            InputSet._set_input(self, 'Address', value)

        """
        Set the value of the AppID input for this choreography. ((required, string) The App ID provided by Yahoo!)
        """
        def set_AppID(self, value):
            InputSet._set_input(self, 'AppID', value)

        """
        Set the value of the ResponseFormat input for this choreography. ((optional, string) You can specify json to get this output format in JSON. Otherwise, the default output will be in XML.)
        """
        def set_ResponseFormat(self, value):
            InputSet._set_input(self, 'ResponseFormat', value)


"""
A ResultSet with methods tailored to the values returned by the FindByAddress choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class FindByAddressResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The response from Yahoo! PlaceFinder.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class FindByAddressChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return FindByAddressResultSet(response, path)
