import gpio

def reset():
    for i in range(0,8):
        gpio.cleanup(i)
    return 0

def setport(port):
    try:
        gpio.set(port,gpio.HIGH)
    except IOError ,err:
        print err

def resetport(port):
    try:
        gpio.set(port,gpio.LOW)
    except IOError, err:
        print err

def setbylist(list):
    for (k,v) in list:

        if v==0:
            resetport(k)
        else:
            setport(k)