# -*- coding: utf-8 -*-

###############################################################################
#
# FindByCoordinates
# Retrieves complete location information from a specified pair of lattitude and longitude coordinates.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class FindByCoordinates(Choreography):

    """
    Create a new instance of the FindByCoordinates Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Yahoo/PlaceFinder/FindByCoordinates')


    def new_input_set(self):
        return FindByCoordinatesInputSet()

    def _make_result_set(self, result, path):
        return FindByCoordinatesResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return FindByCoordinatesChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the FindByCoordinates
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class FindByCoordinatesInputSet(InputSet):
        """
        Set the value of the AppID input for this choreography. ((required, string) The App ID provided by Yahoo!)
        """
        def set_AppID(self, value):
            InputSet._set_input(self, 'AppID', value)

        """
        Set the value of the Lattitude input for this choreography. ((required, decimal) The lattitude coordinate of the location you want to find.)
        """
        def set_Lattitude(self, value):
            InputSet._set_input(self, 'Lattitude', value)

        """
        Set the value of the Longitude input for this choreography. ((required, decimal) The longitude coordinate of the location you want to find.)
        """
        def set_Longitude(self, value):
            InputSet._set_input(self, 'Longitude', value)

        """
        Set the value of the ResponseFormat input for this choreography. ((optional, any) You can specify json to get this output format in JSON. Otherwise, the default output will be in XML.)
        """
        def set_ResponseFormat(self, value):
            InputSet._set_input(self, 'ResponseFormat', value)


"""
A ResultSet with methods tailored to the values returned by the FindByCoordinates choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class FindByCoordinatesResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response from Yahoo! PlaceFinder.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class FindByCoordinatesChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return FindByCoordinatesResultSet(response, path)
