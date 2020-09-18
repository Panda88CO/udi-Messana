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
                                        #,'mCurrentSetPointRH':'/api/zone/currentSetpointRH/'
                                        #,'mCurrentSetPointDP':'/api/zone/currentSetpointDP/'
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
                                        'mName':'/api/fcu/name/'
                                        ,'mState':'/api/fcu/state/'
                                        ,'mCoolingSpeed':'/api/fcu/coolingSpeed/'
                                        ,'mHeatingSpeed':'/api/fcu/heatingSpeed/'
                                        ,'mType':'/api/fcu/type/'
                                        ,'mAlarmOn':'/api/fcu/alarmOn/'
                                        }
                                     ,
                                     'PUTstr':{                                        
                                        'mName':'/api/fcu/name/'
                                        ,'mState':'/api/fcu/state/'
                                        ,'mCoolingSpeed':'/api/fcu/coolingSpeed/'
                                        ,'mHeatingSpeed':'/api/fcu/heatingSpeed/'}
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
                                            'mName':'/api/energySource/name/'
                                            ,'mStatus':'/api/energySource/status/'
                                            ,'mDHWstatus':'/api/energySource/dhwStatus/'
                                            ,'mType':'/api/energySource/type/'
                                            ,'mAlarmOn':'/api/energySource/alarmOn/' 
                                            }
                                         ,
                                         'PUTstr':{'mName':'/api/energySource/name/'}
                                         ,
                                         'active':['mAlarmOn']
                                         ,
                                         'data' : {}
                        }, 
                        'buffer_tanks': {'GETstr' : {
                                            'mName':'/api/bufferTank/name/'
                                            ,'mStatus':'/api/bufferTank/status/'
                                            ,'mMode':'/api/bufferTank/mode/'
                                            ,'mTemp':'/api/bufferTank/temperature/'
                                            ,'mAlarmOn':'/api/bufferTank/alarmOn/'
                                            }
                                         ,
                                         'PUTstr':{
                                            'mName':'/api/bufferTank/name/'
                                            ,'mStatus':'/api/bufferTank/status/'
                                            ,'mMode':'/api/bufferTank/mode/' 
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
        nodeData = {}
        if mKey in self.mSystem[mNodeKey]['GETstr']:
            GETStr =self.IP+self.mSystem[mNodeKey]['GETstr'][mKey]+str(instNbr)+'?'+ self.APIStr 
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

    #System

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
    

    # Zones
    
    def pullZoneDataAll(self, zoneNbr):
        print('pullZoneDataAll: ' + str(zoneNbr))
        for mKey in self.mSystem['zones']['GETstr']:
            self.pullZoneDataIndividual(zoneNbr, mKey)


    def pullZoneDataActive(self, zoneNbr):
        print('pullZoneDataActive: ' + str(zoneNbr))
        for mKey in self.mSystem['zones']['active']:
            self.pullZoneDataIndividual(zoneNbr, mKey)
        
    def pullZoneDataIndividual(self, zoneNbr, mKey):  
        print('pullZoneDataIndividual: ' +str(zoneNbr)  + ' ' + mKey)    
        self.GETNodeData('zones', zoneNbr, mKey)

    def pushZoneDataIndividual(self, zoneNbr, mKey, value):
        print('pushZoneDataIndividual: ' +str(zoneNbr)  + ' ' + mKey + ' ' + str(value))  
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
            if self.mSystem['zones']['data']:
                for mKey in self.mSystem['zones']['data'][zoneNbr]:
                    if not(mKey in keys):
                        keys.append(mKey)
            else:
                print('No zones present')
        return(keys)

    #MacroZone

    def pullMacroZoneDataAll(self, macrozoneNbr):
        print('pullMacroZoneDataAll: ' + str(macrozoneNbr))
        for mKey in self.mSystem['macrozones']['GETstr']:
            self.pullMacroZoneDataIndividual(macrozoneNbr, mKey)


    def pullMacroZoneDataActive(self, macrozoneNbr):
        print('pullMacroZoneDataActive: ' + str(macrozoneNbr))
        for mKey in self.mSystem['macrozones']['active']:
            self.pullMacroZoneDataIndividual(macrozoneNbr, mKey)
        
    def pullMacroZoneDataIndividual(self, macrozoneNbr, mKey):  
        print('pullMacroZoneDataIndividual: ' +str(macrozoneNbr)  + ' ' + mKey)    
        self.GETNodeData('macrozones', macrozoneNbr, mKey)

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
            if self.mSystem['macrozones']['data']: 
                for mKey in self.mSystem['macrozones']['data'][macrozoneNbr]:
                    if not(mKey in keys):
                        keys.append(mKey)
            else:
                print('No macro zons present')
        return(keys)

    def pushMacroZoneDataIndividual(self, macrozoneNbr, mKey, value):
        print('pushMacroZoneDataIndividual: ' +str(macrozoneNbr)  + ' ' + mKey + ' ' + str(value))  
        status = self.PUTNodeData('macrozones', macrozoneNbr, mKey, value)
        return(status)


    # Hot Cold Change Over

    def pullHCCODataAll(self, HCCO_Nbr):
        print('pullHCCODataAll: ' + str(HCCO_Nbr))
        for mKey in self.mSystem['hc_changeover']['GETstr']:
            self.pullHCCODataIndividual(HCCO_Nbr, mKey)


    def pullHCCODataActive(self, HCCO_Nbr):
        print('pullHCCODataActive: ' + str(HCCO_Nbr))
        for mKey in self.mSystem['hc_changeover']['active']:
            self.pullHCCODataIndividual(HCCO_Nbr, mKey)
        
    def pullHCCODataIndividual(self, HCCO_Nbr, mKey):  
        print('pullHCCODataMessanaIndividual: ' +str(HCCO_Nbr)  + ' ' + mKey)    
        self.GETNodeData('hc_changeover', HCCO_Nbr, mKey)

    def pullHCCOKeys(self, HCCO_Nbr):
        print('pullHCCOKeys')
        keys=[]
        if self.mSystem['hc_changeover']['data']:
            if HCCO_Nbr in self.mSystem['hc_changeover']['data']: 
                for mKey in self.mSystem['hc_changeover']['data'][HCCO_Nbr]:
                    if not(mKey in keys):
                        keys.append(mKey)
            else:
                self.pullHCCODataAll(HCCO_Nbr)
                for mKey in self.mSystem['hc_changeover']['data'][HCCO_Nbr]:
                    if not(mKey in keys):
                        keys.append(mKey)
        else:
            print('No Keys found - trying to fetch Messana data')
            self.pullSystemDataAll()
            self.pullHCCODataAll(HCCO_Nbr)
            if self.mSystem['hc_changeover']['data']:
                for mKey in self.mSystem['hc_changeover']['data'][HCCO_Nbr]:
                    if not(mKey in keys):
                        keys.append(mKey)
            else:
                print('NO Hot Cold Change Over present')
        return(keys)

    def pushHCCODataIndividual(self, HCCO_Nbr, mKey, value):
        print('pushHCCODataMessanaIndividual: ' +str(HCCO_Nbr)  + ' ' + mKey + ' ' + str(value))  
        status = self.PUTNodeData('hc_changeover', HCCO_Nbr, mKey, value)
        return(status)

    #ATU

    def pullATUDataAll(self, ATUNbr):
        print('pullATUDataAll: ' + str(ATUNbr))
        for mKey in self.mSystem['atus']['GETstr']:
            self.pullATUDataIndividual(ATUNbr, mKey)


    def pullATUDataActive(self, ATUNbr):
        print('pullATUDataActive: ' + str(ATUNbr))
        for mKey in self.mSystem['atus']['active']:
            self.pullATUDataIndividual(ATUNbr, mKey)
        
    def pullATUDataIndividual(self, ATUNbr, mKey):  
        print('pullATUDataIndividual: ' +str(ATUNbr)  + ' ' + mKey)    
        self.GETNodeData('atus', ATUNbr, mKey)

    def pullATUKeys(self, ATUNbr):
        print('pullATUKeys')
        keys=[]
        if self.mSystem['atus']['data']:
            if ATUNbr in self.mSystem['atus']['data']: 
                for mKey in self.mSystem['atus']['data'][ATUNbr]:
                    if not(mKey in keys):
                        keys.append(mKey)
            else:
                self.pullATUDataAll(ATUNbr)
                for mKey in self.mSystem['atus']['data'][ATUNbr]:
                    if not(mKey in keys):
                        keys.append(mKey)
        else:
            print('No Keys found - trying to fetch Messana data')
            self.pullSystemDataAll()
            self.pullATUDataAll(ATUNbr)
            if self.mSystem['atus']['data']:
                for mKey in self.mSystem['atus']['data'][ATUNbr]:
                    if not(mKey in keys):
                        keys.append(mKey)
            else:
                print('No ATU present')
        return(keys)

    def pushATUDataIndividual(self, ATUNbr, mKey, value):
        print('pushATUDataIndividual: ' +str(ATUNbr)  + ' ' + mKey + ' ' + str(value))  
        status = self.PUTNodeData('atus', ATUNbr, mKey, value)
        return(status)

    #Fan Coils

    def pullFanCoilDataAll(self, FC_Nbr):
        print('pullFanCoilDataAll: ' + str(FC_Nbr))
        for mKey in self.mSystem['fan_coils']['GETstr']:
            self.pullFanCoilDataIndividual(FC_Nbr, mKey)


    def pullFanCoilDataActive(self, FC_Nbr):
        print('pullFanCoilDataActive: ' + str(FC_Nbr))
        for mKey in self.mSystem['fan_coils']['active']:
            self.pullFanCoilDataIndividual(FC_Nbr, mKey)
        
    def pullFanCoilDataIndividual(self, FC_Nbr, mKey):  
        print('pullFanCoilDataIndividual: ' +str(FC_Nbr)  + ' ' + mKey)    
        self.GETNodeData('fan_coils', FC_Nbr, mKey)

    def pullFanCoilKeys(self, FC_Nbr):
        print('pullFanCoilKeys')
        keys=[]
        if self.mSystem['fan_coils']['data']:
            if FC_Nbr in self.mSystem['fan_coils']['data']: 
                for mKey in self.mSystem['fan_coils']['data'][FC_Nbr]:
                    if not(mKey in keys):
                        keys.append(mKey)
            else:
                self.pullFanCoilDataAll(FC_Nbr)
                for mKey in self.mSystem['fan_coils']['data'][FC_Nbr]:
                    if not(mKey in keys):
                        keys.append(mKey)
        else:
            print('No Keys found - trying to fetch Messana data')
            self.pullSystemDataAll()
            self.pullFanCoilDataAll(FC_Nbr)
            if self.mSystem['fan_coils']['data']:
                for mKey in self.mSystem['fan_coils']['data'][FC_Nbr]:
                    if not(mKey in keys):
                        keys.append(mKey)
            else:
                print('No Fan Coil present')
        return(keys)

    def pushFanCoilDataIndividual(self, FC_Nbr, mKey, value):
        print('pushFanCoilDataIndividual: ' +str(FC_Nbr)  + ' ' + mKey + ' ' + str(value))  
        status = self.PUTNodeData('fan_coils', FC_Nbr, mKey, value)
        return(status)



    #energy_sources

    def pullEnergySourceDataAll(self, EnergySourceNbr):
        print('pullEnergySourceDataAll: ' + str(EnergySourceNbr))
        for mKey in self.mSystem['energy_sources']['GETstr']:
            self.pullEnergySourceDataIndividual(EnergySourceNbr, mKey)


    def pullEnergySourceDataActive(self, EnergySourceNbr):
        print('pullEnergySourceDataActive: ' + str(EnergySourceNbr))
        for mKey in self.mSystem['energy_sources']['active']:
            self.pullEnergySourceDataIndividual(EnergySourceNbr, mKey)
        
    def pullEnergySourceDataIndividual(self, EnergySourceNbr, mKey):  
        print('pullEnergySourceDataIndividual: ' +str(EnergySourceNbr)  + ' ' + mKey)    
        self.GETNodeData('energy_sources', EnergySourceNbr, mKey)

    def pullEnergySourceKeys(self, EnergySourceNbr):
        print('pullEnergySourceKeys')
        keys=[]
        if  self.mSystem['energy_sources']['data']:
            if EnergySourceNbr in self.mSystem['energy_sources']['data']: 
                for mKey in self.mSystem['energy_sources']['data'][EnergySourceNbr]:
                    if not(mKey in keys):
                        keys.append(mKey)
                    else:
                        self.pullEnergySourceDataAll(EnergySourceNbr)
                        for mKey in self.mSystem['energy_sources']['data'][EnergySourceNbr]:
                            if not(mKey in keys):
                                keys.append(mKey)
        else:
            print('No Keys found - trying to fetch Messana data')
            self.pullSystemDataAll()
            self.pullEnergySourceDataAll(EnergySourceNbr)
            if  self.mSystem['energy_sources']['data']:
                if EnergySourceNbr in self.mSystem['energy_sources']['data']: 
                    for mKey in self.mSystem['energy_sources']['data'][EnergySourceNbr]:
                        if not(mKey in keys):
                            keys.append(mKey)
            else:
                print('No Energy Source Present')
        return(keys)

    def pushEnergySourceDataIndividual(self, EnergySourceNbr, mKey, value):
        print('pushEnergySourceDataIndividual: ' +str(EnergySourceNbr)  + ' ' + mKey + ' ' + str(value))  
        status = self.PUTNodeData('energy_sources', EnergySourceNbr, mKey, value)
        return(status)


     #Buffer Tank

    def pullBufferTankDataAll(self, BT_Nbr):
        print('pullBufferTankDataAll: ' + str(BT_Nbr))
        for mKey in self.mSystem['buffer_tanks']['GETstr']:
            self.pullBufferTankDataIndividual(BT_Nbr, mKey)


    def pullBufferTankDataActive(self, BT_Nbr):
        print('pullBufferTankDataActive: ' + str(BT_Nbr))
        for mKey in self.mSystem['buffer_tanks']['active']:
            self.pullBufferTankDataIndividual(BT_Nbr, mKey)
        
    def pullBufferTankDataIndividual(self, BT_Nbr, mKey):  
        print('pullBufferTankDataIndividual: ' +str(BT_Nbr)  + ' ' + mKey)    
        self.GETNodeData('buffer_tanks', BT_Nbr, mKey)

    def pullBufferTankKeys(self, BT_Nbr):
        print('pullBufferTankKeys')
        keys=[]
        if self.mSystem['buffer_tanks']['data']:
            if BT_Nbr in self.mSystem['buffer_tanks']['data']: 
                for mKey in self.mSystem['buffer_tanks']['data'][BT_Nbr]:
                    if not(mKey in keys):
                        keys.append(mKey)
            else:
                self.pullBufferTankDataAll(BT_Nbr)
                for mKey in self.mSystem['buffer_tanks']['data'][BT_Nbr]:
                    if not(mKey in keys):
                        keys.append(mKey)
        else:
            print('No Keys found - trying to fetch Messana data')
            self.pullSystemDataAll()
            self.pullBufferTankDataAll(BT_Nbr)
            if self.mSystem['buffer_tanks']['data']:
                for mKey in self.mSystem['buffer_tanks']['data'][BT_Nbr]:
                    if not(mKey in keys):
                        keys.append(mKey)
            else:
                print('No Buffer Tank present')
        return(keys)


    def pushBufferTankDataIndividual(self, BT_Nbr, mKey, value):
        print('pushBufferTankDataIndividual: ' +str(BT_Nbr)  + ' ' + mKey + ' ' + str(value))  
        status = self.PUTNodeData('buffer_tanks', BT_Nbr, mKey, value)
        return(status)


        #Domestic Hot Water

    def pullDHWDataAll(self, DHW_Nbr):
        print('pullDHWDataAll: ' + str(DHW_Nbr))
        for mKey in self.mSystem['domsetic_hot_waters']['GETstr']:
            self.pullDHWDataIndividual(DHW_Nbr, mKey)


    def pullDHWDataActive(self, DHW_Nbr):
        print('pullDHWDataActive: ' + str(DHW_Nbr))
        for mKey in self.mSystem['domsetic_hot_waters']['active']:
            self.pullDHWDataIndividual(DHW_Nbr, mKey)
        
    def pullDHWDataIndividual(self, DHW_Nbr, mKey):  
        print('pullDHWDataIndividual: ' +str(DHW_Nbr)  + ' ' + mKey)    
        self.GETNodeData('domsetic_hot_waters', DHW_Nbr, mKey)

    def pullDHWKeys(self, DHW_Nbr):
        print('pullDHWKeys')
        keys=[]
        if self.mSystem['domsetic_hot_waters']['data']:
            if DHW_Nbr in self.mSystem['domsetic_hot_waters']['data']: 
                for mKey in self.mSystem['domsetic_hot_waters']['data'][DHW_Nbr]:
                    if not(mKey in keys):
                        keys.append(mKey)
            else:
                self.pullDHWDataAll(DHW_Nbr)
                for mKey in self.mSystem['domsetic_hot_waters']['data'][DHW_Nbr]:
                    if not(mKey in keys):
                        keys.append(mKey)
        else:
            print('No Keys found - trying to fetch Messana data')
            self.pullSystemDataAll()
            self.pullDHWDataAll(DHW_Nbr)
            if self.mSystem['domsetic_hot_waters']['data']:
                for mKey in self.mSystem['domsetic_hot_waters']['data'][DHW_Nbr]:
                    if not(mKey in keys):
                        keys.append(mKey)
            else:
                print('No Domestic Hot Water present')
        return(keys)

    def pushDHWDataIndividual(self, DHW_Nbr, mKey, value):
        print('pushDHWDataIndividual: ' +str(DHW_Nbr)  + ' ' + mKey + ' ' + str(value))  
        status = self.PUTNodeData('domsetic_hot_waters', DHW_Nbr, mKey, value)
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
