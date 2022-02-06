from manual import Manual 
import RPi.GPIO as GPIO
from time import sleep

def followLine (bot, rSensor, lSensor):
    lineValue = 1200
    straightSpeed = 0.6
    turnSpeed = 0.8
    interval = 0.5
    pauseTime = 30

    while (True):
        if (rSensor == lineValue and lSensor == lineValue):
            bot.pause(pauseTime)
        elif (rSensor != lineValue and lSensor != lineValue):
            bot.forward(straightSpeed, interval)
        elif (rSensor == lineValue and lSensor != lineValue):
            bot.right(turnSpeed, interval)
        elif (rSensor != lineValue and lSensor == lineValue):
            bot.left(turnSpeed, interval)


GPIO.setmode(GPIO.BCM)

lSensor = 23 #gpio pin
rSensor = 24 #gpio pin

GPIO.setup(lSensor, GPIO.IN)
GPIO.setup(rSensor, GPIO.IN)

bot = Manual()
followLine(bot, rSensor, lSensor)