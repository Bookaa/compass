# -*- coding: utf-8 -*-

###############################################################################
#
# Image
# Generates a thumbnail for an image from the content database to the requested size. 
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class Image(Choreography):

    """
    Create a new instance of the Image Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Freebase/Image')


    def new_input_set(self):
        return ImageInputSet()

    def _make_result_set(self, result, path):
        return ImageResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ImageChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the Image
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class ImageInputSet(InputSet):
        """
        Set the value of the APIKey input for this choreography. ((required, string) The API Key provided by Freebase.)
        """
        def set_APIKey(self, value):
            InputSet._set_input(self, 'APIKey', value)

        """
        Set the value of the FallbackID input for this choreography. ((optional, string) Use this second (fallback) image ID, if the primary ID is not available.)
        """
        def set_FallbackID(self, value):
            InputSet._set_input(self, 'FallbackID', value)

        """
        Set the value of the ID input for this choreography. ((required, string) Enter the ID of the entity for which description information will be retrieved. IDs and MIDs can be obtained by running the Search Choreo in this bundle. Example input: /en/bob_dylan)
        """
        def set_ID(self, value):
            InputSet._set_input(self, 'ID', value)

        """
        Set the value of the MaximumHeight input for this choreography. ((optional, integer) Enter the desired maximum image height in pixels. Integers must be in the following range: (0 --> 4,096))
        """
        def set_MaximumHeight(self, value):
            InputSet._set_input(self, 'MaximumHeight', value)

        """
        Set the value of the MaximumWidth input for this choreography. ((optional, integer) Enter the desired maximum image width in pixels. Integers must be in the following range: (0 --> 4,096))
        """
        def set_MaximumWidth(self, value):
            InputSet._set_input(self, 'MaximumWidth', value)

        """
        Set the value of the Mode input for this choreography. ((optional, string) Specify the method used to crop or scale images.  Available methods include: fill, fillcrop, fillcropmid, fit.)
        """
        def set_Mode(self, value):
            InputSet._set_input(self, 'Mode', value)

        """
        Set the value of the Pad input for this choreography. ((optional, boolean) Enter 0, or 1 to specify whether the provided image should be padded to the requested dimensions.)
        """
        def set_Pad(self, value):
            InputSet._set_input(self, 'Pad', value)


"""
A ResultSet with methods tailored to the values returned by the Image choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class ImageResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((string) The response from the Freebase Image API returns the thumbnail in base 64-encoded  format.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class ImageChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ImageResultSet(response, path)
