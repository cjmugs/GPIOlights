import RPi.GPIO as GPIO
GPIO.setwarnings(False)
 GPIO.setmode(GPIO.BOARD)   

redPin   = 12
greenPin = 24
bluePin  = 5
def blink(pin):