#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import lcdtext

sock = socket.socket()
sock.bind(('', 9090))
sock.listen(2)
#lcd = lcddriver.lcd()

while True:
   conn, addr = sock.accept()
   string=''
   print 'connected:', addr
   c=0
   while True:
       data = conn.recv(2048)
       string+=data
       if not data:
           print "Not connected..."
           break
       #conn.send(data.upper())
   print "Data:",string
#   lcdtext.out(string)
   conn.close()





