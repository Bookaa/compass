# -*- coding: utf-8 -*-

###############################################################################
#
# LookupMajors
# Allows you to search for majors by id or keyword.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class LookupMajors(Choreography):

    """
    Create a new instance of the LookupMajors Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/DeptOfEducation/CollegesAndUniversities/LookupMajors')


    def new_input_set(self):
        return LookupMajorsInputSet()

    def _make_result_set(self, result, path):
        return LookupMajorsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return LookupMajorsChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the LookupMajors
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class LookupMajorsInputSet(InputSet):
        """
        Set the value of the Keyword input for this choreography. ((conditional, string) A keyword search term to lookup majors (i.e. Agriculture).)
        """
        def set_Keyword(self, value):
            InputSet._set_input(self, 'Keyword', value)

        """
        Set the value of the MajorID input for this choreography. ((conditional, decimal) The unique id associated with a major to return (i.e. 01.0000). Note that these ids are also returned in the output of the DegreesConferred Choreo.)
        """
        def set_MajorID(self, value):
            InputSet._set_input(self, 'MajorID', value)

        """
        Set the value of the ResponseFormat input for this choreography. ((optional, string) The format that the response should be in. Valid values are: xml (the default) and json.)
        """
        def set_ResponseFormat(self, value):
            InputSet._set_input(self, 'ResponseFormat', value)


"""
A ResultSet with methods tailored to the values returned by the LookupMajors choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class LookupMajorsResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The results from the search in XML or JSON format.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class LookupMajorsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return LookupMajorsResultSet(response, path)
