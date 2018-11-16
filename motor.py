import RPi.GPIO as GPIO

def initMotor():
	
	global initialized
	if initialized:
		return
	GPIO.setmode(GPIO.BCM)
	GPIO.setwarnings(False)
	initialized = True


class Motor():

	def __init__(self, pwm, in1, in2):
		GPIO.setup(pwm, GPIO.OUT)
		pwm_speed = GPIO.PWM(pwm, 100) #instancja pwm rpi
		pwm_speed.start(self.nowSpeed)
		GPIO.setup(in1, GPIO.OUT)
		GPIO.setup(in2, GPIO.OUT)
		self.direction = 0
		self.nowSpeed = 0
		self.stepSpeed = 1
		self.in1 = in1
		self.in2 = in2


	def setSpeed(self, speed=0):
		if type(speed) == int:
			if speed < 0:
				self.direction = -1
				self.stepSpeed = -1
			else:
				if speed > 0:
					self.direction=1
					self.stepSpeed=1
				else:
					self.direction=0

			deltaSpeed = abs(speed-self.nowSpeed)
			for i in range(0, deltaSpeed):
				self.nowSpeed += stepSpeed
				pwm_speed.ChangeDutyCycle(self.nowSpeed)


	def setDirection(self, direction=0)
		if type(direction) == int:
			if direction == 1:
				GPIO.output(self.in1, 1)
				GPIO.output(self.in2, 0)
			else:
				if direction == -1:
					GPIO.output(self.in1, 0)
					GPIO.output(self.in2, 1)
				else:
					if direction == 0:
						GPIO.output(self.in1, 0)
						GPIO.output(self.in2, 0)
					else:
						return False



