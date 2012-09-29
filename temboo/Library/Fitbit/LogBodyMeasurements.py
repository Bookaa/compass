# -*- coding: utf-8 -*-

###############################################################################
#
# LogBodyMeasurements
# Log a new weight for a particular date.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class LogBodyMeasurements(Choreography):

    """
    Create a new instance of the LogBodyMeasurements Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Fitbit/LogBodyMeasurements')


    def new_input_set(self):
        return LogBodyMeasurementsInputSet()

    def _make_result_set(self, result, path):
        return LogBodyMeasurementsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return LogBodyMeasurementsChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the LogBodyMeasurements
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class LogBodyMeasurementsInputSet(InputSet):
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
        Set the value of the Format input for this choreography. ((optional, string) The format that you want the response to be in: xml or json. Defaults to xml.)
        """
        def set_Format(self, value):
            InputSet._set_input(self, 'Format', value)

        """
        Set the value of the UserId input for this choreography. ((optional, string) The user's encoded id. Defaults to "-" (dash) which will return data for the user associated with the token credentials provided.)
        """
        def set_UserId(self, value):
            InputSet._set_input(self, 'UserId', value)

        """
        Set the value of the Weight input for this choreography. ((required, decimal) A new value (in pounds) to log for weight. In the format of X.XX.)
        """
        def set_Weight(self, value):
            InputSet._set_input(self, 'Weight', value)


"""
A ResultSet with methods tailored to the values returned by the LogBodyMeasurements choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class LogBodyMeasurementsResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The response from Fitbit.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class LogBodyMeasurementsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return LogBodyMeasurementsResultSet(response, path)
