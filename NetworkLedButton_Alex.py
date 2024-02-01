from esp_helper import *

start_wifi()
add_peer("7C:9E:BD:DE:74:48")  # change address for the second ESP32

previous_status = False
button = IN(12)  # button on pin 12
led = OUT(21)

while True:

    sender, in_message = receive()
    if in_message:
        print("Received", in_message, "from", sender)
        if in_message == "ON":
            LED.on()
            led.on()
            sleep(1)
        if in_message == "OFF":
            LED.off()
            led.off()
            sleep(1)
    

    status = button.value() > 0         # get current status, True or False
    if status != previous_status:       # detect a change
        if status is True:
            out_message = "ON"
            send(out_message)
            print("Sending", out_message)
            #print("Switch turned on!")
        else:
            out_message = "OFF"
            send(out_message)
            print("Sending", out_message)
            #print("Switch turned off!")
        previous_status = status        # store the status for next time
    sleep(.01)  # make it a bit faster for an interface where timing counts

