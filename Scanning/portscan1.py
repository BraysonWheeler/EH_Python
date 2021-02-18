#!/usr/bin/python

# nmap allows scanning target for open ports running vulnerbal software allowing us to exploit them
# this will scan for open ports and later see if software running is vulnerable
# ex of nmap -> nmap [target ip]

import socket #library we want to import

sock = socket.socket_ex(socket.AF_INET, socket.SOCK_STREAM) #AF_INET is for ipv4 and pv6 Sock Stream for tcp packets going for 3 way handshake

host = "192.168.1.52" #target pc
port = 443 #can be any port nnmap -sV [ip] for open ports

#takes in argument port
def portscanner(port):
	if sock.connect((host,port)):
		print "Port %d closed" % (port) #if error
	else:
		print "Port %d is open" % (port) #if success
portscanner(port) #calling the function
