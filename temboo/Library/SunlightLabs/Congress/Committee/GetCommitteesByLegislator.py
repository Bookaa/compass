# -*- coding: utf-8 -*-

###############################################################################
#
# GetCommitteesByLegislator
# Returns a list of all committees that a specified member serves on, including subcommittes.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class GetCommitteesByLegislator(Choreography):

    """
    Create a new instance of the GetCommitteesByLegislator Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/SunlightLabs/Congress/Committee/GetCommitteesByLegislator')


    def new_input_set(self):
        return GetCommitteesByLegislatorInputSet()

    def _make_result_set(self, result, path):
        return GetCommitteesByLegislatorResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetCommitteesByLegislatorChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the GetCommitteesByLegislator
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class GetCommitteesByLegislatorInputSet(InputSet):
        """
        Set the value of the APIKey input for this choreography. ((required, string) The API Key provided by Sunlight Labs.)
        """
        def set_APIKey(self, value):
            InputSet._set_input(self, 'APIKey', value)

        """
        Set the value of the BioGuideID input for this choreography. ((required, string) A legislator's bioguide_id. Note that this can be retrieved by running the Choreos within the Congress.Legislator bundle.)
        """
        def set_BioGuideID(self, value):
            InputSet._set_input(self, 'BioGuideID', value)

        """
        Set the value of the ResponseFormat input for this choreography. ((optional, string) The format that the response should be in. Valid values are: json (the default) and xml.)
        """
        def set_ResponseFormat(self, value):
            InputSet._set_input(self, 'ResponseFormat', value)


"""
A ResultSet with methods tailored to the values returned by the GetCommitteesByLegislator choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class GetCommitteesByLegislatorResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The response from the Sunlight Congress API.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class GetCommitteesByLegislatorChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetCommitteesByLegislatorResultSet(response, path)
