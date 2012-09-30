#!/usr/bin/env python

import foursquare
import json
from config import *

def connect():
    return foursquare.Foursquare(access_token=FOURSQUARE_OAUTH_KEY)

if __name__ == '__main__':
    client = foursquare.Foursquare(client_id=FOURSQUARE_CLIENT_ID,
            client_secret=FOURSQUARE_CLIENT_SECRET,
            redirect_uri='http://www.httpdump.com/')
    print('Authenticate at ' + client.oauth.auth_url())
    #client = foursquare.Foursquare(access_token=FOURSQUARE_OAUTH_KEY)
    
