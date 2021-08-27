import RPi.GPIO as GPIO 

def button_callback(channel):
    return some()

def some():
    print('button is working normally')

GPIO.setwarnings(False) 
GPIO.setmode(GPIO.BCM) 
GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(6,GPIO.RISING,callback=button_callback) 
message = input("Press enter to quit\n\n") 
GPIO.cleanup() 