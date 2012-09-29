# -*- coding: utf-8 -*-

###############################################################################
#
# MQLRead
# Search the Freebase dataset using the Metaweb query language (MQL).
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class MQLRead(Choreography):

    """
    Create a new instance of the MQLRead Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Freebase/MQLRead')


    def new_input_set(self):
        return MQLReadInputSet()

    def _make_result_set(self, result, path):
        return MQLReadResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return MQLReadChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the MQLRead
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class MQLReadInputSet(InputSet):
        """
        Set the value of the APIKey input for this choreography. ((required, string) The API Key provided by Freebase.)
        """
        def set_APIKey(self, value):
            InputSet._set_input(self, 'APIKey', value)

        """
        Set the value of the AsOfTime input for this choreography. ((optional, string) Run a query as it would have run at a specific point in time. Timestamps must be entered in the following format: 2007-01-09T22, or 2007-02.)
        """
        def set_AsOfTime(self, value):
            InputSet._set_input(self, 'AsOfTime', value)

        """
        Set the value of the Cost input for this choreography. ((optional, boolean) If cost is set to true, a key is returned in the results, indicating the computational cost incurred by lower levels of the service. Default value: false)
        """
        def set_Cost(self, value):
            InputSet._set_input(self, 'Cost', value)

        """
        Set the value of the Cursor input for this choreography. ((optional, string) If set. results can be paged.  See examples at: http://wiki.freebase.com/wiki/MQL_Read_Service)
        """
        def set_Cursor(self, value):
            InputSet._set_input(self, 'Cursor', value)

        """
        Set the value of the EscapeHTMLResults input for this choreography. ((optional, boolean) Specify whether html results are to be escaped or not.  Default is set to: true.)
        """
        def set_EscapeHTMLResults(self, value):
            InputSet._set_input(self, 'EscapeHTMLResults', value)

        """
        Set the value of the Indent input for this choreography. ((optional, boolean) Specify whether the JSON results should be indented, or not. Enter true, or false. Default: false. Range of values: 0-10.)
        """
        def set_Indent(self, value):
            InputSet._set_input(self, 'Indent', value)

        """
        Set the value of the Language input for this choreography. ((optional, string) Specify the language in which the searches will be performed.  Multiple languages can be specified. Default is: /lang/en)
        """
        def set_Language(self, value):
            InputSet._set_input(self, 'Language', value)

        """
        Set the value of the Query input for this choreography. ((required, string) Enter a search query  in a valid MQL JSON format.)
        """
        def set_Query(self, value):
            InputSet._set_input(self, 'Query', value)

        """
        Set the value of the UniqenessFailure input for this choreography. ((optional, string) Specify how MQL responds to uniqueness failures. Enter hard, or soft.  Default is set to: hard.)
        """
        def set_UniqenessFailure(self, value):
            InputSet._set_input(self, 'UniqenessFailure', value)


"""
A ResultSet with methods tailored to the values returned by the MQLRead choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class MQLReadResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The response from the Freebase MQL Read API in JSON format.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class MQLReadChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return MQLReadResultSet(response, path)
