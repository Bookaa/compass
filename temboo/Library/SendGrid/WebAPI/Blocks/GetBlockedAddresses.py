# -*- coding: utf-8 -*-

###############################################################################
#
# GetBlockedAddresses
# Retrieve a list of blocked emails, with response codes, and optional dates.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class GetBlockedAddresses(Choreography):

    """
    Create a new instance of the GetBlockedAddresses Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/SendGrid/WebAPI/Blocks/GetBlockedAddresses')


    def new_input_set(self):
        return GetBlockedAddressesInputSet()

    def _make_result_set(self, result, path):
        return GetBlockedAddressesResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetBlockedAddressesChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the GetBlockedAddresses
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class GetBlockedAddressesInputSet(InputSet):
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
        Set the value of the Date input for this choreography. ((optional, string) Enter: 1, to obtain the timestamp of the Block records. Dates will be returned in a MySQL timestamp format - YYYY-MM-DD HH:MM:SS)
        """
        def set_Date(self, value):
            InputSet._set_input(self, 'Date', value)

        """
        Set the value of the Days input for this choreography. ((optional, integer) Enter the number of days (greater than 0) for which block data will be retrieved.)
        """
        def set_Days(self, value):
            InputSet._set_input(self, 'Days', value)

        """
        Set the value of the EndDate input for this choreography. ((optional, string) Specify the end of the date range for which blocks are to be retireved. The specified date must be in YYYY-MM-DD format.)
        """
        def set_EndDate(self, value):
            InputSet._set_input(self, 'EndDate', value)

        """
        Set the value of the ResponseFormat input for this choreography. ((optional, string) Specify the format of the response from SendGrid: json, or xml.  Default is set to json.)
        """
        def set_ResponseFormat(self, value):
            InputSet._set_input(self, 'ResponseFormat', value)

        """
        Set the value of the StartDate input for this choreography. ((optional, string) Specify the start of the date range for which blocks are to be retireved. The specified date must be in YYYY-MM-DD format, and must be earlier than the EndDate variable value.)
        """
        def set_StartDate(self, value):
            InputSet._set_input(self, 'StartDate', value)

        """
        Set the value of the VaultFile input for this choreography. ()
        """


"""
A ResultSet with methods tailored to the values returned by the GetBlockedAddresses choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class GetBlockedAddressesResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The response from SendGrid. The format corresponds to the ResponseFormat input. Default is json.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class GetBlockedAddressesChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetBlockedAddressesResultSet(response, path)
