import socket
import sys
import math
import json
import utility
import datetime
import hashlib

myip = utility.get_ip()
myid = myip.split('.')[3]

def sendcmd(id,port,msg):

    exIP = utility.get_ip()
    arr_ex_IP = exIP.split('.')
    # print arr_ex_IP
    IP_ = arr_ex_IP[0] + '.' + arr_ex_IP[1] + '.' + arr_ex_IP[2] + '.' + id

    BC_IP = arr_ex_IP[0] + '.' + arr_ex_IP[1] + '.' + arr_ex_IP[2] + '.255'

    msg['dest'] = IP_
    msg['src'] = exIP
    msg['id'] = utility.id_generator(10)



    print msg

    s = socket.socket(socket.AF_INET,  # Internet
                      socket.SOCK_DGRAM)  # UDP

    for i in range(1,255):

        itr_ip = arr_ex_IP[0] + '.' + arr_ex_IP[1] + '.' + arr_ex_IP[2] + '.'+str(i)
        #print itr_ip
        s.sendto(json.dumps(msg), (itr_ip, port))

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
    cmd['path']=str(myid)

    for ent in on:
        cmd['arg'].append((ent,1))

    for ent in off:
        cmd['arg'].append((ent,0))

    print cmd

    sendcmd(_ID,_PORT,cmd)