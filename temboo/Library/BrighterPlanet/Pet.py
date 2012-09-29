# -*- coding: utf-8 -*-

###############################################################################
#
# Pet
# Returns lifecycle food production and veterinary care emissions modeling for domestic animals.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class Pet(Choreography):

    """
    Create a new instance of the Pet Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/BrighterPlanet/Pet')


    def new_input_set(self):
        return PetInputSet()

    def _make_result_set(self, result, path):
        return PetResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return PetChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the Pet
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class PetInputSet(InputSet):
        """
        Set the value of the APIKey input for this choreography. ((required, string) The API Key provided by Brighter Planet.)
        """
        def set_APIKey(self, value):
            InputSet._set_input(self, 'APIKey', value)

        """
        Set the value of the Acquisition input for this choreography. ((optional, string) Enter date the pet was acquired.)
        """
        def set_Acquisition(self, value):
            InputSet._set_input(self, 'Acquisition', value)

        """
        Set the value of the Breed input for this choreography. ((optional, string) Enter a cat, dog, or horse breed.)
        """
        def set_Breed(self, value):
            InputSet._set_input(self, 'Breed', value)

        """
        Set the value of the Gender input for this choreography. ((optional, string) Enter cat, dog, or horse gender.)
        """
        def set_Gender(self, value):
            InputSet._set_input(self, 'Gender', value)

        """
        Set the value of the ResponseFormat input for this choreography. ((optional, string) Specify your desired response format. Accepted values are xml and json (the default).)
        """
        def set_ResponseFormat(self, value):
            InputSet._set_input(self, 'ResponseFormat', value)

        """
        Set the value of the Retirement input for this choreography. ((optional, string) Enter date you no longer have the pet.)
        """
        def set_Retirement(self, value):
            InputSet._set_input(self, 'Retirement', value)

        """
        Set the value of the Species input for this choreography. ((optional, string) Enter the species type (e.g. bird, cat, dog, ferret, fish).)
        """
        def set_Species(self, value):
            InputSet._set_input(self, 'Species', value)

        """
        Set the value of the Weight input for this choreography. ((optional, decimal) Enter pet weight in kilograms.)
        """
        def set_Weight(self, value):
            InputSet._set_input(self, 'Weight', value)


"""
A ResultSet with methods tailored to the values returned by the Pet choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class PetResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The response from Brighter Planet.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class PetChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return PetResultSet(response, path)
