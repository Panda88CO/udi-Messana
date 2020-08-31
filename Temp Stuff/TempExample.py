# --------------------------------------------------------
# PURPOSE: - To monitor temperatures within a backup server's 
#            case and within the garden shed it is running in
#          - To turn on heating or cooling if temperature within
#            server case gets out of a predetermined range    
#          - To log temperatures/times in a tab-delimited file
#            on a NAS box. 

import os
import glob
import time
import datetime
import RPi.GPIO as iO
import os,subprocess
from subprocess import call
from w1thermsensor import W1ThermSensor
from collections import deque
import json

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

fileName = './sensors.json'
sensorList = {}
with open(fileName)as infile:
    sensorList = json.load(infile)
infile.close()
    
sensorList['sensors'].append({
                                "serialNumber": "0000ffff",
                                "ISYname":      "test123"      
                            })
sensorList['sensors'].append({
                                "serialNumber": "0000aaaa",
                                "ISYname":      "test321"      
                            })
print(sensorList)
with open(fileName, 'w') as outfile:
    json.dump(sensorList, outfile)
outfile.close()


tQ = []
tQ.append(1)
tQ.append(2)
tQ.append(3)
tQ.append(4)
print(max(tQ), min(tQ))
tQ.pop()
print(max(tQ), min(tQ))
tQ.append(5)
tQ.append(3)
print(max(tQ), min(tQ))

currentTime1 = datetime.datetime.now()
currentTime2 = datetime.datetime.now()
timeDiff = currentTime2 - currentTime1
print(timeDiff.days, timeDiff.seconds)
# ======================================================================
# Define our subroutines:
# --------------------------------------------------
# Define a function to convert Celsius to Fahrenheit 

def celsiusToFahrenheit(theTempCelsius):
 myTempFarenheit = ((theTempCelsius*9)/5) + 32
 return myTempFarenheit
 
# --------------------------------------------------
# Define a function to get current temperature of the
# Raspberry Pi's CPU  (which, just for grins, we also
# want to monitor)

def getPiCPUtemperature():  
 res = os.popen('vcgencmd measure_temp').readline()  
 return(res.replace("temp=","").replace("'C\n",""))  
 

# Capture the date we started this script

myDateStamp_Startup =datetime.datetime.now().strftime("%Y-%m-%d")
myDateStamp_Today = myDateStamp_Startup


# -------------------------------------
# Refer to pins by Broadcom SOC channel
# instead of physical pin#

iO.setmode(iO.BCM)

# -------------------------------------
# Specify which pins are used to flip
# which relay switch on/off and then
# define them as "Output"

relaySensors = 21
iO.setwarnings(False)
iO.setup(relaySensors, iO.OUT)


# -------------------------------------
# Turn off both relay switches - for 
# convenience in testing

iO.output(relaySensors, False)


# -------------------------------------
# Set a pointer to our W1Thermsensor object,
# which will give us easy access to the sensors

try:
    mySensor = W1ThermSensor()
    numberSensors = len(W1ThermSensor.get_available_sensors())
except:
    print('error')
# -------------------------------------
# Define sensors by ID (we had to experimentally
# discover these by writing a little script that
# opened the W1ThermSensor class, looped through
# the sensors it knew about and displayed "sensorID"
# for each sensor

#sensorID_Case = "0000080222f8"
#sensorID_Shed = "04165661cdff"

# ======================================================================
# Drop into the script's main loop, which keeps on executing until the
# script abends or is cancelled:
#
#    - Reading temp, 
#    - Checking to see if we need heating or cooling, and
#    - Writing temps to the log file

while True:
#   --------------------------------------------
#   See if we need to start a new 24-hour log
#
#   NB: re/"a" vs "w".... Greater Minds have decreed
#       there is no sense in using "w"... because
#       with "a" if the file does not exist, it 
#       gets created same as if we used "w".


    
#   --------------------------------------------
#   Loop through the available sensors (only 2 assumed,
#   for which we experimentally determined their IDs 
#   and hard-coded them into this script)
        
    for mySensor in W1ThermSensor.get_available_sensors():
        curSensorID = mySensor.id
        curTempC = round(float(mySensor.get_temperature()),1)   
        print (curSensorID,curTempC)
    myTimeStamp = datetime.datetime.now().strftime("%Y-%m-%d@%H:%M:%S")
    print(myTimeStamp)
    
    iO.output(relaySensors, False)
    time.sleep(5)
    iO.output(relaySensors, True)
#       ---------------------------------------
#       Identify/assign temp as Case or Shed

#        if curSensorID == sensorID_Case:
#            myTempCaseC = curTempC
#        elif curSensorID == sensorID_Shed:
#            myTempShedC = curTempC
#        else:
#            print("Unexpected SensorID=" + curSensorID)
            
#       ---------------------------------------
#       When we have temps for both inside computer 
#       case and shed, turn heating/cooling on/off
#       accordingly and then write to the 2 logs
#
#       Yes, this will break if/when we do not have
#       both sensors present....



#            myTempPiC = round(float(getPiCPUtemperature()),1)
#            myTempCaseF = round(float(celsiusToFahrenheit(myTempCaseC)))
#            myTempShedF = round(float(celsiusToFahrenheit(myTempShedC)))
#           -------------------------------------
#           Just for testing/debugging, print some
#           info on the console

#            print("ServerCase=" + str(myTempCaseC) + "C / " + str(myTempCaseF) + "F  Shed=" + str(myTempShedC) + "C / " + str(myTempShedF) + "F   TempState=" + str(curTempState) + "   PiCPU=" + str(myTempPiC) + " at " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")) 
   
    time.sleep(60)
#   sys.exit
