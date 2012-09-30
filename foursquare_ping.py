#!/usr/bin/env

import time
import foursquare_authenticate

client = foursquare_authenticate.connect()
lastupdate = 0

def ping():
    def parse(checkin):
        lat = checkin['venue']['location']['lat']
        lng = checkin['venue']['location']['lng']
        return ('foursquare', (lat, lng))
    global lastupdate
    all_recent = client.checkins.recent()['recent']
    since_last = [c for c in all_recent if c['createdAt'] > lastupdate]
    lastupdate = all_recent[0]['createdAt']
    return [parse(s) for s in since_last]

if __name__ == '__main__':
    while True:
        recent = ping()
        for event in recent:
            print event
        time.sleep(1)

