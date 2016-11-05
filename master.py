import socket
import sys
import math
import json

def sendcmd(id,port,msg):
    IP_ = '127.0.0.'+id

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(10)
    try:
        s.connect((IP_, port))
    except socket.error, errmsg:
        print errmsg
        sys.exit(1)

    s.send(json.dumps(msg))
    data = s.recv(1024)
    s.close()
    print "return :", data

def readfile(path):
    return 0

if __name__ == '__main__':

    if(len(sys.argv)>3):
        if(sys.argv[1]=='file'):
            readfile(sys.argv[2])
            sys.exit(0)

    arg = dict([('port',5050),
                ('id','1'),
                ('message','hi')])

    i=1
    on = []
    off = []
    while i<len(sys.argv):
        try:
            if(sys.argv[i] =='on'):
                i+=1
                while i<len(sys.argv):
                    try:
                        anint = int(sys.argv[i])
                        on.append(anint)
                    except ValueError:
                        break
                    i+=1
            if (sys.argv[i] == 'off'):
                i += 1
                while i<len(sys.argv):
                    try:
                        anint = int(sys.argv[i])
                        off.append(anint)
                    except ValueError:
                        break
                    i+=1
            if(i+1<len(sys.argv)):
                arg[sys.argv[i]] = sys.argv[i+1]
                i+=2
            else:
                break
        except IndexError:
            break

    print on,off

    arg['on'] = on
    arg['off'] = off

    print arg

    _ID = arg['id']
    try:
        _PORT = int(arg['port'])
    except ValueError:
        _PORT = 5050
    _MSG = arg['message']

    cmd = dict()
    cmd['cmd']=0
    cmd['arg']=[]

    for ent in on:
        cmd['arg'].append((ent,1))

    for ent in off:
        cmd['arg'].append((ent,0))

    #print cmd

    sendcmd(_ID,_PORT,cmd)