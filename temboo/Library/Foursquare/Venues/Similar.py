# -*- coding: utf-8 -*-

###############################################################################
#
# Similar
# Returns a list of venues similar to the specified venue.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class Similar(Choreography):

    """
    Create a new instance of the Similar Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Foursquare/Venues/Similar')


    def new_input_set(self):
        return SimilarInputSet()

    def _make_result_set(self, result, path):
        return SimilarResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return SimilarChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the Similar
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class SimilarInputSet(InputSet):
        """
        Set the value of the OauthToken input for this choreography. ((required, string) The Foursquare API Oauth token string.)
        """
        def set_OauthToken(self, value):
            InputSet._set_input(self, 'OauthToken', value)

        """
        Set the value of the ResponseFormat input for this choreography. ((optional, string) The format that response should be in. Can be set to xml or json. Defaults to json.)
        """
        def set_ResponseFormat(self, value):
            InputSet._set_input(self, 'ResponseFormat', value)

        """
        Set the value of the VenueID input for this choreography. ((required, string) The id for the venue you want similar venues for.)
        """
        def set_VenueID(self, value):
            InputSet._set_input(self, 'VenueID', value)


"""
A ResultSet with methods tailored to the values returned by the Similar choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class SimilarResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The response from Foursquare. Corresponds to the ResponseFormat input. Defaults to JSON.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class SimilarChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return SimilarResultSet(response, path)
