# -*- coding: utf-8 -*-

###############################################################################
#
# Role
# Returns terms held in office by Members of Congress and U.S. Presidents.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class Role(Choreography):

    """
    Create a new instance of the Role Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/GovTrack/Role')


    def new_input_set(self):
        return RoleInputSet()

    def _make_result_set(self, result, path):
        return RoleResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return RoleChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the Role
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class RoleInputSet(InputSet):
        """
        Set the value of the Current input for this choreography. ((optional, string) Whether the role is currently held, or it is archival information.)
        """
        def set_Current(self, value):
            InputSet._set_input(self, 'Current', value)

        """
        Set the value of the District input for this choreography. ((optional, string) For representatives, the number of their congressional district. 0 for at-large districts, -1 in historical data if the district is not known.)
        """
        def set_District(self, value):
            InputSet._set_input(self, 'District', value)

        """
        Set the value of the EndDate input for this choreography. ((optional, string) The date the role ended - when the person resigned, died, etc. (in YYYY-MM-DD format).)
        """
        def set_EndDate(self, value):
            InputSet._set_input(self, 'EndDate', value)

        """
        Set the value of the Limit input for this choreography. ((optional, integer) Results are paged 20 per call by default. Set the limit input to a high value to get all of the results at once.)
        """
        def set_Limit(self, value):
            InputSet._set_input(self, 'Limit', value)

        """
        Set the value of the Order input for this choreography. ((optional, string) You can order the results by date using fieldname (ascending) or -fieldname (descending), where "fieldname" is either startdate or enddate.)
        """
        def set_Order(self, value):
            InputSet._set_input(self, 'Order', value)

        """
        Set the value of the Party input for this choreography. ((optional, string) The political party of the person. If the person changes party, it is usually the most recent party during this role.)
        """
        def set_Party(self, value):
            InputSet._set_input(self, 'Party', value)

        """
        Set the value of the ResponseFormat input for this choreography. ((optional, string) Specify the format of the response. Default is JSON, but XML is also possible.)
        """
        def set_ResponseFormat(self, value):
            InputSet._set_input(self, 'ResponseFormat', value)

        """
        Set the value of the RoleID input for this choreography. ((optional, integer) Specify the ID number of a role object to retrieve the record for only that role.)
        """
        def set_RoleID(self, value):
            InputSet._set_input(self, 'RoleID', value)

        """
        Set the value of the RoleType input for this choreography. ((optional, string) Acceptable values: senator, representative, or president.)
        """
        def set_RoleType(self, value):
            InputSet._set_input(self, 'RoleType', value)

        """
        Set the value of the SenatorClass input for this choreography. ((optional, integer) For senators, their election class, which determines which years they are up for election. Acceptable values: class1, class2, class3.)
        """
        def set_SenatorClass(self, value):
            InputSet._set_input(self, 'SenatorClass', value)

        """
        Set the value of the StartDate input for this choreography. ((optional, string) The date the role began  - when the person took office (in YYYY-MM-DD format).)
        """
        def set_StartDate(self, value):
            InputSet._set_input(self, 'StartDate', value)

        """
        Set the value of the State input for this choreography. ((optional, integer) For senators and representatives, the two-letter USPS abbreviation for the state or territory they are serving. See documentation for more on territories and historical data.)
        """
        def set_State(self, value):
            InputSet._set_input(self, 'State', value)


"""
A ResultSet with methods tailored to the values returned by the Role choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class RoleResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The resopnse from GovTrack.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class RoleChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return RoleResultSet(response, path)
