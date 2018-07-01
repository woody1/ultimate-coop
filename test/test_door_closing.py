# get the libs
from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor, Adafruit_StepperMotor
import atexit
import threading
import time
from squid import *
import RPi.GPIO as GPIO
import schedule

# Get the pins sorted
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

rgb = Squid(18, 23, 24)

# A var with the LDR reader pin number
pinldr = 14

# create a default object, no changes to I2C address or frequency
mh = Adafruit_MotorHAT()


# recommended for auto-disabling motors on shutdown!
def turnoffmotors():
    mh.getMotor(1).run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor(2).run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor(3).run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor(4).run(Adafruit_MotorHAT.RELEASE)


atexit.register(turnoffmotors)

# DC motor test!
myMotor = mh.getMotor(3)

# set the speed to start, from 0 (off) to 255 (max speed)
myMotor.setSpeed(150)
myMotor.run(Adafruit_MotorHAT.FORWARD)
# turn on motor
myMotor.run(Adafruit_MotorHAT.RELEASE)


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

        time.sleep(1)  # just chill for a sec
        print("Night Time - Good Night Chickens ")
        print("Closing")
        rgb.set_color(RED)
        myMotor.run(Adafruit_MotorHAT.FORWARD)
        time.sleep(0.01)
        myMotor.run(Adafruit_MotorHAT.RELEASE)
        print("Closed")
        rgb.set_color(OFF)


def open_door():

        time.sleep(1)  # just chill for a sec
        print("Day Time")
        print("Opening")
        rgb.set_color(YELLOW)
        myStepper.step(200, Adafruit_MotorHAT.FORWARD,  Adafruit_MotorHAT.SINGLE)
        print("Open")
        rgb.set_color(OFF)


schedule.every(2).minutes.do(close_door)

schedule.every().day.at("23:07").do(close_door)  # open door
schedule.every().day.at("07:00").do(open_door)  # close door

while True:
    time.sleep(1)
    schedule.run_pending()
