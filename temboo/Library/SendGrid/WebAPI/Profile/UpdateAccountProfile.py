# -*- coding: utf-8 -*-

###############################################################################
#
# UpdateAccountProfile
# Update a SendGrid account profile.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class UpdateAccountProfile(Choreography):

    """
    Create a new instance of the UpdateAccountProfile Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/SendGrid/WebAPI/Profile/UpdateAccountProfile')


    def new_input_set(self):
        return UpdateAccountProfileInputSet()

    def _make_result_set(self, result, path):
        return UpdateAccountProfileResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return UpdateAccountProfileChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the UpdateAccountProfile
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class UpdateAccountProfileInputSet(InputSet):
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
        Set the value of the Address input for this choreography. ((optional, string) Enter a company address.)
        """
        def set_Address(self, value):
            InputSet._set_input(self, 'Address', value)

        """
        Set the value of the City input for this choreography. ((optional, string) Enter the city where this address is located in.)
        """
        def set_City(self, value):
            InputSet._set_input(self, 'City', value)

        """
        Set the value of the FirstName input for this choreography. ((optional, string) Enter a first name.)
        """
        def set_FirstName(self, value):
            InputSet._set_input(self, 'FirstName', value)

        """
        Set the value of the LastName input for this choreography. ((optional, string) Enter a last name.)
        """
        def set_LastName(self, value):
            InputSet._set_input(self, 'LastName', value)

        """
        Set the value of the Phone input for this choreography. ((optional, string) Provide a phone number, where you can be reached.)
        """
        def set_Phone(self, value):
            InputSet._set_input(self, 'Phone', value)

        """
        Set the value of the ResponseFormat input for this choreography. ((optional, string) Specify the format of the response from SendGrid: json, or xml.  Default is set to json.)
        """
        def set_ResponseFormat(self, value):
            InputSet._set_input(self, 'ResponseFormat', value)

        """
        Set the value of the State input for this choreography. ((optional, string) Enter the state where this company is located in.)
        """
        def set_State(self, value):
            InputSet._set_input(self, 'State', value)

        """
        Set the value of the Website input for this choreography. ((optional, string) Enter your company's website.)
        """
        def set_Website(self, value):
            InputSet._set_input(self, 'Website', value)

        """
        Set the value of the Zip input for this choreography. ((optional, string) Enter a the zipcode where this company is located.)
        """
        def set_Zip(self, value):
            InputSet._set_input(self, 'Zip', value)

        """
        Set the value of the VaultFile input for this choreography. ()
        """


"""
A ResultSet with methods tailored to the values returned by the UpdateAccountProfile choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class UpdateAccountProfileResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The response from SendGrid. The format corresponds to the ResponseFormat input. Default is json.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class UpdateAccountProfileChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return UpdateAccountProfileResultSet(response, path)
