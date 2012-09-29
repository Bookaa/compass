# -*- coding: utf-8 -*-

###############################################################################
#
# SendMail
# Allows you to send emails.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class SendMail(Choreography):

    """
    Create a new instance of the SendMail Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/SendGrid/WebAPI/Mail/SendMail')


    def new_input_set(self):
        return SendMailInputSet()

    def _make_result_set(self, result, path):
        return SendMailResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return SendMailChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the SendMail
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class SendMailInputSet(InputSet):
        """
        Set the value of the FileContents input for this choreography. ((optional, string) The Base64-encoded contents of the file you want to attach.)
        """
        def set_FileContents(self, value):
            InputSet._set_input(self, 'FileContents', value)

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
        Set the value of the BCC input for this choreography. ((optional, string) Enter a BCC recipient.  Multiple recipients can also be passed in as an array of email addresses.)
        """
        def set_BCC(self, value):
            InputSet._set_input(self, 'BCC', value)

        """
        Set the value of the Date input for this choreography. ((optional, string) Specify the date of your email in RFC 2822 format.  For example: Thu, 21 Dec 2000 16:01:07 +0200)
        """
        def set_Date(self, value):
            InputSet._set_input(self, 'Date', value)

        """
        Set the value of the FileName input for this choreography. ((optional, string) The name of the file you are attaching to your email.)
        """
        def set_FileName(self, value):
            InputSet._set_input(self, 'FileName', value)

        """
        Set the value of the FromName input for this choreography. ((optional, string) Enter a name to be appended to the from email.  For example, your company name, or your name.)
        """
        def set_FromName(self, value):
            InputSet._set_input(self, 'FromName', value)

        """
        Set the value of the From input for this choreography. ((required, string) Specfiy the originating email address.  Must be from your domain.)
        """
        def set_From(self, value):
            InputSet._set_input(self, 'From', value)

        """
        Set the value of the HTML input for this choreography. ((conditional, string) The HTML to be used in the body of your email message. Required unless specifying a plain text body in the Text input.)
        """
        def set_HTML(self, value):
            InputSet._set_input(self, 'HTML', value)

        """
        Set the value of the Headers input for this choreography. ((optional, json) Specify collection of key/value pairs in JSON format. Each key represents a header name and the value the header value. For example: {"X-Accept-Language": "en", "X-Mailer": "MyApp"})
        """
        def set_Headers(self, value):
            InputSet._set_input(self, 'Headers', value)

        """
        Set the value of the ReplyTo input for this choreography. ((optional, string) Enter an email address to append to the reply-to field of your email.)
        """
        def set_ReplyTo(self, value):
            InputSet._set_input(self, 'ReplyTo', value)

        """
        Set the value of the ResponseFormat input for this choreography. ((optional, string) Specify the format of the response from SendGrid: json, or xml.  Default is set to json.)
        """
        def set_ResponseFormat(self, value):
            InputSet._set_input(self, 'ResponseFormat', value)

        """
        Set the value of the Subject input for this choreography. ((required, string) Enter the subject of the email message.)
        """
        def set_Subject(self, value):
            InputSet._set_input(self, 'Subject', value)

        """
        Set the value of the Text input for this choreography. ((conditional, string) The text of the email message. Required unless providing the message body using the HTML input.)
        """
        def set_Text(self, value):
            InputSet._set_input(self, 'Text', value)

        """
        Set the value of the ToName input for this choreography. ((optional, string) Enter the name of the email recipient.)
        """
        def set_ToName(self, value):
            InputSet._set_input(self, 'ToName', value)

        """
        Set the value of the To input for this choreography. ((required, string) Enter a valid recipient email address.  Multiple addresses can be entered as elements of an array.)
        """
        def set_To(self, value):
            InputSet._set_input(self, 'To', value)

        """
        Set the value of the XSMTPAPI input for this choreography. ((optional, json) Must be specified in valid JSON format.  See here for additional info: http://docs.sendgrid.com/documentation/api/smtp-api/)
        """
        def set_XSMTPAPI(self, value):
            InputSet._set_input(self, 'XSMTPAPI', value)

        """
        Set the value of the VaultFile input for this choreography. (A path to a vault file to use for the attachment. Can be used as an alternative to the FileContents input.)
        """


"""
A ResultSet with methods tailored to the values returned by the SendMail choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class SendMailResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The response from SendGrid. The format corresponds to the ResponseFormat input. Default is json.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class SendMailChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return SendMailResultSet(response, path)
