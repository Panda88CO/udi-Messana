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
                                        ,'mAirQuality' : '/api/zone/airQuality/'
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
                                    ,'mCurrentSetpointRH':'/api/atu/currentSetpointRH/'
                                    ,'mCurrentSetpointDP':'/api/atu/currentSetpointDP/'
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
                                    ,'mCurrentSetpointRH':'/api/atu/currentSetpointRH/'
                                    ,'mCurrentSetpointDP':'/api/atu/currentSetpointDP/'
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
    def init(self):
        return(True)

    def GETSystem(self, mKey):
        sysData= {}
        print('GETSystem: ' + mKey )
        GETStr = self.IP+self.mSystem['system']['GETstr'][mKey] + '?' + self.APIStr 
        print( GETStr)
        try:
            systemTemp = requests.get(GETStr)
            print(str(systemTemp))
            if str(systemTemp) == self.RESPONSE_OK:
                systemTemp = systemTemp.json()
                print(systemTemp)
                self.mSystem['system']['data'][mKey] = systemTemp[str(list(systemTemp.keys())[0])]
                sysData['statusOK'] = True 
                sysData['data'] = self.mSystem['system']['data'][mKey] 
            else:
                print(str(mKey) + ' error')
                sysData['statusOK'] = False
                sysData['error'] = str(systemTemp)
                #self.systemDict[mKey] = -1
            return(sysData) #No data for given keyword - remove from list 
        except:
            print ('System GET operation failed for :' + mKey)
            sysData['statusOK'] = False
            sysData['error'] = 'EXCEPT: System GET operation failed for :' + mKey  
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
            try:
                resp = requests.put(PUTStr, json=mData)
                print(resp)
                if str(resp) != self.RESPONSE_OK:
                    sysData['statusOK'] = False
                    sysData['error'] = str(resp)+ ': Not able to PUT Key: : '+ mKey + ' value:' + str( value )
                else:
                    sysData['statusOK'] = True
                    sysData['data'] = value
                print(sysData)    
                return(sysData)          
            except:
                sysData['statusOK'] = False
                sysData['error'] = 'System PUT operation failed for :' + mKey + ' '+ str(value)
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
            elif str(resp) == self.RESPONSE_NO_SUPPORT:
                temp1 =  resp.content
                res_dict = json.loads(temp1.decode('utf-8')) 
                nodeData['error'] = str(resp) + ': Not able to PUT key: '+ str(res_dict.values()) + ' Subnode ' + str(id) + ' for key: ' + str(mKey) + ' value:', str(value)
                print(nodeData['error'])
                nodeData['statusOK'] =False
            elif str(resp) == self.RESPONSE_NO_RESPONSE:
                nodeData['error'] = str(resp) + ': Error: No response from API for key: ' + str(mKey)+ ' value:', str(value)
                print(nodeData['error'])
                nodeData['statusOK'] =False
            else:
                nodeData['error'] = str(resp) + ': Error: Unknown:for key: ' + str(mKey)+ ' value:', str(value)
                print(nodeData['error'])
                nodeData['statusOK'] =False
        else:
            nodeData['error'] = 'Node ' + mNodeKey + ' does not accept keyword: ' + mKey
            print(nodeData['error'])
            nodeData['nodeDataOK'] =False
        return(nodeData)

    def getSubSystemKeys (self, subsystemNbr, subsystemKey, cmdKey):
        keys=[]
        if self.mSystem[subsystemKey]['data']:
            if subsystemNbr in self.mSystem[subsystemKey]['data']: 
                for mKey in self.mSystem[subsystemKey]['data'][subsystemNbr]:
                    if mKey in self.mSystem[subsystemKey][cmdKey]:
                        if not(mKey in keys):
                            keys.append(mKey)
            else:
                self.updateSubSystemData(subsystemNbr, subsystemKey)
                for mKey in self.mSystem[subsystemKey]['data'][subsystemNbr]:
                    if mKey in self.mSystem[subsystemKey][cmdKey]:
                        if not(mKey in keys):
                            keys.append(mKey)
        else:
            print('No Keys found - trying to fetch Messana data')
            self.updateSystemData()
            self.updateSubSystemData(subsystemNbr, subsystemKey)
            if self.mSystem[subsystemKey]['data']:
                for mKey in self.mSystem[subsystemKey]['data'][subsystemNbr]:
                    if mKey in self.mSystem[subsystemKey][cmdKey]:
                        if not(mKey in keys):
                            keys.append(mKey)
            else:
                print('No '+ subsystemKey + ' present')
        return(keys)

    def updateSubSystemData(self, subsystemNbr, subsystemKey):
        print('updatSubSystemData: ' + str(subsystemNbr) + ' ' + subsystemKey)
        Data = {}
        dataOK = True
        for mKey in self.mSystem[subsystemKey]['GETstr']:
            print ('GET ' + mKey + ' in zone ' + str(subsystemNbr))
            Data = self.pullSubSystemDataIndividual(subsystemNbr, subsystemKey,  mKey)
            if not(Data['statusOK']):
                dataOK = False
                print ('Error GET' + Data['error'])
        return(dataOK)
    
    def pullSubSystemDataIndividual(self, subsystemNbr, subsystemKey, mKey): 
        Data = {} 
        print('pullSubSystemDataIndividual: ' +str(subsystemNbr)  + ' ' + mKey)    
        if mKey in mKey in self.mSystem[subsystemKey]['GETstr']:
            Data = self.GETNodeData(subsystemKey, subsystemNbr, mKey)
        else:
            Data['statusOK'] = False
            Data['error'] = mKey +' is not a supported GETstr command'
        return(Data)    

    def pushSubSystemDataIndividual(self, subsystemNbr, subsystemKey, mKey, value):
        print('pushZoneDataIndividual: ' +str(subsystemNbr)  + ' ' + mKey + ' ' + str(value))  
        zoneData = {}
        zoneData= self.PUTNodeData(subsystemKey, subsystemNbr, mKey, value)
        if zoneData['statusOK']:
            return(True)
        else:
            print(zoneData['error'])
            return(False)
    
    #System
    def updateSystemData(self):
        print('Update Messana Sytem Data')
        #LOGGER.info(self.mSystem['system'])
        sysData = {}
        DataOK = True
        for mKey in self.mSystem['system']['GETstr']:
            print('GET ' + mKey)
            sysData= self.pullSystemDataIndividual(mKey)
            if not(sysData['statusOK']):
                print ('Error System GET: ' + mKey)
                DataOK = False       
        return(DataOK)

    def pullSystemDataIndividual(self, mKey):
        print('MessanaInfo pull System Data: ' + mKey)
        sysData = {}
        if mKey in self.mSystem['system']['GETstr']:
            sysData = self.GETSystem(mKey)

        else:
            sysData['statusOK'] = False
            sysData['error'] = (mKey + ' is not a supported GETstr command')
        return(sysData)   

    def pushSystemDataIndividual(self, mKey, value):
        sysData={}
        print('MessanaInfo push System Data: ' + mKey)
        sysData = self.PUTSystem(mKey, value)
        if sysData['statusOK']:
           return(True)
        else:
            print(sysData['error'])
            return(False)  
     
    def systemPullKeys(self):
        print('systemPullKeys')
        keys=[]
        if self.mSystem['system']['data']:
            for mKey in self.mSystem['system']['data']:
                keys.append(mKey)
        else:
            print('No Keys found - trying to fetch system data ')
            self.updateSystemData()
            for mKey in self.mSystem['system']['data']:
                keys.append(mKey)
        return(keys)

    def systemPushKeys(self):
        print('systemPushKeys')
        keys=[]
        if self.mSystem['system']['data']:
            for mKey in self.mSystem['system']['data']:
                if mKey in self.mSystem['system']['PUTstr']:
                    keys.append(mKey)
        else:
            print('No Keys found - trying to fetch system data ')
            self.updateSystemData()
            for mKey in self.mSystem['system']['data']:
                if mKey in self.mSystem['system']['PUTstr']:
                    keys.append(mKey)
        return(keys)  
            
    def systemActiveKeys(self):
        print('systemActiveKeys')
        keys = []
        if self.mSystem['system']['data']:
            for mKey in self.mSystem['system']['data']:
                if mKey in self.mSystem['system']['PUTstr']:
                    keys.append(mKey)
        else:
            print('No Keys found - trying to fetch system data ')
            self.updateSystemData()
            for mKey in self.mSystem['system']['data']:
                if mKey in self.mSystem['system']['active']:
                    keys.append(mKey)
        return(keys)  
            
    # Zones
    def updateZoneData(self, zoneNbr):
        print('updatZoneData: ' + str(zoneNbr))
        return(self.updateSubSystemData(zoneNbr, 'zones'))

    def pullZoneDataIndividual(self, zoneNbr, mKey): 
        print('pullZoneDataIndividual: ' +str(zoneNbr)  + ' ' + mKey)    
        return(self.pullSubSystemDataIndividual(zoneNbr, 'zones', mKey))

    def pushZoneDataIndividual(self, zoneNbr, mKey, value):
        print('pushZoneDataIndividual: ' +str(zoneNbr)  + ' ' + mKey + ' ' + str(value))  
        return(self.pushSubSystemDataIndividual(zoneNbr, 'zones', mKey, value))

    def zonePullKeys(self, zoneNbr):
        print('zonePullKeys')
        return( self.getSubSystemKeys (zoneNbr, 'zones', 'GETstr'))

    def zonePushKeys(self, zoneNbr):
        print('zonePushKeys')
        return( self.getSubSystemKeys (zoneNbr, 'zones', 'PUTstr'))
  
    def zoneActiveKeys(self, zoneNbr):
        print('zoneActiveKeys')
        return( self.getSubSystemKeys (zoneNbr, 'zones', 'active'))


    #MacroZone
    def updateMacroZoneData(self, macrozoneNbr):
        print('updatMacroZoneData: ' + str(macrozoneNbr))
        return(self.updateSubSystemData(macrozoneNbr, 'macrozones'))

    def pullMacroZoneDataIndividual(self, macrozoneNbr, mKey): 
        print('pullMacroZoneDataIndividual: ' +str(macrozoneNbr)  + ' ' + mKey)    
        return(self.pullSubSystemDataIndividual(macrozoneNbr, 'macrozones', mKey))

    def pushMacroZoneDataIndividual(self, macrozoneNbr, mKey, value):
        print('pushMacroZoneDataIndividual: ' +str(macrozoneNbr)  + ' ' + mKey + ' ' + str(value))  
        return(self.pushSubSystemDataIndividual(macrozoneNbr, 'macrozones', mKey, value))

    def macrozonePullKeys(self, macrozoneNbr):
        print('macrozonePullKeys')
        return( self.getSubSystemKeys (macrozoneNbr, 'macrozones', 'GETstr'))

    def macrozonePushKeys(self, macrozoneNbr):
        print('macrozonePushKeys')
        return( self.getSubSystemKeys (macrozoneNbr, 'macrozones', 'PUTstr'))
  
    def macrozoneActiveKeys(self, macrozoneNbr):
        print('macrozoneActiveKeys')
        return( self.getSubSystemKeys (macrozoneNbr, 'macrozones', 'active'))    


    # Hot Cold Change Over
    def updateHC_COData(self, HC_CONbr):
        print('updatHC_COData: ' + str(HC_CONbr))
        return(self.updateSubSystemData(HC_CONbr, 'hc_changeover'))

    def pullHC_CODataIndividual(self, HC_CONbr, mKey): 
        print('pullHC_CODataIndividual: ' +str(HC_CONbr)  + ' ' + mKey)    
        return(self.pullSubSystemDataIndividual(HC_CONbr, 'hc_changeover', mKey))

    def pushHC_CODataIndividual(self, HC_CONbr, mKey, value):
        print('pushHC_CODataIndividual: ' +str(HC_CONbr)  + ' ' + mKey + ' ' + str(value))  
        return(self.pushSubSystemDataIndividual(HC_CONbr, 'hc_changeover', mKey, value))

    def hc_changeoverPullKeys(self, HC_CONbr):
        print('hc_changeoverPullKeys')
        return( self.getSubSystemKeys (HC_CONbr, 'hc_changeover', 'GETstr'))

    def hc_changeoverPushKeys(self, HC_CONbr):
        print('hc_changeoverPushKeys')
        return( self.getSubSystemKeys (HC_CONbr, 'hc_changeover', 'PUTstr'))
  
    def hc_changeoverActiveKeys(self, HC_CONbr):
        print('hc_changeoverActiveKeys')
        return( self.getSubSystemKeys (HC_CONbr, 'hc_changeover', 'active'))    
   

    #ATU
    def updateATUData(self, ATUNbr):
        print('updatATUData: ' + str(ATUNbr))
        return(self.updateSubSystemData(ATUNbr, 'atus'))

    def pullATUDataIndividual(self, ATUNbr, mKey): 
        print('pullATUDataIndividual: ' +str(ATUNbr)  + ' ' + mKey)    
        return(self.pullSubSystemDataIndividual(ATUNbr, 'atus', mKey))

    def pushATUDataIndividual(self, ATUNbr, mKey, value):
        print('pushATUDataIndividual: ' +str(ATUNbr)  + ' ' + mKey + ' ' + str(value))  
        return(self.pushSubSystemDataIndividual(ATUNbr, 'atus', mKey, value))

    def atuPullKeys(self, ATUNbr): 
        print('atusPullKeys')
        return( self.getSubSystemKeys (ATUNbr, 'atus', 'GETstr'))

    def atuPushKeys(self, ATUNbr):
        print('atusPushKeys')
        return( self.getSubSystemKeys (ATUNbr, 'atus', 'PUTstr'))
  
    def atuActiveKeys(self, ATUNbr):
        print('atusActiveKeys')
        return( self.getSubSystemKeys (ATUNbr, 'atus', 'active'))    
  
    #Fan Coils
    def updateFanCoilData(self, FanCoilNbr):

        print('updatFanCoilData: ' + str(FanCoilNbr))
        return(self.updateSubSystemData(FanCoilNbr, 'fan_coils'))

    def pullFanCoilDataIndividual(self, FanCoilNbr, mKey): 
        print('pullFanCoilDataIndividual: ' +str(FanCoilNbr)  + ' ' + mKey)    
        return(self.pullSubSystemDataIndividual(FanCoilNbr, 'fan_coils', mKey))

    def pushFanCoilDataIndividual(self, FanCoilNbr, mKey, value):
        print('pushFanCoilDataIndividual: ' +str(FanCoilNbr)  + ' ' + mKey + ' ' + str(value))  
        return(self.pushSubSystemDataIndividual(FanCoilNbr, 'fan_coils', mKey, value))

    def fan_coilPullKeys(self, FanCoilNbr):
        print('fan_coilPullKeys')
        return( self.getSubSystemKeys (FanCoilNbr, 'fan_coils', 'GETstr'))

    def fan_coilPushKeys(self, FanCoilNbr):
        print('fan_coilPushKeys')
        return( self.getSubSystemKeys (FanCoilNbr, 'fan_coils', 'PUTstr'))
  
    def fan_coilActiveKeys(self, FanCoilNbr):
        print('fan_coilActiveKeys')
        return( self.getSubSystemKeys (FanCoilNbr, 'fan_coils', 'active'))    
  
    #energy_sources
    def updateEnergySourceData(self, EnergySourceNbr):
        print('updatEnergySourceData: ' + str(EnergySourceNbr))
        return(self.updateSubSystemData(EnergySourceNbr, 'energy_sources'))

    def pullEnergySourceDataIndividual(self, EnergySourceNbr, mKey): 
        print('pullEnergySourceDataIndividual: ' +str(EnergySourceNbr)  + ' ' + mKey)    
        return(self.pullSubSystemDataIndividual(EnergySourceNbr, 'energy_sources', mKey))

    def pushEnergySourceDataIndividual(self, EnergySourceNbr, mKey, value):
        print('pushEnergySourceDataIndividual: ' +str(EnergySourceNbr)  + ' ' + mKey + ' ' + str(value))  
        return(self.pushSubSystemDataIndividual(EnergySourceNbr, 'energy_sources', mKey, value))

    def energy_sourcePullKeys(self, EnergySourceNbr):
        print('energy_sourcePullKeys')
        return( self.getSubSystemKeys (EnergySourceNbr, 'energy_sources', 'GETstr'))

    def energy_sourcePushKeys(self, EnergySourceNbr):
        print('energy_sourcePushKeys')
        return( self.getSubSystemKeys (EnergySourceNbr, 'energy_sources', 'PUTstr'))
  
    def energy_sourceActiveKeys(self, EnergySourceNbr):
        print('energy_sourceActiveKeys')
        return( self.getSubSystemKeys (EnergySourceNbr, 'energy_sources', 'active'))    


    #Buffer Tank
    def updateBufferTankData(self, BufferTankNbr):
        print('updatBufferTankData: ' + str(BufferTankNbr))
        return(self.updateSubSystemData(BufferTankNbr, 'buffer_tanks'))

    def pullBufferTankDataIndividual(self, BufferTankNbr, mKey): 
        print('pullBufferTankDataIndividual: ' +str(BufferTankNbr)  + ' ' + mKey)    
        return(self.pullSubSystemDataIndividual(BufferTankNbr, 'buffer_tanks', mKey))

    def pushBufferTankDataIndividual(self, BufferTankNbr, mKey, value):
        print('pushBufferTankDataIndividual: ' +str(BufferTankNbr)  + ' ' + mKey + ' ' + str(value))  

        if mKey == 'mStatus':
            BTdata = {}
            BTdata = self.pullSubSystemDataIndividual(BufferTankNbr, 'buffer_tanks', 'mMode')
            if BTdata['data'] != 0:
                return(self.pushSubSystemDataIndividual(BufferTankNbr, 'buffer_tanks', mKey, value))
            else:
                print ('Mode = 0, Cannot set status if mode = 0')
                return(False)
        else:
             return(self.pushSubSystemDataIndividual(BufferTankNbr, 'buffer_tanks', mKey, value))

    def buffer_tankPullKeys(self, BufferTankNbr):
        print('buffer_tankPullKeys')
        return( self.getSubSystemKeys (BufferTankNbr, 'buffer_tanks', 'GETstr'))

    def buffer_tankPushKeys(self, BufferTankNbr):
        print('buffer_tankPushKeys')
        return( self.getSubSystemKeys (BufferTankNbr, 'buffer_tanks', 'PUTstr'))
  
    def buffer_tankActiveKeys(self, BufferTankNbr):
        print('buffer_tankActiveKeys')
        return( self.getSubSystemKeys (BufferTankNbr, 'buffer_tanks', 'active'))    


        #Domestic Hot Water
 

    # Domestic Hot Water
    def updateDHWData(self, DHWNbr):
        print('updatDHWData: ' + str(DHWNbr))
        return(self.updateSubSystemData(DHWNbr, 'domsetic_hot_waters'))

    def pullDHWDataIndividual(self, DHWNbr, mKey): 
        print('pullDHWDataIndividual: ' +str(DHWNbr)  + ' ' + mKey)    
        return(self.pullSubSystemDataIndividual(DHWNbr, 'domsetic_hot_waters', mKey))

    def pushDHWDataIndividual(self, DHWNbr, mKey, value):
        print('pushDHWDataIndividual: ' +str(DHWNbr)  + ' ' + mKey + ' ' + str(value))  
        return(self.pushSubSystemDataIndividual(DHWNbr, 'domsetic_hot_waters', mKey, value))


    def DHWPullKeys(self, DHWNbr):
        print('DHWPullKeys')
        return( self.getSubSystemKeys (DHWNbr, 'domsetic_hot_waters', 'GETstr'))

    def DHWPushKeys(self, DHWNbr):
        print('DHWPushKeys')
        return( self.getSubSystemKeys (DHWNbr, 'domsetic_hot_waters', 'PUTstr'))
  
    def DHWActiveKeys(self, DHWNbr):
        print('DHWActiveKeys')
        return( self.getSubSystemKeys (DHWNbr, 'domsetic_hot_waters', 'active'))    


        #Domestic Hot Water
 







    '''

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

    
   


    '''
