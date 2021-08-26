# import necessary libraries
import RPi.GPIO as GPIO
import time

# initialize the GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.OUT)
GPIO.setup(19, GPIO.OUT)


# define a function to turn the light on then off
def blinkOnce(pin):
    GPIO.output(pin, True)
    time.sleep(.4)
    GPIO.output(pin, False)
    time.sleep(.4)

# use blinkOnce function in a loop
for i in range(99999):
        blinkOnce(26)
        blinkOnce(19)

# cleanup
GPIO.cleanup()