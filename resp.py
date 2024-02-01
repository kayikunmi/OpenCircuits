from esp_helper import *

# Initialize the capacitive touch pads
touch_pad1 = CAP(14)
touch_pad2 = CAP(15)
touch_pad3 = CAP(33)

# Initialize the NeoPixel 
pixels = NEOPIXELS(32, 20, 3)

# Define the range for truth detection
TRUTH_MIN = 35  # example value, adjust as needed
TRUTH_MAX = 160  # example value, adjust as needed

while True:
    # Read the values from the capacitive touch pads
    value1 = touch_pad1.read()
    value2 = touch_pad2.read()
    value3 = touch_pad3.read()

    # Print the capacitive touch values
    print("Pad1:", value1, "Pad2:", value2, "Pad3:", value3)

    # Check conditions for each touch pad
    if value1 < 250:
        print("Lie detected!", value1)
        
        # Set all pixels to red to indicate a "lie"
        for i in range(20):
            pixels[i] = (255, 0, 0)  # RGB value for red
        pixels.write()
        sleep(1)  # Pause for 1 second after lights turn red

    elif TRUTH_MIN <= value2 <= TRUTH_MAX or value2 == 330:
        print("Truth detected!", value2)
        
        # Set all pixels to green to indicate a "truth"
        for i in range(20):
            pixels[i] = (0, 255, 0)  # RGB value for green
        pixels.write()
        sleep(1)  # Pause for 1 second after lights turn green

    elif 85<= value3 < 715:
        print("Undetermined", value3)
        
        # Set all pixels to blue to indicate "undetermined"
        for i in range(20):
            pixels[i] = (0, 0, 255)  # RGB value for blue
        pixels.write()
        sleep(1)

    
    else:
        # Turn off all pixels if no specific condition is met
        for i in range(20):
            pixels[i] = (0, 0, 0)  # RGB value for off
        pixels.write()
        sleep(0.5)


