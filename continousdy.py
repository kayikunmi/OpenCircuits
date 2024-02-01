from esp_helper import *
import time

# Initialize components
start_servos()
wheel = Servo(0)  # Continuous servo for clock hand
pot = A2  # Potentiometer connected to analog pin A2
smoother = Smoother(10)  # Increase the number of readings to average

# Constants
POT_MAX = 4095  # Maximum reading from potentiometer
MIN_SPEED = 0  # Minimum speed of the servo
MAX_SPEED = 1.0  # Maximum speed of the servo
BASE_ROTATION_TIME = 5  # Base time in seconds for one full rotation at maximum speed

# Function to map potentiometer value to servo speed
def map_pot_to_speed(pot_value, pot_max, min_speed, max_speed):
    return min_speed + ((pot_value / pot_max) * (max_speed - min_speed))

# Variable to store the last potentiometer value
last_pot_value = None

# Main loop
while True:
    # Read and smooth the potentiometer value
    pot_value = pot.read()
    pot_value = smoother.smooth(pot_value)

    # If the potentiometer value has changed, initiate the rotation
    if last_pot_value is None or pot_value != last_pot_value:
        # Map the potentiometer value to a servo speed
        servo_speed = map_pot_to_speed(pot_value, POT_MAX, MIN_SPEED, MAX_SPEED)

        # Calculate the time for one full rotation based on the speed
        rotation_duration = BASE_ROTATION_TIME / servo_speed

        # Only initiate rotation if the potentiometer value is above a certain threshold
        if pot_value > 0:
            print(f"Rotating with speed {servo_speed:.2f}.")
            wheel.speed(servo_speed)  # Start rotating the servo
            time.sleep(rotation_duration)  # Wait for the rotation to complete
            wheel.stop()  # Stop the servo
            print("Rotation completed.")

        # Update the last potentiometer value
        last_pot_value = pot_value

    time.sleep(0.1)  # Small delay to reduce reading frequency when idle

