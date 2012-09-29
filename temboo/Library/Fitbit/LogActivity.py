# -*- coding: utf-8 -*-

###############################################################################
#
# LogActivity
# Log a new activity for a particular date.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class LogActivity(Choreography):

    """
    Create a new instance of the LogActivity Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Fitbit/LogActivity')


    def new_input_set(self):
        return LogActivityInputSet()

    def _make_result_set(self, result, path):
        return LogActivityResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return LogActivityChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the LogActivity
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class LogActivityInputSet(InputSet):
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
        Set the value of the ActivityId input for this choreography. ((required, integer) This can be the id of the activity, directory activity, or intensity level activity.)
        """
        def set_ActivityId(self, value):
            InputSet._set_input(self, 'ActivityId', value)

        """
        Set the value of the ConsumerKey input for this choreography. ((required, string) The Consumer Key provided by Fitbit.)
        """
        def set_ConsumerKey(self, value):
            InputSet._set_input(self, 'ConsumerKey', value)

        """
        Set the value of the ConsumerSecret input for this choreography. ((required, string) The Consumer Secret provided by Fitbit.)
        """
        def set_ConsumerSecret(self, value):
            InputSet._set_input(self, 'ConsumerSecret', value)

        """
        Set the value of the Date input for this choreography. ((required, date) The date that corresponds with the new log entry (in the format yyyy-MM-dd).)
        """
        def set_Date(self, value):
            InputSet._set_input(self, 'Date', value)

        """
        Set the value of the DistanceUnit input for this choreography. ((optional, string) Corresponds with the Distance parameter (i.e. Mile). See Choreo documentation for links to unit charts.)
        """
        def set_DistanceUnit(self, value):
            InputSet._set_input(self, 'DistanceUnit', value)

        """
        Set the value of the Distance input for this choreography. ((optional, decimal) The activity distance. Used when activityId corresponds to 'Running'  or 'Walking' for example.)
        """
        def set_Distance(self, value):
            InputSet._set_input(self, 'Distance', value)

        """
        Set the value of the DurationMilliseconds input for this choreography. ((required, integer) The duration of the activity in milliseconds.)
        """
        def set_DurationMilliseconds(self, value):
            InputSet._set_input(self, 'DurationMilliseconds', value)

        """
        Set the value of the Format input for this choreography. ((optional, string) The format that you want the response to be in: xml or json. Defaults to xml.)
        """
        def set_Format(self, value):
            InputSet._set_input(self, 'Format', value)

        """
        Set the value of the StartTime input for this choreography. ((required, string) The hour and minutes for the start of the activity formatted like HH:mm.)
        """
        def set_StartTime(self, value):
            InputSet._set_input(self, 'StartTime', value)

        """
        Set the value of the UserId input for this choreography. ((optional, string) The user's encoded id. Defaults to "-" (dash) which will return data for the user associated with the token credentials provided.)
        """
        def set_UserId(self, value):
            InputSet._set_input(self, 'UserId', value)


"""
A ResultSet with methods tailored to the values returned by the LogActivity choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class LogActivityResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The response from Fitbit.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class LogActivityChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return LogActivityResultSet(response, path)
