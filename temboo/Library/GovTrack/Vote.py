# -*- coding: utf-8 -*-

###############################################################################
#
# Vote
# Returns roll call votes in the U.S. Congress since 1789.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class Vote(Choreography):

    """
    Create a new instance of the Vote Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/GovTrack/Vote')


    def new_input_set(self):
        return VoteInputSet()

    def _make_result_set(self, result, path):
        return VoteResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return VoteChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the Vote
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class VoteInputSet(InputSet):
        """
        Set the value of the Category input for this choreography. ((optional, string) The type of the vote. See documentation for acceptable inputs.)
        """
        def set_Category(self, value):
            InputSet._set_input(self, 'Category', value)

        """
        Set the value of the Chamber input for this choreography. ((optional, string) The chamber in which the vote was held, house or senate.)
        """
        def set_Chamber(self, value):
            InputSet._set_input(self, 'Chamber', value)

        """
        Set the value of the Congress input for this choreography. ((optional, integer) The number of the congress in which the bill was introduced. The current congress is 112.)
        """
        def set_Congress(self, value):
            InputSet._set_input(self, 'Congress', value)

        """
        Set the value of the Created input for this choreography. ((optional, string) The date (and in recent history also the time) on which the vote was held.)
        """
        def set_Created(self, value):
            InputSet._set_input(self, 'Created', value)

        """
        Set the value of the Limit input for this choreography. ((optional, integer) Results are paged 20 per call by default. Set the limit input to a high value to get all of the results at once.)
        """
        def set_Limit(self, value):
            InputSet._set_input(self, 'Limit', value)

        """
        Set the value of the Number input for this choreography. ((optional, integer) The number of the vote, unique to a Congress and session pair.)
        """
        def set_Number(self, value):
            InputSet._set_input(self, 'Number', value)

        """
        Set the value of the Order input for this choreography. ((optional, string) You can order the results using created (ascending) or -created (descending) for the dates that each vote was held.)
        """
        def set_Order(self, value):
            InputSet._set_input(self, 'Order', value)

        """
        Set the value of the RelatedBill input for this choreography. ((optional, string) A bill related to this vote.)
        """
        def set_RelatedBill(self, value):
            InputSet._set_input(self, 'RelatedBill', value)

        """
        Set the value of the ResponseFormat input for this choreography. ((optional, string) Specify the format of the response. Default is JSON, but XML is also possible.)
        """
        def set_ResponseFormat(self, value):
            InputSet._set_input(self, 'ResponseFormat', value)

        """
        Set the value of the Session input for this choreography. ((optional, integer) Session of congress. For congress = 112 roughly covers the period 2011-2012, so session=2011 and session=2012 can each be specified. In historical data sessions may be named in other ways.)
        """
        def set_Session(self, value):
            InputSet._set_input(self, 'Session', value)

        """
        Set the value of the VoteID input for this choreography. ((optional, integer) Specify the ID of a vote object to retrieve the record for just that object.)
        """
        def set_VoteID(self, value):
            InputSet._set_input(self, 'VoteID', value)


"""
A ResultSet with methods tailored to the values returned by the Vote choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class VoteResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The resopnse from GovTrack.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class VoteChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return VoteResultSet(response, path)
