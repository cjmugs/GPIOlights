import RPi.GPIO as GPIO
import time

# initialize the GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.OUT)
GPIO.setup(19, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)
GPIO.setup(25, GPIO.OUT)
GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def blinkOnce(pin):
    GPIO.output(pin, True)
    time.sleep(.02)
    GPIO.output(pin, False)
    time.sleep(.02)

def blinkSlow(pin): 
    GPIO.output(pin, True)
    time.sleep(.05)
    GPIO.output(pin, False)
    time.sleep(.05)

def motion(blinkOnce):
    blinkOnce(17)
    blinkOnce(26)
    blinkOnce(19)
    blinkOnce(25)
    blinkOnce(27)
    blinkOnce(25)
    blinkOnce(19)
    blinkOnce(26)

def slow_motion(blinkSlow):
    blinkSlow(17)
    blinkSlow(26)
    blinkSlow(19)
    blinkSlow(25)
    blinkSlow(27)
    blinkSlow(25)
    blinkSlow(19)
    blinkSlow(26)

def all():
    chan_list = (17, 26, 19, 25, 27)
    GPIO.output(chan_list, True)
    time.sleep(.1)
    GPIO.output(chan_list, False)
    time.sleep(.1)
    

while True:
    motion(blinkOnce)
    all()
    slow_motion(blinkSlow)
    all()
    motion(blinkOnce)
    all()
    all()
    all()

GPIO.cleanup()