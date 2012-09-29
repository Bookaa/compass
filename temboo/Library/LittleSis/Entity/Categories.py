# -*- coding: utf-8 -*-

###############################################################################
#
# Categories
# Retrieves a list of all the Relationships possible among people and organizations in LittleSis.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class Categories(Choreography):

    """
    Create a new instance of the Categories Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/LittleSis/Entity/Categories')


    def new_input_set(self):
        return CategoriesInputSet()

    def _make_result_set(self, result, path):
        return CategoriesResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CategoriesChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the Categories
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class CategoriesInputSet(InputSet):
        """
        Set the value of the ResponseFormat input for this choreography. ((optional, string) The format of the response from LittleSis.org. Acceptable inputs: xml or json. Defautls to xml.)
        """
        def set_ResponseFormat(self, value):
            InputSet._set_input(self, 'ResponseFormat', value)


"""
A ResultSet with methods tailored to the values returned by the Categories choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class CategoriesResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The response from LittleSis.org.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class CategoriesChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return CategoriesResultSet(response, path)
