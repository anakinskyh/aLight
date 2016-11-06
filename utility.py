import os
import string
import random

def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def get_ip():
    str = os.popen('ifconfig| grep Bcast | grep -E -o "([0-9]{1,3}[\.]){3}[0-9]{1,3}"').read()
    return str.split()[0]

if __name__ == '__main__':
    print get_ip()