# let there be light

# get the libs
import time
from squid import *
import RPi.GPIO as GPIO

# Get the pins sorted
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

rgb = Squid(18, 23, 24)

# A var with the LDR reader pin number
pinldr = 14


def readldr():
    ldrcount = 0 # set the count to zero
    GPIO.setup(pinldr, GPIO.OUT)
    GPIO.output(pinldr, GPIO.LOW)
    time.sleep(0.1) # drains the cap

    GPIO.setup(pinldr, GPIO.IN) # sets teh pin to input
    # while the input pin reas low or off or fa
    while (GPIO.input(pinldr) == GPIO.LOW):
        ldrcount += 1 # add 1 to the count
    return ldrcount

while True:
    print(readldr())
    time.sleep(1) #just chill for a sec
    if readldr() > 299:
        print("Night Time - Good Night Chickens ")
        rgb.set_color(RED)
    elif readldr() < 300 or readldr() != 0:
        print("Day Time - Go and play - Door opening")
        rgb.set_color(GREEN)
    else:
        print("BRGHT LIGHT!!!")