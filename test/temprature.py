# show temp

# Import Librereies
import os
import glob
import time
import RPi.GPIO as GPIO

#set up the nameing
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Set up the light
GPIO.setup(18, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)

# Initialize the GPIO pins
os.system('modprobe w1-gpio') # Turns on the GPIO modul
os.system('modprobe w1-therm') # Turns on the Temprature module

# finds the correct device file that hold the temperature data
base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'


# A function that reads the sensors data
def read_temp_raw():
    f = open(device_file, 'r') # Opens the temperature device file
    lines = f.readlines() # Returns the text
    f.close()
    return lines


# convert the value of the sensor into a temperature
def read_temp():
    lines = read_temp_raw() # Read the temperature 'device file'

    # while the line does not contain 'YES', wait for 0.2s
    # and then read the device file again.
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw()

    # look for the position of the '=' in the second line of the device file
    equals_pos = lines[1].find('t=')

    # If the '=' is found, convert the resy of the lines after the '=' into deg$
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        temp_f = temp_c * 9.0 / 5.0 + 32.0
        return temp_c

# print out the temp until the program is stopped.
while True:
    print(read_temp(),  'C')
    time.sleep(1)
    temprature = read_temp()
    if temprature > 21.0:
        print("Too hot")
        GPIO.output(18, GPIO.LOW)
        GPIO.output(24, GPIO.HIGH)
    else:
        GPIO.output(18, GPIO.HIGH)



GPIO.cleanup()
