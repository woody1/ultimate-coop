#!/usr/bin/python
from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor, Adafruit_StepperMotor
import time
import atexit
import threading
import schedule

from squid import *
# Sqet the squid

rgb = Squid(18, 23, 24)

# create a default object, no changes to I2C address or frequency
mh = Adafruit_MotorHAT()

# create empty threads (these will hold the stepper 1 and 2 threads)
st1 = threading.Thread()


# recommended for auto-disabling motors on shutdown!
def turnOffMotors():
    mh.getMotor(1).run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor(2).run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor(3).run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor(4).run(Adafruit_MotorHAT.RELEASE)

atexit.register(turnOffMotors)

myStepper = mh.getStepper(10, 1)  # 200 steps/rev, motor port #1
myStepper.setSpeed(255)             # 30 RPM


def stepper_worker(stepper, numsteps, direction, style):
    print("Steppin!")
    stepper.step(numsteps, direction, style)
    print("Done")


def close_door():
    rgb.set_color(RED)
    myStepper.step(3000, Adafruit_MotorHAT.FORWARD,  Adafruit_MotorHAT.SINGLE)
    print("Closed")
    rgb.set_color(GREEN)
    time.sleep(10)
    rgb.set_color(OFF)


def open_door():
    rgb.set_color(RED)
    myStepper.step(3000, Adafruit_MotorHAT.BACKWARD,  Adafruit_MotorHAT.SINGLE)
    print("Open")
    rgb.set_color(GREEN)
    time.sleep(10)
    rgb.set_color(OFF)


schedule.every().day.at("15:40").do(close_door) # close door
schedule.every().day.at("15:42").do(open_door) # open door


while True:

    open_door()
    schedule.run_pending()
    time.sleep(0.2)  # Small delay to stop from constantly polling threads (see: https://forums.adafruit.com/viewtopic.php?f=50&t=104354&p=562733#p562733)


