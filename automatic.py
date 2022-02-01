from manual.py import Manual 


def followLine (bot, rSensor, lSensor):
    lineValue = 1200
    straightSpeed = 0.6
    turnSpeed = 0.8
    interval = 0.5
    pauseTime = 30

    while (true):
        if (rSensor == lineValue and lSensor == lineValue):
            bot.pause(pauseTime)
        elif (rSensor != lineValue and lSensor != lineValue):
            bot.forward(straightSpeed, interval)
        elif (rSensor == lineValue and lSensor != lineValue):
            bot.right(turnSpeed, interval)
        elif (rSensor != lineValue and lSensor == lineValue):
            bot.left(turnSpeed, interval)

bot = Manual()
followLine(bot, rSensor, lSensor)