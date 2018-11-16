import RPi.GPIO as GPIO

def initMotor():
	
	global initialized
	if initialized:
		return
	GPIO.setmode(GPIO.BCM)
	GPIO.setwarnings(False)
	initialized = True

class Motor():
	pass