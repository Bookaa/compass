# -*- coding: utf-8 -*-

###############################################################################
#
# GeoPoint
# Associates a Geo point with an existing object.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class GeoPoint(Choreography):

    """
    Create a new instance of the GeoPoint Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Parse/GeoPoints/GeoPoint')


    def new_input_set(self):
        return GeoPointInputSet()

    def _make_result_set(self, result, path):
        return GeoPointResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GeoPointChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the GeoPoint
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class GeoPointInputSet(InputSet):
        """
        Set the value of the ApplicationID input for this choreography. ((required, string) The Application ID provided by Parse.)
        """
        def set_ApplicationID(self, value):
            InputSet._set_input(self, 'ApplicationID', value)

        """
        Set the value of the ClassName input for this choreography. ((required, string) The class name for the object being created.)
        """
        def set_ClassName(self, value):
            InputSet._set_input(self, 'ClassName', value)

        """
        Set the value of the Latitude input for this choreography. ((required, decimal) The latitude coordinate of the Geo Point.)
        """
        def set_Latitude(self, value):
            InputSet._set_input(self, 'Latitude', value)

        """
        Set the value of the Longitude input for this choreography. ((required, decimal) The longitude coordinate of the Geo Point.)
        """
        def set_Longitude(self, value):
            InputSet._set_input(self, 'Longitude', value)

        """
        Set the value of the RESTAPIKey input for this choreography. ((required, string) The REST API Key provided by Parse.)
        """
        def set_RESTAPIKey(self, value):
            InputSet._set_input(self, 'RESTAPIKey', value)


"""
A ResultSet with methods tailored to the values returned by the GeoPoint choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class GeoPointResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((json) The response from Parse.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class GeoPointChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GeoPointResultSet(response, path)
