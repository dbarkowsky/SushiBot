import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

sensor = 17 #gpio pin

GPIO.setup(sensor, GPIO.IN)

try:
    while True:
        if (GPIO.input(sensor)):
            print("on line")
        else:
            print("off line")

        sleep(0.5)
except KeyboardInterrupt:
    GPIO.cleanup()