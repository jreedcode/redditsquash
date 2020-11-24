#!/usr/bin/python

import time
import urllib2

base_url = 'https://psaworldtour.com/players/view/%s'

for player_id in range(0, 9999):
  req = urllib2.Request(base_url % player_id)
  try:
    resp = urllib2.urlopen(req)
  except urllib2.HTTPError as e:
    if e.code == 404:
      print 'player %d not found' % player_id
  except urllib2.URLError as e:
    print 'got error %s' % str(e)
  else:
    # 200
    body = resp.read()
    with open('players/%s' % player_id, 'wb') as player_file:
      player_file.write(str(body))

  time.sleep(1)
  print player_id
