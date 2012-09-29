# -*- coding: utf-8 -*-

###############################################################################
#
# NearbyContacts
# Retrieves nearby Dwolla spots within the range of the provided latitude and longitude.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class NearbyContacts(Choreography):

    """
    Create a new instance of the NearbyContacts Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Dwolla/Contacts/NearbyContacts')


    def new_input_set(self):
        return NearbyContactsInputSet()

    def _make_result_set(self, result, path):
        return NearbyContactsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return NearbyContactsChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the NearbyContacts
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class NearbyContactsInputSet(InputSet):
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
        Set the value of the Latitude input for this choreography. ((required, decimal) Current latitude.)
        """
        def set_Latitude(self, value):
            InputSet._set_input(self, 'Latitude', value)

        """
        Set the value of the Limit input for this choreography. ((optional, integer) Number of spots to retrieve. Defaults to 10.)
        """
        def set_Limit(self, value):
            InputSet._set_input(self, 'Limit', value)

        """
        Set the value of the Longitude input for this choreography. ((required, decimal) Current longitude.)
        """
        def set_Longitude(self, value):
            InputSet._set_input(self, 'Longitude', value)

        """
        Set the value of the Range input for this choreography. ((optional, integer) Range to retrieve spots for in miles.)
        """
        def set_Range(self, value):
            InputSet._set_input(self, 'Range', value)


"""
A ResultSet with methods tailored to the values returned by the NearbyContacts choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class NearbyContactsResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((json) The response from Dwolla.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class NearbyContactsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return NearbyContactsResultSet(response, path)
