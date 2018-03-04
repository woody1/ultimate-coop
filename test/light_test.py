# let there be light

# get the libs
import time
import RPi.GPIO as GPIO

# Get the pins sorted
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Set up the light
GPIO.setup(18, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)

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
        GPIO.output(18, GPIO.LOW)
        GPIO.output(24, GPIO.HIGH)
    elif readldr() < 300 or readldr() != 0:
        print("Day Time - Go and play - Door opening")
        GPIO.output(18, GPIO.HIGH)
        GPIO.output(24, GPIO.LOW)
    else:
        print("BRGHT LIGHT!!!")
