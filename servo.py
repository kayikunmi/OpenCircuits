from esp_helper import *

start_servos() 			# start the servos

while True:
    arm = Servo(0)			# set up a new servo, called "arm", plugged into slot 0

    arm.position(0)			# move the arm all the way one way and then back again
    sleep(1)
    arm.position(180)

