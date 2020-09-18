#!/usr/bin/env python3
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
                                        ,'mExternalAlarm':'/api/system/externalAlarm/'
                                        }
                                    ,
                                    'PUTstr' : {
                                        'mName':'/api/system/name/'
                                        ,'mStatus':'/api/system/status/'
                                        ,'mEnergySavings':'/api/system/energySaving/'
                                        ,'mSetback':'/api/system/setback/' 
                                        }
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
                                        ,'mCapability':'/api/zone/capability/'
                                        }
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
                                        ,'mEnergySave' : '/api/zone/energySaving/'
                                        }
                                    ,
                                    'active':['mCurrentSetPointRH', 'mCurrentSetPointDP'
                                        ,'mHumidity', 'mDewPoint', 'mTemp', 'mAirTemp', 'mAlarmOn'                                         ]
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
                                            ,'mTemp' :'/api/macrozone/temperature/'
                                            }
                                        ,
                                        'PUTstr':{
                                            'mName': '/api/macrozone/name/'
                                            ,'mSetPoint' :'/api/macrozone/setpoint/'
                                            ,'mStatus':'/api/macrozone/status/'
                                            ,'mScheduleOn' : '/api/macrozone/scheduleOn/'
                                            }
                                        ,
                                        'active':['mTemp', 'mHumidity','mDewPoint' ]
                                        ,
                                        'data' : {}
                        },
                        'hc_changeover' :{ 'GETstr' : {
                                                'mName':'/api/hc/name/'
                                                ,'mMode':'/api/hc/mode/'
                                                ,'mExcutiveSeason':'/api/hc/executiveSeason/'
                                                ,'mAdaptiveComfort':'/api/hc/adaptiveComfort/'
                                                }
                                            ,
                                            'PUTstr':{
                                                'mName':'/api/hc/name/'
                                                ,'mMode':'/api/hc/mode/'
                                                ,'mAdaptiveComfort':'/api/hc/adaptiveComfort/' 
                                                }
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
                                        ,'mAlarmOn':'/api/fan/alarmOn/'
                                        }
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
                                    #,'mCurrentSetpointRH':'/api/atu/currentSetpointRH/'
                                    #,'mCurrentSetpointDP':'/api/atu/currentSetpointDP/'
                                    }
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
                                    #,'mCurrentSetpointRH':'/api/atu/currentSetpointRH/'
                                    #,'mCurrentSetpointDP':'/api/atu/currentSetpointDP/'
                                    }
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
                                            ,'mAlarmOn':'/api/enr/alarmOn/' 
                                            }
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
                                            ,'mAlarmOn':'/api/tnk/alarmOn/'
                                            }
                                         ,
                                         'PUTstr':{
                                            'mName':'/api/tnk/name/'
                                            ,'mStatus':'/api/tnk/status/'
                                            ,'mMode':'/api/tnk/mode/' 
                                            }
                                         ,
                                         'active':['mTemp', 'mAlarmOn']
                                         ,
                                         'data' : {}
                        },
                        'domsetic_hot_waters': {'GETstr' : {
                                                    'mStatus':'/api/dhw/status/'
                                                    ,'mName':'/api/dhw/name/'
                                                    ,'mTemp':'/api/dhw/temperature/'
                                                    ,'mTargetTemp':'/api/dhw/targetTemperature/' 
                                                    }
                                                ,
                                                'PUTstr':{ 
                                                    'mStatus':'/api/dhw/status/'
                                                    ,'mName':'/api/dhw/name/'
                                                    ,'mTargetTemp':'/api/dhw/targetTemperature/'
                                                    }
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
        sysData= {}
        print('GETSystem: ' + mKey )
        GETStr = self.IP+self.mSystem['system']['GETstr'][mKey] + '?' + self.APIStr 
        print( GETStr)
        systemTemp = requests.get(GETStr)
        print(str(systemTemp))
        if str(systemTemp) == self.RESPONSE_OK:
           systemTemp = systemTemp.json()
           print(systemTemp)
           self.mSystem['system']['data'][mKey] = systemTemp[str(list(systemTemp.keys())[0])]
           sysData['statusOK'] = True   
        else:
           print(str(mKey) + ' error')
           sysData['statusOK'] = False
           #self.systemDict[mKey] = -1
        return(sysData) 

    def PUTSystem(self, mKey, value):
            sysData= {}
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
               sysData['statusOK'] =True
            else:
               sysData['statusOK'] = False
            return(sysData)          

    def GETNodeData(self, mNodeKey, instNbr, mKey):
        print('GETSubNodeData: ' + mNodeKey + ' ' + str(instNbr)+ ' ' + mKey)
        if mKey in self.mSystem[mNodeKey]['GETstr']:
            GETStr =self.IP+self.mSystem[mNodeKey]['GETstr'][mKey]+str(instNbr)+'?'+ self.APIStr 
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
        else: 
                nodeData['error'] = 'Put does not accept keywork: ' + mKey
                nodeData['statusOK'] =False
        return(nodeData)   
   

    def PUTNodeData(self, mNodeKey, nodeNbr, mKey, value):
        nodeData = {}
        if mKey in self.mSystem[mNodeKey]['PUTstr']:
            PUTStr = self.IP + self.mSystem[mNodeKey]['PUTstr'][mKey]
            print('PUT str: ' + PUTStr + str(value))
            mData = {'id':nodeNbr, 'value': value, self.APIKey : self.APIKeyVal}
            resp = requests.put(PUTStr, json=mData)
            if str(resp) == self.RESPONSE_OK:
                self.mSystem[mNodeKey]['data'][nodeNbr][mKey] = value
                nodeData['statusOK'] = True
                return(nodeData)
            elif str(resp) == self.RESPONSE_NO_SUPPORT:
                temp1 =  resp.content
                res_dict = json.loads(temp1.decode('utf-8')) 
                nodeData['error'] = str(resp) + ': Not able to PUT key: '+ str(res_dict.values()) + ' Subnode ' + str(id) + ' for key: ' + str(mKey) + ' value:', str(value)
                print(nodeData['error'])
                nodeData['statusOK'] =False
                return(nodeData)
            elif str(resp) == self.RESPONSE_NO_RESPONSE:
                nodeData['error'] = str(resp) + ': Error: No response from API for key: ' + str(mKey)+ ' value:', str(value)
                print(nodeData['error'])
                nodeData['statusOK'] =False
                return(nodeData)
            else:
                nodeData['error'] = str(resp) + ': Error: Unknown:for key: ' + str(mKey)+ ' value:', str(value)
                print(nodeData['error'])
                nodeData['statusOK'] =False
                return(nodeData)
        else:
            nodeData['error'] = 'Node ' + mNodeKey + ' does not accept keyword: ' + mKey
            print(nodeData['error'])
            nodeData['nodeDataOK'] =False
            return(nodeData)

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
        status = self.PUTNodeData('zones', zoneNbr, mKey, value)
        return(status)

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

    def pullMacroZoneKeys(self, macrozoneNbr):
        print('pullMacroZoneKeys')
        keys=[]
        if self.mSystem['macrozones']['data']:
            if macrozoneNbr in self.mSystem['macrozones']['data']: 
                for mKey in self.mSystem['macrozones']['data'][macrozoneNbr]:
                    if not(mKey in keys):
                        keys.append(mKey)
            else:
                self.pullMacroZoneDataAll(macrozoneNbr)
                for mKey in self.mSystem['macrozones']['data'][macrozoneNbr]:
                    if not(mKey in keys):
                        keys.append(mKey)
        else:
            print('No Keys found - trying to fetch Messana data')
            self.pullSystemDataAll()
            self.pullMacroZoneDataAll(macrozoneNbr)
            for mKey in self.mSystem['macrozones']['data'][macrozoneNbr]:
                if not(mKey in keys):
                    keys.append(mKey)
        return(keys)

    def pushMacroZoneDataIndividual(self, macrozoneNbr, mKey, value):
        print('pullMacroZoneDataMessanaIndividual: ' +str(macrozoneNbr)  + ' ' + mKey + ' ' + str(value))  
        status = self.PUTNodeData('macrozones', macrozoneNbr, mKey, value)
        return(status)


   
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
