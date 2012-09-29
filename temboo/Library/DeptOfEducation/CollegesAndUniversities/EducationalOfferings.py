# -*- coding: utf-8 -*-

###############################################################################
#
# EducationalOfferings
# Returns educational offerings and admissions data for any college or university.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class EducationalOfferings(Choreography):

    """
    Create a new instance of the EducationalOfferings Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/DeptOfEducation/CollegesAndUniversities/EducationalOfferings')


    def new_input_set(self):
        return EducationalOfferingsInputSet()

    def _make_result_set(self, result, path):
        return EducationalOfferingsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return EducationalOfferingsChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the EducationalOfferings
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class EducationalOfferingsInputSet(InputSet):
        """
        Set the value of the InstitutionID input for this choreography. ((optional, string) Specify an institutionID to return data on a specific institution. These ids can be retrieved from the LookupSchool Choreo.)
        """
        def set_InstitutionID(self, value):
            InputSet._set_input(self, 'InstitutionID', value)

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
A ResultSet with methods tailored to the values returned by the EducationalOfferings choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class EducationalOfferingsResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The response from Data.ed.gov.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class EducationalOfferingsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return EducationalOfferingsResultSet(response, path)
