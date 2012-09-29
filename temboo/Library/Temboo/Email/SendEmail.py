# -*- coding: utf-8 -*-

###############################################################################
#
# SendEmail
# Sends an email using a specified email server.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class SendEmail(Choreography):

    """
    Create a new instance of the SendEmail Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Temboo/Email/SendEmail')


    def new_input_set(self):
        return SendEmailInputSet()

    def _make_result_set(self, result, path):
        return SendEmailResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return SendEmailChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the SendEmail
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class SendEmailInputSet(InputSet):
        """
        Set the value of the BCC input for this choreography. ((optional, string) An email address to BCC on the email you're sending. Can be a comma separated list of email addresses.)
        """
        def set_BCC(self, value):
            InputSet._set_input(self, 'BCC', value)

        """
        Set the value of the CC input for this choreography. ((optional, string) An email address to CC on the email you're sending. Can be a comma separated list of email addresses.)
        """
        def set_CC(self, value):
            InputSet._set_input(self, 'CC', value)

        """
        Set the value of the MessageBody input for this choreography. ((required, string) The message body for the email.)
        """
        def set_MessageBody(self, value):
            InputSet._set_input(self, 'MessageBody', value)

        """
        Set the value of the Password input for this choreography. ((required, string) The password for your email account.)
        """
        def set_Password(self, value):
            InputSet._set_input(self, 'Password', value)

        """
        Set the value of the Port input for this choreography. ((required, integer) Specify the port number (i.e. 25 or 465).)
        """
        def set_Port(self, value):
            InputSet._set_input(self, 'Port', value)

        """
        Set the value of the Server input for this choreography. ((required, string) The name or IP address of the email server.)
        """
        def set_Server(self, value):
            InputSet._set_input(self, 'Server', value)

        """
        Set the value of the Subject input for this choreography. ((required, string) The subject line of the email.)
        """
        def set_Subject(self, value):
            InputSet._set_input(self, 'Subject', value)

        """
        Set the value of the ToAddress input for this choreography. ((required, string) The email address that you want to send an email to. Can be a comma separated list of email addresses.)
        """
        def set_ToAddress(self, value):
            InputSet._set_input(self, 'ToAddress', value)

        """
        Set the value of the UseSSL input for this choreography. ((optional, boolean) Set to 1 to connect over SSL. Set to 0 for no SSL. Defaults to 1.)
        """
        def set_UseSSL(self, value):
            InputSet._set_input(self, 'UseSSL', value)

        """
        Set the value of the Username input for this choreography. ((required, string) Your username for your email account. Note, this will used to authenticate your account and as the From Address for the email you are sending.)
        """
        def set_Username(self, value):
            InputSet._set_input(self, 'Username', value)


"""
A ResultSet with methods tailored to the values returned by the SendEmail choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class SendEmailResultSet(ResultSet):
    pass

class SendEmailChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return SendEmailResultSet(response, path)
