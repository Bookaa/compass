# -*- coding: utf-8 -*-

###############################################################################
#
# CreateChatPost
# Creates a new chat post for a specified Tumblr blog.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class CreateChatPost(Choreography):

    """
    Create a new instance of the CreateChatPost Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Tumblr/CreateChatPost')


    def new_input_set(self):
        return CreateChatPostInputSet()

    def _make_result_set(self, result, path):
        return CreateChatPostResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CreateChatPostChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the CreateChatPost
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class CreateChatPostInputSet(InputSet):
        """
        Set the value of the Conversation input for this choreography. ((required, string) The text of the conversation/chat, with dialogue labels (no HTML).)
        """
        def set_Conversation(self, value):
            InputSet._set_input(self, 'Conversation', value)

        """
        Set the value of the APIKey input for this choreography. ((required, string) The API Key provided by Tumblr (AKA the OAuth Consumer Key).)
        """
        def set_APIKey(self, value):
            InputSet._set_input(self, 'APIKey', value)

        """
        Set the value of the AccessTokenSecret input for this choreography. ((required, string) The Access Token Secret retrieved during the OAuth process.)
        """
        def set_AccessTokenSecret(self, value):
            InputSet._set_input(self, 'AccessTokenSecret', value)

        """
        Set the value of the AccessToken input for this choreography. ((required, string) The Access Token retrieved during the OAuth process.)
        """
        def set_AccessToken(self, value):
            InputSet._set_input(self, 'AccessToken', value)

        """
        Set the value of the BaseHostname input for this choreography. ((required, string) The standard or custom blog hostname (i.e. temboo.tumblr.com).)
        """
        def set_BaseHostname(self, value):
            InputSet._set_input(self, 'BaseHostname', value)

        """
        Set the value of the Date input for this choreography. ((optional, date) The GMT date and time of the post. Can be an epoch timestamp in milliseconds or formatted like: Dec 8th, 2011 4:03pm. Defaults to NOW().)
        """
        def set_Date(self, value):
            InputSet._set_input(self, 'Date', value)

        """
        Set the value of the Markdown input for this choreography. ((optional, boolean) Indicates whether the post uses markdown syntax. Defaults to false. Set to 1 to indicate true.)
        """
        def set_Markdown(self, value):
            InputSet._set_input(self, 'Markdown', value)

        """
        Set the value of the SecretKey input for this choreography. ((required, string) The Secret Key provided by Tumblr (AKA the OAuth Consumer Secret).)
        """
        def set_SecretKey(self, value):
            InputSet._set_input(self, 'SecretKey', value)

        """
        Set the value of the Slug input for this choreography. ((optional, string) Adds a short text summary to the end of the post URL.)
        """
        def set_Slug(self, value):
            InputSet._set_input(self, 'Slug', value)

        """
        Set the value of the State input for this choreography. ((optional, string) The state of the post. Specify one of the following:  published, draft, queue. Defaults to published.)
        """
        def set_State(self, value):
            InputSet._set_input(self, 'State', value)

        """
        Set the value of the Tags input for this choreography. ((optional, string) Comma-separated tags for this post.)
        """
        def set_Tags(self, value):
            InputSet._set_input(self, 'Tags', value)

        """
        Set the value of the Title input for this choreography. ((optional, string) The title of the chat.)
        """
        def set_Title(self, value):
            InputSet._set_input(self, 'Title', value)

        """
        Set the value of the Tweet input for this choreography. ((optional, string) Manages the autotweet (if enabled) for this post. Defaults to off for no tweet. Enter text to override the default tweet.)
        """
        def set_Tweet(self, value):
            InputSet._set_input(self, 'Tweet', value)


"""
A ResultSet with methods tailored to the values returned by the CreateChatPost choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class CreateChatPostResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response from Tumblr in XML format.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class CreateChatPostChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return CreateChatPostResultSet(response, path)
