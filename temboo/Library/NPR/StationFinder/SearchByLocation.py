# -*- coding: utf-8 -*-

###############################################################################
#
# SearchByLocation
# Retrieves local NPR member stations near the specified lattitude and longitude location coordinates.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class SearchByLocation(Choreography):

    """
    Create a new instance of the SearchByLocation Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/NPR/StationFinder/SearchByLocation')


    def new_input_set(self):
        return SearchByLocationInputSet()

    def _make_result_set(self, result, path):
        return SearchByLocationResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return SearchByLocationChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the SearchByLocation
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class SearchByLocationInputSet(InputSet):
        """
        Set the value of the APIKey input for this choreography. ((required, string) The API Key provided by NPR.)
        """
        def set_APIKey(self, value):
            InputSet._set_input(self, 'APIKey', value)

        """
        Set the value of the Lattitude input for this choreography. ((required, decimal) The lattitude point of a station's location. Must be used together with the longitude parameter. This must be a positive value.)
        """
        def set_Lattitude(self, value):
            InputSet._set_input(self, 'Lattitude', value)

        """
        Set the value of the Longitude input for this choreography. ((required, decimal) The longitude point of a station's location. Must be used together with the lattitude parameter. This must be a positive value.)
        """
        def set_Longitude(self, value):
            InputSet._set_input(self, 'Longitude', value)


"""
A ResultSet with methods tailored to the values returned by the SearchByLocation choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class SearchByLocationResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) )
        """
        def get_Response(self):
            return self._output.get('Response', None)

class SearchByLocationChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return SearchByLocationResultSet(response, path)
