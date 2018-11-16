import RPi.GPIO as GPIO
import time
"""
Moduł do obsługi drivera silników.
"""

def initMotor():
	global initialized
	if initialized:
		return
	GPIO.setmode(GPIO.BCM)
	GPIO.setwarnings(False)
	initialized = True


class Motor():

	def __init__(self, pwm, in1, in2):
		"""
		Funkcja inicjująca obiekt klasy Motor
		https://www.dfrobot.com/wiki/index.php/7A_Dual_DC_Motor_Driver_SKU:_DRI0041
		Argumenty:
		pwm - pin prędkości
		in1, in2 - piny kierunku prędkości 

		Funkcja przyjmuje wyłącznie numery pinów w postaci liczb całkowitych
		"""
		if type(in1) == int and type(in2) == int and type(pwm) == int:
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
		"""
		Funkcja ustawiająca prędkość silnika

		Przykład uzycia: Motor1.setSpeed(-100)

		Argumenty:
		speed - wartośc prędkości jaka ma zostać ustawiona.
		Argument ten przyjmuje wartości z zakresu (-100, 100).
		Znak przy prędkości określa kierunek jazdy: -1 do tyłu, 1 do przodu.
		Funkcja przyjmuje wyłącznie wartości całkowite. 

		To-do:
		przypadek gdy speed=0 i silnik ma wyhamować
		"""
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
				time.sleep(0.1) #przerwa 100ms


	def setDirection(self, direction=0):
		"""
		Funkcja ustawiająca kierunek działania silnika

		Przykład uzycia: Motor1.setDirection(-1)

		Argumenty:
		direction - możliwe wartości: 1 - do przodu, 0 - stój w miejscu, -1 - do tyłu
		Funkcja przyjmuje wyłącznie ten zestaw wartości.		
		"""
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





