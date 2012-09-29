# -*- coding: utf-8 -*-

###############################################################################
#
# ScheduleNewsletterDelivery
# Schedule a delivery time for an existing Newsletter.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class ScheduleNewsletterDelivery(Choreography):

    """
    Create a new instance of the ScheduleNewsletterDelivery Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/SendGrid/NewsletterAPI/Schedule/ScheduleNewsletterDelivery')


    def new_input_set(self):
        return ScheduleNewsletterDeliveryInputSet()

    def _make_result_set(self, result, path):
        return ScheduleNewsletterDeliveryResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ScheduleNewsletterDeliveryChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the ScheduleNewsletterDelivery
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class ScheduleNewsletterDeliveryInputSet(InputSet):
        """
        Set the value of the APIKey input for this choreography. ((required, string) Enter a SendGrid API Key.)
        """
        def set_APIKey(self, value):
            InputSet._set_input(self, 'APIKey', value)

        """
        Set the value of the APIUser input for this choreography. ((required, string) Enter a SendGrid username.)
        """
        def set_APIUser(self, value):
            InputSet._set_input(self, 'APIUser', value)

        """
        Set the value of the After input for this choreography. ((optional, integer) Enter the number of minites after which the newsletter will be delivered.)
        """
        def set_After(self, value):
            InputSet._set_input(self, 'After', value)

        """
        Set the value of the At input for this choreography. ((optional, string) Specify the date and time when the newsletter is to be delievered, in ISO 8601 format (YYYY-MM-DD HH:MM:SS+-HH:MM))
        """
        def set_At(self, value):
            InputSet._set_input(self, 'At', value)

        """
        Set the value of the Name input for this choreography. ((required, string) Enter the name of the newsletter that is being scheduled for delivery.  If the newsletter is to be sent immediately, then leave the At, and After parameters empty.)
        """
        def set_Name(self, value):
            InputSet._set_input(self, 'Name', value)

        """
        Set the value of the ResponseFormat input for this choreography. ((optional, string) Specify the format of the response from SendGrid: json, or xml.  Default is set to json.)
        """
        def set_ResponseFormat(self, value):
            InputSet._set_input(self, 'ResponseFormat', value)

        """
        Set the value of the VaultFile input for this choreography. ()
        """


"""
A ResultSet with methods tailored to the values returned by the ScheduleNewsletterDelivery choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class ScheduleNewsletterDeliveryResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The response from SendGrid. The format corresponds to the ResponseFormat input. Default is json.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class ScheduleNewsletterDeliveryChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ScheduleNewsletterDeliveryResultSet(response, path)
