# get the libs
from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor, Adafruit_StepperMotor
import atexit
import threading
import time
from squid import *
import RPi.GPIO as GPIO

# Get the pins sorted
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

rgb = Squid(18, 23, 24)

# A var with the LDR reader pin number
pinldr = 14

# create a default object, no changes to I2C address or frequency
mh = Adafruit_MotorHAT()

# recommended for auto-disabling motors on shutdown!
def turnOffMotors():
    mh.getMotor(1).run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor(2).run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor(3).run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor(4).run(Adafruit_MotorHAT.RELEASE)

atexit.register(turnOffMotors)

myStepper = mh.getStepper(300, 1)  # 200 steps/rev, motor port #1
myStepper.setSpeed(30)             # 30 RPM


def readldr():
    ldrcount = 0 # set the count to zero
    GPIO.setup(pinldr, GPIO.OUT)
    GPIO.output(pinldr, GPIO.LOW)
    time.sleep(0.1) # drains the cap

    GPIO.setup(pinldr, GPIO.IN) # sets the pin to input
    # while the input pin reads low or off or fa
    while (GPIO.input(pinldr) == GPIO.LOW):
        ldrcount += 1 # add 1 to the count
    return ldrcount


def close_door():
    print("Night Time - Good Night Chickens ")
    print("Closing")
    rgb.set_color(RED)
    myStepper.step(200, Adafruit_MotorHAT.FORWARD,  Adafruit_MotorHAT.SINGLE)
    print("Closed")


while True:
    time.sleep(1)
    print(readldr())
    if readldr() < 499:
            print("Too Light waiting for it to get dark")
            rgb.set_color(GREEN)
    else:
        close_door()
        break
    time.sleep(1) #just chill for a sec


