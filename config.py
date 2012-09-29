#!/bin/env python
from temboo.core.session import TembooSession

temboo_session = TembooSession(
        "ACCOUNT_NAME",
        "APP_NAME",
        "APP_KEY",
        )

try:
    from local_config import *
except ImportError:
    pass
