from manual import Manual 
import RPi.GPIO as GPIO
from time import sleep

def followLine (bot, rSensor, lSensor):
    lineValue = 1
    straightSpeed = 0.6
    turnSpeed = 0.8
    interval = 0.5
    pauseTime = 30

    while (True):
        if (GPIO.input(rSensor) and GPIO.input(lSensor)):
            bot.pause(pauseTime)
        elif (not GPIO.input(rSensor) and not GPIO.input(lSensor)):
            bot.forward(straightSpeed, interval)
        elif (GPIO.input(rSensor) and not GPIO.input(lSensor)):
            bot.right(turnSpeed, interval)
        elif (not GPIO.input(rSensor) and GPIO.input(lSensor)):
            bot.left(turnSpeed, interval)


GPIO.setmode(GPIO.BCM)

lSensor = 23 #gpio pin
rSensor = 24 #gpio pin

GPIO.setup(lSensor, GPIO.IN)
GPIO.setup(rSensor, GPIO.IN)

bot = Manual()
followLine(bot, rSensor, lSensor)