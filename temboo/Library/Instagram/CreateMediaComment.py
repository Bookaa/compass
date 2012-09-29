# -*- coding: utf-8 -*-

###############################################################################
#
# CreateMediaComment
# Creates a comment on a specified media object. 
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class CreateMediaComment(Choreography):

    """
    Create a new instance of the CreateMediaComment Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Instagram/CreateMediaComment')


    def new_input_set(self):
        return CreateMediaCommentInputSet()

    def _make_result_set(self, result, path):
        return CreateMediaCommentResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CreateMediaCommentChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the CreateMediaComment
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class CreateMediaCommentInputSet(InputSet):
        """
        Set the value of the AccessToken input for this choreography. ((required, string) The access token retrieved during the Oauth 2.0 process.)
        """
        def set_AccessToken(self, value):
            InputSet._set_input(self, 'AccessToken', value)

        """
        Set the value of the MediaID input for this choreography. ((required, integer) The ID of the media object that you want to get comments for. For example, a valid MediaID could be 3.)
        """
        def set_MediaID(self, value):
            InputSet._set_input(self, 'MediaID', value)

        """
        Set the value of the Text input for this choreography. ((required, string) The text to post as a comment on the media.)
        """
        def set_Text(self, value):
            InputSet._set_input(self, 'Text', value)


"""
A ResultSet with methods tailored to the values returned by the CreateMediaComment choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class CreateMediaCommentResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((json) The response from Instagram.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class CreateMediaCommentChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return CreateMediaCommentResultSet(response, path)
