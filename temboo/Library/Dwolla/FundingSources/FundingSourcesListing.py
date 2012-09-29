# -*- coding: utf-8 -*-

###############################################################################
#
# FundingSourcesListing
# Retrieves a list of verified funding sources for the user associated with the authorized access token.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class FundingSourcesListing(Choreography):

    """
    Create a new instance of the FundingSourcesListing Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Dwolla/FundingSources/FundingSourcesListing')


    def new_input_set(self):
        return FundingSourcesListingInputSet()

    def _make_result_set(self, result, path):
        return FundingSourcesListingResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return FundingSourcesListingChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the FundingSourcesListing
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class FundingSourcesListingInputSet(InputSet):
        """
        Set the value of the AccessToken input for this choreography. ((required, string) A valid OAuth token.)
        """
        def set_AccessToken(self, value):
            InputSet._set_input(self, 'AccessToken', value)


"""
A ResultSet with methods tailored to the values returned by the FundingSourcesListing choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class FundingSourcesListingResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((json) The response from Dwolla.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class FundingSourcesListingChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return FundingSourcesListingResultSet(response, path)
