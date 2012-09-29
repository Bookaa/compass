# -*- coding: utf-8 -*-

###############################################################################
#
# EditLinkPost
# Updates a specified link post on a Tumblr blog.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class EditLinkPost(Choreography):

    """
    Create a new instance of the EditLinkPost Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Tumblr/EditLinkPost')


    def new_input_set(self):
        return EditLinkPostInputSet()

    def _make_result_set(self, result, path):
        return EditLinkPostResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return EditLinkPostChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the EditLinkPost
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class EditLinkPostInputSet(InputSet):
        """
        Set the value of the URL input for this choreography. ((required, string) The link you want to post.)
        """
        def set_URL(self, value):
            InputSet._set_input(self, 'URL', value)

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
        Set the value of the Description input for this choreography. ((optional, string) A user-supplied description. HTML is allowed.)
        """
        def set_Description(self, value):
            InputSet._set_input(self, 'Description', value)

        """
        Set the value of the ID input for this choreography. ((required, integer) The ID of the post you want to edit.)
        """
        def set_ID(self, value):
            InputSet._set_input(self, 'ID', value)

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
        Set the value of the Title input for this choreography. ((optional, string) The title of the page the link points to. HTML entities should be escaped.)
        """
        def set_Title(self, value):
            InputSet._set_input(self, 'Title', value)

        """
        Set the value of the Tweet input for this choreography. ((optional, string) Manages the autotweet (if enabled) for this post. Defaults to off for no tweet. Enter text to override the default tweet.)
        """
        def set_Tweet(self, value):
            InputSet._set_input(self, 'Tweet', value)


"""
A ResultSet with methods tailored to the values returned by the EditLinkPost choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class EditLinkPostResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response from Tumblr in XML format.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class EditLinkPostChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return EditLinkPostResultSet(response, path)
