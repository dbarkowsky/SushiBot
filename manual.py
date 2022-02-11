#from adafruit_motorkit import MotorKit
from mockMotor import MotorKit
import time

class Manual:
	def __init__(self):
		print("Starting Up")
		self.kit = MotorKit()
		self.speed = 0
		self.turnVariable = 2
		self.accelerationVariable = 0.3

	def forward(self, speed, seconds):
		print("Forward. Speed=" + str(speed) + ",  Time=" + str(seconds))
		if (speed > self.speed):
			accelerate(abs(speed))
		else:
			decelerate(abs(speed))
		self.speed = abs(speed)
		time.sleep(seconds)
		self.coast()

	def back(self, speed, seconds):
		print("Backward, Speed=" + str(speed) + ", Time=" + str(seconds))
		speed = 0 - abs(speed)
		if (speed > self.speed):
			accelerate(speed)
		else:
			decelerate(speed)
		self.speed = speed
		time.sleep(seconds)
		self.coast()

	#motors 1, 3 full speed; motors 2, 4 speed determined by TURN_VARIABLE constant
	def right(self, speed, seconds): 
		print("Right, Speed=" + str(speed) + ", Time=" + str(seconds))
		self.speed = abs(speed)
		insideSpeed = self.speed / self.turnVariable
		self.kit.motor1.throttle = self.speed
		self.kit.motor2.throttle = insideSpeed
		self.kit.motor3.throttle = self.speed
		self.kit.motor4.throttle = insideSpeed
		time.sleep(seconds)
		self.coast()

	#motors 2, 4 full speed; motors 1, 3 speed determined by TURN_VARIABLE constant
	def left(self, speed, seconds):
		print("Left, Speed=" + str(speed) + ", Time=" + str(seconds))
		self.speed = abs(speed)
		insideSpeed = self.speed / self.turnVariable
		self.kit.motor1.throttle = insideSpeed
		self.kit.motor2.throttle = self.speed
		self.kit.motor3.throttle = insideSpeed
		self.kit.motor4.throttle = self.speed
		time.sleep(seconds)
		self.coast()

	#wheels hold positions, full stop
	def stop(self):
		print("Stop")
		self.kit.motor1.throttle = 0
		self.kit.motor2.throttle = 0
		self.kit.motor3.throttle = 0
		self.kit.motor4.throttle = 0

	#no power to wheels, freespinning
	def coast(self):
		print("Coast")
		self.kit.motor1.throttle = None
		self.kit.motor2.throttle = None
		self.kit.motor3.throttle = None
		self.kit.motor4.throttle = None

	#pause for a second, then continue forwards just a bit
	def pause(self, seconds):
		print("Pause, Time=" + str(seconds))
		self.kit.motor1.throttle = 0
		self.kit.motor2.throttle = 0
		self.kit.motor3.throttle = 0
		self.kit.motor4.throttle = 0
		time.sleep(seconds)
		self.forward(self.speed, 1)

	#accelerate from previous speed to current speed
	#if applied in reverse direction, actually slows down reverse
	def accelerate(self, speed):
		for (i = self.speed, i >= speed; i += 0.1):
			self.kit.motor1.throttle = i
			self.kit.motor2.throttle = i
			self.kit.motor3.throttle = i
			self.kit.motor4.throttle = i
			time.sleep(self.accelerationVariable)

	#decelerate from previous speed to current speed
	#if applied in reverse direction, actually speeds up reverse
	def decelerate(self, speed):
		for (i = self.speed, i <= speed; i -= 0.1):
			self.kit.motor1.throttle = i
			self.kit.motor2.throttle = i
			self.kit.motor3.throttle = i
			self.kit.motor4.throttle = i
			time.sleep(self.accelerationVariable)
