# -*- coding: utf-8 -*-

###############################################################################
#
# GetAllTimeCategoryTotals
# Obtain statistics by specified categories.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class GetAllTimeCategoryTotals(Choreography):

    """
    Create a new instance of the GetAllTimeCategoryTotals Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/SendGrid/WebAPI/Statistics/GetAllTimeCategoryTotals')


    def new_input_set(self):
        return GetAllTimeCategoryTotalsInputSet()

    def _make_result_set(self, result, path):
        return GetAllTimeCategoryTotalsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetAllTimeCategoryTotalsChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the GetAllTimeCategoryTotals
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class GetAllTimeCategoryTotalsInputSet(InputSet):
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
        Set the value of the Aggregate input for this choreography. ((required, integer) Must be set to 1 to retrieve category statistics.  Default is set to 1.)
        """
        def set_Aggregate(self, value):
            InputSet._set_input(self, 'Aggregate', value)

        """
        Set the value of the Category input for this choreography. ((required, string) Enter a category for which statistics will be retrieved. It must be an existing category that has statistics. If the category entered does not exist, an empty result set will be returned.)
        """
        def set_Category(self, value):
            InputSet._set_input(self, 'Category', value)

        """
        Set the value of the Days input for this choreography. ((optional, integer) Enter the number of days (greater than 0) for which block data will be retrieved. Note that you can use either the days parameter or the start_date and end_date parameter.)
        """
        def set_Days(self, value):
            InputSet._set_input(self, 'Days', value)

        """
        Set the value of the ResponseFormat input for this choreography. ((optional, string) Specify the format of the response from SendGrid: json, or xml.  Default is set to json.)
        """
        def set_ResponseFormat(self, value):
            InputSet._set_input(self, 'ResponseFormat', value)

        """
        Set the value of the StartDate input for this choreography. ((optional, string) Specify the start of the date range for which blocks are to be retireved. The specified date must be in YYYY-MM-DD format, and must be earlier than the EndDate variable value. Use this ,or Days.)
        """
        def set_StartDate(self, value):
            InputSet._set_input(self, 'StartDate', value)

        """
        Set the value of the VaultFile input for this choreography. ()
        """


"""
A ResultSet with methods tailored to the values returned by the GetAllTimeCategoryTotals choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class GetAllTimeCategoryTotalsResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The response from SendGrid. The format corresponds to the ResponseFormat input. Default is json.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class GetAllTimeCategoryTotalsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetAllTimeCategoryTotalsResultSet(response, path)
