from esp_helper import *

start_servos() 			# start the servos
wheel = Servo(0)			# set up a new servo, called "arm", plugged into slot 0
led = OUT(21)
# so from here on out, what do i need this shit to do?
# the wheel to spin in a continous circle
# and the led to shine 
# here
while True:
    led.on()
    wheel.speed(0.05)	
    sleep(1)
    
    led.off()
    wheel.stop()
    sleep(1)

    

