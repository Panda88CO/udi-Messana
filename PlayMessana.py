import os
import sys
import glob
import time
import datetime
import os,subprocess
import json
import requests
from collections import defaultdict


MessanaSystem = defaultdict(dict)
MessanaSystem = {   'zones': {  
                            'mName': '/api/zone/name', 
                            'mSetPoint' :'/api/zone/setpoint', 
                            'mStatus':'/api/zone/status',
                            'mHumSetPointRH': '/api/zone/humidSetpointRH',
                            'mHumidity':'/api/zone/humidity',
                            'mDewPoint' : '/api/zone/dewpoint',
                            'mTemp' :'/api/zone/temperature',
                            'mAirQuality' : '/api/zone/airQuality',
                            'mScheduleOn' : '/api/zone/scheduleOn',
                            'mCO2' : '/api/zone/co2',
                            'mAirTemp' : '/api/zone/airTemperature',
                            'mMacrozoneId' :'/api/zone/macrozoneId',
                            'mEnergySave' : '/api/zone/energySaving'
                    }
                    'macrozones' : {

                    },
                    'system' : {

                    },

                    'ATU': {

                    }
                }


messanaAPIKey = 'apikey=9bf711fc-54e2-4387-9c7f-991bbb02ab3a'
MessanaIP = 'http://192.168.2.45'






zoneNameKey = 'zoneName'
zoneSetPtKey = 'setPoint'
RESPONSE_OK = '<Response [200]>'

GetStr =MessanaIP+systemStr+'/zoneCount/?'+ messanaAPIKey
zones =  requests.get(GetStr).json()
MessanaSystem['zoneCount'] = zones['count']

namedZones= defaultdict(dict)
namedZones['zoneCount'] = MessanaSystem['zoneCount']

def getMessanaSystemData( MessanaKey, newKey, systemDict):
    temp={}
    GetStr =MessanaIP+systemStr+MessanaKey+'/?'+ messanaAPIKey
    systemTemp = requests.get(GetStr)
    if str(systemTemp) == RESPONSE_OK:
        systemTemp = systemTemp.json()
        jsonKey= list(systemTemp.keys())[0]
        temp[newKey] = systemTemp[str(jsonKey)]
        systemDict.update(temp)
    else:
        print('error')

def getMessanaZoneData(MessanaZone, mKey, zoneDict):
    temp={}
    for i in range(0, zoneDict['zoneCount']):
        GetStr =MessanaIP+MessanaZone[mKey]+'/'+str(i)+'?'+ messanaAPIKey
        zoneTemp = requests.get(GetStr)
        if str(zoneTemp) == RESPONSE_OK:
            zoneTemp = zoneTemp.json()
            temp[mKey] = zoneTemp[str(list(zoneTemp.keys())[0])]
            zoneDict[i].update(temp)
        else:
            print('error')


#getMessanaZoneData(MessanaSystem['zones'],  namedZones)
#getMessanaZoneData(MessanaSystem['zones']['mSetPoint'], namedZones)
for mZoneKeys in MessanaSystem['zones']:
   getMessanaZoneData(MessanaSystem['zones'], mZoneKeys, namedZones)
print()


