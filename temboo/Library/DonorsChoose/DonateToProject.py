# -*- coding: utf-8 -*-

###############################################################################
#
# DonateToProject
# Makes a donation to a specified DonorsChoose.org project.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class DonateToProject(Choreography):

    """
    Create a new instance of the DonateToProject Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/DonorsChoose/DonateToProject')


    def new_input_set(self):
        return DonateToProjectInputSet()

    def _make_result_set(self, result, path):
        return DonateToProjectResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return DonateToProjectChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the DonateToProject
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class DonateToProjectInputSet(InputSet):
        """
        Set the value of the APIKey input for this choreography. ((required, string) The APIKey provided by DonorsChoose.org.)
        """
        def set_APIKey(self, value):
            InputSet._set_input(self, 'APIKey', value)

        """
        Set the value of the APIPassword input for this choreography. ((required, string) Your DonorsChoose.org API password. This is only required when performing transactions.)
        """
        def set_APIPassword(self, value):
            InputSet._set_input(self, 'APIPassword', value)

        """
        Set the value of the Address1 input for this choreography. ((optional, string) Line one of the donor's address.)
        """
        def set_Address1(self, value):
            InputSet._set_input(self, 'Address1', value)

        """
        Set the value of the Address2 input for this choreography. ((optional, string) Line two of the donor's address.)
        """
        def set_Address2(self, value):
            InputSet._set_input(self, 'Address2', value)

        """
        Set the value of the Amount input for this choreography. ((required, integer) The donation amount. Must be a whole number.)
        """
        def set_Amount(self, value):
            InputSet._set_input(self, 'Amount', value)

        """
        Set the value of the Callback input for this choreography. ((optional, string) To wrap the response in a callback function, include the name in this input.)
        """
        def set_Callback(self, value):
            InputSet._set_input(self, 'Callback', value)

        """
        Set the value of the City input for this choreography. ((optional, string) The donor's city.)
        """
        def set_City(self, value):
            InputSet._set_input(self, 'City', value)

        """
        Set the value of the Email input for this choreography. ((required, string) The email address of the person who is making the donation.)
        """
        def set_Email(self, value):
            InputSet._set_input(self, 'Email', value)

        """
        Set the value of the FirstName input for this choreography. ((optional, string) The first name of the donor.)
        """
        def set_FirstName(self, value):
            InputSet._set_input(self, 'FirstName', value)

        """
        Set the value of the LastName input for this choreography. ((optional, string) The last name of the donor.)
        """
        def set_LastName(self, value):
            InputSet._set_input(self, 'LastName', value)

        """
        Set the value of the ProposalId input for this choreography. ((required, integer) The ID of the project that will receive the donation.)
        """
        def set_ProposalId(self, value):
            InputSet._set_input(self, 'ProposalId', value)

        """
        Set the value of the ResponseFormat input for this choreography. ((optional, string) The format that the response should be in. Can be set to xml or json. Defaults to xml.)
        """
        def set_ResponseFormat(self, value):
            InputSet._set_input(self, 'ResponseFormat', value)

        """
        Set the value of the Salutation input for this choreography. ((optional, string) Hwo the donor wants to be acknowledged on donorschoose.org.)
        """
        def set_Salutation(self, value):
            InputSet._set_input(self, 'Salutation', value)

        """
        Set the value of the State input for this choreography. ((optional, string) The donor's state.)
        """
        def set_State(self, value):
            InputSet._set_input(self, 'State', value)

        """
        Set the value of the Zip input for this choreography. ((optional, string) The donor's five-digit zip code.)
        """
        def set_Zip(self, value):
            InputSet._set_input(self, 'Zip', value)


"""
A ResultSet with methods tailored to the values returned by the DonateToProject choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class DonateToProjectResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The response from DonorsChoose.org.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class DonateToProjectChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return DonateToProjectResultSet(response, path)
