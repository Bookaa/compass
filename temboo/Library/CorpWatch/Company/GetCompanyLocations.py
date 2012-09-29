# -*- coding: utf-8 -*-

###############################################################################
#
# GetCompanyLocations
# Returns a list of mailing addresses, business addresses, and jurisdiction of incorporation associated with a given company.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class GetCompanyLocations(Choreography):

    """
    Create a new instance of the GetCompanyLocations Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/CorpWatch/Company/GetCompanyLocations')


    def new_input_set(self):
        return GetCompanyLocationsInputSet()

    def _make_result_set(self, result, path):
        return GetCompanyLocationsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetCompanyLocationsChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the GetCompanyLocations
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class GetCompanyLocationsInputSet(InputSet):
        """
        Set the value of the APIKey input for this choreography. ((optional, string) The APIKey from CorpWatch if you have one.)
        """
        def set_APIKey(self, value):
            InputSet._set_input(self, 'APIKey', value)

        """
        Set the value of the CWID input for this choreography. ((required, string) CoprWatch ID for the company. Format looks like: cw_8484.)
        """
        def set_CWID(self, value):
            InputSet._set_input(self, 'CWID', value)

        """
        Set the value of the Index input for this choreography. ((optional, integer) Set the index number of the first result to be returned. The index of the first result is 0.)
        """
        def set_Index(self, value):
            InputSet._set_input(self, 'Index', value)

        """
        Set the value of the Limit input for this choreography. ((optional, integer) The number of results to be returned. Defaults to 100. Maximum is 5000.)
        """
        def set_Limit(self, value):
            InputSet._set_input(self, 'Limit', value)

        """
        Set the value of the ResponseType input for this choreography. ((optional, string) Specify json or xml for the type of response to be returned. Defaults to xml.)
        """
        def set_ResponseType(self, value):
            InputSet._set_input(self, 'ResponseType', value)


"""
A ResultSet with methods tailored to the values returned by the GetCompanyLocations choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class GetCompanyLocationsResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The response from CorpWatch.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class GetCompanyLocationsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetCompanyLocationsResultSet(response, path)
