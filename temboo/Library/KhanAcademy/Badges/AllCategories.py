# -*- coding: utf-8 -*-

###############################################################################
#
# AllCategories
# Retrieves all the badge categories in Khan Academy.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class AllCategories(Choreography):

    """
    Create a new instance of the AllCategories Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/KhanAcademy/Badges/AllCategories')


    def new_input_set(self):
        return AllCategoriesInputSet()

    def _make_result_set(self, result, path):
        return AllCategoriesResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return AllCategoriesChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the AllCategories
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class AllCategoriesInputSet(InputSet):
    pass

"""
A ResultSet with methods tailored to the values returned by the AllCategories choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class AllCategoriesResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((json) The response from Khan Academy.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class AllCategoriesChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return AllCategoriesResultSet(response, path)
