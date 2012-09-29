# -*- coding: utf-8 -*-

###############################################################################
#
# ListIndustryCodes
# Returns a complete list of all Standard Industrial Classification (SIC) codes and sectors.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class ListIndustryCodes(Choreography):

    """
    Create a new instance of the ListIndustryCodes Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/CorpWatch/Lists/ListIndustryCodes')


    def new_input_set(self):
        return ListIndustryCodesInputSet()

    def _make_result_set(self, result, path):
        return ListIndustryCodesResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ListIndustryCodesChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the ListIndustryCodes
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class ListIndustryCodesInputSet(InputSet):
        """
        Set the value of the APIKey input for this choreography. ((optional, string) The APIKey from CorpWatch if you have one.)
        """
        def set_APIKey(self, value):
            InputSet._set_input(self, 'APIKey', value)

        """
        Set the value of the Index input for this choreography. ((optional, integer) Set the index number of the first result to be returned. The index of the first result is 0.)
        """
        def set_Index(self, value):
            InputSet._set_input(self, 'Index', value)

        """
        Set the value of the Limit input for this choreography. ((optional, integer) The number of results to be returned. Defaults to 100. Maximum is 5000.)
        """
        def set_Limit(self, value):
            InputSet._set_input(self, 'Limit', value)

        """
        Set the value of the ResponseType input for this choreography. ((optional, string) Specify json or xml for the type of response to be returned. Defaults to xml.)
        """
        def set_ResponseType(self, value):
            InputSet._set_input(self, 'ResponseType', value)


"""
A ResultSet with methods tailored to the values returned by the ListIndustryCodes choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class ListIndustryCodesResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The response from CorpWatch.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class ListIndustryCodesChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ListIndustryCodesResultSet(response, path)
