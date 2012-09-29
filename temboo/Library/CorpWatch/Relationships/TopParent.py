# -*- coding: utf-8 -*-

###############################################################################
#
# TopParent
# For a given ID of the highest-level owning parent of a family of corporations, retrieves all of the companies that are "below" it in the hierarchy.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class TopParent(Choreography):

    """
    Create a new instance of the TopParent Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/CorpWatch/Relationships/TopParent')


    def new_input_set(self):
        return TopParentInputSet()

    def _make_result_set(self, result, path):
        return TopParentResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return TopParentChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the TopParent
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class TopParentInputSet(InputSet):
        """
        Set the value of the APIKey input for this choreography. ((optional, string) The APIKey from CorpWatch if you have one.)
        """
        def set_APIKey(self, value):
            InputSet._set_input(self, 'APIKey', value)

        """
        Set the value of the CWID input for this choreography. ((required, string) The CWID of the highest-level owning parent of a family of corprorations (or Top Parent). Most company records contain a field for top_parent_id.)
        """
        def set_CWID(self, value):
            InputSet._set_input(self, 'CWID', value)

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
        Set the value of the Year input for this choreography. ((optional, integer) If a year is specified, only subsidiaries for that year will be returned and the data in the company objects returned will be set appropriately for the request year. Defaults to most recent.)
        """
        def set_Year(self, value):
            InputSet._set_input(self, 'Year', value)


"""
A ResultSet with methods tailored to the values returned by the TopParent choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class TopParentResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The response from CorpWatch.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class TopParentChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return TopParentResultSet(response, path)
