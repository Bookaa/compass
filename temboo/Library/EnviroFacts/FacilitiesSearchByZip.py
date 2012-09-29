# -*- coding: utf-8 -*-

###############################################################################
#
# FacilitiesSearchByZip
# Retrieves a list of EPA-regulated facilities in the Toxins Release Inventory (TRI) database within a given area code.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class FacilitiesSearchByZip(Choreography):

    """
    Create a new instance of the FacilitiesSearchByZip Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/EnviroFacts/FacilitiesSearchByZip')


    def new_input_set(self):
        return FacilitiesSearchByZipInputSet()

    def _make_result_set(self, result, path):
        return FacilitiesSearchByZipResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return FacilitiesSearchByZipChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the FacilitiesSearchByZip
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class FacilitiesSearchByZipInputSet(InputSet):
        """
        Set the value of the ResponseFormat input for this choreography. ((optional, string) Specify the desired response format. Valid formats are: xml (the default) and csv.)
        """
        def set_ResponseFormat(self, value):
            InputSet._set_input(self, 'ResponseFormat', value)

        """
        Set the value of the RowEnd input for this choreography. ((optional, integer) Number 1 or greater indicates the ending row number of the results displayed. Default is 4999 when RowStart is 0. Up to 5000 entries are returned in the output.)
        """
        def set_RowEnd(self, value):
            InputSet._set_input(self, 'RowEnd', value)

        """
        Set the value of the RowStart input for this choreography. ((optional, integer) Indicates the starting row number of the results displayed. Default is 0.)
        """
        def set_RowStart(self, value):
            InputSet._set_input(self, 'RowStart', value)

        """
        Set the value of the Zip input for this choreography. ((required, string) Zip code to be searched.)
        """
        def set_Zip(self, value):
            InputSet._set_input(self, 'Zip', value)


"""
A ResultSet with methods tailored to the values returned by the FacilitiesSearchByZip choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class FacilitiesSearchByZipResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The response from EnviroFacts.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class FacilitiesSearchByZipChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return FacilitiesSearchByZipResultSet(response, path)
