from esp_helper import *
import time

# Initialize components
start_servos()
wheel = Servo(0)  # Continuous rotation servo for clock hand
pot = A2  # Potentiometer connected to analog pin A2
smoother = Smoother(10)  # Increase the number of readings to average

# Constants
POT_MAX = 4095  # Maximum reading from potentiometer
MIN_SPEED = 0  # Stop the servo
MAX_SPEED = 1.0  # Maximum speed of the servo

# Function to map potentiometer value to servo speed
def map_pot_to_speed(pot_value, pot_max, min_speed, max_speed):
    # This maps the potentiometer value to a speed value
    # The servo will not move if the pot_value is at the midpoint (POT_MAX / 2)
    # The further away from the midpoint, the faster the servo will move
    if pot_value < (pot_max / 2):
        return -((pot_max / 2 - pot_value) / (pot_max / 2) * max_speed)
    else:
        return ((pot_value - pot_max / 2) / (pot_max / 2) * max_speed)

# Variable to store the last potentiometer value
last_pot_value = 0  # Initialize to 0 for the first run

# Main loop
while True:
    # Read and smooth the potentiometer value
    pot_value = pot.read()
    pot_value = smoother.smooth(pot_value)

    # Check if the potentiometer has been turned
    if pot_value != last_pot_value:
        # Map the potentiometer value to a servo speed
        servo_speed = map_pot_to_speed(pot_value, POT_MAX, MIN_SPEED, MAX_SPEED)

        # If the potentiometer is not at the midpoint, move the servo
        if pot_value != POT_MAX / 2:
            wheel.speed(servo_speed)  # Set the servo speed
            print(f"Servo speed set to {servo_speed:.2f}")
        else:
            wheel.stop()  # Stop the servo if the potentiometer is at the midpoint
            print("Servo stopped.")

        last_pot_value = pot_value  # Update the last potentiometer value

    time.sleep(0.1)  # Small delay to reduce reading frequency

