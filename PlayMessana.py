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
MessanaSystem = {   'system' : {
                        'mName' : '/api/system/name', 
                       # 'mApiVer' : '/api/system/apiVersion',
                        'mStatus':'/api/system/status',
                        'mATUcount':'/api/system/atuCount',
                        'mDHWcount':'/api/system/dhwCount',
                        'mFanCoilCount':'/api/system/fancoilCount',
                        'mEnergySourceCount':'/api/system/energySourceCount',
                        'mZoneCount':'/api/system/zoneCount',
                        'mMacrozoneCount':'/api/system/macrozoneCount',
                        'mGroupCount':'/api/system/groupCount',
                        'mBufTankCount':'/api/system/bufferTankCount',
                        'mUnitTemp':'/api/system/tempUnit',
                        'mEnergySaving':'/api/system/energySaving',
                        'mSetback':'/api/system/setback',
                        'mExternalAlarm':'/api/system/externalAlarm'
                    },
                    'zones': {  
                        'mName': '/api/zone/name', 
                        'mSetPoint' :'/api/zone/setpoint', 
                        'mStatus':'/api/zone/status',
                        'mHumSetPointRH': '/api/zone/humidSetpointRH',
                        'mHumSetPointDP':'/api/zone/humidSetpointDP',
                        'mHumSetPointRH':'/api/zone/dehumSetpointRH',
                        'mDehumSetPointDP':'/api/zone/dehumSetpointDP',
                        'mDehumSetPointRH':'/api/zone/currentSetpointRH',
                        'mCurrentSetPoint':'/api/zone/currentSetpointDP',
                        'mHumidity':'/api/zone/humidity',
                        'mDewPoint' : '/api/zone/dewpoint',
                        'mTemp' :'/api/zone/temperature',
                        'mAirQuality' : '/api/zone/airQuality',
                        'mScheduleOn' : '/api/zone/scheduleOn',
                        'mCO2' : '/api/zone/co2',
                        'mAirTemp' : '/api/zone/airTemperature',
                        'mMacrozoneId' :'/api/zone/macrozoneId',
                        'mEnergySave' : '/api/zone/energySaving',
                        'mAlarmOn':'/api/zone/alarmOn',
                        'mThermalStatus':'/api/zone/thermalStatus',
                        'mCapability':'/api/zone/capability'
                    },
                    'macrozones' : {
                        'mName': '/api/macrozone/name', 
                        'mSetPoint' :'/api/macrozone/setpoint', 
                        'mStatus':'/api/macrozone/status',
                        'mScheduleOn' : '/api/zone/scheduleOn',
                        'mHumidity':'/api/macrozone/humidity',
                        'mDewPoint' : '/api/macrozone/dewpoint',
                        'mTemp' :'/api/macrozone/temperature'
                    },
                    'HCChangeOvers' :{
                        'mName':'/api/hc/name',
                        'mMode':'/api/hc/mode',
                        'mExcutiveSession':'/api/hc/executiveSeason',
                        'mAdaptiveComfort':'/api/hc/adaptiveComfort'
                    },
                    'FanCoils' :{
                        'mName':'/api/fan/name',
                        'mState':'/api/fan/state',
                        'mCoolingSpeed':'/api/fan/coolingSpeed',
                        'mHeatingSpeed':'/api/fan/heatingSpeed',
                        'mType':'/api/fan/type',
                        'mAlarmOn':'/api/fan/alarmOn'
                    },
                    'ATU': {
                        'mName':'/api/atu/name',
                        'mFlowLevel':'/api/atu/flowLevel',
                        'mStatus':'/api/atu/status',
                        'HRVOn':'/api/atu/hrvOn',
                        'mHUMOn':'/api/atu/humOn',
                        'mNTDOn':'/api/atu/ntdOn',
                        'mINTOn':'/api/atu/intOn',
                        'mHumidity':'/api/atu/humidity',
                        'mDewPoint':'/api/atu/dewpoint',
                        'mTargetAirTemp':'/api/atu/targetAirTemperature',
                        'mDehumudityStatus':'/api/atu/dehumidificationStatus',
                        'mHumidityStatus':'/api/atu/humidificationStatus',
                        'mHRVstatus':'/api​/atu​/hrvStatus',
                        'mIntegrationStatus':'/api/atu/integrationStatus',
                        'mAlarmOn':'/api/atu/alarmOn',
                        'mAirTemp':'/api/atu/airTemperature'
                    },
                    'EnergySources' :{
                        'mName':'/api/enr/name',
                        'mStatus':'/api/enr/status',
                        'mDHWtatus':'/api/enr/dhwStatus',
                        'mType':'/api/enr/type',
                        'mAlarmOn':'/api/enr/alarmOn'
                    },
                    'BufferTank' : {
                        'mName':'/api/tnk/name',
                        'mStatus':'/api/tnk/status',
                        'mMode':'/api/tnk/mode',
                        'mTemp':'/api/tnk/temperature',
                        'mAlarmOn':'/api/tnk/alarmOn'
                    },
                    'DomseticHotWater':{
                        'mStatus':'/api/dhw/status',
                        'mName':'/api/dhw/name',
                        'mTemp':'/api/dhw/temperature',
                        'mTargetTemp':'/api/dhw/targetTemperature'
                    }
                }


messanaAPIKey = 'apikey=9bf711fc-54e2-4387-9c7f-991bbb02ab3a'
MessanaIP = 'http://192.168.2.45'






zoneNameKey = 'zoneName'
zoneSetPtKey = 'setPoint'
RESPONSE_OK = '<Response [200]>'

#GetStr =MessanaIP+'/api/system/zoneCount/?'+ messanaAPIKey

#zones =  requests.get(GetStr).json()
#GetStr =MessanaIP+'/api/macrozone/name/0?'+ messanaAPIKey
#zones1 =  requests.get(GetStr).json()
#MessanaSystem['zoneCount'] = zones['count']

systemDict = {}
zoneDict = defaultdict(list)
macrozoneDict = defaultdict(list)

def getMessanaSystemData( MessanaSystem, mKey, systemDict):

    temp = {}
    GetStr =MessanaIP+MessanaSystem[mKey] + '/?' + messanaAPIKey
    systemTemp = requests.get(GetStr)
    if str(systemTemp) == RESPONSE_OK:
       systemTemp = systemTemp.json()
       #jsonKey= list(systemTemp.keys())[0]
       temp[mKey] = systemTemp[str(list(systemTemp.keys())[0])]
       systemDict.update(temp)
       return True
    else:
        print(str(mKey) + ' error')
        return False 


def getMessanaZoneData(MessanaZone, mKey, zoneDict):
    temp={}
    for i in range(0, zoneDict['zoneCount']):

        GetStr =MessanaIP+MessanaZone[mKey] +'/'+str(i)+'?'+ messanaAPIKey
        zoneTemp = requests.get(GetStr)
        if str(zoneTemp) == RESPONSE_OK:
            zoneTemp = zoneTemp.json()
            temp[mKey] = zoneTemp[str(list(zoneTemp.keys())[0])]
            zoneDict[i].update(temp)
        else:
            print('error')

def getMessanaSubSystemData(MessanaSubSys, Count, mKey, subDict):
   
    for i in range(0, Count):
        temp={}
        GetStr =MessanaIP+MessanaSubSys[mKey]+'/'+str(i)+'?'+ messanaAPIKey
        zoneTemp = requests.get(GetStr)
        if str(zoneTemp) == RESPONSE_OK:
            zoneTemp = zoneTemp.json()
            temp[mKey] = zoneTemp[str(list(zoneTemp.keys())[0])]
            subDict[i].append(temp)
        else:
            print(str(mKey) + ' error')


#getMessanaZoneData(MessanaSystem['zones'],  namedZones)
#getMessanaZoneData(MessanaSystem['zones']['mSetPoint'], namedZones)
for nSystemKey in MessanaSystem['system']:
    getMessanaSystemData(MessanaSystem['system'], nSystemKey, systemDict)

for mMacrozoneKey in MessanaSystem['macrozones']:
   getMessanaSubSystemData(MessanaSystem['macrozones'],systemDict['mMacrozoneCount'], mMacrozoneKey, macrozoneDict)

for mZoneKey in MessanaSystem['zones']:
   getMessanaSubSystemData(MessanaSystem['zones'],systemDict['mZoneCount'], mZoneKey, zoneDict)


print()


