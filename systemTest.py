from adafruit_motorkit import MotorKit
import time

def test_wheels(kit):
    print("Test Started")
    print("Spinning motor1")
    kit.motor1.throttle = 1
    time.sleep(3)
    kit.motor1.throttle = 0
    print("Spinning motor2")
    kit.motor2.throttle = 1
    time.sleep(3)
    kit.motor2.throttle = 0
    print("Spinning motor3")
    kit.motor3.throttle = 1
    time.sleep(3)
    kit.motor3.throttle = 0
    print("Spinning motor4")
    kit.motor4.throttle = 1
    time.sleep(3)
    kit.motor4.throttle = 0
    print("Test Complete!")

def forward10(kit):
    kit.motor1.throttle = 1
    kit.motor2.throttle = 1
    kit.motor3.throttle = 1
    kit.motor4.throttle = 1
    time.sleep(2)
    print("Forward! 10% speed!")
    stop(kit)
    
def backward10(kit):
    kit.motor1.throttle = -0.1
    kit.motor2.throttle = -0.1
    kit.motor3.throttle = -0.1
    kit.motor4.throttle = -0.1
    time.sleep(2)
    print("Backward! 10% speed!")
    stop(kit)

def stop(kit):
    kit.motor1.throttle = 0
    kit.motor2.throttle = 0
    kit.motor3.throttle = 0
    kit.motor4.throttle = 0
    print("Halting!")
    
kit = MotorKit()

forward10(kit)
