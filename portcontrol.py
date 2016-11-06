#import RPi.GPIO as GPIO

def reset():
    for i in range(0,8):
        print 'what'
    return 0

def setport(port):
    try:
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(port,GPIO.OUT)
        GPIO.output(port,GPIO.HIGH)
    except IOError ,err:
        print err

def resetport(port):
    try:
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(port, GPIO.OUT)
        GPIO.output(port, GPIO.LOW)
    except IOError, err:
        print err

def setbylist(list):
    print 'fuck'
    #for (k,v) in list:

        #if v==0:
            #resetport(k)
        #else:
            #setport(k)