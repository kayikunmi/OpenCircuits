from esp_helper import *
start_servos()             # Start the servos
wheel = Servo(0)           # Set up a new servo, called "wheel", plugged into slot 0
led1 = OUT(21)             # LED on pin 21
led2 = OUT(13)             # LED on pin 13
smoother = Smoother(5)

# Range sensor logic
# 0 - No one is close
# 1 - Someone is close

while True:
    # Read the sensor value and map it to either 0 or 1
    raw_value = A2.read()  # Read the raw sensor value
    value = 1 if raw_value > 200 else 0  # Threshold set at 200, adjust as needed
    value = smoother.smooth(value)
    print(0, 20, value)

    if value > 0.5:
        led1.on()       # Turn on LED1
        led2.on()       # Turn on LED2
        wheel.stop()    # Stop the wheel

    else:
        led1.off()      # Turn off LED1
        led2.off()      # Turn off LED2
        wheel.speed(0.05)  # Set wheel speed

    sleep(1)

#so what is my resolution?
#design this so that the tree thing is at the bottom 
# and i have something hiding my breadboard and shit
#
#
#
#
#

