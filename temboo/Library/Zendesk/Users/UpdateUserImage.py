# -*- coding: utf-8 -*-

###############################################################################
#
# UpdateUserImage
# Updates a user's profile image.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class UpdateUserImage(Choreography):

    """
    Create a new instance of the UpdateUserImage Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Zendesk/Users/UpdateUserImage')


    def new_input_set(self):
        return UpdateUserImageInputSet()

    def _make_result_set(self, result, path):
        return UpdateUserImageResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return UpdateUserImageChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the UpdateUserImage
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class UpdateUserImageInputSet(InputSet):
        """
        Set the value of the Response input for this choreography. ((required, json) The response from Zendesk.)
        """
        def set_Response(self, value):
            InputSet._set_input(self, 'Response', value)

        """
        Set the value of the Email input for this choreography. ((required, string) The email address you use to login to your Zendesk account.)
        """
        def set_Email(self, value):
            InputSet._set_input(self, 'Email', value)

        """
        Set the value of the ImageURL input for this choreography. ((required, string) Set the URL of the image.)
        """
        def set_ImageURL(self, value):
            InputSet._set_input(self, 'ImageURL', value)

        """
        Set the value of the Password input for this choreography. ((required, string) Your Zendesk password.)
        """
        def set_Password(self, value):
            InputSet._set_input(self, 'Password', value)

        """
        Set the value of the Server input for this choreography. ((required, string) Your Zendesk domain and subdomain (i.e. temboocare.zendesk.com).)
        """
        def set_Server(self, value):
            InputSet._set_input(self, 'Server', value)

        """
        Set the value of the UserID input for this choreography. ((required, integer) The id of the user being updated.)
        """
        def set_UserID(self, value):
            InputSet._set_input(self, 'UserID', value)


"""
A ResultSet with methods tailored to the values returned by the UpdateUserImage choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class UpdateUserImageResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((required, json) The response from Zendesk.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class UpdateUserImageChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return UpdateUserImageResultSet(response, path)
