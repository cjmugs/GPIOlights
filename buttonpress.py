import RPi.GPIO as GPIO
import webbrowser

# initialize the GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.OUT)
GPIO.setup(19, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)
GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def button_callback(channel):
    webbrowser.open('www.google.com', new=1)
    print('page has opened')

GPIO.add_event_detect(6,GPIO.RISING,callback=button_callback) 
message = input("Press enter to quit\n\n") 
GPIO.cleanup()