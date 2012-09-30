#!/bin/env python
from temboo.core.session import TembooSession

temboo_session = TembooSession(
        "ACCOUNT_NAME",
        "APP_NAME",
        "APP_KEY",
        )

FOURSQUARE_CLIENT_ID = ''
FOURSQUARE_CLIENT_SECRET = ''

try:
    from local_config import *
except ImportError:
    pass
