#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import datetime
from time import sleep

#print time
sock = socket.socket()
sock.connect(('localhost', 9090))

while True:
    now_time = datetime.datetime.now()
    time=now_time.strftime("%M:%S")
    sock.send('603'+time)
#    data = sock.recv(1024)
    print time
    sleep(0.1)
sock.close()

#print data
