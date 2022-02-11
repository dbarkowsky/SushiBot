# SushiBot
A Raspberry-Pi-controlled robot designed for household sushi delivery.

Final product goal: wheel'd robot that follows line using IR sensors.

########################
File Descriptions
########################

systemTest.py
Simple test of all four motors individually. 
Used to test that motors are hooked up correctly.

sensorTest.py
Prints output depending on sensor signal.
Used to test that sensor is hooked up correctly.

mockMotor.py
Used for development on RPi emulator where adafruit board is not available. 
There is a reference to this in the manual.py file, as well as the import statement for the actual adafruit package. Comment out the one you don't want to use. 

manual.py
Contains all functions for movement and basic commands. Can be initialized in the Python shell for manually issued commands.

automatic.py
The implements the algorithm for following the line using two sensors and giving the correct commands to the motors depending on sensor input. Uses manual.py to run those commands. 