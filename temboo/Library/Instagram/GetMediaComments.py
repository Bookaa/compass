# -*- coding: utf-8 -*-

###############################################################################
#
# GetMediaComments
# Retrieves a full list of comments for a specified media object.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class GetMediaComments(Choreography):

    """
    Create a new instance of the GetMediaComments Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Instagram/GetMediaComments')


    def new_input_set(self):
        return GetMediaCommentsInputSet()

    def _make_result_set(self, result, path):
        return GetMediaCommentsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetMediaCommentsChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the GetMediaComments
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class GetMediaCommentsInputSet(InputSet):
        """
        Set the value of the AccessToken input for this choreography. ((conditional, string) The access token retrieved during the Oauth 2.0 process. Required unless you provide the ClientID.)
        """
        def set_AccessToken(self, value):
            InputSet._set_input(self, 'AccessToken', value)

        """
        Set the value of the ClientID input for this choreography. ((conditional, string) The Client ID provided by Instagram after registering your application. Required unless you provide the AccessToken.)
        """
        def set_ClientID(self, value):
            InputSet._set_input(self, 'ClientID', value)

        """
        Set the value of the MediaID input for this choreography. ((required, integer) The ID of the media object that you want to get comments for. For example, a valid MediaID could be 3.)
        """
        def set_MediaID(self, value):
            InputSet._set_input(self, 'MediaID', value)


"""
A ResultSet with methods tailored to the values returned by the GetMediaComments choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class GetMediaCommentsResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((json) The response from Instagram.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class GetMediaCommentsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetMediaCommentsResultSet(response, path)
