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
    # Read the sensor value and map it to a range of 0 to 1
    raw_value = A2.read()  # Read the raw sensor value
    mapped_value = map(raw_value, 0, 4095, 0, 1)  # Map from 0-4095 to 0-1
    value = smoother.smooth(mapped_value)
    print("Sensor value:", value)

    if value < 0.027:
        led1.on()       # Turn on LED1
        led2.on()       # Turn on LED2
        wheel.stop()    # Stop the wheel
    else:
        led1.off()      # Turn off LED1
        led2.off()      # Turn off LED2
        wheel.speed(0.05)  # Set wheel speed

    sleep(1)

