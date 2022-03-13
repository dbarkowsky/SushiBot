from manual import Manual 
import RPi.GPIO as GPIO
from time import sleep

def followLine (bot, rSensor, lSensor):
    straightSpeed = 0.8
    turnSpeed = 0.9
    interval = 0.05
    pauseTime = 6

    while (True):
        if (not GPIO.input(rSensor) and not GPIO.input(lSensor)):
            bot.pause(pauseTime)
        elif (GPIO.input(rSensor) and GPIO.input(lSensor)):
            bot.forward(straightSpeed, interval)
        elif (not GPIO.input(rSensor) and GPIO.input(lSensor)):
            bot.rightTank(turnSpeed, interval)
            #bot.right(turnSpeed, interval)
        elif (GPIO.input(rSensor) and not GPIO.input(lSensor)):
            bot.leftTank(turnSpeed, interval)
            #bot.left(turnSpeed, interval)


GPIO.setmode(GPIO.BCM)

lSensor = 23 #gpio pin
rSensor = 24 #gpio pin

GPIO.setup(lSensor, GPIO.IN)
GPIO.setup(rSensor, GPIO.IN)

bot = Manual()
followLine(bot, rSensor, lSensor)
