# -*- coding: utf-8 -*-

###############################################################################
#
# GetReferenceData
# Retrieves a wide variety of reference data sets provided by Brighter Planet.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class GetReferenceData(Choreography):

    """
    Create a new instance of the GetReferenceData Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/BrighterPlanet/GetReferenceData')


    def new_input_set(self):
        return GetReferenceDataInputSet()

    def _make_result_set(self, result, path):
        return GetReferenceDataResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetReferenceDataChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the GetReferenceData
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class GetReferenceDataInputSet(InputSet):
        """
        Set the value of the Resource input for this choreography. ((required, string) The name of the reference data resource you want to retrieve (i.e. airports, airlines, etc). Resource names are formatted using plural, lowercase, and underscores (i.e. automobile_makes).)
        """
        def set_Resource(self, value):
            InputSet._set_input(self, 'Resource', value)

        """
        Set the value of the ResponseFormat input for this choreography. ((optional, string) The desired response format. Accepted formats are: csv, xml, and json (the default).)
        """
        def set_ResponseFormat(self, value):
            InputSet._set_input(self, 'ResponseFormat', value)


"""
A ResultSet with methods tailored to the values returned by the GetReferenceData choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class GetReferenceDataResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The response from Brighter Planet.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class GetReferenceDataChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetReferenceDataResultSet(response, path)
