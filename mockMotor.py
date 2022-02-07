class MotorKit():
    def __init__(self):
        print("MotorKit Initialized")
        self.motor1 = Motor();
        self.motor2 = Motor();
        self.motor3 = Motor();
        self.motor4 = Motor();
        
class Motor():
    def __init__(self):
        self.throttle = 0