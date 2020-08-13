#import polyinterface
import os
import sys
import glob
import time
import datetime
import os,subprocess
import json
import requests
from collections import defaultdict


#sys.stdout = open('MEssanaoutput.txt','wt')
class MessanaInfo:
    def __init__ (self):
        self.mSystem = defaultdict(dict)
        self.mSystem = {'system' : {
                            'mName' : '/api/system/name/', 
                            'mApiVer' : '/api/system/apiVersion/',
                            'mStatus':'/api/system/status/',
                            'mATUcount':'/api/system/atuCount/',
                            'mDHWcount':'/api/system/dhwCount/',
                            'mFanCoilCount':'/api/system/fancoilCount/',
                            'mEnergySourceCount':'/api/system/energySourceCount/',
                            'mZoneCount':'/api/system/zoneCount/',
                            'mMacrozoneCount':'/api/system/macrozoneCount/',
                            'mHCGroupCount':'/api/system/HCgroupCount/',
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
                            'mName': '/api/macro/name/', 
                            'mSetPoint' :'/api/macro/setpoint/', 
                            'mStatus':'/api/macro/status/',
                            'mScheduleOn' : '/api/zone/scheduleOn/',
                            'mHumidity':'/api/macro/humidity/',
                            'mDewPoint' : '/api/macro/dewpoint/',
                            'mTemp' :'/api/macro/temperature/'
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
                            'mTargetAirTemp':'/api/atu/targetAirTemperature/',
                            'mDehumudityStatus':'/api/atu/dehumidificationStatus/',
                            'mHumidityStatus':'/api/atu/humidificationStatus/',
                            'mHRVstatus':'/api?/atu?/hrvStatus/',
                            'mIntegrationStatus':'/api/atu/integrationStatus/',
                            'mAlarmOn':'/api/atu/alarmOn/',
                            'mAirTemp':'/api/atu/airTemperature/',
                            'mHumSetpointRH':'/api/atu/humidSetpointRH',
                            'mHumSetpointDP':'/api/atu/humidSetpointDP',
                            'mDehumSetpointRH':'/api/atu/dehumSetpointRH',
                            'mDehumSetpointDP':'/api/atu/dehumSetpointDP',
                            'mCurrentSetpointRH':'/api/atu/currentSetpointRH',
                            'mCurrentSetpointDP':'/api/atu/currentSetpointDP'
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
                            # 'mStatus':'/api/tnk/status/',
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
    
        self.APIKey = 'apikey'
        self.APIKeyVal = '9bf711fc-54e2-4387-9c7f-991bbb02ab3a'
        self.APIStr =self.APIKey + '='+ self.APIKeyVal
        self.IP = '192.168.2.65'

        self.RESPONSE_OK = '<Response [200]>'
        self.RESPONSE_NO_SUPPORT = '<Response [400]>'
        self.RESPONSE_NO_RESPONSE = '<Response [404]>'

        self.systemDict = defaultdict(list)
        self.zoneDict = defaultdict(dict)
        self.macrozoneDict = defaultdict(dict)
        self.hc_changeoverDict = defaultdict(dict)
        self.fan_coilsDict = defaultdict(dict)
        self.atusDict =defaultdict(dict)
        self.energy_sourcesDict = defaultdict(dict)
        self.buffer_tanksDict = defaultdict(dict)
        self.domsetic_hot_waterDict =defaultdict(dict)

    def setIP (self, mIPAddress, mAPIKeyVal):
        self.APIKeyVal = mAPIKeyVal
        self.APIStr = self.APIKey + '='+ mAPIKeyVal
        self.IP ='htp://'+ mIPAddress


    def retrieveSystemData(self):
        GETStr =self.IP+self.mSystem[mKey] + '?' + self.APIStr 
        print('\n' +  GETStr)
        systemTemp = requests.get(GETStr)
        if str(systemTemp) == self.RESPONSE_OK:
            systemTemp = systemTemp.json()
            self.systemDict[mKey] = systemTemp[str(list(systemTemp.keys())[0])]
            return True
        else:
            print(str(mKey) + ' error')
            self.systemDict[mKey] = -1
            return False 


    '''
    def getSubSystemData(mSystem, Count, mKey, subSysDict):
        for mId in range(0, Count):
            GETStr =MessanaIP+mSystem[mKey]+str(mId)+'?'+ massanaAPIStr 
            subSysTemp = requests.get(GETStr)
            if str(subSysTemp) == RESPONSE_OK:
                subSysTemp = subSysTemp.json()
                subSysDict[mId][mKey] =subSysTemp[str(list(subSysTemp.keys())[0])]
            else:
                print(str(mKey) + ' error for id: ', mId)

    '''


    def putSystem(self, mSystem, mKey, value, systemDict):
        mData = defaultdict(list)
        PUTStr = self.IP+mSystem[mKey] 
        print('\n' + PUTStr)
        mData = {'value':value, self.APIKey : self.APIKeyVal}
        resp = requests.put(PUTStr, mData)
        if str(resp) == self.RESPONSE_OK:
            systemDict[mKey] = value
            return True
        else:
            print (str(resp)+ ': Not able to PUT Key: : '+ mKey + ' value:', str(value) )
            return False


    def putSubSystem(self, mSystem, mKey, id, value, subSysDict):
        PUTStr = self.IP+mSystem[mKey] 
        value = subSysDict[id][mKey]
        print('\n' + PUTStr + ' ' + str(value))

        mData = {'id':id, 'value': value, self.APIKey : self.APIKeyVal}
        resp = requests.put(PUTStr, mData)
        if str(resp) == self.RESPONSE_OK:
            subSysDict[id][mKey] = value
            return True
        elif str(resp) == self.RESPONSE_NO_SUPPORT:
            temp1 =  resp.content
            res_dict = json.loads(temp1.decode('utf-8')) 
            mData['error'] = str(resp) + ': Not able to PUT key: '+ str(res_dict.values()) + ' Subnode ' + str(id) + ' for key: ' + str(mKey) + ' value:', str(value)
            print(mData['error'])
            mData['statusOK'] =False
        elif str(resp) == self.RESPONSE_NO_RESPONSE:
            mData['error'] = str(resp) + ': Error: No response from API:  Subnode ' + str(id) + ' for key: ' + str(mKey)+ ' value:', str(value)
            print(mData['error'])
            mData['statusOK'] =False
        else:
            mData['error'] = str(resp) + ': Error: Unklown: Subnode ' + str(id) + ' for key: ' + str(mKey)+ ' value:', str(value)
            print(mData['error'])
            mData['statusOK'] =False
            return False

    def retrieveSubNodeData(self, mSystem, instNbr, mKey, mData):
        GETStr =self.IP+mSystem[mKey]+str(instNbr)+'?'+ self.APIStr 
        print('\n' +  GETStr)
        subSysTemp = requests.get(GETStr)
        if str(subSysTemp) == self.RESPONSE_OK:
            subSysTemp = subSysTemp.json()
            mData['data']  = subSysTemp[str(list(subSysTemp.keys())[0])]
            mData['statusOK'] =True
        elif str(subSysTemp) == self.RESPONSE_NO_SUPPORT:
            temp1 =  subSysTemp.content
            res_dict = json.loads(temp1.decode('utf-8')) 
            mData['error'] = str(subSysTemp) + ': Error: '+ str(res_dict.values()) + ' Subnode ' + str(instNbr) + ' for id: ' + str(mKey)
            mData['statusOK'] =False
        elif str(subSysTemp) == self.RESPONSE_NO_RESPONSE:
            mData['error'] = str(subSysTemp) + ': Error: No response from API:  Subnode ' + str(instNbr) + ' for id: ' + str(mKey)
            mData['statusOK'] =False
        else:
            mData['error'] = str(subSysTemp) + ': Error: Unknown: Subnode ' + str(instNbr) + ' for id: ' + str(mKey)
            mData['statusOK'] =False


    def retrieveSubSystemData(self, MessanaSubSystem, instNbr, subSysDict):
        for mKey in MessanaSubSystem:
            mData = {}
            self.retrieveSubNodeData(MessanaSubSystem, instNbr, mKey, mData)
            if mData['statusOK']:
                subSysDict[instNbr][mKey] = mData['data']
            else:
                print(mData['error'])


messana = MessanaInfo()


#Retrive basic system info
print('\nSYSTEM')
for mSystemKey in messana.mSystem['system']:
    messana.retrieveSystemData(messana.mSystem['system'], mSystemKey, systemDict)

print('\nZONES')
for zoneNbr in range(0,systemDict['mZoneCount']):
    messana.retrieveSubSystemData(messana.mSystem['zones'], zoneNbr, zoneDict)

print('\nMACROZONES')
for mzoneNbr in range(0,systemDict['mMacrozoneCount']):
    messana.retrieveSubSystemData(messana.mSystem['macrozones'], mzoneNbr, macrozoneDict)

print('\nhc_changeover')
for hcchangeoverNbr in range (0,systemDict['mHCGroupCount']):
    messana.retrieveSubSystemData(messana.mSystem['hc_changeover'],hcchangeoverNbr , hc_changeoverDict)

print('\nFAN COILS')
for fcNbr in range(0,systemDict['mFanCoilCount']):
    messana.retrieveSubSystemData(messana.mSystem['fan_coils'], fcNbr, fan_coilsDict)

print('\nATU')
for zoneNbr in range(0,systemDict['mATUcount']):
    messana.retrieveSubSystemData(messana.mSystem['atus'], zoneNbr, atusDict)

print('\nBUFFER TANK')
for zoneNbr in range(0,systemDict['mBufTankCount']):
    retrieveSubSystemData(messana.mSystem['buffer_tanks'], zoneNbr, buffer_tanksDict)

print('\nENERGY SOURCE')
for zoneNbr in range(0,systemDict['mEnergySourceCount']):
    messana.retrieveSubSystemData(messana.mSystem['energy_sources'], zoneNbr, energy_sourcesDict)

print('\nDHW')
for zoneNbr in range(0,systemDict['mDHWcount']):
    messana.retrieveSubSystemData(messana.mSystem['domsetic_hot_waters'], zoneNbr, domsetic_hot_waterDict)

print('\n end extracting data')

print('\nSYSTEM - PUT')
for mKey in systemDict:
    putmessana.mSystem(messana.mSystem['system'], mKey, systemDict[mKey], systemDict)

print('\nZONES - PUT')
for zoneNbr in zoneDict:
    for mKey in zoneDict[zoneNbr]:
        putMessanaSubSystem(messana.mSystem['zones'], mKey, zoneNbr,zoneDict[zoneNbr][mKey], zoneDict)
        

print('\nMACROZONES - PUT')
for macrozoneNbr in macrozoneDict:
    for mKey in macrozoneDict[macrozoneNbr]:
        putSubSystem(messana.mSystem['macrozones'], mKey, macrozoneNbr, macrozoneDict[macrozoneNbr][mKey], macrozoneDict)

print('\nhc_changeover - PUT')
for hcgroupcountNbr in hc_changeoverDict:
    for mKey in hc_changeoverDict[hcgroupcountNbr]:
        putSubSystem(messana.mSystem['hc_changeover'], mKey, hcgroupcountNbr, hc_changeoverDict[hcgroupcountNbr][mKey], hc_changeoverDict)

print('\nFAN COILS - PUT')
for fan_coilNbr in fan_coilsDict:
    for mKey in fan_coilsDict[fan_coilNbr]:
        putSubSystem(messana.mSystem['fan_coils'], mKey, fan_coilNbr, fan_coilsDict[fan_coilNbr][mKey], fan_coilsDict)

print('\nATU - PUT')
for atuNbr in atusDict:
    for mKey in atusDict[atuNbr]:
        putSubSystem(messana.mSystem['atus'], mKey, atuNbr, atusDict[atuNbr][mKey],  atusDict)

print('\nBUFFER TANK - PUT')
for bufferTankNbr in buffer_tanksDict:
    for mKey in buffer_tanksDict[bufferTankNbr]:
        putSubSystem(messana.mSystem['buffer_tanks'], mKey, bufferTankNbr, buffer_tanksDict[bufferTankNbr][mKey], buffer_tanksDict)

print('\nENERGY SOURCE - PUT')
for energySourceNbr in energy_sourcesDict:
    for mKey in energy_sourcesDict[energySourceNbr]:
        putSubSystem(messana.mSystem['energy_sources'], mKey, energySourceNbr, energy_sourcesDict[energySourceNbr][mKey], energy_sourcesDict)

print('\nDHW - PUT')
for DHwaterNbr in domsetic_hot_waterDict:
    for mKey in domsetic_hot_waterDict[DHwaterNbr]:
        putMessanaSubSystem(messana.mSystem['domsetic_hot_waters'], mKey, DHwaterNbr, domsetic_hot_waterDict[DHwaterNbr][mKey], domsetic_hot_waterDict)
print('\nEND put')
#sys.stdout.close() 
