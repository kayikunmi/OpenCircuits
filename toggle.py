from esp_helper import *

toggle = IN(12)  # toggle on pin 12
start_servos()

while True:
    if toggle.value() > 0:
        arm = Servo(0)			# set up a new servo, called "arm", plugged into slot 0
        arm.position(0)			# move the arm all the way one way and then back again
        sleep(1)
        arm.position(180)
        print("Toggle is on!")
    else:
        arm = Servo(0)			# set up a new servo, called "arm", plugged into slot 0
        arm.position(0)
        print("Toggle is off!")
    sleep(.1)



