#!/usr/bin/env python
# -*- coding: utf-8 -*-

import mpd
from time import sleep

def title():
  client = mpd.MPDClient()
  try:
    client.connect("localhost", 6600) # подключаемся к серверу
    s=client.currentsong()
    elapsed=0
    cnt=0
    stat=0

    while True:
      if 'name' in s:
        break
      s=client.currentsong()
      sleep(0.05)
      s1=client.status()
      if s1['elapsed'] ==  elapsed:
	cnt+=1
      else:
	elapsed=s1['elapsed']
      if cnt == 30:
	print "No input"
	stat=1
	break

    if 'name' in s:
	fst=s['name']
    else:
	fst='                '
    if 'title' in s:
	snd=s['title']
    else:
	snd='                '
  except Exception:
	stat=2    
	fst='                '
	snd='                '
	
  return stat,fst,snd
