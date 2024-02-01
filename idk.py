from esp_helper import *
smoother = Smoother(3)

start_servos() 			# start the servos
while True:
    pot = A2.read()
    print(pot)

    wheel = Servo(0)		# set up a new continuous servo, called "wheel", plugged into slot 0

    wheel.speed(1)			# go top speed in one direction, and then go in the other
    sleep(1)

    wheel.stop()			# stop the wheel


# so, the speed will be based on the knob. "wheel.speed()" is basically a turn. after each turn, stop the wheel. the wheel can only be started when the knob is turned (pot is changed from its previous value) or the knob is not zero
