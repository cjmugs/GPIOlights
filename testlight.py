import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(20, GPIO.OUT)

def blinkOnce(pin):
    GPIO.output(pin, True)
    time.sleep(.02)
    GPIO.output(pin, False)
    time.sleep(.02)

while True:
    blinkOnce(20)
GPIO.cleanup()