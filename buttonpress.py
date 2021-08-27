import RPi.GPIO as GPIO
from testlight import blinkOnce

# initialize the GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.OUT)
GPIO.setup(19, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)
GPIO.setup(20, GPIO.OUT)
GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def button_callback(channel):
    blinkOnce(20)
    print('light is on')

GPIO.add_event_detect(6,GPIO.RISING,callback=button_callback) 
message = input("Press enter to quit\n\n") 
GPIO.cleanup()