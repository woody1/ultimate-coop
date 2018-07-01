#!/usr/bin/python
from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor

import time
import atexit

# create a default object, no changes to I2C address or frequency
mh = Adafruit_MotorHAT(addr=0x6f)

# recommended for auto-disabling motors on shutdown!
def turnOffMotors():
    mh.getMotor(1).run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor(2).run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor(3).run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor(4).run(Adafruit_MotorHAT.RELEASE)


atexit.register(turnOffMotors)

# DC motor test!
myMotor = mh.getMotor(3)

# set the speed to start, from 0 (off) to 255 (max speed)
myMotor.setSpeed(150)
myMotor.run(Adafruit_MotorHAT.FORWARD)
# turn on motor
myMotor.run(Adafruit_MotorHAT.RELEASE)


while True:


    time.sleep(1)  # just chill for a sec
    print("Night Time - Good Night Chickens ")
    print("Closing")
    myMotor.run(Adafruit_MotorHAT.FORWARD)
    time.sleep(5.0)
    myMotor.run(Adafruit_MotorHAT.RELEASE)
    print("Closed")

    time.sleep(5.0)
