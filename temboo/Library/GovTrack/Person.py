# -*- coding: utf-8 -*-

###############################################################################
#
# Person
# Returns members of Congress and U.S. Presidents since the founding of the nation.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class Person(Choreography):

    """
    Create a new instance of the Person Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/GovTrack/Person')


    def new_input_set(self):
        return PersonInputSet()

    def _make_result_set(self, result, path):
        return PersonResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return PersonChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the Person
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class PersonInputSet(InputSet):
        """
        Set the value of the FirstName input for this choreography. ((optional, string) First name of the representative to find.)
        """
        def set_FirstName(self, value):
            InputSet._set_input(self, 'FirstName', value)

        """
        Set the value of the Gender input for this choreography. ((optional, string) The person's gender (male or female). For historical data, gender is sometimes not specified.)
        """
        def set_Gender(self, value):
            InputSet._set_input(self, 'Gender', value)

        """
        Set the value of the LastName input for this choreography. ((optional, string) The representative's last name.)
        """
        def set_LastName(self, value):
            InputSet._set_input(self, 'LastName', value)

        """
        Set the value of the Limit input for this choreography. ((optional, integer) Results are paged 20 per call by default. Set the limit input to a high value to get all of the results at once.)
        """
        def set_Limit(self, value):
            InputSet._set_input(self, 'Limit', value)

        """
        Set the value of the MetaVidID input for this choreography. ((optional, string) The person's ID on metavid.org.)
        """
        def set_MetaVidID(self, value):
            InputSet._set_input(self, 'MetaVidID', value)

        """
        Set the value of the MiddleName input for this choreography. ((optional, string) The representative's middle name.)
        """
        def set_MiddleName(self, value):
            InputSet._set_input(self, 'MiddleName', value)

        """
        Set the value of the NameMod input for this choreography. ((optional, string) The suffix of the person's name, ususally one of Jr., Sr., I, II, etc.)
        """
        def set_NameMod(self, value):
            InputSet._set_input(self, 'NameMod', value)

        """
        Set the value of the OSID input for this choreography. ((optional, integer) The person's ID on opensecrets.org (The Center for Responsive Politics).)
        """
        def set_OSID(self, value):
            InputSet._set_input(self, 'OSID', value)

        """
        Set the value of the PVSID input for this choreography. ((optional, integer) The person's ID on vote-smart.org (Project Vote Smart).)
        """
        def set_PVSID(self, value):
            InputSet._set_input(self, 'PVSID', value)

        """
        Set the value of the PersonID input for this choreography. ((optional, integer) Specify the ID number for a person to retrieve only that person.)
        """
        def set_PersonID(self, value):
            InputSet._set_input(self, 'PersonID', value)

        """
        Set the value of the ResponseFormat input for this choreography. ((optional, string) Specify the format of the response. Default is JSON, but XML is also possible.)
        """
        def set_ResponseFormat(self, value):
            InputSet._set_input(self, 'ResponseFormat', value)

        """
        Set the value of the Roles input for this choreography. ((optional, string) ID number of a term in Congress or as President that this person has been elected to.)
        """
        def set_Roles(self, value):
            InputSet._set_input(self, 'Roles', value)

        """
        Set the value of the TwitterID input for this choreography. ((optional, string) Official Twitter handle of the representative.)
        """
        def set_TwitterID(self, value):
            InputSet._set_input(self, 'TwitterID', value)

        """
        Set the value of the YoutubeID input for this choreography. ((optional, string) The name of the person't official YouTube channel.)
        """
        def set_YoutubeID(self, value):
            InputSet._set_input(self, 'YoutubeID', value)


"""
A ResultSet with methods tailored to the values returned by the Person choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class PersonResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The resopnse from GovTrack.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class PersonChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return PersonResultSet(response, path)
