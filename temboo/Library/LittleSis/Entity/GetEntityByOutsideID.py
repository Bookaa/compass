# -*- coding: utf-8 -*-

###############################################################################
#
# GetEntityByOutsideID
# Retrieves the record for an Entity in LittleSis using the ID of a number of third-party organizations such as the SEC or GovTrack.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class GetEntityByOutsideID(Choreography):

    """
    Create a new instance of the GetEntityByOutsideID Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/LittleSis/Entity/GetEntityByOutsideID')


    def new_input_set(self):
        return GetEntityByOutsideIDInputSet()

    def _make_result_set(self, result, path):
        return GetEntityByOutsideIDResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetEntityByOutsideIDChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the GetEntityByOutsideID
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class GetEntityByOutsideIDInputSet(InputSet):
        """
        Set the value of the APIKey input for this choreography. ((required, string) The API Key obtained from LittleSis.org.)
        """
        def set_APIKey(self, value):
            InputSet._set_input(self, 'APIKey', value)

        """
        Set the value of the IDType input for this choreography. ((required, string) You can search for a record by the IDs of other third-party services. Acceptable inputs: ticker, sec_cik, fec_id, bioguide_id, govtrack_id, crp_id, watchdog_id. See documentation for more information.)
        """
        def set_IDType(self, value):
            InputSet._set_input(self, 'IDType', value)

        """
        Set the value of the ID input for this choreography. ((required, integer) The ID of the record to be returned.)
        """
        def set_ID(self, value):
            InputSet._set_input(self, 'ID', value)

        """
        Set the value of the ResponseFormat input for this choreography. ((optional, string) Format of the response returned by LittleSis.org. Acceptable inputs: xml or json. Defaults to xml)
        """
        def set_ResponseFormat(self, value):
            InputSet._set_input(self, 'ResponseFormat', value)


"""
A ResultSet with methods tailored to the values returned by the GetEntityByOutsideID choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class GetEntityByOutsideIDResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The response from LittleSis.org.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class GetEntityByOutsideIDChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetEntityByOutsideIDResultSet(response, path)
