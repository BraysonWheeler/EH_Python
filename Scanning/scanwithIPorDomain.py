import socket
from IPy import IP
def check_function():
    print('Scan:\n1.IP\n2.Domain')
    hello = input('enter:')
    if(hello == '1'):
        scanwithip()
    else:
        convert_ip = check_ip()
        print(convert_ip)
        for port in range(1,443):
            scan_port(convert_ip, port)

def scanwithip():
    ip = input('Enter IP to scan ')
    for port in range(1, 443):
        scan_port(ip, port)
def check_ip():
    ip = input('Enter domain to scan ')
    try:
        IP(ip)
        return(ip)
    except ValueError:
        return socket.gethostbyname(ip)

def scan_port(ip, port):
    try:
        sock = socket.socket()
        sock.settimeout(0.5)
        sock.connect((ip, port))
        print('[+] Port' + str(port) + 'is open')
    except:
        pass
        ##print('[-] Port' + str(port) + 'is closed')

check_function()

