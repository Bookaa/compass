# -*- coding: utf-8 -*-

###############################################################################
#
# CreateEvent
# Creates a new event.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class CreateEvent(Choreography):

    """
    Create a new instance of the CreateEvent Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/OneLogin/Events/CreateEvent')


    def new_input_set(self):
        return CreateEventInputSet()

    def _make_result_set(self, result, path):
        return CreateEventResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CreateEventChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the CreateEvent
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class CreateEventInputSet(InputSet):
        """
        Set the value of the APIKey input for this choreography. ((required, string) The API Key provided by OneLogin.)
        """
        def set_APIKey(self, value):
            InputSet._set_input(self, 'APIKey', value)

        """
        Set the value of the EventTypeID input for this choreography. ((required, integer) The id for the type of event you want to create. Note that depending on the event type id specified, you may need to provide the ObjectName and ObjectID that is being affected.)
        """
        def set_EventTypeID(self, value):
            InputSet._set_input(self, 'EventTypeID', value)

        """
        Set the value of the ObjectID input for this choreography. ((conditional, integer) The object id that is being affected. Required for certain event types. When specified, ObjectName must also be provided.)
        """
        def set_ObjectID(self, value):
            InputSet._set_input(self, 'ObjectID', value)

        """
        Set the value of the ObjectName input for this choreography. ((conditional, string) The object name that is being affected (i.e. user-id). Required for certain event types. When specified, ObjectID must also be provided.)
        """
        def set_ObjectName(self, value):
            InputSet._set_input(self, 'ObjectName', value)


"""
A ResultSet with methods tailored to the values returned by the CreateEvent choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class CreateEventResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response from OneLogin.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class CreateEventChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return CreateEventResultSet(response, path)
