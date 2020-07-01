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
                        'mHCGroupCount':'/api/system/groupCount/',
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
                        'mExcutiveSeason':'/api/hc/executiveSeason/',
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
                        'mDHWstatus':'/api/enr/dhwStatus/',
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

messanaAPIKey = 'apikey'
messanaAPIKeyVal = '9bf711fc-54e2-4387-9c7f-991bbb02ab3a'
massanaAPIStr =messanaAPIKey + '='+ messanaAPIKeyVal

#MessanaIP = 'http://192.168.2.45'
MessanaIP ='http://olgaardtahoe1.mynetgear.com:3045'
RESPONSE_OK = '<Response [200]>'


systemDict = defaultdict(list)
zoneDict = defaultdict(dict)
macrozoneDict = defaultdict(dict)
hc_changeoverDict = defaultdict(dict)
fan_coilsDict = defaultdict(dict)
atusDict =defaultdict(dict)
energy_sourcesDict = defaultdict(dict)
buffer_tanksDict = defaultdict(dict)
domsetic_hot_waterDict =defaultdict(dict)



def retrieveMessanaSystemData( MessanaSystem, mKey, systemDict):
    GETStr =MessanaIP+MessanaSystem[mKey] + '?' + massanaAPIStr 
    systemTemp = requests.get(GETStr)
    if str(systemTemp) == RESPONSE_OK:
       systemTemp = systemTemp.json()
       systemDict[mKey] = systemTemp[str(list(systemTemp.keys())[0])]
       return True
    else:
        print(str(mKey) + ' error')
        systemDict[mKey] = -1
        return False 


'''
def getMessanaSubSystemData(MessanaSystem, Count, mKey, subSysDict):
    for mId in range(0, Count):
        GETStr =MessanaIP+MessanaSystem[mKey]+str(mId)+'?'+ massanaAPIStr 
        subSysTemp = requests.get(GETStr)
        if str(subSysTemp) == RESPONSE_OK:
            subSysTemp = subSysTemp.json()
            subSysDict[mId][mKey] =subSysTemp[str(list(subSysTemp.keys())[0])]
        else:
            print(str(mKey) + ' error for id: ', mId)

'''


def putMessanaSystem(MessanaSystem, mKey, value, systemDict):
    mData = defaultdict(list)
    PUTStr = MessanaIP+MessanaSystem[mKey] 
    mData = {'value':value, messanaAPIKey : messanaAPIKeyVal}
    resp = requests.put(PUTStr, mData)
    if str(resp) == RESPONSE_OK:
        systemDict[mKey] = value
        return True
    else:
        print (str(resp)+ ': Not able to PUT Key: : '+ mKey + ' value:', str(value) )
        return False


def putMessanaSubSystem(MessanaSystem, mKey, id, value, subSysDict ):
    PUTStr = MessanaIP+MessanaSystem[mKey] 
    value = subSysDict[id][mKey]
    mData = {'id':id, 'value': value, messanaAPIKey : messanaAPIKeyVal}
    resp = requests.put(PUTStr, mData)
    if str(resp) == RESPONSE_OK:
       subSysDict[id][mKey] = value
       return True
    else:
        print (str(resp) + ': Not able to PUT key:'+ mKey + ' iD: '+ str(id) + ' value:', str(value) )
        return False

def retrieveMessanaSubNodeData(MessanaSystem, instNbr, mKey, mData):
    GETStr =MessanaIP+MessanaSystem[mKey]+str(instNbr)+'?'+ massanaAPIStr 
    subSysTemp = requests.get(GETStr)
    if str(subSysTemp) == RESPONSE_OK:
       subSysTemp = subSysTemp.json()
       mData['data']  = subSysTemp[str(list(subSysTemp.keys())[0])]
       mData['statusOK'] =True
    else:
       mData['error'] = str(subSysTemp) + ': Error: Subnode ' + str(instNbr) + ' for id: ' + str(mKey)
       mData['statusOK'] =False

def retrieveMessanaSubSystemData(MessanaSubSystem, instNbr, subSysDict):
     for mKey in MessanaSubSystem:
        mData = {}
        retrieveMessanaSubNodeData(MessanaSubSystem, instNbr, mKey, mData)
        if mData['statusOK']:
           subSysDict[instNbr][mKey] = mData['data']
        else:
           print(mData['error'])




#Retrive basic system info
print('\nSYSTEM')
for nSystemKey in MessanaSystem['system']:
    retrieveMessanaSystemData(MessanaSystem['system'], nSystemKey, systemDict)

