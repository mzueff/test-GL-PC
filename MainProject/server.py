#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import sys
import lcdtext
import lcddriver
from Queue import Queue
from time import sleep
from thread import *
q = Queue()

lcd = lcddriver.lcd()
HOST = ''   # Symbolic name meaning all available interfaces
PORT = 9090 # Arbitrary non-privileged port
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print 'Socket created'
 
#Bind socket to local host and port
try:
    s.bind((HOST, PORT))
except socket.error , msg:
    print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    sys.exit()
     
print 'Socket bind complete'
 
#Start listening on socket
s.listen(10)
print 'Socket now listening'
 
#Function for handling connections. This will be used to create threads
def out(data):
	#conn.sendall(reply)
	print "Data:",data
	string=lcdtext.out(data)
	lcd.lcd_display_string(string[0], string[1])
#	sleep(2)

def clientthread(conn):
    #Sending message to connected client
    conn.send('Welcome to the server. Type something and hit enter\n') #send only takes string
     
    #infinite loop so that function do not terminate and thread do not end.
    while True:
         
        #Receiving from client
        data = conn.recv(1024)
        #reply = 'OK...' + data
        if not data:
            break
	q.put(data)
	out(data)
    #came out of loop
    conn.close()
 
#now keep talking with the client


while 1:

    #wait to accept a connection - blocking call
    conn, addr = s.accept()
    print 'Next Connected with ' + addr[0] + ':' + str(addr[1])
 
    #start new thread takes 1st argument as a function name to be run, second is the tuple of arguments to the function.
    start_new_thread(clientthread ,(conn,))
 
s.close()