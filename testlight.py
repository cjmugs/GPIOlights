import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(20, GPIO.OUT)
GPIO.setup(25, GPIO.OUT)

def blinkOnce(pin):
    GPIO.output(pin, True)
    

while True:
    blinkOnce(20)
   

GPIO.cleanup()