# -*- coding: utf-8 -*-

###############################################################################
#
# GetReviewerDetails
# Retrieves biographical information about reviewers.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class GetReviewerDetails(Choreography):

    """
    Create a new instance of the GetReviewerDetails Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/NYTimes/MovieReviews/GetReviewerDetails')


    def new_input_set(self):
        return GetReviewerDetailsInputSet()

    def _make_result_set(self, result, path):
        return GetReviewerDetailsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetReviewerDetailsChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the GetReviewerDetails
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class GetReviewerDetailsInputSet(InputSet):
        """
        Set the value of the APIKey input for this choreography. ((required, string) The API Key provided by NY Times.)
        """
        def set_APIKey(self, value):
            InputSet._set_input(self, 'APIKey', value)

        """
        Set the value of the ResourceType input for this choreography. ((optional, string) Specify "all", "full-time", or "part-time" for that subset. Specify a reviewer's name to get details about a reviewer. Names should be separated by hyphens or dots (i.e. manohla-dargis))
        """
        def set_ResourceType(self, value):
            InputSet._set_input(self, 'ResourceType', value)

        """
        Set the value of the ResponseFormat input for this choreography. ((optional, string) The format that the response should be in. Can be set to json, xml, or sphp. Defaults to xml.)
        """
        def set_ResponseFormat(self, value):
            InputSet._set_input(self, 'ResponseFormat', value)


"""
A ResultSet with methods tailored to the values returned by the GetReviewerDetails choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class GetReviewerDetailsResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The response from the NY Times API. Format corresponds to the ResponseFormat input. Defaults to xml.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class GetReviewerDetailsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetReviewerDetailsResultSet(response, path)
