
import os
import glob
import time
import datetime
#import RPi.GPIO as iO
import os,subprocess
from subprocess import call
#from w1thermsensor import W1ThermSensor
import json
import requests



messanaAPIKey = 'apikey=9bf711fc-54e2-4387-9c7f-991bbb02ab3a'
MessanaIP = 'http://192.168.2.45'
systemStr = '/api/system/'
zoneStr = '/api/zone'



nbrZones =  requests.get(MessanaIP+systemStr+'/zoneCount/?'+ messanaAPIKey )