print('\nZONES')
for zoneNbr in range(0,systemDict['mZoneCount']):
    retrieveMessanaSubSystemData(MessanaSystem['zones'], zoneNbr, zoneDict)

print('\nMACROZONES')
for mzoneNbr in range(0,systemDict['mMacrozoneCount']):
    retrieveMessanaSubSystemData(MessanaSystem['macrozones'], mzoneNbr, macrozoneDict)

print('\nhc_changeover')
for hcchangeoverNbr in range (0,systemDict['mHCGroupCount']):
    retrieveMessanaSubSystemData(MessanaSystem['hc_changeover'],hcchangeoverNbr , hc_changeoverDict)

print('\nFAN COILS')
for fcNbr in range(0,systemDict['mFanCoilCount']):
    retrieveMessanaSubSystemData(MessanaSystem['fan_coils'], fcNbr, fan_coilsDict)

print('\nATU')
for zoneNbr in range(0,systemDict['mATUcount']):
    retrieveMessanaSubSystemData(MessanaSystem['atus'], zoneNbr, atusDict)

print('\nBUFFER TANK')
for zoneNbr in range(0,systemDict['mBufTankCount']):
    retrieveMessanaSubSystemData(MessanaSystem['buffer_tanks'], zoneNbr, buffer_tanksDict)

print('\nENERGY SOURCE')
for zoneNbr in range(0,systemDict['mEnergySourceCount']):
    retrieveMessanaSubSystemData(MessanaSystem['energy_sources'], zoneNbr, energy_sourcesDict)

print('\nDHW')
for zoneNbr in range(0,systemDict['mDHWcount']):
    retrieveMessanaSubSystemData(MessanaSystem['domsetic_hot_waters'], zoneNbr, domsetic_hot_waterDict)

print('\n end extracting data')

print('\nSYSTEM - PUT')
for mKey in systemDict:
    putMessanaSystem(MessanaSystem['system'], mKey, systemDict[mKey], systemDict)

print('\nZONES - PUT')
for zoneNbr in zoneDict:
    for mKey in zoneDict[zoneNbr]:
        putMessanaSubSystem(MessanaSystem['zones'], mKey, zoneNbr,zoneDict[zoneNbr][mKey], zoneDict)

print('\nMACROZONES - PUT')
for macrozoneNbr in macrozoneDict:
    for mKey in macrozoneDict[macrozoneNbr]:
        putMessanaSubSystem(MessanaSystem['macrozones'], mKey, macrozoneNbr, macrozoneDict[macrozoneNbr][mKey], macrozoneDict)

print('\nhc_changeover - PUT')
for hcgroupcountNbr in hc_changeoverDict:
    for mKey in hc_changeoverDict[hcgroupcountNbr]:
        putMessanaSubSystem(MessanaSystem['hc_changeover'], mKey, hcgroupcountNbr, hc_changeoverDict[hcgroupcountNbr][mKey], hc_changeoverDict)

print('\nFAN COILS - PUT')
for fan_coilNbr in fan_coilsDict:
    for mKey in fan_coilsDict[fan_coilNbr]:
        putMessanaSubSystem(MessanaSystem['fan_coils'], mKey, fan_coilNbr, fan_coilsDict[fan_coilNbr][mKey], fan_coilsDict)

print('\nATU - PUT')
for atuNbr in atusDict:
    for mKey in atusDict[atuNbr]:
        putMessanaSubSystem(MessanaSystem['atus'], mKey, atuNbr, atusDict[atuNbr][mKey],  atusDict)

print('\nBUFFER TANK - PUT')
for bufferTankNbr in buffer_tanksDict:
    for mKey in buffer_tanksDict[bufferTankNbr]:
        putMessanaSubSystem(MessanaSystem['buffer_tanks'], mKey, bufferTankNbr, buffer_tanksDict[bufferTankNbr][mKey], buffer_tanksDict)

print('\nENERGY SOURCE - PUT')
for energySourceNbr in energy_sourcesDict:
    for mKey in energy_sourcesDict[energySourceNbr]:
        putMessanaSubSystem(MessanaSystem['energy_sources'], mKey, energySourceNbr, energy_sourcesDict[energySourceNbr][mKey], energy_sourcesDict)

print('\nDHW - PUT')
for DHwaterNbr in domsetic_hot_waterDict:
    for mKey in domsetic_hot_waterDict[DHwaterNbr]:
        putMessanaSubSystem(MessanaSystem['domsetic_hot_waters'], mKey, DHwaterNbr, domsetic_hot_waterDict[DHwaterNbr][mKey], domsetic_hot_waterDict)
print('\nEND put')
