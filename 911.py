from esp_helper import *

while True:
    hall = hall_sensor()
    if hall > 0:
        print(hall, "yes mag")
    else:
        print(hall, "no mag")
    sleep(.1)
   

