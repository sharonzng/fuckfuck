#Controlling motor function using hall effect encoder quadrature
#M1,M2 are motor power in and out
#VCC and GND are for powering the encoder
#Out A and out B are the two encoder outputs
#Only using one for now as direction is not needed
#Could update to both if direction becomes useful

import RPI.GPIO as gpio

#set boundaries ex. motorCount>=120 or motorCount<= -12 stops power to motor
spinDirection = #change to thing which checks current direction based on EMG data
motorCount = 0 #position for the motor ~ position of the fingers

def motor_spin_callback(channel): #interrupt action depends on direction
    if (spinDirection == 1): #motorCount represents the 12 counts/rev of motor shaft
        motorCount += 1
    if (spinDirection == 0):
        motorCount -= 1
    return motorCount

OUT_A_PIN = 3
gpio.setmode(gpio.BCM)
gpio.setup(OUT_A_PIN, http://GPIO.IN, pull_up_down = gpio.PUD_UP)

gpio.add_event_detect(OUT_A_PIN, gpio.BOTH, callback=motor_spin_callback, bouncetime = 100)

#main bit of code goes here to loop as needed (EMG?)

GPIO_cleanup()