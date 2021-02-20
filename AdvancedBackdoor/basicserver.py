#!/usr/bin/python3

import socket
import os

#use nc [ip] [port] in other terminal to test connect.

#ipv4 socket running on tcp
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)      #SETTING UP SOCKET
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)   #SOCKET OPTIONS

#port forward if over internet if local network local ip
s.bind(("127.0.0.1",56782))                               #BIND SOCKET TO IP AND A PORT NOT IN USE
s.listen(5)                                               #LISTENS FOR 5 CONNECTIONS
print ("Listening fo Incoming connections")
target, ip = s.accept()                                   #Accpets the connection

print ("Target Connected")
s.close()
