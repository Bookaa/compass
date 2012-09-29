# -*- coding: utf-8 -*-

###############################################################################
#
# DescribeSnapshots
# Returns information on available Amazon EBS snapshots.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class DescribeSnapshots(Choreography):

    """
    Create a new instance of the DescribeSnapshots Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Amazon/EC2/DescribeSnapshots')


    def new_input_set(self):
        return DescribeSnapshotsInputSet()

    def _make_result_set(self, result, path):
        return DescribeSnapshotsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return DescribeSnapshotsChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the DescribeSnapshots
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class DescribeSnapshotsInputSet(InputSet):
        """
        Set the value of the AWSAccessKeyId input for this choreography. ((required, string) The Access Key ID provided by Amazon Web Services.)
        """
        def set_AWSAccessKeyId(self, value):
            InputSet._set_input(self, 'AWSAccessKeyId', value)

        """
        Set the value of the AWSSecretKeyId input for this choreography. ((required, string) The Secret Key ID provided by Amazon Web Services.)
        """
        def set_AWSSecretKeyId(self, value):
            InputSet._set_input(self, 'AWSSecretKeyId', value)

        """
        Set the value of the SnapshotId input for this choreography. ((optional, string) The ID of the snapshot you want to retrieve. Returns all snapshots if not specified.)
        """
        def set_SnapshotId(self, value):
            InputSet._set_input(self, 'SnapshotId', value)


"""
A ResultSet with methods tailored to the values returned by the DescribeSnapshots choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class DescribeSnapshotsResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response from Amazon.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class DescribeSnapshotsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return DescribeSnapshotsResultSet(response, path)
