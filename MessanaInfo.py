#!/usr/bin/env python3
import polyinterface
import requests
from subprocess import call
import json
from collections import defaultdict

LOGGER = polyinterface.LOGGER

class MessanaInfo:
    def __init__ (self, mIPaddress, mAPIKeyVal):
        self.mSystem = defaultdict(dict)
        self.mSystem = {'system': {
                            'mName' : '/api/system/name/'
                            ,'mApiVer' : '/api/system/apiVersion/'
                            ,'mStatus':'/api/system/status/'
                            ,'mATUcount':'/api/system/atuCount/'
                            ,'mDHWcount':'/api/system/dhwCount/'
                            ,'mFanCoilCount':'/api/system/fancoilCount/'
                            ,'mEnergySourceCount':'/api/system/energySourceCount/'
                            ,'mZoneCount':'/api/system/zoneCount/'
                            ,'mMacrozoneCount':'/api/system/macrozoneCount/'
                            ,'mHC_changeoverCount':'/api/system/HCgroupCount/'
                            ,'mBufTankCount':'/api/system/bufferTankCount/'
                            ,'mUnitTemp':'/api/system/tempUnit/'
                            ,'mEnergySaving':'/api/system/energySaving/'
                            ,'mSetback':'/api/system/setback/'
                            ,'mExternalAlarm':'/api/system/externalAlarm/'
                            },
                        'zones': {  
                            'mName': '/api/zone/name/'
                            ,'mSetPoint' :'/api/zone/setpoint/'
                            ,'mStatus':'/api/zone/status/'
                            ,'mHumSetPointRH': '/api/zone/humidSetpointRH/'
                            ,'mHumSetPointDP':'/api/zone/humidSetpointDP/'
                            ,'mDeumSetPointRH':'/api/zone/dehumSetpointRH/'
                            ,'mDehumSetPointDP':'/api/zone/dehumSetpointDP/'
                            #,'mCurrentSetPointRH':'/api/zone/currentSetpointRH/'
                            #,'mCurrentSetPointDP':'/api/zone/currentSetpointDP/'
                            ,'mHumidity':'/api/zone/humidity/'
                            ,'mDewPoint' : '/api/zone/dewpoint/'
                            ,'mTemp' :'/api/zone/temperature/'
                            #,'mAirQuality' : '/api/zone/airQuality/'
                            ,'mScheduleOn' : '/api/zone/scheduleOn/'
                            ,'mCO2' : '/api/zone/co2/'
                            ,'mAirTemp' : '/api/zone/airTemperature/'
                            ,'mMacrozoneId' :'/api/zone/macrozoneId/'
                            ,'mEnergySave' : '/api/zone/energySaving/'
                            ,'mAlarmOn':'/api/zone/alarmOn/'
                            ,'mThermalStatus':'/api/zone/thermalStatus/'
                            ,'mCapability':'/api/zone/capability/'
                            },
                        'macrozones' : {
                            'mName': '/api/macrozone/name/'
                            ,'mSetPoint' :'/api/macrozone/setpoint/'
                            ,'mStatus':'/api/macrozone/status/'
                            ,'mScheduleOn' : '/api/macrozone/scheduleOn/'
                            ,'mHumidity':'/api/macrozone/humidity/'
                            ,'mDewPoint' : '/api/macrozone/dewpoint/'
                            ,'mTemp' :'/api/macrozone/temperature/'
                            },
                        'hc_changeover' :{
                            'mName':'/api/hc/name/'
                            ,'mMode':'/api/hc/mode/'
                            ,'mExcutiveSeason':'/api/hc/executiveSeason/'
                            ,'mAdaptiveComfort':'/api/hc/adaptiveComfort/'
                            },
                        'fan_coils' :{
                            'mName':'/api/fan/name/'
                            ,'mState':'/api/fan/state/'
                            ,'mCoolingSpeed':'/api/fan/coolingSpeed/'
                            ,'mHeatingSpeed':'/api/fan/heatingSpeed/'
                            ,'mType':'/api/fan/type/'
                            ,'mAlarmOn':'/api/fan/alarmOn/'
                            },
                        'atus': {
                            'mName':'/api/atu/name/'
                            ,'mFlowLevel':'/api/atu/flowLevel/'
                            ,'mStatus':'/api/atu/status/'
                            ,'HRVOn':'/api/atu/hrvOn/'
                            ,'mHUMOn':'/api/atu/humOn/'
                            ,'mNTDOn':'/api/atu/ntdOn/'
                            ,'mINTOn':'/api/atu/intOn/'
                            ,'mDehumudityStatus':'/api/atu/dehumidificationStatus/'
                            ,'mHumidityStatus':'/api/atu/humidificationStatus/'
                            ,'mHRVstatus':'/api/atu/status/'
                            ,'mIntegrationStatus':'/api/atu/integrationStatus/'
                            ,'mAlarmOn':'/api/atu/alarmOn/'
                            ,'mAirTemp':'/api/atu/airTemperature/'
                            ,'mHumSetpointRH':'/api/atu/humidSetpointRH/'
                            ,'mHumSetpointDP':'/api/atu/humidSetpointDP/'
                            ,'mDehumSetpointRH':'/api/atu/dehumSetpointRH/'
                            ,'mDehumSetpointDP':'/api/atu/dehumSetpointDP/'
                            #,'mCurrentSetpointRH':'/api/atu/currentSetpointRH/'
                            #,'mCurrentSetpointDP':'/api/atu/currentSetpointDP/'
                            },
                        'energy_sources' :{
                            'mName':'/api/enr/name/'
                            ,'mStatus':'/api/enr/status/'
                            ,'mDHWstatus':'/api/enr/dhwStatus/'
                            ,'mType':'/api/enr/type/'
                            ,'mAlarmOn':'/api/enr/alarmOn/'
                            },
                        'buffer_tanks' : {
                            'mName':'/api/tnk/name/'
                            ,'mStatus':'/api/tnk/status/'
                            ,'mMode':'/api/tnk/mode/'
                            ,'mTemp':'/api/tnk/temperature/'
                            ,'mAlarmOn':'/api/tnk/alarmOn/'
                            },
                        'domsetic_hot_waters' : {
                            'mStatus':'/api/dhw/status/'
                            ,'mName':'/api/dhw/name/'
                            ,'mTemp':'/api/dhw/temperature/'
                            ,'mTargetTemp':'/api/dhw/targetTemperature/'
                            }
                        }
        self.mSystemPut = {
                        'system' : ['mName', 'mStatus', 'mEnergySavings', 'mSetback'],
                        'zones' : [ 'mName', 'mSetPoint', 'mStatus', 'mHumSetPointRH',
                                    'mHumSetPointDP', 'mDeumSetPointRH', 'mDehumSetPointDP',
                                    'mCurrentSetPointRH','mCurrentSetPointDP', 'mScheduleOn',
                                    'mEnergySave' ],
                        'macrozones' : ['mName', 'mSetPoint', 'mStatus', 'mScheduleOn'],
                        'hc_changeover' : ['mName', 'mMode', 'mAdaptiveComfort' ],
                        'fan_coils' :['mName', 'mState', 'mCoolingSpeed','mHeatingSpeed' ],
                        'atus': [ 'mName', 'mFlowLevel', 'mStatus', 'HRVOn', 'mHUMOn', 'mNTDOn',
                                  'mINTOn', 'mHumSetpointRH', 'mHumSetpointDP', 'mDehumSetpointRH',
                                  'mDehumSetpointDP', 'mCurrentSetpointRH', 'mCurrentSetpointDP' ],
                        'energy_sources' : [ 'mName' ],
                        'buffer_tanks' : [ 'mName','mStatus', 'mMode' ],
                        'domsetic_hot_waters':[ 'mStatus', 'mName', 'mTargetTemp' ]
                        }                    
        #self.APIKeyVal = '9bf711fc-54e2-4387-9c7f-991bbb02ab3a'
        #self.IP = '192.168.2.65'    
        self.APIKey = 'apikey'
        self.APIKeyVal = mAPIKeyVal
        self.APIStr = self.APIKey + '=' + self.APIKeyVal

        self.IP ='http://'+ mIPaddress

        self.RESPONSE_OK = '<Response [200]>'
        self.RESPONSE_NO_SUPPORT = '<Response [400]>'
        self.RESPONSE_NO_RESPONSE = '<Response [404]>'

        self.systemDict = defaultdict(dict)
        self.zoneDict = defaultdict(dict)
        self.macrozoneDict = defaultdict(dict)
        self.hc_changeoverDict = defaultdict(dict)
        self.fan_coilsDict = defaultdict(dict)
        self.atuDict =defaultdict(dict)
        self.energy_sourcesDict = defaultdict(dict)
        self.buffer_tanksDict = defaultdict(dict)
        self.domsetic_hot_waterDict =defaultdict(dict)
        LOGGER.debug ('Reading Messana System')
        self.retrieveAllMessanaStatus()
        LOGGER.debug('Finish Reading Messana system')



    def putSystem(self, mKey, value):
            LOGGER.debug('PUT System')
            mData = defaultdict(list)
            PUTStr = self.IP+self.mSystem['system'][mKey] 
            LOGGER.debug(PUTStr)
            mData = {'value':value, self.APIKey : self.APIKeyVal}
            LOGGER.debug(mData)
            resp = requests.put(PUTStr, mData)
            LOGGER.debug(resp)
            if str(resp) != self.RESPONSE_OK:
                #print (str(resp)+ ': Not able to PUT Key: : '+ mKey + ' value:', value )
                return False

    def updateSystemData(self, systemDict):
        for mKey in systemDict:
            if mKey in self.mSystemPut['system']:
                self.putSystem(mKey,systemDict[mKey])

    def putSubSystem(self, mSystemKey, subSysNbr, mKey, subSysDict):
        PUTStr = self.IP + self.mSystem[mSystemKey][mKey]
        value = subSysDict[mKey]
        LOGGER.debug('PUT str: ' + PUTStr + str(value))

        mData = {'id':subSysNbr, 'value': value, self.APIKey : self.APIKeyVal}
        resp = requests.put(PUTStr, mData)
        if str(resp) == self.RESPONSE_OK:
            subSysDict[mKey] = value
            return True
        elif str(resp) == self.RESPONSE_NO_SUPPORT:
            temp1 =  resp.content
            res_dict = json.loads(temp1.decode('utf-8')) 
            mData['error'] = str(resp) + ': Not able to PUT key: '+ str(res_dict.values()) + ' Subnode ' + str(id) + ' for key: ' + str(mKey) + ' value:', str(value)
            LOGGER.debug(mData['error'])
            mData['statusOK'] =False
        elif str(resp) == self.RESPONSE_NO_RESPONSE:
            mData['error'] = str(resp) + ': Error: No response from API for key: ' + str(mKey)+ ' value:', str(value)
            LOGGER.debug(mData['error'])
            mData['statusOK'] =False
        else:
            mData['error'] = str(resp) + ': Error: Unknown:for key: ' + str(mKey)+ ' value:', str(value)
            LOGGER.debug(mData['error'])
            mData['statusOK'] =False
            return False

    def retrieveSubNodeData(self, mSystem, instNbr, mKey, mData):
        GETStr =self.IP+mSystem[mKey]+str(instNbr)+'?'+ self.APIStr 
        #print('\n' +  GETStr)
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

    def retrieveSubSystemData(self, MessanaSubSystem, instNbr):
        subSystemDict = defaultdict(dict)
        for mKey in MessanaSubSystem:
            mData = {}
            self.retrieveSubNodeData(MessanaSubSystem, instNbr, mKey, mData)
            if mData['statusOK']:
                subSystemDict[instNbr][mKey] = mData['data']
            #else:
                #print(mData['error'])
        return subSystemDict

    def retrieveMessanaStatus(self):
        if self.systemDict['mZoneCount'] > 0:
            LOGGER.debug('Reading Zone System')
            self.retrieveAllZoneDataMessana()
        if self.systemDict['mMacrozoneCount'] > 0:    
            LOGGER.debug('Reading MacroZone System')
            self.retrieveAllMacroZoneDataMessana()
        if self.systemDict['mHC_changeoverCount'] > 0:   
            LOGGER.debug('Reading Ht/Cold System')
            self.retrieveAllHC_CODataMessana()
        if self.systemDict['mATUCount'] > 0:
            LOGGER.debug('Reading ATU System')

    def retrieveAllMessanaStatus(self):
        LOGGER.info('Retrieve Full Messana Status')
        LOGGER.debug('Reading Main System')
        self.retrieveSystemDataMessana()
        #LOGGER.debug(self.systemDict)
        #LOGGER.debug('Zone count: '+ str(self.systemDict['mZoneCount'] ))
        if self.systemDict['mZoneCount'] > 0:
            LOGGER.debug('Reading Zone System')
            self.retrieveAllZoneDataMessana()
        if self.systemDict['mMacrozoneCount'] > 0:    
            LOGGER.debug('Reading MacroZone System')
            self.retrieveAllMacroZoneDataMessana()
        if self.systemDict['mHC_changeoverCount'] > 0:   
            LOGGER.debug('Reading Ht/Cold System')
            self.retrieveAllHC_CODataMessana()
        LOGGER.debug('Reading ATU System: ' )
        if self.systemDict['mATUcount'] > 0:
            LOGGER.debug('Reading ATU System')
            self.retrieveAllATUDataMessana()
        #LOGGER.debug('')
        #self.retrieveAllFCData()
        #self.retrieveAllEnergySourceData()
        #self.retrieveAllBufTData()
        #self.retrieveAllDHWData()

    def retrieveSystemDataMessana(self):
        LOGGER.info('retrieve Sytem Data')
        for mKey in self.mSystem['system']:
            GETStr =self.IP+self.mSystem['system'][mKey] + '?' + self.APIStr 
            #LOGGER.debug( GETStr)
            systemTemp = requests.get(GETStr)
            if str(systemTemp) == self.RESPONSE_OK:
                systemTemp = systemTemp.json()
                self.systemDict[mKey] = systemTemp[str(list(systemTemp.keys())[0])]
                if mKey == 'mUnitTemp': 
                    #"we cannot handle strings"
                    #print(self.systemDict[mKey])
                    if self.systemDict[mKey] == 'Celcius':
                        self.systemDict[mKey] = 0
                    else:
                        self.systemDict[mKey] = 1 
            else:
                LOGGER.debug(str(mKey) + ' error')
                #self.systemDict[mKey] = -1
        
    def retrieveSystemData(self):
        LOGGER.debug('MessanaInfo Retrieve System Data')
        return self.systemDict

    def uploadSystemData(self, systemDict):
        for mKey in systemDict:
            if mKey in self.mSystemPut['system']:
                self.putSystem(mKey,systemDict[mKey])

    def retrieveZoneDataMessana(self, zoneNbr):
        tempDict = defaultdict(dict)
        tempDict = self.retrieveSubSystemData(self.mSystem['zones'], zoneNbr)
        for key in tempDict[zoneNbr]:
                    self.zoneDict[zoneNbr][key]=tempDict[zoneNbr][key]

    def retrieveZoneData(self, zoneNbr):
        LOGGER.debug('MessanaInfo Retrieve ZONE Data')
        return(self.zoneDict[zoneNbr])
    
    def retrieveAllZoneDataMessana(self):      
        for zoneNbr in range(0,int(self.systemDict['mZoneCount']) ):
            self.retrieveZoneDataMessana(zoneNbr)

    def uploadZoneData(self, zoneNbr, extZoneDict):
        LOGGER.debug(extZoneDict)
        for mKey in extZoneDict:
            if mKey in self.mSystemPut['zones']:
                # only update changed values
                if extZoneDict[mKey] != self.zoneDict[zoneNbr][mKey]:
                    self.zoneDict[zoneNbr][mKey] = extZoneDict[mKey]
                    self.putSubSystem('zones', zoneNbr, mKey, self.zoneDict)


    def retrieveMacroZoneDataMessana(self, mmacrozoneNbr):
        tempDict = defaultdict(dict)
        tempDict = self.retrieveSubSystemData(self.mSystem['macrozones'], mmacrozoneNbr)
        #LOGGER.debug(tempDict)
        for key in tempDict[mmacrozoneNbr]:
            self.macrozoneDict[mmacrozoneNbr][key]=tempDict[mmacrozoneNbr][key]   

    def retrieveAllMacroZoneDataMessana(self):
        for mzoneNbr in range(0,self.systemDict['mMacrozoneCount']):
            self.retrieveMacroZoneDataMessana(mzoneNbr)
            
    def retrieveMacroZoneData(self, mzoneNbr):
        return self.macrozoneDict[mzoneNbr]

    def uploadMacroZoneData(self, macrozoneNbr, macrozoneDict):
        for mKey in macrozoneDict[macrozoneNbr]:
            if mKey in self.mSystemPut['macrozones']:
                self.putSubSystem('macrozones', macrozoneNbr, mKey, macrozoneDict[macrozoneNbr])

    def retrieveHC_COData(self, hcchangeoverNbr):
        return self.hc_changeoverDict[hcchangeoverNbr]

    def retrieveAllHC_CODataMessana(self):
        for hcchangeoverNbr in range (0,self.systemDict['mHC_changeoverCount']):
            self.retrieveHC_COData(hcchangeoverNbr)

    def retrieveHC_CODataMessana(self, mHCCoNbr):
        tempDict = defaultdict(dict)
        tempDict = self.retrieveSubSystemData(self.mSystem['hc_changeover'], mHCCoNbr)
        for key in tempDict[mHCCoNbr]:
            self.hc_changeoverDict[mHCCoNbr][key]=tempDict[mHCCoNbr][key]

    def uploadHC_COData(self, hcchangeoverNbr, hc_changeoverDict):
        for mKey in hc_changeoverDict[hcchangeoverNbr]:
            if mKey in self.mSystemPut['hc_changeover']:
                self.putSubSystem('hc_changeover', hcchangeoverNbr, mKey, hc_changeoverDict[hcchangeoverNbr])

    def retrieveAllATUDataMessana(self):
        for atuNbr in range(0,self.systemDict['mATUcount']):
            self.retrieveATUDataMessana(atuNbr)

    def retrieveATUDataMessana(self, atuNbr):
        tempDict = defaultdict(dict)
        tempDict = self.retrieveSubSystemData(self.mSystem['atus'], atuNbr)
        for key in tempDict[atuNbr]:
            self.atuDict[atuNbr][key]=tempDict[atuNbr][key]  
 
    def retrieveATUData(self, atuNbr):
        return self.atuDict[atuNbr]

    def uploadATUData(self, atuNbr, atuDict):
        for mKey in atuDict[atuNbr]:
            if mKey in self.mSystemPut['atus']:
                self.putSubSystem('atus', atuNbr, mKey, atuDict[atuNbr])

    '''
    def retrieveFCData(self, fcNbr):
        self.retrieveSubSystemData(self.mSystem['fan_coils'], fcNbr, self.fan_coilsDict)

    def retrieveAllFCData(self):
       for fcNbr in range(0,self.systemDict['mFanCoilCount']):
           self.retrieveFCData(fcNbr)




    def retrieveEnergySourceData(self, esNbr):
        self.retrieveSubSystemData(self.mSystem['energy_sources'], esNbr, self.energy_sourcesDict)

    def retrieveAllEnergySourceData(self):
        for esNbr in range(0,self.systemDict['mEnergySourceCount']):
            self.retrieveEnergySourceData(esNbr)

    def retrieveBufTData(self, btNbr):
            self.retrieveSubSystemData(self.mSystem['buffer_tanks'], btNbr, self.buffer_tanksDict)

    def retrieveAllBufTData(self):
        for btNbr in range(0,self.systemDict['mBufTankCount']):
            self.retrieveBufTData(btNbr)


    def retrieveDHWData(self, dhwNbr):
        self.retrieveSubSystemData(self.mSystem['domsetic_hot_waters'], dhwNbr, self.domsetic_hot_waterDict)

    def retrieveAllDHWData(self):
        for dhwNbr in range(0,self.systemDict['mDHWcount']):
            self.retrieveDHWData(dhwNbr)

    '''

        
