import socket
import json
import portcontrol
import utility
import sys
import os
import datetime

memid = dict()
myip = utility.get_ip()
myid = myip.split('.')[3]

def clear_memid(min=60):
    return 0

def set_bit():
    return 0

def runcmd(cmd):
    if cmd['cmd']==0:
        portcontrol.setbylist(cmd['arg'])

def forward(cmd):

    p_ip = cmd['dest'].split('.')
    cmd['path']+=', '+myid
    clear_memid(60)
    memid[cmd['id']]=datetime.datetime.now()
    s = socket.socket(socket.AF_INET,  # Internet
        socket.SOCK_DGRAM)  # UDP

    for i in range(1, 255):
        i!=myid
        itr_ip = p_ip[0] + '.' + p_ip[1] + '.' + p_ip[2] + '.' + str(i)
        # print itr_ip
        s.sendto(json.dumps(cmd), (itr_ip, 5050))

    return 0

if __name__ == '__main__':

    _IP = utility.get_ip()
    _PORT = 5050

    s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    s.getsockopt(socket.SOL_SOCKET,socket.SO_REUSEPORT,1)
    s.getsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    s.bind((_IP,_PORT))

    print 'blind',_IP

    #s.listen(5)

    while 1:
        data,addr = s.recvfrom(1014)
        #print addr
        #c.send('Hi')

        cmd = json.loads(data)

        if(cmd['dest']==myip):
            runcmd(cmd)
            print 'forme :3'
        else:
            if not memid.has_key(cmd['id']):
                forward(cmd)

        print cmd
