#!/usr/bin/env python3
#import polyinterface
import requests
from subprocess import call
import json
from collections import defaultdict

#LOGGER = polyinterface.LOGGER

class MessanaInfo:
    def __init__ (self, mIPaddress, mAPIKeyVal):
        self.mSystem = defaultdict(dict)
        self.mSystem = {'system': { 'GETstr' : {
                                        'mName':'/api/system/name/'
                                        ,'mApiVer':'/api/system/apiVersion/'
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
                                        ,'mExternalAlarm':'/api/system/externalAlarm/'}
                                    ,
                                    'PUTstr' : {
                                        'mName':'/api/system/name/'
                                        ,'mStatus':'/api/system/status/'
                                        ,'mEnergySavings':'/api/system/energySaving/'
                                        ,'mSetback':'/api/system/setback/' }
                                    ,
                                   'active':
                                        ['mExternalAlarm']
                                   , 
                                    'data':{}
                                   },
                        'zones': {  'GETstr' : {
                                        'mName': '/api/zone/name/'
                                        ,'mSetPoint' :'/api/zone/setpoint/'
                                        ,'mStatus':'/api/zone/status/'
                                        ,'mHumSetPointRH': '/api/zone/humidSetpointRH/'
                                        ,'mHumSetPointDP':'/api/zone/humidSetpointDP/'
                                        ,'mDeumSetPointRH':'/api/zone/dehumSetpointRH/'
                                        ,'mDehumSetPointDP':'/api/zone/dehumSetpointDP/'
                                        ,'mCurrentSetPointRH':'/api/zone/currentSetpointRH/'
                                        ,'mCurrentSetPointDP':'/api/zone/currentSetpointDP/'
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
                                        ,'mCapability':'/api/zone/capability/'}
                                    ,
                                    'PUTstr':{
                                        'mName': '/api/zone/name/'
                                        ,'mSetPoint' :'/api/zone/setpoint/'
                                        ,'mStatus':'/api/zone/status/'
                                        ,'mHumSetPointRH': '/api/zone/humidSetpointRH/'
                                        ,'mHumSetPointDP':'/api/zone/humidSetpointDP/'
                                        ,'mDeumSetPointRH':'/api/zone/dehumSetpointRH/'
                                        ,'mDehumSetPointDP':'/api/zone/dehumSetpointDP/'
                                        ,'mCurrentSetPointRH':'/api/zone/currentSetpointRH/'
                                        ,'mCurrentSetPointDP':'/api/zone/currentSetpointDP/'
                                        ,'mScheduleOn' : '/api/zone/scheduleOn/'
                                        ,'mEnergySave' : '/api/zone/energySaving/'}
                                    ,
                                    'active':['mCurrentSetPointRH', 'mCurrentSetPointDP'
                                        ,'mHumidity', 'mDewPoint', 'mTemp', 'mAirTemp', 'mAlarmOn' ]
                                    ,
                                    'data' :{}
                            },
                        'macrozones' : { 'GETstr' : {
                                            'mName': '/api/macrozone/name/'
                                            ,'mSetPoint' :'/api/macrozone/setpoint/'
                                            ,'mStatus':'/api/macrozone/status/'
                                            ,'mScheduleOn' : '/api/macrozone/scheduleOn/'
                                            ,'mHumidity':'/api/macrozone/humidity/'
                                            ,'mDewPoint' : '/api/macrozone/dewpoint/'
                                            ,'mTemp' :'/api/macrozone/temperature/'}
                                        ,
                                        'PUTstr':{
                                            'mName': '/api/macrozone/name/'
                                            ,'mSetPoint' :'/api/macrozone/setpoint/'
                                            ,'mStatus':'/api/macrozone/status/'
                                            ,'mScheduleOn' : '/api/macrozone/scheduleOn/'}
                                        ,
                                        'active':['mTemp', 'mHumidity','mDewPoint' ]
                                        ,
                                        'data' : {}
                        },
                        'hc_changeover' :{ 'GETstr' : {
                                                'mName':'/api/hc/name/'
                                                ,'mMode':'/api/hc/mode/'
                                                ,'mExcutiveSeason':'/api/hc/executiveSeason/'
                                                ,'mAdaptiveComfort':'/api/hc/adaptiveComfort/'}
                                            ,
                                            'PUTstr':{
                                                'mName':'/api/hc/name/'
                                                ,'mMode':'/api/hc/mode/'
                                                ,'mAdaptiveComfort':'/api/hc/adaptiveComfort/' }
                                            ,
                                            'active':[]
                                            ,
                                            'data' : {}
                        },
                        'fan_coils' :{'GETstr' : {
                                        'mName':'/api/fan/name/'
                                        ,'mState':'/api/fan/state/'
                                        ,'mCoolingSpeed':'/api/fan/coolingSpeed/'
                                        ,'mHeatingSpeed':'/api/fan/heatingSpeed/'
                                        ,'mType':'/api/fan/type/'
                                        ,'mAlarmOn':'/api/fan/alarmOn/'}
                                     ,
                                     'PUTstr':{                                        
                                        'mName':'/api/fan/name/'
                                        ,'mState':'/api/fan/state/'
                                        ,'mCoolingSpeed':'/api/fan/coolingSpeed/'
                                        ,'mHeatingSpeed':'/api/fan/heatingSpeed/'}
                                     ,
                                     'active':['mAlarmOn','mCoolingSpeed','mHeatingSpeed' ]
                                     ,
                                     'data' : {}
                        },
                        'atus': {'GETstr' : {
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
                                    ,'mCurrentSetpointRH':'/api/atu/currentSetpointRH/'
                                    ,'mCurrentSetpointDP':'/api/atu/currentSetpointDP/'}
                                 ,
                                 'PUTstr':{                                    
                                    'mName':'/api/atu/name/'
                                    ,'mFlowLevel':'/api/atu/flowLevel/'
                                    ,'mStatus':'/api/atu/status/'
                                    ,'HRVOn':'/api/atu/hrvOn/'
                                    ,'mHUMOn':'/api/atu/humOn/'
                                    ,'mNTDOn':'/api/atu/ntdOn/'
                                    ,'mINTOn':'/api/atu/intOn/'
                                    ,'mHumSetpointRH':'/api/atu/humidSetpointRH/'
                                    ,'mHumSetpointDP':'/api/atu/humidSetpointDP/'
                                    ,'mDehumSetpointRH':'/api/atu/dehumSetpointRH/'
                                    ,'mDehumSetpointDP':'/api/atu/dehumSetpointDP/'
                                    ,'mCurrentSetpointRH':'/api/atu/currentSetpointRH/'
                                    ,'mCurrentSetpointDP':'/api/atu/currentSetpointDP/'}
                                 ,
                                 'active':['mFlowLevel', 'mAlarmOn', 'mAirTemp', 'mCurrentSetpointRH', 'mCurrentSetpointDP'  ]
                                 ,
                                 'data' : {}
                        },
                        'energy_sources':{'GETstr' : {
                                            'mName':'/api/enr/name/'
                                            ,'mStatus':'/api/enr/status/'
                                            ,'mDHWstatus':'/api/enr/dhwStatus/'
                                            ,'mType':'/api/enr/type/'
                                            ,'mAlarmOn':'/api/enr/alarmOn/' }
                                         ,
                                         'PUTstr':{'mName':'/api/enr/name/'}
                                         ,
                                         'active':['mAlarmOn']
                                         ,
                                         'data' : {}
                        }, 
                        'buffer_tanks': {'GETstr' : {
                                            'mName':'/api/tnk/name/'
                                            ,'mStatus':'/api/tnk/status/'
                                            ,'mMode':'/api/tnk/mode/'
                                            ,'mTemp':'/api/tnk/temperature/'
                                            ,'mAlarmOn':'/api/tnk/alarmOn/'}
                                         ,
                                         'PUTstr':{
                                            'mName':'/api/tnk/name/'
                                            ,'mStatus':'/api/tnk/status/'
                                            ,'mMode':'/api/tnk/mode/' }
                                         ,
                                         'active':['mTemp', 'mAlarmOn']
                                         ,
                                         'data' : {}
                        },
                        'domsetic_hot_waters': {'GETstr' : {
                                                    'mStatus':'/api/dhw/status/'
                                                    ,'mName':'/api/dhw/name/'
                                                    ,'mTemp':'/api/dhw/temperature/'
                                                    ,'mTargetTemp':'/api/dhw/targetTemperature/' }
                                                ,
                                                'PUTstr':{ 
                                                    'mStatus':'/api/dhw/status/'
                                                    ,'mName':'/api/dhw/name/'
                                                    ,'mTargetTemp':'/api/dhw/targetTemperature/'}
                                                ,
                                                'active':['mTemp']
                                                ,
                                                'data' : {}
                        }
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

        '''
        print ('Reading Messana System')
        #self.pullAllMessanaStatus()
        print('Finish Reading Messana system')
        '''


    def GETSystem(self, mKey):
        print('GETSystem: ' + mKey )
        GETStr = self.IP+self.mSystem['system']['GETstr'][mKey] + '?' + self.APIStr 
        print( GETStr)
        systemTemp = requests.get(GETStr)
        print(str(systemTemp))
        if str(systemTemp) == self.RESPONSE_OK:
           systemTemp = systemTemp.json()
           print(systemTemp)
           self.mSystem['system']['data'][mKey] = systemTemp[str(list(systemTemp.keys())[0])]
        else:
           print(str(mKey) + ' error')
           #self.systemDict[mKey] = -1
    
    def PUTSystem(self, mKey, value):
            print('PUT System: {' + mKey +':'+str(value)+'}' )
            mData = defaultdict(list)
            PUTStr = self.IP+self.mSystem['system']['PUTstr'][mKey] 
            print(PUTStr)
            mData = {'value':value, self.APIKey : self.APIKeyVal}
            #mHeaders = { 'accept': 'application/json' , 'Content-Type': 'application/json' }
            print(mData)
            resp = requests.put(PUTStr, json=mData)
            print(resp)
            if str(resp) != self.RESPONSE_OK:
               print(str(resp)+ ': Not able to PUT Key: : '+ mKey + ' value:', value )
               return False
            else:
               return(True)          

    def GETNodeData(self, mNodeKey, instNbr, mKey):
        print('GETSubNodeData: ' + mNodeKey + ' ' + str(instNbr)+ ' ' + mKey)
        try:
            if mKey in self.mSystem[mNodeKey]['GETstr']:
               GETStr =self.IP+self.mSystem[mNodeKey]['GETstr'][mKey]+str(instNbr)+'?'+ self.APIStr 
        except: 
                print('Put does not accept keywork: ' + mKey)
                return()

        nodeData = {}
        subSysTemp = requests.get(GETStr)
        if str(subSysTemp) == self.RESPONSE_OK:
            subSysTemp = subSysTemp.json()
            nodeData['data']  = subSysTemp[str(list(subSysTemp.keys())[0])]
            nodeData['statusOK'] =True
            if instNbr in self.mSystem[mNodeKey]['data']:
                if mKey in self.mSystem[mNodeKey]['data'][instNbr]:
                    self.mSystem[mNodeKey]['data'][instNbr][mKey] = nodeData['data']
                else:
                    self.mSystem[mNodeKey]['data'][instNbr].update({mKey : nodeData['data']})
            else:
                temp = {}
                temp[instNbr] = {mKey : nodeData['data']}
                self.mSystem[mNodeKey]['data'].update(temp)

        elif str(subSysTemp) == self.RESPONSE_NO_SUPPORT:
            temp1 =  subSysTemp.content
            res_dict = json.loads(temp1.decode('utf-8')) 
            nodeData['error'] = str(subSysTemp) + ': Error: '+ str(res_dict.values()) + ' Subnode ' + str(instNbr) + ' for id: ' + str(mKey)
            nodeData['statusOK'] =False
        elif str(subSysTemp) == self.RESPONSE_NO_RESPONSE:
            nodeData['error'] = str(subSysTemp) + ': Error: No response from API:  Subnode ' + str(instNbr) + ' for id: ' + str(mKey)
            nodeData['statusOK'] =False
        else:
            nodeData['error'] = str(subSysTemp) + ': Error: Unknown: Subnode ' + str(instNbr) + ' for id: ' + str(mKey)
            nodeData['statusOK'] =False
        return(nodeData)

    def PUTNodeData(self, mNodeKey, nodeNbr, mKey, value):
        try:
            if mKey in self.mSystem[mNodeKey]['PUTstr']:
                PUTStr = self.IP + self.mSystem[mNodeKey]['PUTstr'][mKey]
                print('PUT str: ' + PUTStr + str(value))
                mData = {'id':nodeNbr, 'value': value, self.APIKey : self.APIKeyVal}
                resp = requests.put(PUTStr, json=mData)
        except:
            print('Node ' + mNodeKey + ' does not accept keyword: ' + mKey)
            return (False)

        if str(resp) == self.RESPONSE_OK:
            self.mSystem[mNodeKey]['data'][nodeNbr][mKey] = value
            return True
        elif str(resp) == self.RESPONSE_NO_SUPPORT:
            temp1 =  resp.content
            res_dict = json.loads(temp1.decode('utf-8')) 
            mData['error'] = str(resp) + ': Not able to PUT key: '+ str(res_dict.values()) + ' Subnode ' + str(id) + ' for key: ' + str(mKey) + ' value:', str(value)
            print(mData['error'])
            mData['statusOK'] =False
        elif str(resp) == self.RESPONSE_NO_RESPONSE:
            mData['error'] = str(resp) + ': Error: No response from API for key: ' + str(mKey)+ ' value:', str(value)
            print(mData['error'])
            mData['statusOK'] =False
        else:
            mData['error'] = str(resp) + ': Error: Unknown:for key: ' + str(mKey)+ ' value:', str(value)
            print(mData['error'])
            mData['statusOK'] =False
            return False

    def pullSystemDataAll(self):
        #LOGGER.info('pull Sytem Data')
        ##LOGGER.info(self.mSystem['system'])
        for mKey in self.mSystem['system']['GETstr']:
            print(mKey)
            self.GETSystem(mKey) 
    
    def pullSystemDataActive(self):
        print ('pullSystemDataNonStatic')
        for mKey in self.mSystem['system']['active']:
            print (mKey)
            self.GETSystem(mKey) 
        
    def pullSystemDataIndividual(self, mKey):
        print('MessanaInfo pull System Data: ' + mKey)
        if mKey in self.mSystem['system']['GETstr']:
           self.GETSystem(mKey) 
        else:         
           print('Unknown keyword :' + mKey)
    
    def pushSystemDataIndividual(self, mKey, value):
        print('MessanaInfo push System Data: ' + mKey)
        if mKey in self.mSystem['system']['PUTstr']:
           if (self.PUTSystem(mKey, value)):
                return(True) 
           else:
                print('Put failed: ' + mKey + ' ' + str(value))
                return(False)
        else:         
           print('PUT not supporting keyword :' + mKey)
           return(False)
    

    def pullSystemKeys(self):
        print('pullSystemKeys')
        keys=[]
        if self.mSystem['system']['data']:
            for mKey in self.mSystem['system']['data']:
                keys.append(mKey)
        else:
            print('No Keys found - trying to fetch system data ')
            self.pullSystemDataAll()
            for mKey in self.mSystem['system']['data']:
                keys.append(mKey)
        return(keys)
    


    
    def pullZoneDataAll(self, zoneNbr):
        print('pullZoneDataMessanaAll: ' + str(zoneNbr))
        for mKey in self.mSystem['zones']['GETstr']:
            self.pullZoneDataIndividual(zoneNbr, mKey)


    def pullZoneDataActive(self, zoneNbr):
        print('pullZoneDataActive: ' + str(zoneNbr))
        for mKey in self.mSystem['zones']['active']:
            self.pullZoneDataIndividual(zoneNbr, mKey)
        
    def pullZoneDataIndividual(self, zoneNbr, mKey):  
        print('pullZoneDataMessanaIndividual: ' +str(zoneNbr)  + ' ' + mKey)    
        self.GETNodeData('zones', zoneNbr, mKey)

    def pushZoneDataIndividual(self, zoneNbr, mKey, value):
        print('pullZoneDataMessanaIndividual: ' +str(zoneNbr)  + ' ' + mKey + ' ' + str(value))  
        self.PUTNodeData('zones', zoneNbr, mKey, value)

    def pullZoneKeys(self, zoneNbr):
        print('pullZoneKeys')
        keys=[]
        if self.mSystem['zones']['data']:
            if zoneNbr in self.mSystem['zones']['data']: 
                for mKey in self.mSystem['zones']['data'][zoneNbr]:
                    if not(mKey in keys):
                        keys.append(mKey)
            else:
                self.pullZoneDataAll(zoneNbr)
                for mKey in self.mSystem['zones']['data'][zoneNbr]:
                    if not(mKey in keys):
                        keys.append(mKey)
        else:
            print('No Keys found - trying to fetch Messana data')
            self.pullSystemDataAll()
            self.pullZoneDataAll(zoneNbr)
            for mKey in self.mSystem['zones']['data'][zoneNbr]:
                if not(mKey in keys):
                    keys.append(mKey)
        return(keys)

    def pullMacroZoneDataAll(self, zoneNbr):
        print('pullZoneDataMessanaAll: ' + str(zoneNbr))
        for mKey in self.mSystem['zones']['GETstr']:
            self.pullZoneDataIndividual(zoneNbr, mKey)


    def pullMacroZoneDataActive(self, zoneNbr):
        print('pullZoneDataActive: ' + str(zoneNbr))
        for mKey in self.mSystem['zones']['active']:
            self.pullZoneDataIndividual(zoneNbr, mKey)
        
    def pullMacroZoneDataIndividual(self, zoneNbr, mKey):  
        print('pullZoneDataMessanaIndividual: ' +str(zoneNbr)  + ' ' + mKey)    
        self.GETNodeData('zones', zoneNbr, mKey)


    '''
    def pushSystemDataAll(self):
        for mKey in self.systemDict:
            if mKey in self.mSystemPUT['system']:
                self.PUTSystem(mKey, self.systemDict[mKey])

    def pushSystemData(self, mKey, value):
        self.PUTSystem(mKey, value)


    #def GETSubNode(self, mKey, subNodeDict)

        
    def PUTSubNode(self, mSystemKey, subSysNbr, mKey, subSysDict):
        PUTStr = self.IP + self.mSystem[mSystemKey][mKey]
        value = subSysDict[mKey]
        print('PUT str: ' + PUTStr + str(value))

        mData = {'id':subSysNbr, 'value': value, self.APIKey : self.APIKeyVal}
        resp = requests.put(PUTStr, json=mData)
    
        if str(resp) == self.RESPONSE_OK:
            subSysDict[mKey] = value
            return True
        elif str(resp) == self.RESPONSE_NO_SUPPORT:
            temp1 =  resp.content
            res_dict = json.loads(temp1.decode('utf-8')) 
            mData['error'] = str(resp) + ': Not able to PUT key: '+ str(res_dict.values()) + ' Subnode ' + str(id) + ' for key: ' + str(mKey) + ' value:', str(value)
            print(mData['error'])
            mData['statusOK'] =False
        elif str(resp) == self.RESPONSE_NO_RESPONSE:
            mData['error'] = str(resp) + ': Error: No response from API for key: ' + str(mKey)+ ' value:', str(value)
            print(mData['error'])
            mData['statusOK'] =False
        else:
            mData['error'] = str(resp) + ': Error: Unknown:for key: ' + str(mKey)+ ' value:', str(value)
            print(mData['error'])
            mData['statusOK'] =False
            return False

    def GETSubNodeData(self, mSubSysKey, instNbr, mKey):
        print('GETSubNodeData: ' + mSubSysKey + ' ' + str(instNbr)+ ' ' + mKey)
        GETStr =self.IP+self.mSystem[mSubSysKey][mKey]+str(instNbr)+'?'+ self.APIStr 
        mData = {}
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
        return mData

     def pullSubNodeDataAll( mSubSysKey, instNbr):
        print('pullSubnNodeDataAll: ' + mSubSysKey + ' ' + str(instNbr) )
        for mKey in 
    '''

    '''
    def pullSubSystemData(self, mSubSysKey, instNbr):
        subSystemDict = defaultdict(dict)
        for mKey in MessanaSubSystem:
            mData = self.GETSubNodeData(MessanaSubSystem, instNbr, mKey, mData)
            if mData['statusOK']:
                subSystemDict[instNbr][mKey] = mData['data']
            #else:
                #print(mData['error'])
        return subSystemDict

    def pullAllMessanaStatus(self):
        #LOGGER.info('pull Full Messana Status')
        print('Reading Main System')
        self.pullSystemDataMessana()
        #print(self.systemDict)
        #print('Zone count: '+ str(self.systemDict['mZoneCount'] ))
        if self.systemDict['mZoneCount'] > 0:
            print('Reading Zone System')
            self.pullAllZoneDataMessana()
        if self.systemDict['mMacrozoneCount'] > 0:    
            print('Reading MacroZone System')
            self.pullAllMacroZoneDataMessana()
        if self.systemDict['mHC_changeoverCount'] > 0:   
            print('Reading Ht/Cold System')
            self.pullAllHC_CODataMessana()
        print('Reading ATU System: ' )
        if self.systemDict['mATUcount'] > 0:
            print('Reading ATU System')
            self.pullAllATUDataMessana()
        #print('')
        #self.pullAllFCData()
        #self.pullAllEnergySourceData()
        #self.pullAllBufTData()
        #self.pullAllDHWData()

    def pullMessanaStatus(self):
        if self.systemDict['mZoneCount'] > 0:
            print('Reading Zone System')
            self.pullAllZoneDataMessana()
        if self.systemDict['mMacrozoneCount'] > 0:    
            print('Reading MacroZone System')
            self.pullAllMacroZoneDataMessana()
        if self.systemDict['mHC_changeoverCount'] > 0:   
            print('Reading Ht/Cold System')
            self.pullAllHC_CODataMessana()
        if self.systemDict['mATUCount'] > 0:
            print('Reading ATU System')

    def pullZoneDataMessana(self, zoneNbr):
        tempDict = defaultdict(dict)
        tempDict = self.pullSubSystemData(self.mSystem['zones'], zoneNbr)
        for key in tempDict[zoneNbr]:
                    self.zoneDict[zoneNbr][key]=tempDict[zoneNbr][key]

    def pullZoneData(self, zoneNbr):
        print('MessanaInfo pull ZONE Data')
        return(self.zoneDict[zoneNbr])
    
    def pullAllZoneDataMessana(self):      
        for zoneNbr in range(0,int(self.systemDict['mZoneCount']) ):
            self.pullZoneDataMessana(zoneNbr)
    
    def pushZoneData(self, zoneNbr, extZoneDict):
        print(extZoneDict)
        for mKey in extZoneDict:
            if mKey in self.mSystemPUT['zones']:
                # only update changed values
                if extZoneDict[mKey] != self.zoneDict[zoneNbr][mKey]:
                    self.zoneDict[zoneNbr][mKey] = extZoneDict[mKey]
                    self.PUTSubNode('zones', zoneNbr, mKey, self.zoneDict)


    def pullMacroZoneDataMessana(self, mmacrozoneNbr):
        tempDict = defaultdict(dict)
        tempDict = self.pullSubSystemData(self.mSystem['macrozones'], mmacrozoneNbr)
        #print(tempDict)
        for key in tempDict[mmacrozoneNbr]:
            self.macrozoneDict[mmacrozoneNbr][key]=tempDict[mmacrozoneNbr][key]   

    def pullAllMacroZoneDataMessana(self):
        for mzoneNbr in range(0,self.systemDict['mMacrozoneCount']):
            self.pullMacroZoneDataMessana(mzoneNbr)
            
    def pullMacroZoneData(self, mzoneNbr):
        return self.macrozoneDict[mzoneNbr]

    def pushMacroZoneData(self, macrozoneNbr, macrozoneDict):
        for mKey in macrozoneDict[macrozoneNbr]:
            if mKey in self.mSystemPUT['macrozones']:
                self.PUTSubNode('macrozones', macrozoneNbr, mKey, macrozoneDict[macrozoneNbr])

    def pullHC_COData(self, hcchangeoverNbr):
        return self.hc_changeoverDict[hcchangeoverNbr]

    def pullAllHC_CODataMessana(self):
        for hcchangeoverNbr in range (0,self.systemDict['mHC_changeoverCount']):
            self.pullHC_COData(hcchangeoverNbr)

    def pullHC_CODataMessana(self, mHCCoNbr):
        tempDict = defaultdict(dict)
        tempDict = self.pullSubSystemData(self.mSystem['hc_changeover'], mHCCoNbr)
        for key in tempDict[mHCCoNbr]:
            self.hc_changeoverDict[mHCCoNbr][key]=tempDict[mHCCoNbr][key]

    def pushHC_COData(self, hcchangeoverNbr, hc_changeoverDict):
        for mKey in hc_changeoverDict[hcchangeoverNbr]:
            if mKey in self.mSystemPUT['hc_changeover']:
                self.PUTSubNode('hc_changeover', hcchangeoverNbr, mKey, hc_changeoverDict[hcchangeoverNbr])

    def pullAllATUDataMessana(self):
        for atuNbr in range(0,self.systemDict['mATUcount']):
            self.pullATUDataMessana(atuNbr)

    def pullATUDataMessana(self, atuNbr):
        tempDict = defaultdict(dict)
        tempDict = self.pullSubSystemData(self.mSystem['atus'], atuNbr)
        for key in tempDict[atuNbr]:
            self.atuDict[atuNbr][key]=tempDict[atuNbr][key]  
 
    def pullATUData(self, atuNbr):
        return self.atuDict[atuNbr]

    def pushATUData(self, atuNbr, atuDict):
        for mKey in atuDict[atuNbr]:
            if mKey in self.mSystemPUT['atus']:
                self.PUTSubNode('atus', atuNbr, mKey, atuDict[atuNbr])

    
    def pullFCData(self, fcNbr):
        self.pullSubSystemData(self.mSystem['fan_coils'], fcNbr, self.fan_coilsDict)

    def pullAllFCData(self):
       for fcNbr in range(0,self.systemDict['mFanCoilCount']):
           self.pullFCData(fcNbr)




    def pullEnergySourceData(self, esNbr):
        self.pullSubSystemData(self.mSystem['energy_sources'], esNbr, self.energy_sourcesDict)

    def pullAllEnergySourceData(self):
        for esNbr in range(0,self.systemDict['mEnergySourceCount']):
            self.pullEnergySourceData(esNbr)

    def pullBufTData(self, btNbr):
            self.pullSubSystemData(self.mSystem['buffer_tanks'], btNbr, self.buffer_tanksDict)

    def pullAllBufTData(self):
        for btNbr in range(0,self.systemDict['mBufTankCount']):
            self.pullBufTData(btNbr)


    def pullDHWData(self, dhwNbr):
        self.pullSubSystemData(self.mSystem['domsetic_hot_waters'], dhwNbr, self.domsetic_hot_waterDict)

    def pullAllDHWData(self):
        for dhwNbr in range(0,self.systemDict['mDHWcount']):
            self.pullDHWData(dhwNbr)

    '''

        
#sys.stdout = open('Messanaoutput.txt','wt')
messana = MessanaInfo('192.168.2.65' , '9bf711fc-54e2-4387-9c7f-991bbb02ab3a')


#Retrive basic system info
print('\nSYSTEM')
#systemKeys = messana.pullSystemKeys()
#print(systemKeys)
messana.pullSystemDataAll()
systemKeys = messana.pullSystemKeys()
print(systemKeys)
messana.pullSystemDataActive()
for mKey in messana.mSystem['system']['GETstr']:
    messana.pullSystemDataIndividual(mKey)
    if messana.pushSystemDataIndividual(mKey,messana.mSystem['system']['data'][mKey] ):
        print('Put :' + mKey +' '+ str(messana.mSystem['system']['data'][mKey]) )
    else:
        print('Put failed: ' + mKey +' '+ str(messana.mSystem['system']['data'][mKey]))

print ('\n Zones')

for zoneNbr in range(0,messana.mSystem['system']['data']['mZoneCount']):
    keys = messana.pullZoneKeys(zoneNbr)
    print (keys)
    messana.pullZoneDataAll(zoneNbr)
    messana.pullZoneDataActive(zoneNbr)
    keys = messana.pullZoneKeys(zoneNbr)
    print (keys)  
    for mKey in messana.mSystem['zones']['GETstr']:
        messana.pullZoneDataIndividual(zoneNbr, mKey)
        messana.pushZoneDataIndividual(zoneNbr, mKey, messana.mSystem['zones']['data'][zoneNbr][mKey])
        print('PUT zones : ' + mKey + ' ' + str( messana.mSystem['zones']['data'][zoneNbr][mKey]))

print ('\n Macro Zones')    
#messana.PUTSystemData(msysInfo)
'''
print('\nZONES')
ZoneDict = defaultdict(dict) 
for zoneNbr in range(0,msysInfo['mZoneCount']):
    ZoneDict[zoneNbr] = messana.pullZoneData(zoneNbr)

for zoneNbr in range(0,msysInfo['mZoneCount']):
    messana.pushZoneData(zoneNbr, ZoneDict)


print('\nMACROZONES')
MacroZoneDict = defaultdict(dict)   
for macroZoneNbr in range(0,  msysInfo['mMacrozoneCount'] ):
    MacroZoneDict[macroZoneNbr] = messana.pullMacroZoneData(macroZoneNbr)  

for macroZoneNbr in range(0, msysInfo['mMacrozoneCount']):
    messana.pushMacroZoneData(macroZoneNbr, MacroZoneDict)

print('\nHC changeover')
HC_CoDict = defaultdict(dict)   
for HC_CoNbr in range(0,  msysInfo['mHC_changeoverCount'] ):
    HC_CoDict[HC_CoNbr] = messana.pullHC_COData(HC_CoNbr)  
for HC_CoNbr in range(0,  msysInfo['mHC_changeoverCount'] ):
    messana.pushHC_COData(HC_CoNbr, HC_CoDict)  

print('\nATU')
atuDict = defaultdict(dict)   
for atuNbr in range(0,  msysInfo['mATUcount'] ):
    atuDict[atuNbr] = messana.pullATUData(atuNbr)  
for atuNbr in range(0,  msysInfo['mATUcount'] ):
    messana.pushATUData(atuNbr, atuDict)

print('\n END')

for mzoneNbr in range(0,systemDict['mMacrozoneCount']):
    messana.pullSubSystemData(messana.mSystem['macrozones'], mzoneNbr, macrozoneDict)

print('\nhc_changeover')
for hcchangeoverNbr in range (0,systemDict['mHCGroupCount']):
    messana.pullSubSystemData(messana.mSystem['hc_changeover'],hcchangeoverNbr , hc_changeoverDict)

print('\nFAN COILS')
for fcNbr in range(0,systemDict['mFanCoilCount']):
    messana.pullSubSystemData(messana.mSystem['fan_coils'], fcNbr, fan_coilsDict)

print('\nATU')
for zoneNbr in range(0,systemDict['mATUcount']):
    messana.pullSubSystemData(messana.mSystem['atus'], zoneNbr, atusDict)

print('\nBUFFER TANK')
for zoneNbr in range(0,systemDict['mBufTankCount']):
    pullSubSystemData(messana.mSystem['buffer_tanks'], zoneNbr, buffer_tanksDict)

print('\nENERGY SOURCE')
for zoneNbr in range(0,systemDict['mEnergySourceCount']):
    messana.pullSubSystemData(messana.mSystem['energy_sources'], zoneNbr, energy_sourcesDict)

print('\nDHW')
for zoneNbr in range(0,systemDict['mDHWcount']):
    messana.pullSubSystemData(messana.mSystem['domsetic_hot_waters'], zoneNbr, domsetic_hot_waterDict)

print('\n end extracting data')

print('\nSYSTEM - PUT')
for mKey in systemDict:
    pushmessana.mSystem(messana.mSystem['system'], mKey, systemDict[mKey], systemDict)

print('\nZONES - PUT')
for zoneNbr in zoneDict:
    for mKey in zoneDict[zoneNbr]:
        pushMessanaSubSystem(messana.mSystem['zones'], mKey, zoneNbr,zoneDict[zoneNbr][mKey], zoneDict)
        

print('\nMACROZONES - PUT')
for macrozoneNbr in macrozoneDict:
    for mKey in macrozoneDict[macrozoneNbr]:
        PUTSubNode(messana.mSystem['macrozones'], mKey, macrozoneNbr, macrozoneDict[macrozoneNbr][mKey], macrozoneDict)

print('\nhc_changeover - PUT')
for hcgroupcountNbr in hc_changeoverDict:
    for mKey in hc_changeoverDict[hcgroupcountNbr]:
        PUTSubNode(messana.mSystem['hc_changeover'], mKey, hcgroupcountNbr, hc_changeoverDict[hcgroupcountNbr][mKey], hc_changeoverDict)

print('\nFAN COILS - PUT')
for fan_coilNbr in fan_coilsDict:
    for mKey in fan_coilsDict[fan_coilNbr]:
        PUTSubNode(messana.mSystem['fan_coils'], mKey, fan_coilNbr, fan_coilsDict[fan_coilNbr][mKey], fan_coilsDict)

print('\nATU - PUT')
for atuNbr in atusDict:
    for mKey in atusDict[atuNbr]:
        PUTSubNode(messana.mSystem['atus'], mKey, atuNbr, atusDict[atuNbr][mKey],  atusDict)

print('\nBUFFER TANK - PUT')
for bufferTankNbr in buffer_tanksDict:
    for mKey in buffer_tanksDict[bufferTankNbr]:
        PUTSubNode(messana.mSystem['buffer_tanks'], mKey, bufferTankNbr, buffer_tanksDict[bufferTankNbr][mKey], buffer_tanksDict)

print('\nENERGY SOURCE - PUT')
for energySourceNbr in energy_sourcesDict:
    for mKey in energy_sourcesDict[energySourceNbr]:
        PUTSubNode(messana.mSystem['energy_sources'], mKey, energySourceNbr, energy_sourcesDict[energySourceNbr][mKey], energy_sourcesDict)

print('\nDHW - PUT')
for DHwaterNbr in domsetic_hot_waterDict:
    for mKey in domsetic_hot_waterDict[DHwaterNbr]:
        pushMessanaSubSystem(messana.mSystem['domsetic_hot_waters'], mKey, DHwaterNbr, domsetic_hot_waterDict[DHwaterNbr][mKey], domsetic_hot_waterDict)
print('\nEND put')
'''
#sys.stdout.close() 
