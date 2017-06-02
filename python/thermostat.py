#thermostat.py
#controlls the exhaust fan, turns it on when temperature is over the target temperature
#Fan is assumed to be wired to Pin 33 (GPIO 13)
#Pin 30 may control a relay or be a transistor switch, assumes HIGH means ON

import RPi.GPIO as GPIO
from logData import logData
from bookshelf import takeOffShelf, putOnShelf
from si7021 import getTempC

def adjustThermostat(temp):
    "Turn the fan on or off in relationship to target temperature"
    print ("Adjust Thermostat %s" %str(temp))
    fanPin = 35
    targetTempKey = "targetTemp"
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(fanPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    fanOn = GPIO.input(fanPin)   
    targetTemp = takeOffShelf(targetTempKey)
    if temp > targetTemp:
        if not fanOn:
            turnFanOn(fanPin)
    else:
        if fanOn:
            turnFanOff(fanPin)

def turnFanOn(fanPin):
    "Turn fan on"
    print ("Turn fan ON")
    GPIO.setup(fanPin, GPIO.OUT, pull_up_down=GPIO.PUD_UP)
    GPIO.output(fanPin, GPIO.HIGH)
    logData("Fan", "ON", "Current Temp: " + str(temp))

def turnFanOff(fanPin):
    "Turn fan off"
    print ("Turn Fan OFF")
    GPIO.setup(fanPin, GPIO.OUT, pull_up_down=GPIO.PUD_UP)
    GPIO.output(fanPin, GPIO.LOW)    
    logData("Fan", "OFF", "Current Temp: " + str(temp))

adjustThermostat(getTempC())    
