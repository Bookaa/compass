# -*- coding: utf-8 -*-

###############################################################################
#
# GetReviewsByKeyword
# Searches movie reviews by keyword and various filter parameters.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class GetReviewsByKeyword(Choreography):

    """
    Create a new instance of the GetReviewsByKeyword Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/NYTimes/MovieReviews/GetReviewsByKeyword')


    def new_input_set(self):
        return GetReviewsByKeywordInputSet()

    def _make_result_set(self, result, path):
        return GetReviewsByKeywordResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetReviewsByKeywordChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the GetReviewsByKeyword
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class GetReviewsByKeywordInputSet(InputSet):
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
        Set the value of the DVD input for this choreography. ((optional, string) Set this parameter to Y to limit the results to movies that have been released on DVD. To get only those movies that have not been released on DVD, specify N.)
        """
        def set_DVD(self, value):
            InputSet._set_input(self, 'DVD', value)

        """
        Set the value of the Limit input for this choreography. ((optional, integer) The number of results to return.)
        """
        def set_Limit(self, value):
            InputSet._set_input(self, 'Limit', value)

        """
        Set the value of the Offset input for this choreography. ((optional, integer) A numeric value indicating the starting point of the result set. This can be used in combination with the Limit input to page through results.)
        """
        def set_Offset(self, value):
            InputSet._set_input(self, 'Offset', value)

        """
        Set the value of the OpeningDate input for this choreography. ((optional, date) Limits by date or range of dates. The opening-date is the date the movie's opening date in the New York region. Format YYYY-MM-DD. Separate ranges with semicolons.)
        """
        def set_OpeningDate(self, value):
            InputSet._set_input(self, 'OpeningDate', value)

        """
        Set the value of the Order input for this choreography. ((optional, string) Sets the sort order of the results. Accepted values are: by-title, by-publication-date, by-opening-date, by-dvd-release-date.)
        """
        def set_Order(self, value):
            InputSet._set_input(self, 'Order', value)

        """
        Set the value of the PublicationDate input for this choreography. ((optional, date) Limits by date or range of dates. The publication-date is the date the review was first publish.ed in The Times. Format YYYY-MM-DD. Separate ranges with semicolons.)
        """
        def set_PublicationDate(self, value):
            InputSet._set_input(self, 'PublicationDate', value)

        """
        Set the value of the Query input for this choreography. ((optional, string) A string of search keywords. Matches movie titles and indexed terms.)
        """
        def set_Query(self, value):
            InputSet._set_input(self, 'Query', value)

        """
        Set the value of the ResponseFormat input for this choreography. ((optional, string) The format that the response should be in. Can be set to json, xml, or sphp. Defaults to xml.)
        """
        def set_ResponseFormat(self, value):
            InputSet._set_input(self, 'ResponseFormat', value)

        """
        Set the value of the Reviewer input for this choreography. ((optional, string) Limits results to reviews by a specific critic. Reviewer names should be hyphenated or concatenated with dots.)
        """
        def set_Reviewer(self, value):
            InputSet._set_input(self, 'Reviewer', value)

        """
        Set the value of the ThousandBest input for this choreography. ((optional, string) Set this parameter to Y to limit the results to movies on the Times list of The Best 1,000 Movies Ever Made. To get only those movies that are not on the list, specify N.)
        """
        def set_ThousandBest(self, value):
            InputSet._set_input(self, 'ThousandBest', value)


"""
A ResultSet with methods tailored to the values returned by the GetReviewsByKeyword choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class GetReviewsByKeywordResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The response from the NY Times API. Format corresponds to the ResponseFormat input. Defaults to xml.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class GetReviewsByKeywordChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetReviewsByKeywordResultSet(response, path)
