#!/usr/bin/python3

import socket

def retBanner(ip,port):
    try:
        socket.setdefaulttimeout(2)
        sock = socket.socket()
        sock.connect((ip,port))
        i = sock.recv(1024) #recieving 1024 bytes. Hope somewhere in there is the porti
        return i
    except:
        #if it doesnt work
        print("error")
        return

def main():
    ip = input(str("Enter target ip: "))
    for port in range(1,100):
        banner = retBanner(ip,port)
        if banner:
            print ("%s/%d : %s" % (ip,port,banner))
            #This result allows you to search for exploits for it.
main()
