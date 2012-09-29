# -*- coding: utf-8 -*-

###############################################################################
#
# Diet
# Returns information about the carbon footprint of an individual's yearly food consumption.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class Diet(Choreography):

    """
    Create a new instance of the Diet Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/BrighterPlanet/Diet')


    def new_input_set(self):
        return DietInputSet()

    def _make_result_set(self, result, path):
        return DietResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return DietChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the Diet
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class DietInputSet(InputSet):
        """
        Set the value of the APIKey input for this choreography. ((required, string) The API Key provided by Brighter Planet.)
        """
        def set_APIKey(self, value):
            InputSet._set_input(self, 'APIKey', value)

        """
        Set the value of the DietClass input for this choreography. ((optional, string) Enter the type of diet. Acceptable inputs: standard, vegetarian, vegan.)
        """
        def set_DietClass(self, value):
            InputSet._set_input(self, 'DietClass', value)

        """
        Set the value of the EndDate input for this choreography. ((optional, string) End date od diet in YYYY-MM-DD format. Defaults to 2013-01-01 when none specified.)
        """
        def set_EndDate(self, value):
            InputSet._set_input(self, 'EndDate', value)

        """
        Set the value of the ResponseFormat input for this choreography. ((optional, string) Specify your desired response format. Accepted values are xml and json (the default).)
        """
        def set_ResponseFormat(self, value):
            InputSet._set_input(self, 'ResponseFormat', value)

        """
        Set the value of the Size input for this choreography. ((required, integer) Enter the number of calories consumed per day. See documentation below for a set of national averages for reference.)
        """
        def set_Size(self, value):
            InputSet._set_input(self, 'Size', value)

        """
        Set the value of the StartDate input for this choreography. ((optional, string) Start date of diet in YYYY-MM-DD format. Defaults to 2012-01-01 when none specified.)
        """
        def set_StartDate(self, value):
            InputSet._set_input(self, 'StartDate', value)


"""
A ResultSet with methods tailored to the values returned by the Diet choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class DietResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The response from Brighter Planet.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class DietChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return DietResultSet(response, path)
