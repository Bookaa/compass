# -*- coding: utf-8 -*-

###############################################################################
#
# LookupSchool
# Allows you to search the U.S. Department of Education college and univeristy listings.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class LookupSchool(Choreography):

    """
    Create a new instance of the LookupSchool Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/DeptOfEducation/CollegesAndUniversities/LookupSchool')


    def new_input_set(self):
        return LookupSchoolInputSet()

    def _make_result_set(self, result, path):
        return LookupSchoolResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return LookupSchoolChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the LookupSchool
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class LookupSchoolInputSet(InputSet):
        """
        Set the value of the Keyword input for this choreography. ((optional, string) Used to perform a full text search on the data set. For example, you can search for an institution's name or an institution's ID.)
        """
        def set_Keyword(self, value):
            InputSet._set_input(self, 'Keyword', value)

        """
        Set the value of the MaxRows input for this choreography. ((optional, integer) Limits the number of rows returned. Defaults to 20.)
        """
        def set_MaxRows(self, value):
            InputSet._set_input(self, 'MaxRows', value)

        """
        Set the value of the ResponseFormat input for this choreography. ((optional, string) The format that the response should be in. Valid values are: xml (the default) and json.)
        """
        def set_ResponseFormat(self, value):
            InputSet._set_input(self, 'ResponseFormat', value)


"""
A ResultSet with methods tailored to the values returned by the LookupSchool choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class LookupSchoolResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The response from Data.ed.gov.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class LookupSchoolChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return LookupSchoolResultSet(response, path)
