# -*- coding: utf-8 -*-

###############################################################################
#
# VoteAndVoter
# Retrieves how people voted on roll call votes in the U.S. Congress since 1789. 
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class VoteAndVoter(Choreography):

    """
    Create a new instance of the VoteAndVoter Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/GovTrack/VoteAndVoter')


    def new_input_set(self):
        return VoteAndVoterInputSet()

    def _make_result_set(self, result, path):
        return VoteAndVoterResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return VoteAndVoterChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the VoteAndVoter
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class VoteAndVoterInputSet(InputSet):
        """
        Set the value of the Created input for this choreography. ((optional, string) The date (and in recent history also the time) on which the vote was held (in YYYY-MM-DD format).)
        """
        def set_Created(self, value):
            InputSet._set_input(self, 'Created', value)

        """
        Set the value of the Limit input for this choreography. ((optional, integer) Results are paged 20 per call by default. Set the limit input to a high value to get all of the results at once.)
        """
        def set_Limit(self, value):
            InputSet._set_input(self, 'Limit', value)

        """
        Set the value of the ObjectID input for this choreography. ((optional, integer) Specify the ID of a vote object to retrieve just that object's record.)
        """
        def set_ObjectID(self, value):
            InputSet._set_input(self, 'ObjectID', value)

        """
        Set the value of the Option input for this choreography. ((optional, string) The way a particular person voted. The value corresponds to the key of an option returned on the Vote Choreo. See documentation for details.)
        """
        def set_Option(self, value):
            InputSet._set_input(self, 'Option', value)

        """
        Set the value of the Order input for this choreography. ((optional, string) You can order the results by date using fieldname (ascending) or -fieldname (descending), where "fieldname" is either startdate or enddate.)
        """
        def set_Order(self, value):
            InputSet._set_input(self, 'Order', value)

        """
        Set the value of the Person input for this choreography. ((optional, integer) The person making this vote. This is an ID number.)
        """
        def set_Person(self, value):
            InputSet._set_input(self, 'Person', value)

        """
        Set the value of the ResponseFormat input for this choreography. ((optional, string) Specify the format of the response. Default is JSON, but XML is also possible.)
        """
        def set_ResponseFormat(self, value):
            InputSet._set_input(self, 'ResponseFormat', value)

        """
        Set the value of the Vote input for this choreography. ((optional, string) The ID number of the vote that this was part of. This is in the form of an ID number.)
        """
        def set_Vote(self, value):
            InputSet._set_input(self, 'Vote', value)


"""
A ResultSet with methods tailored to the values returned by the VoteAndVoter choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class VoteAndVoterResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The resopnse from GovTrack.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class VoteAndVoterChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return VoteAndVoterResultSet(response, path)
