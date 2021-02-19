#!/usr/bin/python3
 
import socket
#imports colors for print statements

from termcolor import colored

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.setdefaulttimeout(1)

host = input(str("Enter the host to scan: "))

def portscanner(port):
  if sock.connect_ex((host,port)):
    print (colored("port %d is closed" % port, 'red'))
  else:
    print (colored("port %d is open" % port,'green'))

#for (i = 1; i < 100; 1++)
for i in range(1,100):
  portscanner(i)
