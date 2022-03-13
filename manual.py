from adafruit_motorkit import MotorKit
#from mockMotor import MotorKit
import time

class Manual:
	def __init__(self):
		print("Starting Up")
		self.kit = MotorKit()
		self.speed = 0
		self.turnVariable = 1
		self.accelerationVariable = 0.1


	def forwardAccel(self, speed, seconds):
		print("Forward. Speed=" + str(speed) + ",  Time=" + str(seconds))
		if (speed > self.speed):
			self.accelerate(abs(speed))
		else:
			self.decelerate(abs(speed))
		self.speed = abs(speed)
		time.sleep(seconds)
		self.coast()

	def backAccel(self, speed, seconds):
		print("Backward, Speed=" + str(speed) + ", Time=" + str(seconds))
		speed = 0 - abs(speed)
		if (speed > self.speed):
			self.accelerate(speed)
		else:
			self.decelerate(speed)
		self.speed = speed
		time.sleep(seconds)
		self.coast()

	def forward(self, speed, seconds):
		print("Forward. Speed = " + str(speed) + ",  Time= " + str(seconds))
		speed = abs(speed)
		self.kit.motor1.throttle = speed
		self.kit.motor2.throttle = speed
		self.kit.motor3.throttle = speed
		self.kit.motor4.throttle = speed
		time.sleep(seconds)
		#self.coast()

	#motors 1, 3 full speed; motors 2, 4 speed determined by TURN_VARIABLE constant
	def rightTank(self, speed, seconds): 
		print("Right, Speed=" + str(speed) + ", Time=" + str(seconds))
		self.speed = abs(speed)
		self.kit.motor1.throttle = self.speed
		self.kit.motor2.throttle = -self.speed
		self.kit.motor3.throttle = self.speed
		self.kit.motor4.throttle = -self.speed
		time.sleep(seconds)
		#self.coast()

	def right(self, speed, seconds):
		print("Right")
		self.kit.motor1.throttle = 0.8
		self.kit.motor2.throttle = 0.5
		self.kit.motor3.throttle = 0.8
		self.kit.motor4.throttle = 0.5
		time.sleep(seconds)

	#motors 2, 4 full speed; motors 1, 3 speed determined by TURN_VARIABLE constant
	def leftTank(self, speed, seconds):
		print("Left, Speed=" + str(speed) + ", Time=" + str(seconds))
		self.speed = abs(speed)
		self.kit.motor1.throttle = -self.speed
		self.kit.motor2.throttle = self.speed
		self.kit.motor3.throttle = -self.speed
		self.kit.motor4.throttle = self.speed
		time.sleep(seconds)
		#self.coast()

	def left(self, speed, seconds):
		print("Left")
		sleeptimer = seconds / 2
		self.kit.motor1.throttle = 0.5
		self.kit.motor2.throttle = 0.8
		self.kit.motor3.throttle = 0.5
		self.kit.motor4.throttle = 0.8
		time.sleep(sleeptimer)
		self.forward(0.8, sleeptimer)

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
		time.sleep(seconds-3)
		#beep - announcing it will go again
		self.alarm(10)
		time.sleep(3)
		self.forward(self.speed, 0.5)

	def alarm(self, beeps):
		for i in range(beeps):
			self.kit.motor1.throttle = 0.3
			time.sleep(0.1)
			self.kit.motor1.throttle = None
			time.sleep(0.1)

	#accelerate from previous speed to current speed
	#if applied in reverse direction, actually slows down reverse
	def accelerate(self, speed):
		steps = int((speed - self.speed) * 10)
		for i in range(steps):
			self.kit.motor1.throttle = self.speed
			self.kit.motor2.throttle = self.speed
			self.kit.motor3.throttle = self.speed
			self.kit.motor4.throttle = self.speed
			self.speed += 0.1
			time.sleep(self.accelerationVariable)

	#decelerate from previous speed to current speed
	#if applied in reverse direction, actually speeds up reverse
	def decelerate(self, speed):
		steps = int((self.speed - speed) * 10)
		for i in range(steps):
			self.kit.motor1.throttle = self.speed
			self.kit.motor2.throttle = self.speed
			self.kit.motor3.throttle = self.speed
			self.kit.motor4.throttle = self.speed
			self.speed -= 0.1
			time.sleep(self.accelerationVariable)
