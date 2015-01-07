#!/usr/bin/python
# -*- coding: utf-8 -*-


import mpd
from time import sleep

client = mpd.MPDClient()

client.connect("localhost", 6600) # подключаемся к серверу

#s=client.commands() # выводим список доступных команд
#print s
client.clear()
client.load('radio')
print "Load default playlist: Radio"
s=client.status()
print s
client.stop()
client.play()
c=1
while True:
    s=client.currentsong()
    print c,s
    s=client.status()
    print s

    sleep(0.1)
    c+=1