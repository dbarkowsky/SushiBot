import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

sensor = 23 #gpio pin

GPIO.setup(sensor, GPIO.IN)

try:
    while True:
        if (GPIO.input(sensor)):
            print("on line " + str(GPIO.input(sensor)))
        else:
            print("off line " + str(GPIO.input(sensor)))

        sleep(0.5)
except KeyboardInterrupt:
    GPIO.cleanup()
