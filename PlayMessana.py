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
                        'mName' : '/api/system/name/', 
                        #'mApiVer' : '/api/system/apiVersion/',
                        'mStatus':'/api/system/status/',
                        'mATUcount':'/api/system/atuCount/',
                        'mDHWcount':'/api/system/dhwCount/',
                        'mFanCoilCount':'/api/system/fancoilCount/',
                        'mEnergySourceCount':'/api/system/energySourceCount/',
                        'mZoneCount':'/api/system/zoneCount/',
                        'mMacrozoneCount':'/api/system/macrozoneCount/',
                        'mGroupCount':'/api/system/groupCount/',
                        'mBufTankCount':'/api/system/bufferTankCount/',
                        'mUnitTemp':'/api/system/tempUnit/',
                        'mEnergySaving':'/api/system/energySaving/',
                        'mSetback':'/api/system/setback/',
                        'mExternalAlarm':'/api/system/externalAlarm/'
                    },
                    'zones': {  
                        'mName': '/api/zone/name/', 
                        'mSetPoint' :'/api/zone/setpoint/', 
                        'mStatus':'/api/zone/status/',
                        'mHumSetPointRH': '/api/zone/humidSetpointRH/',
                        'mHumSetPointDP':'/api/zone/humidSetpointDP/',
                        'mDeumSetPointRH':'/api/zone/dehumSetpointRH/',
                        'mDehumSetPointDP':'/api/zone/dehumSetpointDP/',
                        'mCurrentSetPointRH':'/api/zone/currentSetpointRH/',
                        'mCurrentSetPointDP':'/api/zone/currentSetpointDP/',
                        'mHumidity':'/api/zone/humidity/',
                        'mDewPoint' : '/api/zone/dewpoint/',
                        'mTemp' :'/api/zone/temperature/',
                        'mAirQuality' : '/api/zone/airQuality/',
                        'mScheduleOn' : '/api/zone/scheduleOn/',
                        'mCO2' : '/api/zone/co2/',
                        'mAirTemp' : '/api/zone/airTemperature/',
                        'mMacrozoneId' :'/api/zone/macrozoneId/',
                        'mEnergySave' : '/api/zone/energySaving/',
                        'mAlarmOn':'/api/zone/alarmOn/',
                        'mThermalStatus':'/api/zone/thermalStatus/',
                        'mCapability':'/api/zone/capability/'
                    },
                    'macrozones' : {
                        'mName': '/api/macrozone/name/', 
                        'mSetPoint' :'/api/macrozone/setpoint/', 
                        'mStatus':'/api/macrozone/status/',
                        'mScheduleOn' : '/api/zone/scheduleOn/',
                        'mHumidity':'/api/macrozone/humidity/',
                        'mDewPoint' : '/api/macrozone/dewpoint/',
                        'mTemp' :'/api/macrozone/temperature/'
                    },
                    'hc_changeover' :{
                        'mName':'/api/hc/name/',
                        'mMode':'/api/hc/mode/',
                        'mExcutiveSession':'/api/hc/executiveSeason/',
                        'mAdaptiveComfort':'/api/hc/adaptiveComfort/'
                    },
                    'fan_coils' :{
                        'mName':'/api/fan/name/',
                        'mState':'/api/fan/state/',
                        'mCoolingSpeed':'/api/fan/coolingSpeed/',
                        'mHeatingSpeed':'/api/fan/heatingSpeed/',
                        'mType':'/api/fan/type/',
                        'mAlarmOn':'/api/fan/alarmOn/'
                    },
                    'atus': {
                        'mName':'/api/atu/name/',
                        'mFlowLevel':'/api/atu/flowLevel/',
                        'mStatus':'/api/atu/status/',
                        'HRVOn':'/api/atu/hrvOn/',
                        'mHUMOn':'/api/atu/humOn/',
                        'mNTDOn':'/api/atu/ntdOn/',
                        'mINTOn':'/api/atu/intOn/',
                        'mHumidity':'/api/atu/humidity/',
                        'mDewPoint':'/api/atu/dewpoint/',
                        'mTargetAirTemp':'/api/atu/targetAirTemperature/',
                        'mDehumudityStatus':'/api/atu/dehumidificationStatus/',
                        'mHumidityStatus':'/api/atu/humidificationStatus/',
                        'mHRVstatus':'/api​/atu​/hrvStatus/',
                        'mIntegrationStatus':'/api/atu/integrationStatus/',
                        'mAlarmOn':'/api/atu/alarmOn/',
                        'mAirTemp':'/api/atu/airTemperature/'
                    },
                    'energy_sources' :{
                        'mName':'/api/enr/name/',
                        'mStatus':'/api/enr/status/',
                        'mDHWtatus':'/api/enr/dhwStatus/',
                        'mType':'/api/enr/type/',
                        'mAlarmOn':'/api/enr/alarmOn/'
                    },
                    'buffer_tanks' : {
                        'mName':'/api/tnk/name/',
                        #'mStatus':'/api/tnk/status/',
                        'mMode':'/api/tnk/mode/',
                        'mTemp':'/api/tnk/temperature/',
                        'mAlarmOn':'/api/tnk/alarmOn/'
                    },
                    'domsetic_hot_waters':{
                        'mStatus':'/api/dhw/status/',
                        'mName':'/api/dhw/name/',
                        'mTemp':'/api/dhw/temperature/',
                        'mTargetTemp':'/api/dhw/targetTemperature/'
                    }
                }


messanaAPIKey = 'apikey=9bf711fc-54e2-4387-9c7f-991bbb02ab3a'
messanaAPIKeyList = {'apikey' : '9bf711fc-54e2-4387-9c7f-991bbb02ab3a'}
MessanaIP = 'http://192.168.2.45'
#MessanaIP ='http://olgaardtahoe1.mynetgear.com:3045'
RESPONSE_OK = '<Response [200]>'


systemDict = defaultdict(list)
zoneDict = defaultdict(list)
macrozoneDict = defaultdict(list)
hc_changeoverDict = defaultdict(list)
fan_coilsDict = defaultdict(list)
atuDict =defaultdict(list)
energy_sourcesDict = defaultdict(list)
buffer_tankDict = defaultdict(list)
domsetic_hot_waterDict =defaultdict(list)


def getMessanaSystemData( MessanaSystem, mKey, systemDict):
    temp = {}
    GETStr =MessanaIP+MessanaSystem[mKey] + '?' + messanaAPIKey
    systemTemp = requests.get(GETStr)
    if str(systemTemp) == RESPONSE_OK:
       systemTemp = systemTemp.json()
       temp[mKey] = systemTemp[str(list(systemTemp.keys())[0])]
       systemDict.update(temp)
       return True
    else:
        print(str(mKey) + ' error')
        temp[mKey] = -1
        systemDict.update(temp)
        return False 



def getMessanaSubSystemData(MessanaSystem, Count, mKey, subDict):
    for i in range(0, Count):
        temp={}
        GETStr =MessanaIP+MessanaSystem[mKey]+str(i)+'?'+ messanaAPIKey
        subSysTemp = requests.get(GETStr)
        if str(subSysTemp) == RESPONSE_OK:
            subSysTemp = subSysTemp.json()
            temp[mKey] = subSysTemp[str(list(subSysTemp.keys())[0])]
            subDict[i].append(temp)
        else:
            print(str(mKey) + ' error for id:', i)


def putMessanaSystem(MessanaSystem, mKey, value):
    PUTStr = MessanaIP+MessanaSystem[mKey] 
    data = {'value':value, 'apikey':'9bf711fc-54e2-4387-9c7f-991bbb02ab3a'}

    resp = requests.put(PUTStr, data)
    if str(resp) == RESPONSE_OK:
        return True
    else:
        return False


def putMessanaSubSystem(MessanaSystem, mKey, id, value ):
    PUTStr = MessanaIP+MessanaSystem[mKey] 
    data = {'id':id, 'value': value, 'apikey':'9bf711fc-54e2-4387-9c7f-991bbb02ab3a'}

    resp = requests.put(PUTStr, data)
    if str(resp) == RESPONSE_OK:
        return True
    else:
        return False


#Retrive basic system info
print('\nSYSTEM')
for nSystemKey in MessanaSystem['system']:
    getMessanaSystemData(MessanaSystem['system'], nSystemKey, systemDict)


'''
data1 = {'id': 0, 'value': 'DS Small Bedroom', 'apikey':'9bf711fc-54e2-4387-9c7f-991bbb02ab3a'}
PutStr = MessanaIP+'/api/zone/name/' 
resp = requests.put(PutStr, data1)
resp1 = resp.json()
'''


print('\nZONES')
if systemDict['mZoneCount'] > 0:
    for mKey in MessanaSystem['zones']:
        getMessanaSubSystemData(MessanaSystem['zones'],systemDict['mZoneCount'], mKey, zoneDict)

print('\nMACROZONES')
if systemDict['mMacrozoneCount'] > 0:
    for mKey in MessanaSystem['macrozones']:
        getMessanaSubSystemData(MessanaSystem['macrozones'],systemDict['mMacrozoneCount'], mKey, macrozoneDict)

print('\nhc_changeover')
for mKey in MessanaSystem['hc_changeover']:
    getMessanaSubSystemData(MessanaSystem['hc_changeover'],1, mKey, hc_changeoverDict)

print('\nFAN COILS')
if systemDict['mFanCoilCount'] > 0:
    for mKey in MessanaSystem['fan_coils']:
        getMessanaSubSystemData(MessanaSystem['fan_coils'],systemDict['mFanCoilCount'], mKey, fan_coilsDict )

print('\nATU')
if systemDict['mATUcount'] > 0:
    for mKey in MessanaSystem['atus']:
        getMessanaSubSystemData(MessanaSystem['atus'],systemDict['mATUcount'], mKey, atuDict)

print('\nBUFFER TANK')
if systemDict['mBufTankCount'] > 0:
    for mKey in MessanaSystem['buffer_tanks']:
        getMessanaSubSystemData(MessanaSystem['buffer_tanks'],systemDict['mBufTankCount'], mKey, buffer_tankDict)

print('\nENERGY SOURCE')
if systemDict['mEnergySourceCount'] > 0:
    for mKey in MessanaSystem['energy_sources']:
        getMessanaSubSystemData(MessanaSystem['energy_sources'],systemDict['mEnergySourceCount'], mKey, energy_sourcesDict)

print('\nDHW')
if systemDict['mDHWcount'] > 0:
    for mZoneKey in MessanaSystem['domsetic_hot_waters']:
        getMessanaSubSystemData(MessanaSystem['domsetic_hot_waters'],systemDict['mDHWcount'], mZoneKey, domsetic_hot_waterDict)

print('\n end')





