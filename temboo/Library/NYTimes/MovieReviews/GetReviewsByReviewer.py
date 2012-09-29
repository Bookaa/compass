# -*- coding: utf-8 -*-

###############################################################################
#
# GetReviewsByReviewer
# Retrieves reviews by a specific Times reviewer.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class GetReviewsByReviewer(Choreography):

    """
    Create a new instance of the GetReviewsByReviewer Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/NYTimes/MovieReviews/GetReviewsByReviewer')


    def new_input_set(self):
        return GetReviewsByReviewerInputSet()

    def _make_result_set(self, result, path):
        return GetReviewsByReviewerResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetReviewsByReviewerChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the GetReviewsByReviewer
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class GetReviewsByReviewerInputSet(InputSet):
        """
        Set the value of the APIKey input for this choreography. ((required, string) The API Key provided by NY Times.)
        """
        def set_APIKey(self, value):
            InputSet._set_input(self, 'APIKey', value)

        """
        Set the value of the CriticsPick input for this choreography. ((optional, string) Set this parameter to Y to limt the results to NYT Critics' Picks. To get only those movies that have not been highlighted by Times critics, specify N.)
        """
        def set_CriticsPick(self, value):
            InputSet._set_input(self, 'CriticsPick', value)

        """
        Set the value of the Offset input for this choreography. ((optional, integer) A numeric value indicating the starting point of the result set. Used to page through results.)
        """
        def set_Offset(self, value):
            InputSet._set_input(self, 'Offset', value)

        """
        Set the value of the Order input for this choreography. ((optional, string) Sets the sort order of the results. Accepted values are: by-title, by-publication-date, by-opening-date, by-dvd-release-date.)
        """
        def set_Order(self, value):
            InputSet._set_input(self, 'Order', value)

        """
        Set the value of the ResponseFormat input for this choreography. ((optional, string) The format that the response should be in. Can be set to json, xml, or sphp. Defaults to xml.)
        """
        def set_ResponseFormat(self, value):
            InputSet._set_input(self, 'ResponseFormat', value)

        """
        Set the value of the ReviewerName input for this choreography. ((required, string) The name of the Times reviewer. Reviewer names should be separated by hyphens or dots (i.e. manohla-dargis or manohla.dargis))
        """
        def set_ReviewerName(self, value):
            InputSet._set_input(self, 'ReviewerName', value)


"""
A ResultSet with methods tailored to the values returned by the GetReviewsByReviewer choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class GetReviewsByReviewerResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The response from the NY Times API. Format corresponds to the ResponseFormat input. Defaults to xml.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class GetReviewsByReviewerChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetReviewsByReviewerResultSet(response, path)
