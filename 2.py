from esp_helper import *
import time

# Initialize components
start_servos()
wheel = Servo(0)  # Continuous rotation servo for clock hand
pot = A2  # Potentiometer connected to analog pin A2
smoother = Smoother(20)  # Further increased smoothing

# Constants
POT_MAX = 4095  # Maximum reading from potentiometer
FULL_TURN_TIME = 30  # Time in seconds for one full 360-degree turn at slowest speed
CHANGE_THRESHOLD = 1000  # Further increased threshold for detecting significant change
DEBOUNCE_TIME = 2  # Time in seconds for debounce delay

# Function to calculate rotation duration based on potentiometer value
def calculate_rotation_duration(pot_value, pot_max, full_turn_time):
    return full_turn_time * (1 - (pot_value / pot_max))

# Variable to store the last potentiometer value and time
last_pot_value = 0
last_change_time = time.time()

# Main loop
while True:
    # Read and smooth the potentiometer value
    pot_value = pot.read()
    pot_value = smoother.smooth(pot_value)

    # Check if the potentiometer value has changed significantly and debounce
    if abs(pot_value - last_pot_value) > CHANGE_THRESHOLD and (time.time() - last_change_time) > DEBOUNCE_TIME:
        # Calculate the rotation duration
        rotation_duration = calculate_rotation_duration(pot_value, POT_MAX, FULL_TURN_TIME)

        # Print the potentiometer value and rotation duration
        print(f"Potentiometer Value: {pot_value}, Rotation Duration: {rotation_duration:.2f} seconds")

        # Perform the rotation
        wheel.speed(1)  # Start rotating the servo
        time.sleep(rotation_duration)  # Wait for the rotation to complete
        wheel.stop()  # Stop the servo
        print("Rotation completed.")

        # Update the last potentiometer value and time
        last_pot_value = pot_value
        last_change_time = time.time()

    time.sleep(0.1)  # Small delay to reduce reading frequency

