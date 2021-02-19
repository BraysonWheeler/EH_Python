#!/usr/bin/python3

from socket import *   #from socket lib import everything

import optparse   #lib allows us to use -h for help

from threading import * 


def connScan(tgthost, tgtport):
    try:
        sock = socket(AF_INET, SOCK_STREAM) #becuase we imported all from socket lib we dont have to specify socket.socket*
        sock.connect((tgthost,tgtport))
        print ("+ %d/tcp Open" % (tgtport))
    except:
        print ("- %d/tcp Closed" % (tgtport))

    finally:
        sock.close()


def portScan(tgthost, tgtports):
    try:
        tgtip = gethostbyname(tgthost)
    except:
        #if it cant resolve name of host
        print ("unknown Host %s" % (tgthost))

    try:
        tgtname = gethostbyaddr(tgtip)
        print ("Scan results for: %s" % (tgtname[0]))
    except:
        print ("Scan results for: %s" % (tgtip))

    setdefaulttimeout(1)
    for tgtport in tgtports:
        t = Thread(target=connScan, args=(tgthost, int(tgtport))) #socket lib needs an int val in port to scan
        t.start()

def main():


    parser = optparse.OptionParser('Usage of program: ' + '-H [target host] -p [target port]')
    parser.add_option('-H', dest='tgthost', type='string', help='specify target host')
    parser.add_option('-p', dest='tgtports', type='string', help='specify target port sep by commma')

    (options, args) = parser.parse_args() #from optparse lib

    tgthost = options.tgthost
    tgtports = str(options.tgtports).split(',') #seperates everything with a comma inbetween

    #if nothing is inputted for both ho and port
    if(tgthost == None) | (tgtports[0] == None):
        print (parser.usage)
        exit(0)

    portScan(tgthost,tgtports)
if __name__== "__main__":
    main()
