# -*- coding: utf-8 -*-

###############################################################################
#
# GetList
# Returns a list of legislators that meet a specified search criteria.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class GetList(Choreography):

    """
    Create a new instance of the GetList Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/SunlightLabs/Congress/Legislator/GetList')


    def new_input_set(self):
        return GetListInputSet()

    def _make_result_set(self, result, path):
        return GetListResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetListChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the GetList
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class GetListInputSet(InputSet):
        """
        Set the value of the APIKey input for this choreography. ((required, string) The API Key provided by Sunlight Labs.)
        """
        def set_APIKey(self, value):
            InputSet._set_input(self, 'APIKey', value)

        """
        Set the value of the AllLegislators input for this choreography. ((optional, boolean) A boolean flag indicating to search for all legislators even when they are no longer in office.)
        """
        def set_AllLegislators(self, value):
            InputSet._set_input(self, 'AllLegislators', value)

        """
        Set the value of the BioguideID input for this choreography. ((optional, string) The bioguide_id of the legislator to return.)
        """
        def set_BioguideID(self, value):
            InputSet._set_input(self, 'BioguideID', value)

        """
        Set the value of the CRPID input for this choreography. ((optional, string) The crp_id associated with a legislator to return.)
        """
        def set_CRPID(self, value):
            InputSet._set_input(self, 'CRPID', value)

        """
        Set the value of the District input for this choreography. ((optional, integer) Narrows the search result by district number.)
        """
        def set_District(self, value):
            InputSet._set_input(self, 'District', value)

        """
        Set the value of the FECID input for this choreography. ((optional, string) The fec_id associated with the legislator to return.)
        """
        def set_FECID(self, value):
            InputSet._set_input(self, 'FECID', value)

        """
        Set the value of the FacebookID input for this choreography. ((optional, string) The facebook id of a legislator to return.)
        """
        def set_FacebookID(self, value):
            InputSet._set_input(self, 'FacebookID', value)

        """
        Set the value of the FirstName input for this choreography. ((optional, string) The first name of a legislator to return.)
        """
        def set_FirstName(self, value):
            InputSet._set_input(self, 'FirstName', value)

        """
        Set the value of the Gender input for this choreography. ((optional, string) Narrows the search result by gender.)
        """
        def set_Gender(self, value):
            InputSet._set_input(self, 'Gender', value)

        """
        Set the value of the GovTrackID input for this choreography. ((optional, string) The govetrack_id associated with a legistlator to return.)
        """
        def set_GovTrackID(self, value):
            InputSet._set_input(self, 'GovTrackID', value)

        """
        Set the value of the InOffice input for this choreography. ((optional, boolean) Whether or not the individual is in office currently. Valid values are true or false.)
        """
        def set_InOffice(self, value):
            InputSet._set_input(self, 'InOffice', value)

        """
        Set the value of the LastName input for this choreography. ((optional, string) The last name of the legislator to return.)
        """
        def set_LastName(self, value):
            InputSet._set_input(self, 'LastName', value)

        """
        Set the value of the Party input for this choreography. ((optional, string) Narrows the search result by party (i.e. "D" or "R").)
        """
        def set_Party(self, value):
            InputSet._set_input(self, 'Party', value)

        """
        Set the value of the ResponseFormat input for this choreography. ((optional, string) The format that the response should be in. Valid values are: json (the default) and xml.)
        """
        def set_ResponseFormat(self, value):
            InputSet._set_input(self, 'ResponseFormat', value)

        """
        Set the value of the State input for this choreography. ((optional, string) A state abbreviation to narrow the search results.)
        """
        def set_State(self, value):
            InputSet._set_input(self, 'State', value)

        """
        Set the value of the Title input for this choreography. ((optional, string) The title associated with the individual to return.)
        """
        def set_Title(self, value):
            InputSet._set_input(self, 'Title', value)

        """
        Set the value of the TwitterID input for this choreography. ((optional, string) The twitter id of the legislator to return (note, this can be a twitter screen name).)
        """
        def set_TwitterID(self, value):
            InputSet._set_input(self, 'TwitterID', value)

        """
        Set the value of the VoteSmartID input for this choreography. ((optional, integer) The votesmart_id of a legislator to return.)
        """
        def set_VoteSmartID(self, value):
            InputSet._set_input(self, 'VoteSmartID', value)


"""
A ResultSet with methods tailored to the values returned by the GetList choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class GetListResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The response from the Sunlight Congress API.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class GetListChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetListResultSet(response, path)
