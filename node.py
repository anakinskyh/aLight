import socket
import json
import portcontrol
import utility

def set_bit():
    return 0

def runcmd(cmd):
    if cmd['cmd']==0:
        portcontrol.setbylist(cmd['arg'])

if __name__ == '__main__':

    _IP = '127.0.0.1'
    _IP = utility.get_ip()
    _IP = socket.gethostname()
    _PORT = 5050

    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.getsockopt(socket.SOL_SOCKET,socket.SO_REUSEPORT,1)
    s.getsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    s.bind((_IP,_PORT))

    s.listen(5)

    while 1:
        c,addr = s.accept()
        print addr
        c.send('Hi')
        data = c.recv(1024)

        cmd = json.loads(data)
        runcmd(cmd)

        print "They send ",cmd
        c.close()
