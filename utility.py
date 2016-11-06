import os

def get_ip():
    str = os.popen('ifconfig| grep Bcast | grep -E -o "([0-9]{1,3}[\.]){3}[0-9]{1,3}"').read()
    return str.split()[0]

if __name__ == '__main__':
    print get_ip()