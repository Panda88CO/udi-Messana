#!/usr/bin/env python3
#import polyinterface
import sys
import requests
from subprocess import call
import json
from collections import defaultdict
from MessanaInfoPlay import MessanaInfo


#LOGGER = polyinterface.LOGGER
        
#sys.stdout = open('Messanaoutput.txt','wt')

messana = MessanaInfo('192.168.2.65' , '9bf711fc-54e2-4387-9c7f-991bbb02ab3a')
messana.init()

#Retrive basic system info
print('\nSYSTEM')
messana.updateSystemData()
systemGETKeys = messana.systemPullKeys()
systemPUTKeys = messana.systemPushKeys()
systemActiveKeys = messana.systemActiveKeys()
