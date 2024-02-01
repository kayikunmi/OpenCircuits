from esp_helper import *

smoother = Smoother(3)
start_servos()
wheel = Servo(0)

while True:
    #...
    pot = A2.read()
    pot = smoother.smooth(pot)
    
    s = map(pot, 0, 4095, -1, 1)
    #print(s)
    
    w = map(s, 0, 180, 0, 180)
    print(w)
    wheel.speed(w)
    
    sleep(0.01)



