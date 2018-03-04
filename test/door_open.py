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


# create a default object, no changes to I2C address or frequency
mh = Adafruit_MotorHAT()

# create empty threads (these will hold the stepper 1 and 2 threads)
st1 = threading.Thread()
st2 = threading.Thread()


# recommended for auto-disabling motors on shutdown!
def turnOffMotors():
    mh.getMotor(1).run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor(2).run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor(3).run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor(4).run(Adafruit_MotorHAT.RELEASE)

atexit.register(turnOffMotors)

myStepper1 = mh.getStepper(200, 1)      # 200 steps/rev, motor port #1
myStepper2 = mh.getStepper(200, 2)      # 200 steps/rev, motor port #1
myStepper1.setSpeed(60)          # 30 RPM
myStepper2.setSpeed(60)          # 30 RPM


stepstyles = [Adafruit_MotorHAT.SINGLE, Adafruit_MotorHAT.DOUBLE, Adafruit_MotorHAT.INTERLEAVE, Adafruit_MotorHAT.MICROSTEP]

def stepper_worker(stepper, numsteps, direction, style):
    #print("Steppin!")
    stepper.step(numsteps, direction, style)
    #print("Done")

while True:
    print(readldr())
    time.sleep(1) #just chill for a sec
    if readldr() > 299:
        print("Night Time - Good Night Chickens ")
        dir = Adafruit_MotorHAT.FORWARD
        print("forward")
        rgb.set_color(RED)
    elif readldr() < 300 or readldr() != 0:
        print("Day Time - Go and play - Door opening")
        rgb.set_color(GREEN)
    else:
        print("BRGHT LIGHT!!!")

    st1 = threading.Thread(target=stepper_worker, args=(myStepper1, randomsteps, dir, stepstyles[random.randint(0,3)],))
    st1.start()

    time.sleep(0.1)  # Small delay to stop from constantly polling threads (see: https://forums.adafruit.com/viewtopic.php?f=50&t=104354&p=562733#p562733)
