# -*- coding: utf-8 -*-

###############################################################################
#
# GetCompanyHistory
# Returns a complete set of basic records for a given company, covering all the years for which information is available.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class GetCompanyHistory(Choreography):

    """
    Create a new instance of the GetCompanyHistory Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/CorpWatch/Company/GetCompanyHistory')


    def new_input_set(self):
        return GetCompanyHistoryInputSet()

    def _make_result_set(self, result, path):
        return GetCompanyHistoryResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetCompanyHistoryChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the GetCompanyHistory
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class GetCompanyHistoryInputSet(InputSet):
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
        Set the value of the ResponseType input for this choreography. ((optional, string) Specify json or xml for the type of response to be returned. Defaults to xml.)
        """
        def set_ResponseType(self, value):
            InputSet._set_input(self, 'ResponseType', value)


"""
A ResultSet with methods tailored to the values returned by the GetCompanyHistory choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class GetCompanyHistoryResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The response from CorpWatch.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class GetCompanyHistoryChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetCompanyHistoryResultSet(response, path)
