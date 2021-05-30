import socket
from IPy import IP
def scan(target):
    print('\n' + 'Scanning Target' + str(target))
    for port in range(1, 443):
        scan_port(target, port)

def check_function():
    print('Scan:\n1.IP\n2.Domain \n3.Both')
    hello = input('enter:')
    if(hello == '1'):
        scanwithip()
    elif(hello == '2'):
        convert_ip = check_ip()
        print(convert_ip)
        for port in range(1,443):
            scan_port(convert_ip, port)
    elif(hello == '3'):
        targets = input('Enter IP/s to scan (split multiple targets with ,): ')
        for ip_add in targets.split(','): #splits string at every instance of comma
            try:
                IP(ip_add)
                print('[!]Scanning ' + ip_add + ':')
                for port in range(1, 443):
                    scan_port(ip_add, port)

            except:
                ip_ret = socket.gethostbyname(ip_add)
                print('[!]Scanning ' + ip_add + ':')
                for port in range(1, 443):
                    scan_port(ip_ret, port)

    else:
        pass


def scanwithip():
    targets = input('Enter IP/s to scan (split multiple targets with ,): ')
    if ',' in targets:
        for ip_add in targets.split(','): #splits string at every instance of comma
            scan(ip_add.strip(' '))
    else:
        for port in range(1, 443):
            scan_port(targets, port)


def check_ip():
    ip = input('Enter domain to scan ')
    try:
        IP(ip)
        return(ip)
    except ValueError:
        return socket.gethostbyname(ip)
def get_banner(s):
    return s.recv(1024)

def scan_port(ip, port):
    try:
        sock = socket.socket()
        sock.settimeout(0.5) #dont need as scan is a Virtual Machine
        sock.connect((ip, port))
        #Grabbing banner
        try:
            banner = get_banner(sock)
            print('[+] Open Port ' + str(port) + ' : ' + str(banner.decode().strip('\n')))
        except:
            print('[+] Open Port ' + str(port))
    except:
        pass
        ##print('[-] Port' + str(port) + 'is closed')

check_function()