#sys.stdout = open('Messanaoutput.txt','wt')
'''messana = MessanaInfo('192.168.2.65' , '9bf711fc-54e2-4387-9c7f-991bbb02ab3a')


#Retrive basic system info
print('\nSYSTEM')
msysInfo = defaultdict(dict)
msysInfo = messana.retrieveSystemData()
#messana.uploadSystemData(msysInfo)

print('\nZONES')
ZoneDict = defaultdict(dict) 
for zoneNbr in range(0,msysInfo['mZoneCount']):
    ZoneDict[zoneNbr] = messana.retrieveZoneData(zoneNbr)

for zoneNbr in range(0,msysInfo['mZoneCount']):
    messana.uploadZoneData(zoneNbr, ZoneDict)


print('\nMACROZONES')
MacroZoneDict = defaultdict(dict)   
for macroZoneNbr in range(0,  msysInfo['mMacrozoneCount'] ):
    MacroZoneDict[macroZoneNbr] = messana.retrieveMacroZoneData(macroZoneNbr)  

for macroZoneNbr in range(0, msysInfo['mMacrozoneCount']):
    messana.uploadMacroZoneData(macroZoneNbr, MacroZoneDict)

print('\nHC changeover')
HC_CoDict = defaultdict(dict)   
for HC_CoNbr in range(0,  msysInfo['mHC_changeoverCount'] ):
    HC_CoDict[HC_CoNbr] = messana.retrieveHC_COData(HC_CoNbr)  
for HC_CoNbr in range(0,  msysInfo['mHC_changeoverCount'] ):
    messana.uploadHC_COData(HC_CoNbr, HC_CoDict)  

print('\nATU')
atuDict = defaultdict(dict)   
for atuNbr in range(0,  msysInfo['mATUcount'] ):
    atuDict[atuNbr] = messana.retrieveATUData(atuNbr)  
for atuNbr in range(0,  msysInfo['mATUcount'] ):
    messana.uploadATUData(atuNbr, atuDict)

print('\n END')

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
'''
#sys.stdout.close() 
