#!/usr/bin/env python3
import requests
#from subprocess import call
import json
import os 
from collections import defaultdict
#import polyinterface
#LOGGER = polyinterface.LOGGER


class messanaInfo:
    def __init__ (self, mIPaddress, mAPIkey, mISYcontrollerName):
        
        self.systemID = mISYcontrollerName
        self.zoneID = 'zones'
        self.macrozoneID = 'macrozones'
        self.atuID = 'atus'
        self.dhwID = 'DomHw'
        self.fcID = 'FanCoils'
        self.energySaveID =  'EnergyS'
        self.HotColdcoID = 'HcCo'
        self.bufferTankID = 'BufTanks'
        self.supportedNodeList = [
                             self.zoneID
                            ,self.macrozoneID
                            ,self.atuID
                            ,self.dhwID
                            ,self.fcID
                            ,self.energySaveID
                            ,self.HotColdcoID 
                            ,self.bufferTankID
                            ] 

        self.mSystem = defaultdict(dict)
        self.mSystem = { self.systemID: {  'ISYnode':{ 'nlsICON' :'Thermostat'
                                                ,'sends'   : ['DON', 'DOF']
                                                ,'accepts' : {'UPDATE'         : {   'ISYtext' :'Update System Data'
                                                                                    ,'ISYeditor' : None} 
                                                             ,'SET_STATUS'     : {   'ISYtext' :'System Status'
                                                                                    ,'ISYeditor' : 'mStatus'}
                                                             ,'SET_ENERGYSAVE' : {   'ISYtext' :'Energy Save'
                                                                                    ,'ISYeditor' : 'mEnergySaving'}
                                                             ,'SET_SETBACK'    : {   'ISYtext' :'Setback'
                                                                                    ,'ISYeditor' : 'mSetback' }
                                                            }
                                                }
                                    ,'KeyInfo' : {
                                         'mName':{
                                             'GETstr': '/api/system/name/'
                                            ,'PUTstr': '/api/system/name/'
                                            ,'Active': None 
                                            ,'ISYeditor':{   
                                                     'ISYuom':None
                                                    ,'ISYmin':None
                                                    ,'ISYmax':None
                                                    ,'ISYsubset':None
                                                    ,'ISYstep':None
                                                    ,'ISYprec':None }
                                            , 'ISYnls': None  
                                            }   
                                        ,'mApiVer':{
                                             'GETstr' :'/api/system/apiVersion/'
                                            ,'PUTstr': None 
                                            ,'Active': None 
                                            ,'ISYeditor':{   
                                                     'ISYuom':None
                                                    ,'ISYmin':None
                                                    ,'ISYmax':None
                                                    ,'ISYsubset':None
                                                    ,'ISYstep':None
                                                    ,'ISYprec':None }
                                            , 'ISYnls': None               
                                            }                                           
                                        ,'mStatus': {
                                             'GETstr' : '/api/system/status/'
                                            ,'PUTstr' : '/api/system/status/'
                                            ,'Active' : None
                                            ,'ISYeditor':{   
                                                     'ISYuom': 25
                                                    ,'ISYmin':None
                                                    ,'ISYmax':None
                                                    ,'ISYsubset': '0-1'
                                                    ,'ISYstep':None
                                                    ,'ISYprec':None }
                                            ,'ISYnls': {    
                                                     'nlsTEXT' : 'System state'
                                                    ,'nlsValues' : { 0:'Off', 1:'On' }
                                                   }
                                                 }
                                        ,'mZoneCount':{
                                             'GETstr':'/api/system/zoneCount/'
                                            ,'PUTstr': None 
                                            ,'Active': None                                      
                                            ,'ISYeditor':{   
                                                     'ISYuom': 112
                                                    ,'ISYmin': 0 
                                                    ,'ISYmax': 32
                                                    ,'ISYsubset':None
                                                    ,'ISYstep': 1
                                                    ,'ISYprec': 0}
                                            ,'ISYnls': {    
                                                     'nlsTEXT' : '# of Zones' 
                                                    ,'nlsValues' : None
                                                    }
                                                }                                         
                                        ,'mATUcount':{
                                             'GETstr':'/api/system/atuCount/'
                                            ,'PUTstr': None 
                                            ,'Active': None                               
                                            ,'ISYeditor':{
                                                     'ISYuom': 112
                                                    ,'ISYmin': 0 
                                                    ,'ISYmax': 8
                                                    ,'ISYsubset':None
                                                    ,'ISYstep': 1
                                                    ,'ISYprec': 0}
                                            ,'ISYnls': {    
                                                     'nlsTEXT' : '# of ATU' 
                                                    ,'nlsValues' : None
                                                    }
                                                }
                                        ,'mDHWcount': {
                                             'GETstr':'/api/system/dhwCount/'
                                            ,'PUTstr': None 
                                            ,'Active': None                                     
                                            ,'ISYeditor':{   
                                                     'ISYuom': 112
                                                    ,'ISYmin': 0 
                                                    ,'ISYmax': 8
                                                    ,'ISYsubset':None
                                                    ,'ISYstep': 1
                                                    ,'ISYprec': 0}
                                            ,'ISYnls': {    
                                                     'nlsTEXT' : '# of Hot Water' 
                                                    ,'nlsValues' :None
                                                    }
                                                }
                                        ,'mMacrozoneCount': {
                                             'GETstr':'/api/system/macrozoneCount/'
                                            ,'PUTstr': None 
                                            ,'Active': None                                        
                                            ,'ISYeditor':{   
                                                     'ISYuom': 112
                                                    ,'ISYmin': 0 
                                                    ,'ISYmax': 16
                                                    ,'ISYsubset':None
                                                    ,'ISYstep': 1
                                                    ,'ISYprec': 0}
                                            ,'ISYnls': {    
                                                     'nlsTEXT' : '# of MacroZones (all=1)' 
                                                    ,'nlsValues' : None 
                                                    }
                                                }                                        
                                        ,'mFanCoilCount': {
                                            'GETstr':'/api/system/fancoilCount/'
                                            ,'PUTstr': None 
                                            ,'Active': None                                      
                                            ,'ISYeditor':{   
                                                     'ISYuom': 112
                                                    ,'ISYmin': 0 
                                                    ,'ISYmax': 16
                                                    ,'ISYsubset':None
                                                    ,'ISYstep': 1
                                                    ,'ISYprec': 0}
                                            ,'ISYnls': {    
                                                     'nlsTEXT' : '# of Fan Coils' 
                                                    ,'nlsValues' : None
                                                    }
                                                }                                          
                                        ,'mEnergySourceCount':{
                                             'GETstr':'/api/system/energySourceCount/'
                                            ,'PUTstr': None 
                                            ,'Active': None                                       
                                            ,'ISYeditor':{   
                                                     'ISYuom': 112
                                                    ,'ISYmin': 0 
                                                    ,'ISYmax': 16
                                                    ,'ISYsubset':None
                                                    ,'ISYstep': 1
                                                    ,'ISYprec': 0}
                                            ,'ISYnls': {    
                                                     'nlsTEXT' : '# of Energy Sources' 
                                                    ,'nlsValues' :  None 
                                                    }
                                                }                                          
                                        ,'mhc_coCount':{
                                             'GETstr':'/api/system/HCgroupCount/'
                                            ,'PUTstr': None 
                                            ,'Active': None                                       
                                            ,'ISYeditor':{   
                                                     'ISYuom': 112
                                                    ,'ISYmin': 0 
                                                    ,'ISYmax': 16
                                                    ,'ISYsubset':None
                                                    ,'ISYstep': 1
                                                    ,'ISYprec': 0}
                                            ,'ISYnls': {    
                                                     'nlsTEXT' : '# of Hot Cold ' 
                                                    ,'nlsValues' :  None 
                                                     }
                                                }                                          
                                        ,'mBufTankCount':{
                                             'GETstr':'/api/system/bufferTankCount/'
                                            ,'PUTstr': None 
                                            ,'Active': None                                  
                                            ,'ISYeditor':{   
                                                     'ISYuom': 112
                                                    ,'ISYmin': 0 
                                                    ,'ISYmax': 16
                                                    ,'ISYsubset':None
                                                    ,'ISYstep': 1
                                                    ,'ISYprec': 0}
                                            ,'ISYnls': {    
                                                     'nlsTEXT' : '# of Buffer Tanks' 
                                                    ,'nlsValues' : None
                                                        }
                                                }                                                                                                                           
                                        ,'mUnitTemp':{
                                             'GETstr' : '/api/system/tempUnit/'
                                            ,'PUTstr' : None
                                            ,'Active' : None
                                            ,'ISYeditor':{   
                                                     'ISYuom': 25
                                                    ,'ISYmin':None
                                                    ,'ISYmax':None
                                                    ,'ISYsubset':'0-1'
                                                    ,'ISYstep':None
                                                    ,'ISYprec':None }
                                            ,'ISYnls': {    
                                                    'nlsTEXT' : 'Temp Unit' 
                                                    ,'nlsValues' : {0:'Celcius', 1:'Farenheit'}
                                                        }
                                                }                                        
                                        ,'mEnergySaving':{
                                             'GETstr' : '/api/system/energySaving/'
                                            ,'PUTstr' : '/api/system/energySaving/'
                                            ,'Active' : None
                                            ,'ISYeditor':{   
                                                     'ISYuom': 25
                                                    ,'ISYmin':None
                                                    ,'ISYmax':None
                                                    ,'ISYsubset': '0-1'
                                                    ,'ISYstep':None
                                                    ,'ISYprec':None }
                                            ,'ISYnls': {    
                                                     'nlsTEXT' : 'Energy Savings' 
                                                    ,'nlsValues' : { 0:'Disabled', 1:'Enabled' }
                                                        }
                                                }                                        
                                        ,'mSetback':{
                                             'GETstr' : '/api/system/setback/'
                                            ,'PUTstr' : '/api/system/setback/'
                                            ,'Active' : None
                                            ,'ISYeditor':{   
                                                     'ISYuom': 25
                                                    ,'ISYmin':None
                                                    ,'ISYmax':None
                                                    ,'ISYsubset': '0-1'
                                                    ,'ISYstep':None
                                                    ,'ISYprec':None }
                                            ,'ISYnls': {    
                                                     'nlsTEXT' : 'Setback Status' 
                                                    ,'nlsValues' : { 0:'Disabled',  1:'Enabled' }
                                                        }
                                                }                                          
                                        ,'mExternalAlarm':{
                                             'GETstr' : '/api/system/externalAlarm/'
                                            ,'PUTstr' : None
                                            ,'Active' : '/api/system/externalAlarm/'
                                            ,'ISYeditor':{    
                                                     'ISYuom': 25
                                                    ,'ISYmin':None
                                                    ,'ISYmax':None
                                                    ,'ISYsubset': '0-1'
                                                    ,'ISYstep':None
                                                    ,'ISYprec':None }
                                            ,'ISYnls': {    
                                                     'nlsTEXT' : 'External Alarm' 
                                                    ,'nlsValues' : { 0:'Off', 1:'On' }
                                                        }
                                                }   
                                         }                                         
                                     ,'data':{}
                                     ,'SensorCapability' : {}
                                     ,'GETkeysList' :{}
                                     ,'PUTkeysList' :{}
                        },
                        self.zoneID: {   'ISYnode':{'nlsICON':'TempSensor'
                                                ,'sends'   : []
                                                ,'accepts' : {'UPDATE'          : {   'ISYtext' :'Update System Data'
                                                                                    ,'ISYeditor' : None} 
                                                             ,'SET_SETPOINT'    : {   'ISYtext' :'Set Temperature'
                                                                                    ,'ISYeditor' : 'mSetpoint' }
                                                             ,'SET_STATUS'      : {   'ISYtext' :'Zone State'
                                                                                    ,'ISYeditor' : 'mStatus' }                                                         
                                                             ,'SET_ENERGYSAVE'  : {   'ISYtext' :'Energy Saving'
                                                                                    ,'ISYeditor' : 'mEnergySaving' }
                                                             ,'SET_SCHEDULEON'  : {   'ISYtext' :'Schedule Status'
                                                                                    ,'ISYeditor' : 'mScheduleOn' }
                                                             ,'CurrentSetpointDP': { 'ISYtext' :'Current Setpoint Dewpoint'
                                                                                    ,'ISYeditor' : 'mCurrentSetpointDP'}
                                                             ,'CurrentSetpointRH' : { 'ISYtext' :'Current Setpoint Rel. Humidity'
                                                                                    ,'ISYeditor' : 'mCurrentSetpointRH'}
                                                             ,'DehumSetpointDP' : { 'ISYtext' :'Dehumdification Setpoint Dewpoint'
                                                                                    ,'ISYeditor' : 'mDehumSetpointDP'}
                                                             ,'DehumSetpointRH' : { 'ISYtext' :'Dehumdification Setpoint Rel. Humidity'
                                                                                    ,'ISYeditor' : 'mDehumSetpointRH'}
                                                             ,'HumSetpointDP'   : { 'ISYtext' :'Humdification Setpoint Dewpoint'
                                                                                    ,'ISYeditor' : 'mHumSetpointDP'}
                                                             ,'HumSetpointRH'   : { 'ISYtext' :'Humdification Setpoint Rel. Humidity'
                                                                                    ,'ISYeditor' : 'mHumSetpointRH'}
                                                             ,'SET_CO2'         :{ 'ISYtext' :'CO2 Setpoint'
                                                                                    ,'ISYeditor' : 'mCO2'}

                                                            } 
                                                }
                                    ,'KeyInfo' : {
                                         'mName':{
                                             'GETstr': '/api/zone/name/'
                                            ,'PUTstr': '/api/zone/name/'
                                            ,'Active': None 
                                            ,'ISYeditor':{   
                                                     'ISYuom':None
                                                    ,'ISYmin':None
                                                    ,'ISYmax':None
                                                    ,'ISYsubset':None
                                                    ,'ISYstep':None
                                                    ,'ISYprec':None }
                                            , 'ISYnls': {    
                                                     'nlsTEXT' : 'Zone Name' 
                                                    ,'nlsValues' : None 
                                                        }  
                                                }  
                                        ,'mSetpoint' :{
                                             'GETstr': '/api/zone/setpoint/'
                                            ,'PUTstr': '/api/zone/setpoint/'
                                            ,'Active': None 
                                            ,'ISYeditor':{   
                                                     'ISYuom':17
                                                    ,'ISYmin':40
                                                    ,'ISYmax':120
                                                    ,'ISYsubset':None
                                                    ,'ISYstep':0.5
                                                    ,'ISYprec':1 }
                                            , 'ISYnls': {    
                                                     'nlsTEXT' : 'Set Temp' 
                                                    ,'nlsValues' : None
                                                        }
                                                    }
                                        ,'mStatus':{ 
                                             'GETstr': '/api/zone/status/'
                                            ,'PUTstr': '/api/zone/status/'
                                            ,'Active': None 
                                            ,'ISYeditor':{   
                                                     'ISYuom': 25
                                                    ,'ISYmin':None
                                                    ,'ISYmax':None
                                                    ,'ISYsubset': '0-1'
                                                    ,'ISYstep':None
                                                    ,'ISYprec':None }
                                            ,'ISYnls': {    
                                                     'nlsTEXT' : 'Zone state'
                                                    ,'nlsValues' : {0:'Off', 1:'On' }
                                                        }
                                                    }
                                        ,'mHumSetpointRH': { 
                                             'GETstr': '/api/zone/humidSetpointRH/'
                                            ,'PUTstr': '/api/zone/humidSetpointRH/'
                                            ,'Active': None 
                                            ,'ISYeditor':{   
                                                     'ISYuom':112
                                                    ,'ISYmin':0
                                                    ,'ISYmax':100
                                                    ,'ISYsubset':None
                                                    ,'ISYstep':1
                                                    ,'ISYprec':0 }
                                            , 'ISYnls': {    
                                                     'nlsTEXT' : 'Hum Set Point RH'  
                                                    ,'nlsValues' : None 
                                                        }
                                                    }
                                        ,'mHumSetpointDP': { 
                                             'GETstr': '/api/zone/humidSetpointDP/'
                                            ,'PUTstr': '/api/zone/humidSetpointDP/'
                                            ,'Active': None 
                                            ,'ISYeditor':{   
                                                     'ISYuom':112
                                                    ,'ISYmin':0
                                                    ,'ISYmax':100
                                                    ,'ISYsubset':None
                                                    ,'ISYstep':1
                                                    ,'ISYprec':0 }
                                            , 'ISYnls': {    
                                                     'nlsTEXT' : 'Hum Set Point DP'  
                                                    ,'nlsValues' : None 
                                                        }
                                                    }
                                        ,'mDehumSetpointRH':{ 
                                             'GETstr': '/api/zone/dehumSetpointRH/'
                                            ,'PUTstr': '/api/zone/dehumSetpointRH/'
                                            ,'Active': None 
                                            ,'ISYeditor':{   
                                                     'ISYuom':112
                                                    ,'ISYmin':0
                                                    ,'ISYmax':100
                                                    ,'ISYsubset':None
                                                    ,'ISYstep':1
                                                    ,'ISYprec':0 }
                                            , 'ISYnls': {    
                                                     'nlsTEXT' : 'DeHum Set Point RH'  
                                                    ,'nlsValues' : None 
                                                        }
                                                    }
                                        ,'mDehumSetpointDP': { 
                                             'GETstr': '/api/zone/dehumSetpointDP/'
                                            ,'PUTstr': '/api/zone/dehumSetpointDP/'
                                            ,'Active': None 
                                            ,'ISYeditor':{   
                                                     'ISYuom':112
                                                    ,'ISYmin':0
                                                    ,'ISYmax':100
                                                    ,'ISYsubset':None
                                                    ,'ISYstep':1
                                                    ,'ISYprec':0 }
                                            , 'ISYnls': {    
                                                     'nlsTEXT' : 'DeHum Set Point DP'  
                                                    ,'nlsValues' : None 
                                                        }
                                                    }
                                        ,'mCurrentSetpointRH': { 
                                             'GETstr': '/api/zone/currentSetpointRH/'
                                            ,'PUTstr': '/api/zone/currentSetpointRH/'
                                            ,'Active': None
                                            ,'ISYeditor':{   
                                                     'ISYuom':112
                                                    ,'ISYmin':0
                                                    ,'ISYmax':100
                                                    ,'ISYsubset':None
                                                    ,'ISYstep':1
                                                    ,'ISYprec':0 }
                                            , 'ISYnls': {    
                                                     'nlsTEXT' : 'Current Set Point RH'  
                                                    ,'nlsValues' : None 
                                                        }
                                                    }
                                        ,'mCurrentSetpointDP': { 
                                             'GETstr': '/api/zone/currentSetpointDP/'
                                            ,'PUTstr': '/api/zone/currentSetpointDP/' 
                                            ,'Active': None
                                            ,'ISYeditor':{   
                                                     'ISYuom':112
                                                    ,'ISYmin':0
                                                    ,'ISYmax':100
                                                    ,'ISYsubset':None
                                                    ,'ISYstep':1
                                                    ,'ISYprec':0 }
                                            , 'ISYnls': {    
                                                     'nlsTEXT' : 'Current Set Point DP'  
                                                    ,'nlsValues' : None 
                                                        }
                                                    }
                                        ,'mHumidity': { 
                                             'GETstr': '/api/zone/humidity/'
                                            ,'PUTstr': None
                                            ,'Active': None
                                            ,'ISYeditor':{   
                                                     'ISYuom':51
                                                    ,'ISYmin':0
                                                    ,'ISYmax':100
                                                    ,'ISYsubset':None
                                                    ,'ISYstep':1
                                                    ,'ISYprec':1 }
                                            , 'ISYnls': {    
                                                     'nlsTEXT' : 'Humidity' 
                                                    ,'nlsValues' : None
                                                        }
                                                    }
                                        ,'mDewPoint' : { 
                                             'GETstr': '/api/zone/dewpoint/'
                                            ,'PUTstr': None
                                            ,'Active': None
                                            ,'ISYeditor':{   
                                                     'ISYuom':51
                                                    ,'ISYmin':0
                                                    ,'ISYmax':100
                                                    ,'ISYsubset':None
                                                    ,'ISYstep':1
                                                    ,'ISYprec':1 }
                                            , 'ISYnls': {    
                                                     'nlsTEXT' : 'Dew Point' 
                                                    ,'nlsValues' : None
                                                        } 
                                                    }
                                        ,'mTemp' : { 
                                             'GETstr': '/api/zone/temperature/'
                                            ,'PUTstr': None
                                            ,'Active': '/api/zone/temperature/'
                                            ,'ISYeditor':{   
                                                     'ISYuom':17
                                                    ,'ISYmin':-40
                                                    ,'ISYmax':120
                                                    ,'ISYsubset':None
                                                    ,'ISYstep':0.5
                                                    ,'ISYprec':1 }
                                            , 'ISYnls': {    
                                                     'nlsTEXT' : 'Perceived Temp' 
                                                    ,'nlsValues' : None
                                                        } 
                                                    }
                                        ,'mAirQuality' : { 
                                             'GETstr': '/api/zone/airQuality/'
                                            ,'PUTstr': None
                                            ,'Active': '/api/zone/airQuality/'
                                            ,'ISYeditor':{   
                                                     'ISYuom':108
                                                    ,'ISYmin':0
                                                    ,'ISYmax':1000
                                                    ,'ISYsubset':None
                                                    ,'ISYstep':1
                                                    ,'ISYprec':0 }
                                            , 'ISYnls': {    
                                                     'nlsTEXT' : 'Air Quality'  
                                                    ,'nlsValues' : None 
                                                        }
                                                    }                                     
                                        ,'mScheduleOn' : {
                                            'GETstr': '/api/zone/scheduleOn/'
                                            ,'PUTstr': '/api/zone/scheduleOn/'
                                            ,'Active': None 
                                            ,'ISYeditor':{   
                                                     'ISYuom':25
                                                    ,'ISYmin':None
                                                    ,'ISYmax':None
                                                    ,'ISYsubset':'0-1'
                                                    ,'ISYstep':None
                                                    ,'ISYprec':None }
                                            , 'ISYnls': {    
                                                     'nlsTEXT' : 'Schedule Status' 
                                                    ,'nlsValues' : { 0:'Off', 1:'On' }
                                                        }  
                                                    } 
                                        ,'mCO2' : { 
                                             'GETstr': '/api/zone/co2/'
                                            ,'PUTstr': None
                                            ,'Active': '/api/zone/co2/'
                                            ,'ISYeditor':{   
                                                     'ISYuom':108
                                                    ,'ISYmin':0
                                                    ,'ISYmax':1000
                                                    ,'ISYsubset':None
                                                    ,'ISYstep':1
                                                    ,'ISYprec':0 }
                                            , 'ISYnls': {    
                                                     'nlsTEXT' : 'CO2'  
                                                    ,'nlsValues' : None 
                                                        }
                                                    }                                     
                                        ,'mVoc' : { 
                                             'GETstr': '/api/zone/voc/'
                                            ,'PUTstr': None
                                            ,'Active': '/api/zone/voc/'
                                            ,'ISYeditor':{   
                                                     'ISYuom':108
                                                    ,'ISYmin':0
                                                    ,'ISYmax':1000
                                                    ,'ISYsubset':None
                                                    ,'ISYstep':1
                                                    ,'ISYprec':0 }
                                            , 'ISYnls': {    
                                                     'nlsTEXT' : 'Volatile Organic Compound'  
                                                    ,'nlsValues' : None 
                                                        }
                                                    }                                                  
                                        ,'mAirTemp' : { 
                                             'GETstr': '/api/zone/airTemperature/'
                                            ,'PUTstr': None
                                            ,'Active': '/api/zone/airTemperature/' 
                                            ,'ISYeditor':{   
                                                     'ISYuom':17
                                                    ,'ISYmin':-40
                                                    ,'ISYmax':120
                                                    ,'ISYsubset':None
                                                    ,'ISYstep':1
                                                    ,'ISYprec':1 }
                                            , 'ISYnls': {    
                                                     'nlsTEXT' : 'Roon air Temp' 
                                                    ,'nlsValues' : None
                                                        } 
                                                    }
                                        ,'mMacrozoneId' : { 
                                             'GETstr': '/api/zone/macrozoneId/'
                                            ,'PUTstr': None
                                            ,'Active': None 
                                            ,'ISYeditor':{   
                                                     'ISYuom':112
                                                    ,'ISYmin':0
                                                    ,'ISYmax':40
                                                    ,'ISYsubset':None
                                                    ,'ISYstep':1
                                                    ,'ISYprec':0 }
                                            , 'ISYnls': {    
                                                     'nlsTEXT' : 'Macro Zone member'  
                                                    ,'nlsValues' : None 
                                                        }
                                                    }  
                                        ,'mEnergySaving' : { 
                                             'GETstr': '/api/zone/energySaving/'
                                            ,'PUTstr': '/api/zone/energySaving/'
                                            ,'Active': None 
                                            ,'ISYeditor':{   
                                                     'ISYuom':25
                                                    ,'ISYmin':None
                                                    ,'ISYmax':None
                                                    ,'ISYsubset':'0-1'
                                                    ,'ISYstep':None
                                                    ,'ISYprec':None }
                                            , 'ISYnls': {    
                                                     'nlsTEXT' : 'Energy Save Status' 
                                                    ,'nlsValues' : { 0:'Off', 1:'On' }
                                                        }  
                                                    } 
                                        ,'mAlarmOn':{ 
                                             'GETstr': '/api/zone/alarmOn/'
                                            ,'PUTstr': None
                                            ,'Active': '/api/zone/alarmOn/'
                                            ,'ISYeditor':{   
                                                     'ISYuom':25
                                                    ,'ISYmin':None
                                                    ,'ISYmax':None
                                                    ,'ISYsubset':'0-1'
                                                    ,'ISYstep':None
                                                    ,'ISYprec':None }
                                            , 'ISYnls': {    
                                                     'nlsTEXT' : 'Alarm Status' 
                                                    ,'nlsValues' : { 0:'Off', 1:'On' }
                                                        }  
                                                    } 
                                        ,'mThermalStatus': { 
                                             'GETstr': '/api/zone/thermalStatus/'
                                            ,'PUTstr': None
                                            ,'Active': '/api/zone/thermalStatus/'
                                            ,'ISYeditor':{   
                                                     'ISYuom':25
                                                    ,'ISYmin':None
                                                    ,'ISYmax':None
                                                    ,'ISYsubset':'0-4'
                                                    ,'ISYstep':None
                                                    ,'ISYprec':None }
                                            , 'ISYnls': {    
                                                     'nlsTEXT' : 'Thermal Status'  
                                                    ,'nlsValues' : { 0:'No Thermal'
                                                                    ,1:'Heating Request'
                                                                    ,2:'Cooling Request'
                                                                    ,3:'H & C request' }
                                                        }
                                                    }    
                                        ,'mCapability': {
                                             'GETstr': '/api/zone/capability/'
                                            ,'PUTstr': None
                                            ,'Active': None 
                                            ,'ISYeditor':{   
                                                     'ISYuom':None
                                                    ,'ISYmin':None
                                                    ,'ISYmax':None
                                                    ,'ISYsubset':None
                                                    ,'ISYstep':None
                                                    ,'ISYprec':None }
                                            , 'ISYnls': {    
                                                     'nlsTEXT' : None
                                                    }
                                        }
                                    }
                                    ,'data' :{}
                                    ,'SensorCapability' : {}
                                    ,'GETkeysList' :{}
                                    ,'PUTkeysList' :{}
                        },
                        self.macrozoneID : {   'ISYnode':{   'nlsICON' :'TempSensor'
                                                        ,'sends'   : []
                                                        ,'accepts' : {'UPDATE'        : { 'ISYtext'   :'Update System'
                                                                                         ,'ISYeditor' : None }
                                                                    ,'SET_SETPOINT'   : {   'ISYtext' :'Set Temperature'
                                                                                         ,'ISYeditor' : 'mSetpoint' }
                                                                    ,'SET_STATUS'     : { 'ISYtext'   :'Macro Zone State'
                                                                                         ,'ISYeditor' : 'mStatus' } 
                                                                    ,'SET_SCHEDULEON' : {   'ISYtext' :'Schedule Status'
                                                                                         ,'ISYeditor' : 'mScheduleOn' }
   
                                                                    }
                                                        }

                                        ,'KeyInfo' : {
                                        'mName':{
                                             'GETstr': '/api/macrozone/name/'
                                            ,'PUTstr': '/api/macrozone/name/'
                                            ,'Active': None 
                                            ,'ISYeditor':{
                                                     'ISYuom':None
                                                    ,'ISYmin':None
                                                    ,'ISYmax':None
                                                    ,'ISYsubset':None
                                                    ,'ISYstep':None
                                                    ,'ISYprec':None }
                                            , 'ISYnls': {    
                                                     'nlsTEXT' : 'Zone Name' 
                                                    ,'nlsValues' : None 
                                                        }
                                                } 
                                        ,'mSetpoint': {
                                              'GETstr':'/api/macrozone/setpoint/'
                                             ,'PUTstr':'/api/macrozone/setpoint/'
                                             ,'Active': None 
                                             ,'ISYeditor':{   
                                                     'ISYuom':17
                                                    ,'ISYmin':40
                                                    ,'ISYmax':120
                                                    ,'ISYsubset':None
                                                    ,'ISYstep':0.5
                                                    ,'ISYprec':1 }
                                            , 'ISYnls': {    
                                                     'nlsTEXT' : 'Set Macro Zone Temp' 
                                                    ,'nlsValues' : None 
                                                    }  
                                                 }
                                        ,'mStatus':{
                                             'GETstr':'/api/macrozone/status/'
                                            ,'PUTstr':'/api/macrozone/status/'
                                            ,'Active': None 
                                            ,'ISYeditor':{   
                                                     'ISYuom': 25
                                                    ,'ISYmin':None
                                                    ,'ISYmax':None
                                                    ,'ISYsubset': '0-1'
                                                    ,'ISYstep':None
                                                    ,'ISYprec':None }
                                            ,'ISYnls': {    
                                                     'nlsTEXT' : 'Macro Zone status'
                                                    ,'nlsValues' : {0:'Off', 1:'On' }
                                                        }
                                                    }
                                        ,'mScheduleOn' :{
                                            'GETstr':'/api/macrozone/scheduleOn/'
                                            ,'PUTstr':'/api/macrozone/scheduleOn/'
                                            ,'Active': None 
                                            ,'ISYeditor':{   
                                                     'ISYuom':25
                                                    ,'ISYmin':None
                                                    ,'ISYmax':None
                                                    ,'ISYsubset':'0-1'
                                                    ,'ISYstep':None
                                                    ,'ISYprec':None }
                                            , 'ISYnls': {    
                                                     'nlsTEXT' : 'Schedule Status' 
                                                    ,'nlsValues' : { 0:'disabled', 1:'Enabled' }
                                                        }  
                                                    } 
                                        ,'mHumidity':{
                                            'GETstr':'/api/macrozone/humidity/'
                                            ,'PUTstr': None
                                            ,'Active': '/api/macrozone/humidity/' 
                                            ,'ISYeditor':{   
                                                     'ISYuom':51
                                                    ,'ISYmin':0
                                                    ,'ISYmax':100
                                                    ,'ISYsubset':None
                                                    ,'ISYstep':1
                                                    ,'ISYprec':1 }
                                            , 'ISYnls': {    
                                                     'nlsTEXT' : 'Humidity' 
                                                    ,'nlsValues' : None
                                                        }
                                                    }                                            }
                                        ,'mDewPoint' : {
                                            'GETstr':'/api/macrozone/dewpoint/'
                                            ,'PUTstr': None
                                            ,'Active': '/api/macrozone/dewpoint/'
                                            ,'ISYeditor':{   
                                                     'ISYuom':51
                                                    ,'ISYmin':0
                                                    ,'ISYmax':100
                                                    ,'ISYsubset':None
                                                    ,'ISYstep':1
                                                    ,'ISYprec':1 }
                                            , 'ISYnls': {    
                                                     'nlsTEXT' : 'Dew Point' 
                                                    ,'nlsValues' : None
                                                        } 
                                                    }                                            
                                        ,'mTemp' : {
                                            'GETstr':'/api/macrozone/temperature/'
                                            ,'PUTstr': None
                                            ,'Active': '/api/macrozone/temperature/'
                                            ,'ISYeditor':{   
                                                     'ISYuom':17
                                                    ,'ISYmin':-40
                                                    ,'ISYmax':120
                                                    ,'ISYsubset':None
                                                    ,'ISYstep':1
                                                    ,'ISYprec':1 }
                                            , 'ISYnls': {    
                                                     'nlsTEXT' : 'Perceived Temp' 
                                                    ,'nlsValues' : None
                                                        } 
                                                    }                                     
                                    ,'data' :{}
                                    ,'SensorCapability' : {}
                                    ,'GETkeysList' :{}
                                    ,'PUTkeysList' :{}                                    
                        }, 
                        self.HotColdcoID  :{ 'ISYnode':{   'nlsICON' :'GenericCtl'
                                                        ,'sends'   : []
                                                        ,'accepts' : {  'UPDATE':  { 'ISYtext'   :'Update System'
                                                                                    ,'ISYeditor' : None } 
                                                                       ,'SET_MODE': { 'ISYtext' :'Set Mode'
                                                                                     ,'ISYeditor' : 'mMode' }
                                                                       ,'SET_ADAPTIVE_COMFORT' :{ 'ISYtext' :'Adaptive System'
                                                                                        ,'ISYeditor' : 'mAdaptiveComfort' } }
                                                        }
                                    ,'KeyInfo' : {
                                         'mName':{
                                             'GETstr': '/api/hc/name/'
                                            ,'PUTstr': '/api/hc/name/'
                                            ,'Active': None 
                                            ,'ISYeditor':{
                                                     'ISYuom':None
                                                    ,'ISYmin':None
                                                    ,'ISYmax':None
                                                    ,'ISYsubset':None
                                                    ,'ISYstep':None
                                                    ,'ISYprec':None }
                                            , 'ISYnls': {    
                                                     'nlsTEXT' : 'Hot Cold CO Name' 
                                                    ,'nlsValues' : None }
                                                }
                                        ,'mMode':{
                                             'GETstr': '/api/hc/mode/'
                                            ,'PUTstr': '/api/hc/mode/'
                                            ,'Active': None 
                                            ,'ISYeditor':{
                                                     'ISYuom':25
                                                    ,'ISYmin':None
                                                    ,'ISYmax':None
                                                    ,'ISYsubset':'0-2'
                                                    ,'ISYstep':None
                                                    ,'ISYprec':None }
                                            , 'ISYnls': {    
                                                     'nlsTEXT' : 'Hot Cold Mode' 
                                                    ,'nlsValues' : {0:'Heat', 1:'Cool' , 2:'Auto' }
                                                    }
                                                }
                                        ,'mExcutiveSeason':{
                                             'GETstr': '/api/hc/executiveSeason/'
                                            ,'PUTstr': None
                                            ,'Active': None 
                                            ,'ISYeditor':{
                                                     'ISYuom':25
                                                    ,'ISYmin':None
                                                    ,'ISYmax':None
                                                    ,'ISYsubset':'0-2'
                                                    ,'ISYstep':None
                                                    ,'ISYprec':None }
                                            , 'ISYnls': {    
                                                     'nlsTEXT' : 'Executive Season' 
                                                    ,'nlsValues' : {0:'Heating', 1:'Cooling' }
                                                    }          
                                                }
                                        ,'mAdaptiveComfort' :{
                                             'GETstr': '/api/hc/adaptiveComfort/'
                                            ,'PUTstr': '/api/hc/adaptiveComfort/'
                                            ,'Active': None 
                                            ,'ISYeditor':{
                                                     'ISYuom':25
                                                    ,'ISYmin':None
                                                    ,'ISYmax':None
                                                    ,'ISYsubset':'0-1'
                                                    ,'ISYstep':None
                                                    ,'ISYprec':None }
                                            , 'ISYnls': {    
                                                     'nlsTEXT' : 'Adaptive Comfort' 
                                                    ,'nlsValues' : {0:'Off', 1:'On' }
                                                    }
                                                }
                                        }   
                                        ,'data' : {}
                                        ,'SensorCapability' : {}
                                        ,'GETkeysList' : {}
                                        ,'PUTkeysList' : {}
                                    },
                        self.fcID :{'ISYnode':{   'nlsICON' :'GenericCtl'
                                                        ,'sends'   : []
                                                        ,'accepts' : {  'SET_STATUS': { 'ISYtext' :'Set System Status'
                                                                                       ,'ISYeditor' :'mStatus' }
                                                                        ,'UPDATE' : { 'ISYtext'   :'Update System'
                                                                                     ,'ISYeditor' : None }
                                                                        ,'SET_COOLING_SPEED' : { 'ISYtext' :'Colling Speed'
                                                                                                ,'ISYeditor' : 'mCoolingSpeed' } 
                                                                        ,'SET_HEATING_SPEED' : { 'ISYtext' :'Heating Speed'
                                                                                                ,'ISYeditor' : 'mHeatingSpeed'} }
                                                }
                                    ,'KeyInfo' : {
                                         'mName':{
                                             'GETstr': '/api/fcu/name/'
                                            ,'PUTstr': '/api/fcu/name/'
                                            ,'Active': None 
                                            ,'ISYeditor':{
                                                     'ISYuom':None
                                                    ,'ISYmin':None
                                                    ,'ISYmax':None
                                                    ,'ISYsubset':None
                                                    ,'ISYstep':None
                                                    ,'ISYprec':None }
                                            , 'ISYnls': {    
                                                     'nlsTEXT' : 'Fan Coil Name' 
                                                    ,'nlsValues' : None }
                                                }
                                        ,'mStatus':{
                                             'GETstr':'/api/fcu/status/'
                                            ,'PUTstr':'/api/fcu/status/'                    
                                            ,'Active': None 
                                            ,'ISYeditor':{   
                                                     'ISYuom': 25
                                                    ,'ISYmin':None
                                                    ,'ISYmax':None
                                                    ,'ISYsubset': '0-1'
                                                    ,'ISYstep':None
                                                    ,'ISYprec':None }
                                            ,'ISYnls': {    
                                                     'nlsTEXT' : 'Fan Coil Status'
                                                    ,'nlsValues' : {0:'Off', 1:'On' }
                                                        }
                                                    }                            
                                        ,'mCoolingSpeed' :{
                                             'GETstr':'/api/fcu/coolingSpeed/'
                                            ,'PUTstr':'/api/fcu/coolingSpeed/'                   
                                            ,'Active':'/api/fcu/coolingSpeed/'  
                                            ,'ISYeditor':{   
                                                     'ISYuom': 25
                                                    ,'ISYmin':0
                                                    ,'ISYmax':100
                                                    ,'ISYsubset': None
                                                    ,'ISYstep':1
                                                    ,'ISYprec':0}
                                            ,'ISYnls': {    
                                                     'nlsTEXT' : 'Fan Coil Cooling Speed'
                                                    ,'nlsValues' : None
                                                        }
                                                    }  
                                        ,'mHeatingSpeed' :{
                                             'GETstr':'/api/fcu/heatingSpeed/'
                                            ,'PUTstr':'/api/fcu/heatingSpeed/'                   
                                            ,'Active':'/api/fcu/heatingSpeed/'
                                            ,'ISYeditor':{   
                                                     'ISYuom': 25
                                                    ,'ISYmin':0
                                                    ,'ISYmax':100
                                                    ,'ISYsubset': None
                                                    ,'ISYstep':1
                                                    ,'ISYprec':0}
                                            ,'ISYnls': {    
                                                     'nlsTEXT' : 'Fan Coil Heating Speed'
                                                    ,'nlsValues' : None
                                                        }
                                                    }      
                                        ,'mType':{
                                             'GETstr':'/api/fcu/type/'
                                            ,'PUTstr': None            
                                            ,'Active': None 
                                            ,'ISYeditor':{   
                                                     'ISYuom': 25
                                                    ,'ISYmin':None
                                                    ,'ISYmax':None
                                                    ,'ISYsubset': '0-3'
                                                    ,'ISYstep':None
                                                    ,'ISYprec':None }
                                            ,'ISYnls': {    
                                                     'nlsTEXT' : 'Fan Coil Type'
                                                    ,'nlsValues' : {0:'Radiator', 1:'Digital On/Off', 
                                                                    2:'Digital variable', 3:'Analog'}       
                                                    }
                                                }                                                                                             
                                        ,'mAlarmOn':{ 
                                             'GETstr': '/api/fcu/alarmOn/'
                                            ,'PUTstr': None
                                            ,'Active': '/api/fcu/alarmOn/'
                                            ,'ISYeditor':{   
                                                     'ISYuom':25
                                                    ,'ISYmin':None
                                                    ,'ISYmax':None
                                                    ,'ISYsubset':'0-1'
                                                    ,'ISYstep':None
                                                    ,'ISYprec':None }
                                            , 'ISYnls': {    
                                                     'nlsTEXT' : 'Alarm Status' 
                                                    ,'nlsValues' : { 0:'Off', 1:'On' }
                                                        }  
                                                    }
                                            }                                       
                                        ,'data' : {}
                                        ,'SensorCapability' : {}
                                        ,'GETkeysList' : {}
                                        ,'PUTkeysList' : {}  
                        },
                        self.atuID: {'ISYnode':{   'nlsICON' :'GenericCtl'
                                                        ,'sends'   : []
                                                        ,'accepts' : {  'SET_STATUS': { 'ISYtext' :'System Status'
                                                                                         ,'ISYeditor' : 'mStatus' }
                                                                        ,'UPDATE': { 'ISYtext'   :'Update System'
                                                                                         ,'ISYeditor'    : None }
                                                                        ,'SET_HRVON' : { 'ISYtext' :'Heat Revopvery'
                                                                                         ,'ISYeditor'    : 'mHRVOn' }
                                                                        ,'SET_FLOWLEVEL' :{ 'ISYtext' :'Set Flow Level'
                                                                                         ,'ISYeditor'    : 'mFlowLevel' }
                                                                        ,'SET_HUMON' : { 'ISYtext' :'Humidity Integration'
                                                                                         ,'ISYeditor'    : 'mHUMOn' }
                                                                        ,'SET_NTDON' : { 'ISYtext' :'NTD Integration'
                                                                                         ,'ISYeditor'    : 'mNTDOn' }
                                                                        ,'SET_INTON' : { 'ISYtext' :'Convective Integration'
                                                                                         ,'ISYeditor' : 'mINTOn' }     
                                                                        ,'SET_HUM_SP_RH' : { 'ISYtext'   :'Hum Setpoint RH'
                                                                                         ,'ISYeditor' : 'mHumSetpointRH'}     
                                                                        ,'SET_HUM_SP_DP' : { 'ISYtext'   :'Hum Setpoint DP'
                                                                                         ,'ISYeditor' : 'mHumSetpointDP' } 
                                                                        ,'SET_DEHUM_SP_RH' : { 'ISYtext' :'DehumSetpointRH'
                                                                                         ,'ISYeditor' : 'mDehumSetpointRH'}
                                                                        ,'SET_DEHUM_SP_DP' : { 'ISYtext' :'Dehum Setpoint DP'
                                                                                         ,'ISYeditor' : 'mDehumSetpointDP' }    
                                                                        ,'SET_CURR_SP_RH' : { 'ISYtext'  :'Current Setpoint RH'
                                                                                         ,'ISYeditor' : 'mCurrentSetpointRH' }     
                                                                        ,'SET_CURR_SP_DP' :{ 'ISYtext'   :'Current Setpoint DP'
                                                                                         ,'ISYeditor' : 'mCurrentSetpointDP' }
                                                                        }}
                                    ,'KeyInfo' : {  
                                        'mName':{
                                             'GETstr': '/api/atu/name/'
                                            ,'PUTstr': '/api/atu/name/'
                                            ,'Active': None 
                                            ,'ISYeditor':{
                                                     'ISYuom':None
                                                    ,'ISYmin':None
                                                    ,'ISYmax':None
                                                    ,'ISYsubset':None
                                                    ,'ISYstep':None
                                                    ,'ISYprec':None }
                                            , 'ISYnls': {    
                                                     'nlsTEXT' : 'ATU Name' 
                                                    ,'nlsValues' : None }
                                                }
                                        ,'mFlowLevel':{                                            
                                             'GETstr': '/api/atu/flowLevel/'
                                            ,'PUTstr': '/api/atu/flowLevel/'
                                            ,'Active': '/api/atu/flowLevel/' 
                                            ,'ISYeditor':{
                                                     'ISYuom':25
                                                    ,'ISYmin':0
                                                    ,'ISYmax':100
                                                    ,'ISYsubset':None
                                                    ,'ISYstep':None
                                                    ,'ISYprec':None }
                                            , 'ISYnls': {    
                                                     'nlsTEXT' : 'ATU Flow Level' 
                                                    ,'nlsValues' : None }
                                                   }
                                        ,'mStatus' : {                                             
                                             'GETstr':'/api/atu/status/'
                                            ,'PUTstr':'/api/atu/status/'                
                                            ,'Active': None 
                                            ,'ISYeditor':{   
                                                     'ISYuom': 25
                                                    ,'ISYmin':None
                                                    ,'ISYmax':None
                                                    ,'ISYsubset': '0-1'
                                                    ,'ISYstep':None
                                                    ,'ISYprec':None }
                                            ,'ISYnls': {    
                                                     'nlsTEXT' : 'ATU Status'
                                                    ,'nlsValues' : {0:'Off', 1:'On' }
                                                       }
                                                    }
                                        ,'mHRVOn' :{                                             
                                             'GETstr': '/api/atu/hrvOn/'
                                            ,'PUTstr': '/api/atu/hrvOn/'
                                            ,'Active': None 
                                            ,'ISYeditor':{ 
                                                     'ISYuom': 25
                                                    ,'ISYmin':None
                                                    ,'ISYmax':None
                                                    ,'ISYsubset': '0-1'
                                                    ,'ISYstep':None
                                                    ,'ISYprec':None }
                                            ,'ISYnls': {   
                                                     'nlsTEXT' : 'Heat Recovery Status'
                                                    ,'nlsValues' : {0:'Off', 1:'On' }
                                                        }
                                                   }
                                        ,'mHUMOn':{                                             
                                             'GETstr': '/api/atu/humOn/'
                                            ,'PUTstr': '/api/atu/humOn/'
                                            ,'Active': None 
                                            ,'ISYeditor':{
                                                     'ISYuom': 25
                                                    ,'ISYmin':None
                                                    ,'ISYmax':None
                                                    ,'ISYsubset': '0-1'
                                                    ,'ISYstep':None
                                                    ,'ISYprec':None }
                                            , 'ISYnls': {    
                                                     'nlsTEXT' : 'Humidufucation' 
                                                     ,'nlsValues' : {0:'Off', 1:'On' }
                                                        }
                                                   }
                                        ,'mNTDOn':{                                             
                                             'GETstr': '/api/atu/ntdOn/'
                                            ,'PUTstr': '/api/atu/ntdOn/'
                                            ,'Active': None 
                                            ,'ISYeditor':{
                                                     'ISYuom': 25
                                                    ,'ISYmin':None
                                                    ,'ISYmax':None
                                                    ,'ISYsubset':'0-1'
                                                    ,'ISYstep':None
                                                    ,'ISYprec':None }
                                            , 'ISYnls': {    
                                                      'nlsTEXT' : 'NTD Dehumidification??' 
                                                     ,'nlsValues' : {0:'Off', 1:'On' }
                                                        }
                                                   }
                                        ,'mINTOn':{                                             
                                             'GETstr': '/api/atu/intOn/'
                                            ,'PUTstr': '/api/atu/intOn/'
                                            ,'Active': None 
                                            ,'ISYeditor':{
                                                     'ISYuom': 25 
                                                    ,'ISYmin':None
                                                    ,'ISYmax':None
                                                    ,'ISYsubset':'0-1'
                                                    ,'ISYstep':None
                                                    ,'ISYprec':None }
                                            , 'ISYnls': {    
                                                     'nlsTEXT' : 'Convective Integration' 
                                                     ,'nlsValues' : {0:'Off', 1:'On' }
                                                        }
                                                   }
                                        ,'mDehumudityStatus':{                                             
                                             'GETstr': '/api/atu/dehumidificationStatus/'
                                            ,'PUTstr': None
                                            ,'Active': '/api/atu/dehumidificationStatus/' 
                                            ,'ISYeditor':{
                                                     'ISYuom':25
                                                    ,'ISYmin':None
                                                    ,'ISYmax':None
                                                    ,'ISYsubset':'0-1'
                                                    ,'ISYstep':None
                                                    ,'ISYprec':None }
                                            , 'ISYnls': {    
                                                      'nlsTEXT' : 'Dehumidification Status' 
                                                     ,'nlsValues' : {0:'Off', 1:'On' }
                                                        }
                                                   }
                                        ,'mHumidityStatus':{                                             
                                             'GETstr': '/api/atu/humidificationStatus/'
                                            ,'PUTstr': None
                                            ,'Active': '/api/atu/humidificationStatus/' 
                                            ,'ISYeditor':{
                                                     'ISYuom':25
                                                    ,'ISYmin':None
                                                    ,'ISYmax':None
                                                    ,'ISYsubset':'0-1'
                                                    ,'ISYstep':None
                                                    ,'ISYprec':None }
                                            , 'ISYnls': {    
                                                      'nlsTEXT' : 'Humidification Status' 
                                                     ,'nlsValues' : {0:'Off', 1:'On' }
                                                        }
                                                   }
                                        ,'mHRVstatus':{                                             
                                             'GETstr': '/api/atu/hrvStatus/'
                                            ,'PUTstr': None
                                            ,'Active': '/api/atu/hrvStatus/'
                                            ,'ISYeditor':{
                                                     'ISYuom':25
                                                    ,'ISYmin':None
                                                    ,'ISYmax':None
                                                    ,'ISYsubset':'0-1'
                                                    ,'ISYstep':None
                                                    ,'ISYprec':None }
                                            , 'ISYnls': {    
                                                      'nlsTEXT' : 'HRV Status' 
                                                     ,'nlsValues' : {0:'Off', 1:'On' }
                                                        }
                                                   }
                                        ,'mIntegrationStatus':{                                             
                                             'GETstr': '/api/atu/integrationStatus/'
                                            ,'PUTstr': None
                                            ,'Active': '/api/atu/integrationStatus/'
                                            ,'ISYeditor':{
                                                     'ISYuom':25
                                                    ,'ISYmin':None
                                                    ,'ISYmax':None
                                                    ,'ISYsubset':'0-1'
                                                    ,'ISYstep':None
                                                    ,'ISYprec':None }
                                            , 'ISYnls': {    
                                                     'nlsTEXT' : 'Integration Status'
                                                    ,'nlsValues' : {0:'Off', 1:'On' }  
                                                        }
                                                   }
                                        ,'mAlarmOn':{                                             
                                             'GETstr': '/api/atu/alarmOn/'
                                            ,'PUTstr': None
                                            ,'Active': '/api/atu/alarmOn/' 
                                            ,'ISYeditor':{
                                                     'ISYuom':25
                                                    ,'ISYmin':None
                                                    ,'ISYmax':None
                                                    ,'ISYsubset':'0-1'
                                                    ,'ISYstep':None
                                                    ,'ISYprec':None }
                                            , 'ISYnls': {    
                                                     'nlsTEXT' : 'Alarm Status' 
                                                    ,'nlsValues' : {0:'Off', 1:'On' }  
                                                        }
                                                   }
                                        ,'mAirTemp':{                                            
                                             'GETstr': '/api/atu/airTemperature/'
                                            ,'PUTstr': None
                                            ,'Active': '/api/atu/airTemperature/'
                                            ,'ISYeditor':{
                                                     'ISYuom':17
                                                    ,'ISYmin':40
                                                    ,'ISYmax':120
                                                    ,'ISYsubset':None
                                                    ,'ISYstep':1
                                                    ,'ISYprec':0}
                                            , 'ISYnls': {    
                                                     'nlsTEXT' : 'Air Temperature (flow)' 
                                                     ,'nlsValues' : None 
                                                        }
                                                   }
                                        ,'mHumSetpointRH':{                                             
                                             'GETstr': '/api/atu/humidSetpointRH/'
                                            ,'PUTstr': '/api/atu/humidSetpointRH/'
                                            ,'Active': None 
                                            ,'ISYeditor':{
                                                     'ISYuom':51
                                                    ,'ISYmin':0
                                                    ,'ISYmax':100
                                                    ,'ISYsubset':None
                                                    ,'ISYstep':1
                                                    ,'ISYprec':1 }
                                            , 'ISYnls': {    
                                                     'nlsTEXT' : 'Humidity Setpoint RH' 
                                                     ,'nlsValues' : None 
                                                        }
                                                   }
                                        ,'mHumSetpointDP':{                                             
                                             'GETstr': '/api/atu/humidSetpointDP/'
                                            ,'PUTstr': '/api/atu/humidSetpointDP/'
                                            ,'Active': None 
                                            ,'ISYeditor':{
                                                     'ISYuom':51
                                                    ,'ISYmin':0
                                                    ,'ISYmax':100
                                                    ,'ISYsubset':None
                                                    ,'ISYstep':1
                                                    ,'ISYprec':1  }
                                            , 'ISYnls': {    
                                                     'nlsTEXT' : 'Humidity Setpoint RH' 
                                                     ,'nlsValues' : None 
                                                        }
                                                   }
                                        ,'mDehumSetpointRH':{                                             
                                             'GETstr': '/api/atu/dehumSetpointRH/'
                                            ,'PUTstr': '/api/atu/dehumSetpointRH/'
                                            ,'Active': None 
                                            ,'ISYeditor':{
                                                     'ISYuom':51
                                                    ,'ISYmin':0
                                                    ,'ISYmax':100
                                                    ,'ISYsubset':None
                                                    ,'ISYstep':1
                                                    ,'ISYprec':1  }
                                            , 'ISYnls': {    
                                                     'nlsTEXT' : 'Deumidity Setpoint RH' 
                                                     ,'nlsValues' : None 
                                                        }
                                                   }
                                        ,'mDehumSetpointDP':{    
                                             'GETstr': '/api/atu/dehumidSetpointDP/'
                                            ,'PUTstr': '/api/atu/dehumidSetpointDP/'
                                            ,'Active': None 
                                            ,'ISYeditor':{
                                                     'ISYuom':51
                                                    ,'ISYmin':0
                                                    ,'ISYmax':100
                                                    ,'ISYsubset':None
                                                    ,'ISYstep':1
                                                    ,'ISYprec':1  }
                                            , 'ISYnls': {    
                                                     'nlsTEXT' : 'Dehumidity Setpoint DP' 
                                                     ,'nlsValues' : None 
                                                        }
                                                   }
                                        ,'mCurrentSetpointRH':{                                             
                                             'GETstr': '/api/atu/currentSetpointRH/'
                                            ,'PUTstr': '/api/atu/currentSetpointRH/'
                                            ,'Active': None 
                                            ,'ISYeditor':{
                                                     'ISYuom':51
                                                    ,'ISYmin':0
                                                    ,'ISYmax':100
                                                    ,'ISYsubset':None
                                                    ,'ISYstep':1
                                                    ,'ISYprec':1  }
                                            , 'ISYnls': {    
                                                     'nlsTEXT' : 'Current Setpoint RH' 
                                                     ,'nlsValues' : None 
                                                        }
                                                   }
                                        ,'mCurrentSetpointDP':{                                             
                                             'GETstr': '/api/atu/currentSetpointDP/'
                                            ,'PUTstr': '/api/atu/currentSetpointDP/'
                                            ,'Active': None 
                                            ,'ISYeditor':{
                                                     'ISYuom':51
                                                    ,'ISYmin':0
                                                    ,'ISYmax':100
                                                    ,'ISYsubset':None
                                                    ,'ISYstep':1
                                                    ,'ISYprec':1  }
                                            , 'ISYnls': {    
                                                     'nlsTEXT' : 'Current Setpoint RH' 
                                                    ,'nlsValues' : None 
                                                        }
                                                   }
                                        ,'mCapability': {
                                             'GETstr': '/api/atu/capability/'
                                            ,'PUTstr': None
                                            ,'Active': None 
                                            ,'ISYeditor':{   
                                                     'ISYuom':None
                                                    ,'ISYmin':None
                                                    ,'ISYmax':None
                                                    ,'ISYsubset':None
                                                    ,'ISYstep':None
                                                    ,'ISYprec':None }
                                            , 'ISYnls': {    
                                                     'nlsTEXT' : None
                                                    ,'nlsValues' : None 
                                                        }
                                                    }
                                    }
                                        ,'data' : {}
                                        ,'SensorCapability' : {}
                                        ,'GETkeysList' : {}
                                        ,'PUTkeysList' : {}     
                        },
                         self.energySaveID:{'ISYnode':{   'nlsICON' :'GenericCtl'
                                                        ,'sends'   : []
                                                        ,'accepts' : {  'SET_STATUS': { 'ISYtext' :'Update System'
                                                                                       ,'ISYeditor' : None }
                                                                        ,'UPDATE'        : { 'ISYtext'   :'Update System'
                                                                                         ,'ISYeditor' : None }}
                                                                        }
                                    ,'KeyInfo' : {  
                                        'mName':{
                                             'GETstr': '/api/energySource/name/'
                                            ,'PUTstr': '/api/energySource/name/'
                                            ,'Active': None 
                                            ,'ISYeditor':{
                                                     'ISYuom':None
                                                    ,'ISYmin':None
                                                    ,'ISYmax':None
                                                    ,'ISYsubset':None
                                                    ,'ISYstep':None
                                                    ,'ISYprec':None }
                                            , 'ISYnls': {    
                                                     'nlsTEXT' : 'Energy Source Name' 
                                                    ,'nlsValues' : None }
                                                }
                                        ,'mStatus' : {                                             
                                             'GETstr':'/api/energySource/status/'
                                            ,'PUTstr': None                  
                                            ,'Active': None 
                                            ,'ISYeditor':{   
                                                     'ISYuom': 25
                                                    ,'ISYmin':None
                                                    ,'ISYmax':None
                                                    ,'ISYsubset': '0-1'
                                                    ,'ISYstep':None
                                                    ,'ISYprec':None }
                                            ,'ISYnls': {    
                                                     'nlsTEXT' : 'ATU Status'
                                                    ,'nlsValues' : {0:'Off', 1:'On' }
                                                       }
                                                    }
                                        ,'mDHWstatus' : {                                             
                                             'GETstr':'/api/energySource/dhwStatus/'
                                            ,'PUTstr': None                  
                                            ,'Active': None 
                                            ,'ISYeditor':{   
                                                     'ISYuom': 25
                                                    ,'ISYmin':None
                                                    ,'ISYmax':None
                                                    ,'ISYsubset': '0-1'
                                                    ,'ISYstep':None
                                                    ,'ISYprec':None }
                                            ,'ISYnls': {    
                                                     'nlsTEXT' : 'ATU Status'
                                                    ,'nlsValues' : {0:'Off', 1:'On' }
                                                       }
                                                    }
                                        ,'mType' : {                                             
                                             'GETstr':'/api/energySource/type/'
                                            ,'PUTstr': None                  
                                            ,'Active': None 
                                            ,'ISYeditor':{   
                                                     'ISYuom': 25
                                                    ,'ISYmin':None
                                                    ,'ISYmax':None
                                                    ,'ISYsubset': '0-3'
                                                    ,'ISYstep':None
                                                    ,'ISYprec':None }
                                            ,'ISYnls': {    
                                                     'nlsTEXT' : 'ATU Status'
                                                    ,'nlsValues' : {0:'Broiler', 1:' H.P. Cooling Only'
                                                                    , 2: 'H.P. Heating Only', 3:'H.P. Heating and Cooling' }
                                                       }
                                                    }
                                        ,'mAlarmOn' : {                                             
                                             'GETstr':'/api/energySource/alarmOn/'
                                            ,'PUTstr': None                  
                                            ,'Active': None 
                                            ,'ISYeditor':{   
                                                     'ISYuom': 25
                                                    ,'ISYmin':None
                                                    ,'ISYmax':None
                                                    ,'ISYsubset': '0-1'
                                                    ,'ISYstep':None
                                                    ,'ISYprec':None }
                                            ,'ISYnls': {    
                                                     'nlsTEXT' : 'ATU Status'
                                                    ,'nlsValues' : {0:'Off', 1:'On' }
                                                       }
                                                    }  
                                        }                                                                                                      
                                        ,'data' : {}
                                        ,'SensorCapability' : {}
                                        ,'GETkeysList' : {}
                                        ,'PUTkeysList' : {}
                        }, 
                        self.bufferTankID: {'ISYnode':{   'nlsICON' :'GenericCtl'
                                                        ,'sends'   : []
                                                        ,'accepts' : {  'SET_STATUS'    : { 'ISYtext' :'Update System'
                                                                                         ,'ISYeditor' : None }
                                                                       ,'UPDATE'        : { 'ISYtext'   :'Update System'
                                                                                         ,'ISYeditor' : None }
                                                                       ,'SET_MODE'      : { 'ISYtext' :'Update System'
                                                                                         ,'ISYeditor' : None }
                                                                       ,'SET_TEMPMODE'  :{ 'ISYtext' :'Update System'
                                                                                         ,'ISYeditor' : None }}
                                                                        }
                                    ,'KeyInfo' : {  
                                        'mName':{
                                             'GETstr': '/api/bufferTank/name/'
                                            ,'PUTstr': '/api/bufferTank/name/'
                                            ,'Active': None 
                                            ,'ISYeditor':{
                                                     'ISYuom':None
                                                    ,'ISYmin':None
                                                    ,'ISYmax':None
                                                    ,'ISYsubset':None
                                                    ,'ISYstep':None
                                                    ,'ISYprec':None }
                                            , 'ISYnls': {    
                                                     'nlsTEXT' : 'Buffer Tank Name' 
                                                    ,'nlsValues' : None }
                                                }
                                        ,'mStatus' : {                                             
                                             'GETstr':'/api/bufferTank/status/'
                                            ,'PUTstr':'/api/bufferTank/status/'                
                                            ,'Active': None 
                                            ,'ISYeditor':{   
                                                     'ISYuom': 25
                                                    ,'ISYmin':None
                                                    ,'ISYmax':None
                                                    ,'ISYsubset': '0-1'
                                                    ,'ISYstep':None
                                                    ,'ISYprec':None }
                                            ,'ISYnls': {    
                                                     'nlsTEXT' : 'Buffer Tank Status'
                                                    ,'nlsValues' : {0:'Off', 1:'On' }
                                                       }
                                                    }
                                         ,'mMode' : {                                             
                                             'GETstr':'/api/bufferTank/mode/'
                                            ,'PUTstr':'/api/bufferTank/mode/'                
                                            ,'Active': None 
                                            ,'ISYeditor':{   
                                                     'ISYuom': 25
                                                    ,'ISYmin':None
                                                    ,'ISYmax':None
                                                    ,'ISYsubset': '0-1'
                                                    ,'ISYstep':None
                                                    ,'ISYprec':None }
                                            ,'ISYnls': {    
                                                     'nlsTEXT' : 'Buffer Tank Mode'
                                                    ,'nlsValues' : {0:'Manual', 1:'Automatic' }
                                                       }
                                                    }                           
                                          ,'mTempMode' : {                                             
                                             'GETstr':'/api/bufferTank/tempMode/'
                                            ,'PUTstr':'/api/bufferTank/tempMode/'                
                                            ,'Active': None 
                                            ,'ISYeditor':{   
                                                     'ISYuom': 25
                                                    ,'ISYmin':None
                                                    ,'ISYmax':None
                                                    ,'ISYsubset': '0-2'
                                                    ,'ISYstep':None
                                                    ,'ISYprec':None }
                                            ,'ISYnls': {    
                                                     'nlsTEXT' : 'Buffer Tank Tempperature Mode'
                                                    ,'nlsValues' : {0:'Fixed Temp', 1:'Follow Loads', 2:'Outdoor Temp Compensation' }
                                                       }
                                                    }                                               
                                         ,'mAlarmOn' : {                                             
                                             'GETstr':'/api/bufferTank/alarmOn/'
                                            ,'PUTstr':None              
                                            ,'Active':None
                                            ,'ISYeditor':{   
                                                     'ISYuom': 25
                                                    ,'ISYmin':None
                                                    ,'ISYmax':None
                                                    ,'ISYsubset': '0-1'
                                                    ,'ISYstep':None
                                                    ,'ISYprec':None }
                                            ,'ISYnls': {    
                                                     'nlsTEXT' : 'Buffer Tank Alarm'
                                                    ,'nlsValues' : {0:'Off', 1:'On' }
                                                       }
                                                    }   
                                        }                        
                                        ,'data' : {}
                                        ,'SensorCapability' : {}
                                        ,'GETkeysList' : {}
                                        ,'PUTkeysList' : {}
                        },
                        self.dhwID: { 'ISYnode':{   'nlsICON' :'GenericCtl'
                                                        ,'sends'   : []
                                                        ,'accepts' : {  'SET_STATUS': { 'ISYtext' :'Update System'
                                                                                         ,'ISYeditor' : None }
                                                                        ,'UPDATE'        : { 'ISYtext'   :'Update System'
                                                                                         ,'ISYeditor' : None }
                                                                        ,'SET_TARGETTEMP': { 'ISYtext' :'Update System'
                                                                                         ,'ISYeditor' : None }}
                                                            }
                                    ,'KeyInfo' : {  
                                        'mName':{
                                             'GETstr': '/api/dhw/name/'
                                            ,'PUTstr': '/api/dhw/name/'
                                            ,'Active': None 
                                            ,'ISYeditor':{
                                                     'ISYuom':None
                                                    ,'ISYmin':None
                                                    ,'ISYmax':None
                                                    ,'ISYsubset':None
                                                    ,'ISYstep':None
                                                    ,'ISYprec':None }
                                            , 'ISYnls': {    
                                                     'nlsTEXT' : 'Domestic Hot Water Name' 
                                                    ,'nlsValues' : None }
                                                }
                                        ,'mStatus' : {                                             
                                             'GETstr':'/api/dhw/status/'
                                            ,'PUTstr':'/api/dhw/status/'              
                                            ,'Active': None 
                                            ,'ISYeditor':{   
                                                     'ISYuom': 25
                                                    ,'ISYmin':None
                                                    ,'ISYmax':None
                                                    ,'ISYsubset': '0-1'
                                                    ,'ISYstep':None
                                                    ,'ISYprec':None }
                                            ,'ISYnls': {    
                                                     'nlsTEXT' : 'Domestic Hot Water Status'
                                                    ,'nlsValues' : {0:'Off', 1:'On' }
                                                       }
                                                    }
                                        ,'mTemp' : {                                             
                                             'GETstr':'/api/dhw/temperature/'
                                            ,'PUTstr':None             
                                            ,'Active': None 
                                            ,'ISYeditor':{   
                                                     'ISYuom':17
                                                    ,'ISYmin':-40
                                                    ,'ISYmax':150
                                                    ,'ISYsubset':None
                                                    ,'ISYstep':1
                                                    ,'ISYprec':1 }
                                            ,'ISYnls': {    
                                                     'nlsTEXT' : 'Domestic Hot Water Temp'
                                                    ,'nlsValues' : None
                                                       }
                                                    }                            
                                        ,'mTargetTemp' : {                                             
                                             'GETstr':'/api/dhw/targetTemperature/'
                                            ,'PUTstr':'/api/dhw/targetTemperature/'              
                                            ,'Active': None 
                                            ,'ISYeditor':{   
                                                     'ISYuom':17
                                                    ,'ISYmin':-40
                                                    ,'ISYmax':150
                                                    ,'ISYsubset':None
                                                    ,'ISYstep':1
                                                    ,'ISYprec':1 }
                                            ,'ISYnls': {    
                                                     'nlsTEXT' : 'Domestic Hot Water Target Temp'
                                                    ,'nlsValues' : None
                                                       }
                                                    } 
                                        }                              
                                        ,'data' : {}
                                        ,'SensorCapability' : {}
                                        ,'GETkeysList' : {}
                                        ,'PUTkeysList' : {}
                        }
                }
        
        
        #self.setupStruct = {'nodeDef': nodeNbr: { 'nodeDef':{}
        ##                                    ,'sts':{}
        #                                  ,'cmds':{
        #                                            'sends':{}
        #                                            ,'accepts':{}
        #                                            } 
        #                                    }
        #                        }
        #            ,'editors':{id:Name, range:{}}
        #            ,'nls':{}
        #                }
        
        self.nodeCount = 0
        self.setupFile = { 'nodeDef':{}
                            ,'editors':{}
                            ,'nls':{}}



        #self.APIKeyVal = '9bf711fc-54e2-4387-9c7f-991bbb02ab3a'
        #self.IP = '192.168.2.65'    
        #self.mIPaddress = '192.168.2.64'
        #self.mAPIkey =  '9bf711fc-54e2-4387-9c7f-991bbb02ab3a'
        
        self.APIKey = 'apikey'
        self.APIStr = self.APIKey + '=' + mAPIkey

        self.IP ='http://'+ mIPaddress

        self.RESPONSE_OK = '<Response [200]>'
        self.RESPONSE_NO_SUPPORT = '<Response [400]>'
        self.RESPONSE_NO_RESPONSE = '<Response [404]>'
        self.NaNlist= [-32768 , -3276.8 ]
        


        #Dummy check to see if there is connection to Messana system)
        if not(self.checkMessanaConnection()):
            print('Error Connecting to MessanaSystem')
        else:  
            
            self. setMessanaCredentials (mIPaddress, mAPIkey) 
            # Need SystemCapability function               
            self.getSystemCapability()
            self.updateSystemData('all')
            print(self.systemID + 'added')
 
            self.addSystemDefStruct(self.systemID)

            for zoneNbr in range(0,self.mSystem[ self.systemID]['data']['mZoneCount']):
                self.getZoneCapability(zoneNbr)
                self.updateZoneData('all', zoneNbr)
                zoneName = self.zoneID+str(zoneNbr)
                self.addNodeDefStruct(zoneNbr, self.zoneID, zoneName )
        
            for macrozoneNbr in range(0,self.mSystem[ self.systemID]['data']['mMacrozoneCount']):
                self.getMacrozoneCapability(macrozoneNbr)
                self.updateMacrozoneData('all', macrozoneNbr)
                macrozoneName = self.macrozoneID+str(macrozoneNbr)
                self.addNodeDefStruct(macrozoneNbr, self.macrozoneID, macrozoneName )
            
            for atuNbr in range(0,self.mSystem[ self.systemID]['data']['mATUcount']):
                self.getAtuCapability(atuNbr)
                self.updateATUData(atuNbr)
                atuName = self.atuID+str(atuNbr)
                self.addNodeDefStruct(atuNbr, self.atuID, atuName )
    
            for dhwNbr in range(0,self.mSystem[ self.systemID]['data']['mDHWcount']):
                self.getDHWCapability(dhwNbr)
                self.updateDHWData(dhwNbr)
                dhwName = self.dhwID+str(dhwNbr)
                self.addNodeDefStruct(dhwNbr, self.dhwID, dhwName )

            for fcNbr in range(0,self.mSystem[ self.systemID]['data']['mFanCoilCount']):
                self.getFanCoilCapability(fcNbr)
                self.updateFanCoilData(fcNbr)
                fcName = self.fcID+str(fcNbr)
                self.addNodeDefStruct(fcNbr, self.fcID, fcName )
        
            for esNbr in range(0,self.mSystem[ self.systemID]['data']['mEnergySourceCount']):
                self.getEnergySourceCapability(esNbr)
                self.updateEnergySourceData(esNbr)
                esName =  self.energySaveID+str(esNbr)
                self.addNodeDefStruct(esNbr,  self.energySaveID, esName )   

            for hccoNbr in range(0,self.mSystem[ self.systemID]['data']['mhc_coCount']):
                self.getHC_COCapability(hccoNbr)
                self.updateHC_COData(hccoNbr)
                hccoName = self.HotColdcoID +str(hccoNbr)
                self.addNodeDefStruct(hccoNbr, self.HotColdcoID , hccoName )          
            
            for btNbr in range(0,self.mSystem[ self.systemID]['data']['mBufTankCount']):
                self.getBufferTankCapability(btNbr)
                self.updateBufferTankData(btNbr)
                btName = self.bufferTankID+str(btNbr)
                self.addNodeDefStruct(btNbr, self.bufferTankID, btName )     
            print ('Create Setup file')
            self.createSetupFiles('./profile/nodedef/nodedefs.xml','./profile/editor/editors.xml', './profile/nls/en_us.txt')
            
            self.ISYmap = self.createISYmapping()


    def createISYmapping(self):
        temp = {}
        for nodes in self.setupFile['nodeDef']:
            temp[nodes]= {}
            for mKeys in self.setupFile['nodeDef'][nodes]['sts']:
                for ISYkey in self.setupFile['nodeDef'][nodes]['sts'][mKeys]:
                    if ISYkey != 'ISYInfo':
                        temp[nodes][ISYkey] = {}
                        temp[nodes][ISYkey].update({'messana': mKeys})
                        temp[nodes][ISYkey].update({'editor': self.setupFile['nodeDef'][nodes]['sts'][mKeys][ISYkey]})
        print(temp) 
        return (temp)

    def setMessanaCredentials (self, mIPaddress, APIkey):
        self.mIPaddress = mIPaddress
        self.APIKeyVal = APIkey



    def getnodeISYdriverInfo(self, node, nodeNbr, mKey):
        info = {}
        if mKey in self.setupFile['nodeDef'][ self.systemID]['sts']:
            keys = list(self.setupFile['nodeDef'][ self.systemID]['sts'][mKey].keys())
            info['driver'] = keys[0]
            tempData =  self.GETSystemData(mKey)
            if tempData['statusOK']:
                val = tempData['data']        
                if val in  ['Celcius', 'Fahrenheit']:
                    if val == 'Celcius':
                        val = 0
                    else:  
                        val = 1 
                info['value'] = val
            else:
                info['value'] = ''
            editor = self.setupFile['nodeDef'][ self.systemID]['sts'][mKey][keys[0]]

            info['uom'] = self.setupFile['editors'][editor]['ISYuom']
        return(info)

    def checkValidNodeCommand(self, key, node, nodeNbr):
        exists = True
        mCmd = self.mSystem[node]['ISYnode']['accepts'][key]['ISYeditor']
        if mCmd != None:
            if not(mCmd in self.mSystem[node]['PUTkeysList'][nodeNbr]):
                exists = False
        return(exists)



    def addNodeDefStruct(self, nodeNbr, nodeName, nodeId):

        self.keyCount = 0
        nodeId.lower()
        print('addNodeDefStruct: ' + nodeName+ ' ' + str(nodeNbr) + ' '+nodeId)
        self.name = nodeName+str(nodeNbr)
        self.nlsKey = 'nls' + self.name
        self.nlsKey.lower()
        #editorName = nodeName+'_'+str(keyCount)
        self.setupFile['nodeDef'][self.name]={}
        self.setupFile['nodeDef'][self.name]['CodeId'] = nodeId
        self.setupFile['nodeDef'][self.name]['nlsId'] = self.nlsKey
        self.setupFile['nodeDef'][self.name]['nlsNAME']=self.mSystem[nodeName]['data'][nodeNbr]['mName']
        self.setupFile['nodeDef'][self.name]['nlsICON']=self.mSystem[nodeName]['ISYnode']['nlsICON']
        self.setupFile['nodeDef'][self.name]['sts']={}

        #for mKey in self.mSystem[nodeName]['data'][nodeNbr]: 
        for mKey in self.mSystem[nodeName]['GETkeysList'][nodeNbr]:             
            #make check if system has unit installed
            if self.mSystem[nodeName]['KeyInfo'][mKey]['ISYeditor']['ISYuom']:
                self.keyCount = self.keyCount + 1
                editorName = nodeName.upper()+str(nodeNbr)+'_'+str(self.keyCount)
                nlsName = editorName
                ISYvar = 'GV'+str(self.keyCount)
                self.setupFile['nodeDef'][self.name]['sts'][mKey]={ISYvar:editorName}
                self.setupFile['editors'][editorName]={}
                #self.setupFile['nls'][editorName][ISYparam]
                for ISYparam in self.mSystem[nodeName]['KeyInfo'][mKey]['ISYeditor']:
                    if self.mSystem[nodeName]['KeyInfo'][mKey]['ISYeditor'][ISYparam]!= None:
                        self.setupFile['editors'][editorName][ISYparam]=self.mSystem[nodeName]['KeyInfo'][mKey]['ISYeditor'][ISYparam]

                if self.mSystem[nodeName]['KeyInfo'][mKey]['ISYnls']:
                    self.setupFile['nls'][nlsName]={}
                for ISYnls in self.mSystem[nodeName]['KeyInfo'][mKey]['ISYnls']:
                    #print( mKey + ' ' + ISYnls)
                    if  self.mSystem[nodeName]['KeyInfo'][mKey]['ISYnls'][ISYnls]:      
                        self.setupFile['nls'][nlsName][ISYnls] = self.mSystem[nodeName]['KeyInfo'][mKey]['ISYnls'][ISYnls]
                        if ISYnls == 'nlsValues':
                            self.setupFile['editors'][editorName]['nlsKey'] = nlsName 

        self.setupFile['nodeDef'][self.name]['cmds']= {}
        if 'accepts' in self.mSystem[nodeName]['ISYnode']:
            self.setupFile['nodeDef'][self.name]['cmds']['accepts']={}
            for key in  self.mSystem[nodeName]['ISYnode']['accepts']:
                if self.checkValidNodeCommand(key, nodeName, nodeNbr ):
                    if self.mSystem[nodeName]['ISYnode']['accepts'][key]['ISYeditor'] in self.setupFile['nodeDef'][self.name]['sts']:
                        self.setupFile['nodeDef'][self.name]['cmds']['accepts'][key]= self.setupFile['nodeDef'][self.name]['sts'][self.mSystem[nodeName]['ISYnode']['accepts'][key]['ISYeditor']]
                        self.setupFile['nodeDef'][self.name]['cmds']['accepts'][key]['ISYInfo']=self.mSystem[nodeName]['ISYnode']['accepts'][key]
                    else:
                        self.setupFile['nodeDef'][self.name]['cmds']['accepts'][key]={}
                        self.setupFile['nodeDef'][self.name]['cmds']['accepts'][key]['ISYInfo']= self.mSystem[nodeName]['ISYnode']['accepts'][key]
                else:
                    print('Removed "accepts" for : ' + key + ' not supported')
                    
        if 'sends' in self.mSystem[nodeName]['ISYnode']:         
            self.setupFile['nodeDef'][self.name]['cmds']['sends'] = self.mSystem[nodeName]['ISYnode']['sends']                                 
        return()

    def addNodeSendComand(self, nodeNbr, nodeId, functionId ):
        self.name = nodeId+str(nodeNbr)
        if self.name in self.setupFile['nodeDef']:
            if 'sends' in self.setupFile['nodeDef'][self.name]['cmds']:
                self.setupFile['nodeDef'][self.name]['cmds']['sends'].append(functionId)
            else:
                self.setupFile['nodeDef'][self.name]['cmds']['sends']=[]
                self.setupFile['nodeDef'][self.name]['cmds']['sends'].append(functionId)
        else:
            print('Unknown name: ' + nodeId)
        return()
   
    def addNodeAcceptComand(self,  nodeNbr, nodeId, functionName, messanaKey):  
        name = nodeId + '_' + str(nodeNbr)
        if len(messanaKey) == 0:
            if 'accepts' in self.setupFile['nodeDef'][name]['cmds']:
                self.setupFile['nodeDef'][name]['cmds']['accepts'][functionName] = {}
            else:
                self.setupFile['nodeDef'][name]['cmds']['accepts'] = {}
                self.setupFile['nodeDef'][name]['cmds']['accepts'][functionName] = {}
        else:
            if not('accepts' in self.setupFile['nodeDef'][name]['cmds']):
                self.setupFile['nodeDef'][self.name]['cmds']['accepts'] = {}
            if messanaKey in self.setupFile['nodeDef'][name]['sts']: 
               self.setupFile['nodeDef'][name]['cmds']['accepts'][functionName] = self.setupFile['nodeDef'][name]['sts'][messanaKey]
            else:
                print(messanaKey + 'not defined')
        return() 


    def addSystemSendComand(self, idName):
        if 'sends' in self.setupFile['nodeDef'][ self.systemID]['cmds']:
            self.setupFile['nodeDef'][ self.systemID]['cmds']['sends'].append(idName)
        else:
            self.setupFile['nodeDef'][ self.systemID]['cmds']['sends']=[]
            self.setupFile['nodeDef'][ self.systemID]['cmds']['sends'].append(idName)
        return()
   
    def addSystemAcceptComand(self, functionName, messanaKey):
        if len(messanaKey) == 0:
            if 'accepts' in self.setupFile['nodeDef'][ self.systemID]['cmds']:
                self.setupFile['nodeDef'][ self.systemID]['cmds']['accepts'][functionName] = {}
            else:
                self.setupFile['nodeDef'][ self.systemID]['cmds']['accepts'] = {}
                self.setupFile['nodeDef'][ self.systemID]['cmds']['accepts'][functionName] = {}
        else:
            if not('accepts' in self.setupFile['nodeDef'][ self.systemID]['cmds']):
                self.setupFile['nodeDef'][ self.systemID]['cmds']['accepts'] = {}
            if messanaKey in self.setupFile['nodeDef'][ self.systemID]['sts']:
                self.setupFile['nodeDef'][ self.systemID]['cmds']['accepts'][functionName] = self.setupFile['nodeDef'][ self.systemID]['sts'][messanaKey]
            else:
                print(messanaKey + 'not defined')
        return() 


    def addSystemDefStruct(self, nodeId):
        self.keyCount = 0
        nodeId.lower()
        self.nlsKey= 'nls' + nodeId
        self.nlsKey.lower()
        print('addSystemDefStruct: ' + nodeId)
        self.setupFile['nodeDef'][ self.systemID]={}
        self.setupFile['nodeDef'][ self.systemID]['CodeId'] = nodeId
        self.setupFile['nodeDef'][ self.systemID]['nlsId'] = self.nlsKey
        self.setupFile['nodeDef'][ self.systemID]['nlsNAME']=self.mSystem[ self.systemID]['data']['mName']
        self.setupFile['nodeDef'][ self.systemID]['nlsICON']=self.mSystem[ self.systemID]['ISYnode']['nlsICON']
        self.setupFile['nodeDef'][ self.systemID]['sts']={}

        #for mKey in self.mSystem[ self.systemID]['data']: 
        for mKey in self.mSystem[ self.systemID]['GETkeysList']:    
            #make check if system has unit installed
            if self.mSystem[ self.systemID]['KeyInfo'][mKey]['ISYeditor']['ISYuom']:
                if ((self.mSystem[ self.systemID]['KeyInfo'][mKey]['ISYeditor']['ISYuom'] == 112
                   and self.mSystem[ self.systemID]['data'][mKey] != 0)
                   or self.mSystem[ self.systemID]['KeyInfo'][mKey]['ISYeditor']['ISYuom'] != 112):
                    self.keyCount = self.keyCount + 1
                    editorName = 'SYSTEM_'+str(self.keyCount)
                    nlsName = editorName
                    ISYvar = 'GV'+str(self.keyCount)
                    self.setupFile['nodeDef'][ self.systemID]['sts'][mKey]={ISYvar:editorName}
                    self.setupFile['editors'][editorName]={}
                    #self.setupFile['nls'][editorName][ISYparam]
                    for ISYparam in self.mSystem[ self.systemID]['KeyInfo'][mKey]['ISYeditor']:
                        if self.mSystem[ self.systemID]['KeyInfo'][mKey]['ISYeditor'][ISYparam]!= None:
                            self.setupFile['editors'][editorName][ISYparam]=self.mSystem[ self.systemID]['KeyInfo'][mKey]['ISYeditor'][ISYparam]

                    if self.mSystem[ self.systemID]['KeyInfo'][mKey]['ISYnls']:
                        self.setupFile['nls'][nlsName]={}
                    for ISYnls in self.mSystem[ self.systemID]['KeyInfo'][mKey]['ISYnls']:
                        #print( mKey + ' ' + ISYnls)
                        if  self.mSystem[ self.systemID]['KeyInfo'][mKey]['ISYnls'][ISYnls]:      
                            self.setupFile['nls'][nlsName][ISYnls] = self.mSystem[ self.systemID]['KeyInfo'][mKey]['ISYnls'][ISYnls]
                            if ISYnls == 'nlsValues':
                                self.setupFile['editors'][editorName]['nlsKey'] = nlsName
        
        self.setupFile['nodeDef'][ self.systemID]['cmds']={}
        if 'accepts' in self.mSystem[ self.systemID]['ISYnode']:
            self.setupFile['nodeDef'][ self.systemID]['cmds']['accepts'] = {}
            for key in  self.mSystem[ self.systemID]['ISYnode']['accepts']:     
                if self.mSystem[ self.systemID]['ISYnode']['accepts'][key]['ISYeditor'] in self.setupFile['nodeDef'][ self.systemID]['sts']:
                    mVal = self.mSystem[ self.systemID]['ISYnode']['accepts'][key]['ISYeditor']
                    self.setupFile['nodeDef'][ self.systemID]['cmds']['accepts'][key]= self.setupFile['nodeDef'][ self.systemID]['sts'][mVal]
                    self.setupFile['nodeDef'][ self.systemID]['cmds']['accepts'][key]['ISYInfo']=self.mSystem[ self.systemID]['ISYnode']['accepts'][key]
                else:
                    self.setupFile['nodeDef'][ self.systemID]['cmds']['accepts'][key]= {}
                    self.setupFile['nodeDef'][ self.systemID]['cmds']['accepts'][key]['ISYInfo']= self.mSystem[ self.systemID]['ISYnode']['accepts'][key]   
        if 'sends' in self.mSystem[ self.systemID]['ISYnode']:
            self.setupFile['nodeDef'][ self.systemID]['cmds']['sends']=self.mSystem[ self.systemID]['ISYnode']['sends']                              
        return()



    def getNodeCapability (self, nodeKey, nodeNbr):    
        #print ('getNodeCapability') 
        self.keyDict = {}
        self.GETkeysList = []
        self.PUTkeysList = []
        for mKey in self.mSystem[nodeKey]['KeyInfo']:
            if mKey == 'mCapability':
                if 'GETstr' in self.mSystem[nodeKey]['KeyInfo']['mCapability']:
                    GETStr =self.IP+self.mSystem[nodeKey]['KeyInfo']['mCapability']['GETstr']+str(nodeNbr)+'?'+ self.APIStr 
                    Nodep = requests.get(GETStr)
                    if str(Nodep) == self.RESPONSE_OK:
                        #self.GETkeysList.append(mKey)
                        tempKeys= Nodep.json()
                        for key in tempKeys:
                            #zones      
                            if key == 'operative_temperature':
                                status = self.checkGETNode( nodeKey, nodeNbr, 'mTemp')   
                                if status['statusOK'] == True:
                                    self.keyDict['mTemp'] = tempKeys['operative_temperature']
                                else:
                                    self.keyDict['mTemp'] = 0
                                status = self.checkGETNode( nodeKey, nodeNbr, 'mSetpoint')   
                                if status['statusOK'] == True:
                                    self.keyDict['mSetpoint'] = tempKeys['operative_temperature']
                                else:
                                    self.keyDict['mSetpoint'] = 0                                    
                            elif key == 'air_temperature':                            
                                status = self.checkGETNode( nodeKey, nodeNbr, 'mAirTemp')   
                                if status['statusOK'] == True:
                                    self.keyDict['mAirTemp'] = tempKeys["air_temperature"]
                                else:
                                    self.keyDict[''] = 0   
                            elif key == 'relative_humidity':                            
                                status = self.checkGETNode( nodeKey, nodeNbr, 'mHumSetpointRH')   
                                if status['statusOK'] == True:
                                    self.keyDict['mHumSetpointRH'] = tempKeys['relative_humidity']
                                else:
                                    self.keyDict['mHumSetpointRH'] = 0                                       
                                status = self.checkGETNode( nodeKey, nodeNbr, 'mHumSetpointDP')   
                                if status['statusOK'] == True:
                                    self.keyDict['mHumSetpointDP'] = tempKeys['relative_humidity']
                                else:
                                    self.keyDict['mHumSetpointDP'] = 0                                       
                                status = self.checkGETNode(nodeKey, nodeNbr, 'mDehumSetpointRH')   
                                if status['statusOK'] == True:
                                    self.keyDict['mDehumSetpointRH'] = tempKeys['relative_humidity']
                                else:
                                    self.keyDict['mDehumSetpointRH'] = 0                                       
                                status = self.checkGETNode(nodeKey,  nodeNbr, 'mDehumSetpointDP')   
                                if status['statusOK'] == True:
                                    self.keyDict['mDehumSetpointDP'] = tempKeys['relative_humidity']
                                else:
                                    self.keyDict['mDehumSetpointDP'] = 0                                       
                                status = self.checkGETNode( nodeKey, nodeNbr, 'mCurrentSetpointRH')   
                                if status['statusOK'] == True:
                                    self.keyDict['mCurrentSetpointRH'] = tempKeys['relative_humidity']
                                else:
                                    self.keyDict['mCurrentSetpointRH'] = 0  
                                status = self.checkGETNode( nodeKey, nodeNbr, 'mCurrentSetpointDP')   
                                if status['statusOK'] == True:
                                    self.keyDict['mCurrentSetpointDP'] = tempKeys['relative_humidity']    
                                else:
                                    self.keyDict['mCurrentSetpointDP'] = 0                                                                          
                                status = self.checkGETNode( nodeKey, nodeNbr, 'mHumidity')   
                                if status['statusOK'] == True:
                                    self.keyDict['mHumidity'] = tempKeys['relative_humidity']      
                                else:
                                    self.keyDict['mHumidity'] = 0                                      
                            elif key == 'dewpoint':
                                status = self.checkGETNode( nodeKey, nodeNbr, 'mDewPoint')   
                                if status['statusOK'] == True:
                                    self.keyDict['mDewPoint'] = tempKeys['dewpoint'] 
                                else:
                                    self.keyDict['mDewPoint'] = 0                                        
                            elif key == 'co2':
                                status = self.checkGETNode( nodeKey, nodeNbr, 'mCO2')   
                                if status['statusOK'] == True:
                                    self.keyDict['mCO2'] = tempKeys['co2']   
                                else:
                                    self.keyDict['mCO2'] = 0                                      
                                status = self.checkGETNode( nodeKey, nodeNbr, 'mAirQuality')   
                                if status['statusOK'] == True:
                                    self.keyDict['mAirQuality'] = tempKeys['co2']          
                                else:
                                    self.keyDict['mAirQuality'] = 0                                                                          
                            elif key == 'voc':
                                status = self.checkGETNode( nodeKey, nodeNbr, 'mVoc')   
                                if status['statusOK'] == True:
                                    self.keyDict['mVoc'] = tempKeys['voc']   
                                else:
                                    self.keyDict['mVoc'] = 0              
                            #ATUs
                            elif key == 'exhaust air extraction':
                                # Not currently supported   - no correspinding
                                None
    
                            elif key == 'freecooling':
                                # Not currently supported  - no correspinding value
                                None
                            
                            elif key == 'convective integration':
                                status = self.checkGETNode( nodeKey, nodeNbr,  'mINTOn')   
                                if status['statusOK'] == True:
                                    if isinstance(tempKeys['convective integration'], int):
                                        self.keyDict['mINTOn'] = tempKeys['convective integration']
                                else:
                                    self.keyDict['mINTOn'] = 0
                            elif key == 'HRV':
                                status = self.checkGETNode( nodeKey, nodeNbr,  'mHRVOn')   
                                if status['statusOK'] == True:
                                    if isinstance(tempKeys['HRV'], int):
                                        self.keyDict['mHRVOn'] = tempKeys['HRV']
                                else:
                                    self.keyDict['mHRVOn'] = 0                            

                            elif key == 'humidification':  
                                status = self.checkGETNode( nodeKey, nodeNbr,  'mHUMOn')   
                                if status['statusOK'] == True:
                                    if isinstance(tempKeys['humidification'], int):
                                        self.keyDict['mHUMOn'] = tempKeys['humidification']
                                else:
                                    self.keyDict['mHUMOn'] = 0   
                                status = self.checkGETNode( nodeKey, nodeNbr,  'mHumidityStatus')   
                                #need to be verified
                                if status['statusOK'] == True:
                                    if isinstance(tempKeys['humidification'], int):
                                        self.keyDict['mHumidityStatus'] = tempKeys['humidification']
                                else:
                                    self.keyDict['mHumidityStatus'] = 0   
                                status = self.checkGETNode( nodeKey, nodeNbr,  'mHumSetpointRH')   
                                #need to be verified
                                if status['statusOK'] == True:
                                    if isinstance(tempKeys['humidification'], int):
                                        self.keyDict['mHumSetpointRH'] = tempKeys['humidification']
                                else:
                                    self.keyDict['mHumSetpointRH'] = 0   
                                status = self.checkGETNode( nodeKey, nodeNbr,  'mHumSetpointDP')   
                                #need to be verified
                                if status['statusOK'] == True:
                                    if isinstance(tempKeys['humidification'], int):
                                        self.keyDict['mHumSetpointDP'] = tempKeys['humidification']
                                else:
                                    self.keyDict['mHumSetpointDP'] = 0   
                            elif key == 'dehumidification':
                                status = self.checkGETNode( nodeKey, nodeNbr,  'mNTDOn')  
                                if status['statusOK'] == True:
                                    if isinstance(tempKeys['dehumidification'], int):
                                        self.keyDict['mNTDOn'] = tempKeys['dehumidification']
                                else:
                                    self.keyDict['mNTDOn'] = 0 
                                status = self.checkGETNode( nodeKey, nodeNbr,  'mDehumudityStatus')  
                                if status['statusOK'] == True:
                                    if isinstance(tempKeys['dehumidification'], int):
                                        self.keyDict['mDehumudityStatus'] = tempKeys['dehumidification']
                                else:
                                    self.keyDict['mDehumudityStatus'] = 0 
                                status = self.checkGETNode( nodeKey, nodeNbr,  'mDehumSetpointRH')  
                                if status['statusOK'] == True:
                                    if isinstance(tempKeys['dehumidification'], int):
                                        self.keyDict['mDehumSetpointRH'] = tempKeys['dehumidification']
                                else:
                                    self.keyDict['mDehumSetpointRH'] = 0 
                                status = self.checkGETNode( nodeKey, nodeNbr,  'mDehumSetpointDP')  
                                if status['statusOK'] == True:
                                    if isinstance(tempKeys['dehumidification'], int):
                                        self.keyDict['mDehumSetpointDP'] = tempKeys['dehumidification']
                                else:
                                    self.keyDict['mDehumSetpointDP'] = 0 




                            else:
                                print(key + ' unknown keyword')

            elif ((self.mSystem[nodeKey]['KeyInfo'][mKey]['GETstr'] != None) ):
                data = self.pullNodeDataIndividual(nodeNbr, nodeKey,  mKey)
                if data['statusOK'] and not(data['data'] in self.NaNlist) and (isinstance(data['data'], float) or isinstance(data['data'], int)):
                    # mKey used by ISY
                    if self.mSystem[nodeKey]['KeyInfo'][mKey]['ISYeditor']['ISYuom'] != None:
                        self.GETkeysList.append(mKey)
                        temp=data['data']
                        if self.mSystem[nodeKey]['KeyInfo'][mKey]['PUTstr']!=None:
                            data =  self.PUTNodeData( nodeKey, nodeNbr, mKey, temp)
                            if data['statusOK']:
                                self.PUTkeysList.append(mKey)
                            else:
                                print( 'Removed ' + mKey + 'from PUT commands')
        #remove capability for GET list
        for mKey in self.keyDict:
            if self.keyDict[mKey] == 0 and mKey in self.GETkeysList:
                self.GETkeysList.remove(mKey)

        self.mSystem[nodeKey]['SensorCapability'][nodeNbr] = self.keyDict
        self.mSystem[nodeKey]['GETkeysList'][nodeNbr] = []
        self.mSystem[nodeKey]['GETkeysList'][nodeNbr].extend(self.GETkeysList)
        self.mSystem[nodeKey]['PUTkeysList'][nodeNbr] = []
        self.mSystem[nodeKey]['PUTkeysList'][nodeNbr].extend(self.PUTkeysList)
    
    def GETSystemData(self, mKey):
        sysData= {}
        #print('GETSystem: ' + mKey )
        GETStr = self.IP+self.mSystem[ self.systemID]['KeyInfo'][mKey]['GETstr'] + '?' + self.APIStr 
        #print( GETStr)
        try:
            systemTemp = requests.get(GETStr)
            #print(str(systemTemp))
            if str(systemTemp) == self.RESPONSE_OK:
                systemTemp = systemTemp.json()
                #print(systemTemp)
                self.mSystem[ self.systemID]['data'][mKey] = systemTemp[str(list(systemTemp.keys())[0])]

                sysData['data'] = self.mSystem[ self.systemID]['data'][mKey]
                if sysData['data'] in self.NaNlist:
                    sysData['statusOK'] = False
                    sysData['error'] = 'NaN received'
                else:
                    sysData['statusOK'] = True 

            else:
                print(str(mKey) + ' error')
                sysData['statusOK'] = False
                sysData['error'] = str(systemTemp)
                #self.systemDict[mKey] = -1
            return(sysData) #No data for given keyword - remove from list 
        except:
            print('System GET operation failed for :' + mKey)
            sysData['statusOK'] = False
            sysData['error'] = 'EXCEPT: System GET operation failed for :' + mKey  
            return(sysData)

    def PUTSystemData(self, mKey, value):
            sysData= {}
            #print('PUT System: {' + mKey +':'+str(value)+'}' )
            mData = defaultdict(list)
            if mKey in self.mSystem[ self.systemID]['KeyInfo']:
                if self.mSystem[ self.systemID]['KeyInfo'][mKey]['PUTstr'] == None:
                    sysData['statusOK'] = False
                    sysData['error'] = 'Not able to PUT Key: : '+ mKey + ' value:' + str( value )
                    #print('Error '+ sysData)    
                    return(sysData)                     
                else:
                    PUTStr = self.IP+self.mSystem[ self.systemID]['KeyInfo'][mKey]['PUTstr']
                    mData = {'value':value, self.APIKey : self.APIKeyVal}
                    try:
                        resp = requests.put(PUTStr, json=mData)
                        print(resp)
                        if str(resp) != self.RESPONSE_OK:
                            sysData['statusOK'] = False
                            sysData['error'] = str(resp)+ ': Not able to PUT Key: : '+ mKey + ' value:' + str( value )
                        else:
                            sysData['statusOK'] = True
                            sysData['data'] = value
                        #print(sysData)    
                        return(sysData)          
                    except:
                        sysData['statusOK'] = False
                        sysData['error'] = 'System PUT operation failed for :' + mKey + ' '+ str(value)
                        return(sysData)
  
    def GETNodeData(self, mNodeKey, nodeNbr, mKey):
        #print('GETNodeData: ' + mNodeKey + ' ' + str(nodeNbr)+ ' ' + mKey)
        nodeData = {}

        if 'GETstr' in self.mSystem[mNodeKey]['KeyInfo'][mKey]:
            GETStr =self.IP+self.mSystem[mNodeKey]['KeyInfo'][mKey]['GETstr']+str(nodeNbr)+'?'+ self.APIStr 
            Nodep = requests.get(GETStr)
            if str(Nodep) == self.RESPONSE_OK:
                Nodep = Nodep.json()
                nodeData['data']  = Nodep[str(list(Nodep.keys())[0])]
                if nodeData in self.NaNlist:
                    nodeData['statusOK'] = False
                    nodeData['error'] = 'NaN received'
                else:
                    nodeData['dataAll'] = Nodep
                    nodeData['statusOK'] =True
                if nodeNbr in self.mSystem[mNodeKey]['data']:
                    if mKey in self.mSystem[mNodeKey]['data'][nodeNbr]:
                        self.mSystem[mNodeKey]['data'][nodeNbr][mKey] = nodeData['data']
                    else:
                        self.mSystem[mNodeKey]['data'][nodeNbr].update({mKey : nodeData['data']})
                else:
                    temp = {}
                    temp[nodeNbr] = {mKey : nodeData['data']}
                    self.mSystem[mNodeKey]['data'].update(temp)

            elif str(Nodep) == self.RESPONSE_NO_SUPPORT:
                temp1 =  Nodep.content
                res_dict = json.loads(temp1.decode('utf-8')) 
                nodeData['error'] = str(Nodep) + ': Error: '+ str(res_dict.values()) + ' Node ' + str(nodeNbr) + ' for id: ' + str(mKey)
                nodeData['statusOK'] =False
            elif str(Nodep) == self.RESPONSE_NO_RESPONSE:
                nodeData['error'] = str(Nodep) + ': Error: No response from API:  Node ' + str(nodeNbr) + ' for id: ' + str(mKey)
                nodeData['statusOK'] =False
            else:
                nodeData['error'] = str(Nodep) + ': Error: Unknown: Node ' + str(nodeNbr) + ' for id: ' + str(mKey)
                nodeData['statusOK'] =False
        else: 
                nodeData['error'] = 'Does not support keyword: ' + mKey
                nodeData['statusOK'] =False
        return(nodeData)   

    def PUTNodeData(self, mNodeKey, nodeNbr, mKey, value):
        nodeData = {}
        if 'PUTstr' in self.mSystem[mNodeKey]['KeyInfo'][mKey]:
            PUTStr = self.IP + self.mSystem[mNodeKey]['KeyInfo'][mKey]['PUTstr']
            #print('PUT str: ' + PUTStr + str(value))
            mData = {'id':nodeNbr, 'value': value, self.APIKey : self.APIKeyVal}
            resp = requests.put(PUTStr, json=mData)
            if str(resp) == self.RESPONSE_OK:
                self.mSystem[mNodeKey]['data'][nodeNbr][mKey] = value
                nodeData['statusOK'] = True
            elif str(resp) == self.RESPONSE_NO_SUPPORT:
                temp1 =  resp.content
                res_dict = json.loads(temp1.decode('utf-8')) 
                nodeData['error'] = str(resp) + ': Not able to PUT key: '+ str(res_dict.values()) + ' Node ' + str(id) + ' for key: ' + str(mKey) + ' value:', str(value)
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

 
    # New Functions Need to be tested
    def getNodeKeys (self, nodeNbr, nodeKey, cmdKey):
        keys = []
        if len(self.mSystem[nodeKey]['GETkeysList'][nodeNbr]) == 0:
            print('NodeCapability must be run first')
        else:
            if cmdKey == 'PUTstr':
                for mKey in self.mSystem[nodeKey]['PUTkeysList'][nodeNbr]:
                    if self.mSystem[nodeKey]['KeyInfo'][mKey][cmdKey] != None:
                        keys.append(mKey)
            else:
                for mKey in self.mSystem[nodeKey]['GETkeysList'][nodeNbr]:
                    if self.mSystem[nodeKey]['KeyInfo'][mKey][cmdKey] != None:
                        keys.append(mKey)

        '''    
        for mKey in self.mSystem[nodeKey]['KeyInfo']:
            if mKey in self.mSystem[nodeKey]['SensorCapability'][nodeNbr]:
                if self.mSystem[nodeKey]['SensorCapability'][nodeNbr][mKey] != 0:
                    if self.mSystem[nodeKey]['KeyInfo'][mKey][cmdKey]!=None:
                        data = self.pullNodeDataIndividual(nodeNbr, nodeKey,  mKey)
                        if data['statusOK']:
                            keys.append(mKey)
            else:
                if mKey != 'mCapability': #mCapability is special case handled by 'SensorCapability'
                    if self.mSystem[nodeKey]['KeyInfo'][mKey][cmdKey]!=None:
                        data = self.pullNodeDataIndividual(nodeNbr, nodeKey,  mKey)
                        if data['statusOK']:
                            keys.append(mKey)
        '''                    
        return(keys)

    def updateNodeData(self, nodeNbr, nodeKey):
        print('updatNodeData: ' + str(nodeNbr) + ' ' + nodeKey)
        Data = {}
        dataOK = True
        #supportedPullKeys = self.getNodeKeys (nodeNbr, nodeKey, 'GETstr')
        supportedPullKeys = self.mSystem[nodeKey]['GETkeysList'][nodeNbr]
        for mKey in supportedPullKeys:
            #print('GET ' + mKey + ' in zone ' + str(nodeNbr))
            Data = self.pullNodeDataIndividual(nodeNbr, nodeKey,  mKey)
            if not(Data['statusOK']):
                dataOK = False
                #print('Error GET' + Data['error'])
        return(dataOK)
    
    def pullNodeDataIndividual(self, nodeNbr, nodeKey, mKey): 
        Data = self.GETNodeData(nodeKey, nodeNbr, mKey)
        return(Data)
    
    def checkGETNode(self,  nodeKey, nodeNbr, mKey): 
        nodeData = {}
        if 'GETstr' in self.mSystem[nodeKey]['KeyInfo'][mKey]:
            GETStr =self.IP+self.mSystem[nodeKey]['KeyInfo'][mKey]['GETstr']+str(nodeNbr)+'?'+ self.APIStr 
            Nodep = requests.get(GETStr)
            if str(Nodep) == self.RESPONSE_OK:
                Nodep = Nodep.json()
                nodeData['data']  = Nodep[str(list(Nodep.keys())[0])] 
                if nodeData['data'] in self.NaNlist:
                    nodeData['statusOK'] =False
                    nodeData['error'] = 'NaN received'
                else:
                    nodeData['statusOK'] =True
            elif str(Nodep) == self.RESPONSE_NO_SUPPORT:
                temp1 =  Nodep.content
                res_dict = json.loads(temp1.decode('utf-8')) 
                nodeData['error'] = str(Nodep) + ': Error: '+ str(res_dict.values()) + ' Node ' + str(nodeNbr) + ' for id: ' + str(mKey)
                nodeData['statusOK'] =False
            elif str(Nodep) == self.RESPONSE_NO_RESPONSE:
                nodeData['error'] = str(Nodep) + ': Error: No response from API:  Node ' + str(nodeNbr) + ' for id: ' + str(mKey)
                nodeData['statusOK'] =False
            else:
                nodeData['error'] = str(Nodep) + ': Error: Unknown: Node ' + str(nodeNbr) + ' for id: ' + str(mKey)
                nodeData['statusOK'] =False
        else: 
                nodeData['error'] = 'Does not support keyword: ' + mKey
                nodeData['statusOK'] =False
        return(nodeData)   

    def pushNodeDataIndividual(self, NodeNbr, NodeKey, mKey, value):
       # print('pushZoneDataIndividual: ' +str(NodeNbr)  + ' ' + mKey + ' ' + str(value))  
        nodeData = {}
        nodeData= self.PUTNodeData(NodeKey, NodeNbr, mKey, value)
        if nodeData['statusOK']:
            return(True)
        else:
            print(nodeData['error'])
            return(False)

    #Setup file generation 
    def createSetupFiles(self, nodeDefFileName, editorFileName, nlsFileName):
        print ('Create Setup Files')
        status = True
        try:
            print('opening files')
            if not(os.path.exists('./profile')):
                os.mkdir('./profile')       
            if not(os.path.exists('./profile/editor')):
                os.mkdir('./profile/editor')
            if not(os.path.exists('./profile/nls')):
                os.mkdir('./profile/nls')           
            if not(os.path.exists('./profile/nodedef')):
                os.mkdir('./profile/nodedef')
            nodeFile = open(nodeDefFileName, 'w+')
            editorFile = open(editorFileName, 'w+')
            nlsFile = open(nlsFileName, 'w+')
            print('Opening Files OK')

            editorFile.write('<editors> \n')
            nodeFile.write('<nodeDefs> \n')
            for node in self.setupFile['nodeDef']:
                nodeDefStr ='   <nodeDef id="' + self.setupFile['nodeDef'][node]['CodeId']+'" '+ 'nls="'+self.setupFile['nodeDef'][node]['nlsId']+'">\n'
                #print(nodeDefStr)
                nodeFile.write(nodeDefStr)
                nodeFile.write('      <editors />\n')
                nodeFile.write('      <sts>\n')
                #nlsStr = 'ND-'+self.setupFile['nodeDef'][node]['nlsId']+'-NAME = '+self.setupFile['nodeDef'][node]['nlsNAME']+ '\n'
                nlsStr = 'ND-'+self.setupFile['nodeDef'][node]['CodeId']+'-NAME = '+self.setupFile['nodeDef'][node]['nlsNAME']+ '\n'
                nlsFile.write(nlsStr)
                #nlsStr = 'ND-'+self.setupFile['nodeDef'][node]['nlsId']+'-ICON = '+self.setupFile['nodeDef'][node]['nlsICON']+ '\n'
                nlsStr = 'ND-'+self.setupFile['nodeDef'][node]['CodeId']+'-ICON = '+self.setupFile['nodeDef'][node]['nlsICON']+ '\n'
                nlsFile.write(nlsStr)
                for acceptCmd in self.setupFile['nodeDef'][node]['cmds']['accepts']:
                    cmdName =  self.setupFile['nodeDef'][node]['cmds']['accepts'][acceptCmd]['ISYInfo']['ISYtext']
                    nlsStr = 'CMD-' + self.setupFile['nodeDef'][node]['nlsId']+'-'+acceptCmd+'-NAME = ' + cmdName +'\n'
                    nlsFile.write(nlsStr)
                    #print(nlsStr)

                for status in self.setupFile['nodeDef'][node]['sts']:
                    for statusId in self.setupFile['nodeDef'][node]['sts'][status]:
                        if statusId != 'ISYInfo':
                            nodeName = self.setupFile['nodeDef'][node]['sts'][status][statusId]
                            nodeDefStr =  '         <st id="' + statusId+'" editor="'+nodeName+'" />\n'
                            #print(nodeDefStr)
                            nodeFile.write(nodeDefStr)
                            editorFile.write( '  <editor id = '+'"'+nodeName+'" > \n')
                            editorStr = '     <range '
                            for key in self.setupFile['editors'][nodeName]:
                                if key == 'ISYsubset':
                                    editorStr = editorStr + ' subset="'+ str(self.setupFile['editors'][nodeName][key])+'"'
                                elif key == 'ISYuom':
                                    editorStr = editorStr + ' uom="'+ str(self.setupFile['editors'][nodeName][key])+'"'
                                elif key == 'ISYmax':
                                    editorStr = editorStr + ' max="'+ str(self.setupFile['editors'][nodeName][key])+'"'
                                elif key == 'ISYmin': 
                                    editorStr = editorStr + ' min="'+ str(self.setupFile['editors'][nodeName][key])+'"'
                                elif key == 'ISYstep':
                                    editorStr = editorStr + ' step="'+ str(self.setupFile['editors'][nodeName][key])+'"'                  
                                elif key == 'ISYprec': 
                                    editorStr = editorStr + ' prec="'+ str(self.setupFile['editors'][nodeName][key])+'"'
                                elif key == 'ISYsubset': 
                                    editorStr = editorStr + ' subset="'+ str(self.setupFile['editors'][nodeName][key])+'"'
                                elif key == 'nlsKey': 
                                    nlsEditorKey = str(self.setupFile['editors'][nodeName][key])
                                    editorStr = editorStr + ' nls="'+ nlsEditorKey+'"'
                                else:
                                    print('unknown editor keyword: ' + str(key))
                            editorStr = editorStr + ' />\n'
                            #print(editorStr)
                            editorFile.write(editorStr)
                            editorFile.write('</editor>\n')

                        for nlsInfo in self.setupFile['nls'][nodeName]:
                            if statusId != 'ISYInfo':
                                if nlsInfo == 'nlsTEXT':
                                    nlsStr = 'ST-' + self.setupFile['nodeDef'][node]['nlsId']+'-'+statusId+'-NAME = '
                                    nlsStr = nlsStr + self.setupFile['nls'][nodeName][nlsInfo] + '\n'
                                    nlsFile.write(nlsStr)
                                elif nlsInfo == 'nlsValues':
                                    nlsValues = 0
                                    for key in self.setupFile['nls'][nodeName][nlsInfo]:
                                        nlsStr = nlsEditorKey+'-'+str(nlsValues)+' = '+self.setupFile['nls'][nodeName][nlsInfo][key]+'\n'
                                        nlsFile.write(nlsStr)
                                        nlsValues = nlsValues + 1
                                #print(nlsStr)

                nodeFile.write('      </sts>\n')
                nodeFile.write('      <cmds>\n')                
                nodeFile.write('         <sends>\n')            
                if self.setupFile['nodeDef'][node]['cmds']:
                    if len(self.setupFile['nodeDef'][node]['cmds']['sends']) != 0:
                        for sendCmd in self.setupFile['nodeDef'][node]['cmds']['sends']:
                            cmdStr = '            <cmd id="' +sendCmd +'" /> \n'
                            #print(cmdStr)
                            nodeFile.write(cmdStr)
                nodeFile.write('         </sends>\n')               
                nodeFile.write('         <accepts>\n')      
                if self.setupFile['nodeDef'][node]['cmds']:
                    if 'accepts' in self.setupFile['nodeDef'][node]['cmds']:
                        for acceptCmd in self.setupFile['nodeDef'][node]['cmds']['accepts']:
                            
                            if len(self.setupFile['nodeDef'][node]['cmds']['accepts'][acceptCmd]) != 1:
                                for key in self.setupFile['nodeDef'][node]['cmds']['accepts'][acceptCmd]:
                                    if key != 'ISYInfo':
                                        cmdStr = '            <cmd id="' +acceptCmd+'" > \n'     
                                        nodeFile.write(cmdStr)  
                                        cmdStr = '               <p id="" editor="'
                                        cmdStr = cmdStr + self.setupFile['nodeDef'][node]['cmds']['accepts'][acceptCmd][key]+ '" init="' + key +'" /> \n' 
                                        #print(cmdStr)                              
                                        nodeFile.write(cmdStr)
                                        nodeFile.write('            </cmd> \n')
                            else:
                                cmdStr = '            <cmd id="' +acceptCmd+'" /> \n' 
                                #print(cmdStr)
                                nodeFile.write(cmdStr)  
                nodeFile.write('         </accepts>\n')                   

                nodeFile.write('      </cmds>\n')                
                                    
                nodeFile.write('   </nodeDef> \n')

            nodeFile.write('</nodeDefs> \n' )
            nodeFile.close()
            editorFile.write('</editors> \n')
            editorFile.close()
            nlsFile.close()
        
        except:
            print('something went wrong in creating setup files')
            status = False
            nodeFile.close()
            editorFile.close()
            nlsFile.close()
        return(status)



    #System
    def updateSystemData(self, level):
        print('Update Messana Sytem Data')
        sysData = {}
        DataOK = True
       
        if level == 'active':
            for mKey in self.systemActiveKeys():
                sysData= self.pullSystemDataIndividual(mKey)
                if not(sysData['statusOK']):
                    print('Error System Active GET: ' + mKey)
                    DataOK = False  
        elif level == 'all':
            for mKey in self.systemPullKeys():
                sysData= self.pullSystemDataIndividual(mKey)
                if not(sysData['statusOK']):
                    print('Error System Active GET: ' + mKey)
                    DataOK = False 
        else:
            print('Unknown level: ' + level)
            DataOK = False               
        return(DataOK)

    #pretty bad solution - just checking if a value can be extracted
    def checkMessanaConnection(self):
        sysData = self.GETSystemData('mApiVer') 
        return (sysData['statusOK'])
    


    def pullSystemDataIndividual(self, mKey):
        print('MessanaInfo pull System Data: ' + mKey)
        return(self.GETSystemData(mKey) )
                 

    def pushSystemDataIndividual(self, mKey, value):
        sysData={}
        print('MessanaInfo push System Data: ' + mKey)       
        sysData = self.PUTSystemData(mKey, value)
        if sysData['statusOK']:
            return(True)
        else:
            print(sysData['error'])
            return(False) 

     
    def getSystemCapability(self):
        GETkeysList=[]
        PUTkeysList=[]
        for mKey in self.mSystem[ self.systemID]['KeyInfo']:
            data = self.pullSystemDataIndividual(mKey)
            if data['statusOK']:
                # Parameter is used by ISY
                if self.mSystem[ self.systemID]['KeyInfo'][mKey]['ISYeditor']['ISYuom'] != None:
                    temp = data['data']
                    GETkeysList.append(mKey)
                    if self.pushSystemDataIndividual(mKey, temp):
                        PUTkeysList.append(mKey)
        self.mSystem[self.systemID]['GETkeysList'] = []
        self.mSystem[self.systemID]['GETkeysList'].extend(GETkeysList)
        self.mSystem[self.systemID]['PUTkeysList'] = []
        self.mSystem[self.systemID]['PUTkeysList'].extend(PUTkeysList)
        

    def systemPullKeys(self):
        print('systemPullKeys')
        return(self.mSystem[self.systemID]['GETkeysList'])

    def systemPushKeys(self):
        print('systemPushKeys')
        return(self.mSystem[self.systemID]['PUTkeysList'])  
            
    def systemActiveKeys(self):
        print('systemActiveKeys')
        keys=[]
        for mKey in self.mSystem[self.systemID]['GETkeysList']:
            if self.mSystem[self.systemID]['KeyInfo'][mKey]['Active'] != None:
                keys.append(mKey)
        return(keys)  
            
    def getSystemISYValue(self, ISYkey):
        messanaKey = self.ISYmap[ self.systemID][ISYkey]['messana']
        systemPullKeys = self.systemPullKeys()
        if messanaKey in systemPullKeys:
            data = self.pullSystemDataIndividual(messanaKey)
            if data['statusOK']:
                val = data['data']        
                if val in  ['Celcius', 'Fahrenheit']:
                    if val == 'Celcius':
                        val = 0
                    else:  
                        val = 1 
                systemValue = val
                status = True
            else:
                systemValue = None
                status = False
        else:
            status = False
            systemValue = None
        return (status, systemValue)

    def PUTSystemISYValue(self, ISYkey, systemValue):
        messanaKey = self.ISYmap[ self.systemID][ISYkey]['messana']
        systemPushKeys = self.systemPushKeys()
        status = False
        if messanaKey in systemPushKeys:
            status = self.pushSystemDataIndividual(messanaKey, systemValue)
        return(status)
    
    def getMessanaSystemKey(self, ISYkey):
        return(self.ISYmap[ self.systemID][ISYkey]['messana'])

    def getSystemISYdriverInfo(self, mKey):
        info = {}
        if mKey in self.setupFile['nodeDef'][ self.systemID]['sts']:
            keys = list(self.setupFile['nodeDef'][ self.systemID]['sts'][mKey].keys())
            info['driver'] = keys[0]
            tempData =  self.GETSystemData(mKey)
            if tempData['statusOK']:
                val = tempData['data']        
                if val in  ['Celcius', 'Fahrenheit']:
                    if val == 'Celcius':
                        val = 0
                    else:  
                        val = 1 
                info['value'] = val
            else:
                info['value'] = ''
            editor = self.setupFile['nodeDef'][ self.systemID]['sts'][mKey][keys[0]]

            info['uom'] = self.setupFile['editors'][editor]['ISYuom']
        return(info)

    def getSystemSetbackISYdriver(self):
        Key = ''
        for ISYkey in self.ISYmap[ self.systemID]:
            if self.ISYmap[ self.systemID][ISYkey]['messana'] == 'mSetback':
                Key = ISYkey
        return(Key)

    def getSystemStatusISYdriver(self):
        Key = ''
        for ISYkey in self.ISYmap[ self.systemID]:
            if self.ISYmap[ self.systemID][ISYkey]['messana'] == 'mStatus':
                Key = ISYkey
        return(Key)

    def getSystemEnergySaveISYdriver(self):
        Key = ''
        for ISYkey in self.ISYmap[ self.systemID]:
            if self.ISYmap[ self.systemID][ISYkey]['messana'] == 'mEnergySaving':
                Key = ISYkey
        return(Key)       

    def systemSetStatus (self, value):
        print('systemSetstatus called')
        status = self.pushSystemDataIndividual('mStatus', value)
        return(status)

    def systemSetEnergySave (self, value):
        print('systemSetEnergySave called')
        status = self.pushSystemDataIndividual('mEnergySaving', value)
        return(status)
        
    def systemSetback (self, value):
        print('setSetback called')
        status = self.pushSystemDataIndividual('mSetback', value)
        return(status)

    def getSystemAddress(self):
        return(self.systemID)


    # Zones
    def getZoneCapability(self, zoneNbr):
        print('getZoneCapability') 
        self.getNodeCapability(self.zoneID, zoneNbr)

    def addZoneDefStruct(self, zoneNbr, nodeId):
        self.addNodeDefStruct(zoneNbr, self.zoneID, nodeId)

    def updateZoneData(self, level, zoneNbr):
        print('updatZoneData: ' + str(zoneNbr))

        keys =[]
        if level == 'all':
            print('ALL update zone ' + str(zoneNbr))
            keys =  self.zonePullKeys(zoneNbr)
        elif level == 'active':
            print('ACTIVE update zone ' + str(zoneNbr))
            keys =  self.zoneActiveKeys(zoneNbr)
        
        self.dataOK = True
        for mKey in keys:
            self.data = self.pullZoneDataIndividual(zoneNbr, mKey)
            self.dataOK = self.dataOK and self.data['statusOK']
        return(self.dataOK)

    def pullZoneDataIndividual(self, zoneNbr, mKey): 
        print('pullZoneDataIndividual: ' +str(zoneNbr)  + ' ' + mKey)    
        return(self.pullNodeDataIndividual(zoneNbr, self.zoneID, mKey))


    def pushZoneDataIndividual(self, zoneNbr, mKey, value):
        print('pushZoneDataIndividual: ' +str(zoneNbr)  + ' ' + mKey + ' ' + str(value))  
        return(self.pushNodeDataIndividual(zoneNbr, self.zoneID, mKey, value))

    def zonePullKeys(self, zoneNbr):
        print('zonePullKeys')
        self.tempZoneKeys =  self.getNodeKeys (zoneNbr, self.zoneID, 'GETstr')
        return( self.tempZoneKeys)

    def zonePushKeys(self, zoneNbr):
        print('zonePushKeys')
        return( self.getNodeKeys (zoneNbr, self.zoneID, 'PUTstr'))
  
    def zoneActiveKeys(self, zoneNbr):
        print('zoneActiveKeys')
        return( self.getNodeKeys (zoneNbr, self.zoneID, 'Active'))

    def getZoneCount(self):
        return(self.mSystem[ self.systemID]['data']['mZoneCount'])

    def getZoneName(self, zoneNbr):
        tempName = self.pullNodeDataIndividual(zoneNbr, self.zoneID, 'mName')
        if tempName['statusOK']:
            return(tempName['data'])
        else:
            return('NA')

    def getZoneAddress(self, zoneNbr):
        return(self.zoneID + str(zoneNbr))


    def getZoneMessanaISYkey(self, ISYkey, zoneNbr):
        zoneName = self.zoneID+str(zoneNbr)
        return(self.ISYmap[zoneName][ISYkey]['messana'])

    def getZoneISYValue(self, ISYkey, zoneNbr):
        zoneName = self.zoneID+str(zoneNbr)
        messanaKey = self.ISYmap[zoneName][ISYkey]['messana']
        #systemPullKeys = self.zonePullKeys(zoneNbr)
        try:
            data = self.pullZoneDataIndividual(zoneNbr, messanaKey)
            if data['statusOK']:
                val = data['data']        
                if val in  ['Celcius', 'Fahrenheit']:
                    if val == 'Celcius':
                        val = 0
                    else:  
                        val = 1 
                systemValue = val
                status = True
            else:
                systemValue = None
                status = False
        except:
            status = False
            systemValue = None
        return (status, systemValue)


    def checkZoneCommand(self, cmd, zoneNbr):
        exists = True
        mCmd = self.mSystem[self.zoneID]['ISYnode']['accepts'][cmd]['ISYeditor']
        
        if mCmd != None:
            if mCmd in self.mSystem[self.zoneID]['SensorCapability'][zoneNbr]:
                if self.mSystem[self.zoneID]['SensorCapability'][zoneNbr][mCmd] == 0:
                    exists = False
        return(exists)



    def zoneSetStatus(self, value, zoneNbr):
        print(' zoneSetstatus called for zone: ' + str(zoneNbr))
        
        status = self.pushZoneDataIndividual(zoneNbr, 'mStatus', value)
        return(status)
 

    def getZoneStatusISYdriver(self, zoneNbr):
        print('getZoneStatusISYdriver called for zone: '+str(zoneNbr))
        
        Key = ''
        zoneName = self.zoneID+str(zoneNbr)
        for ISYkey in self.ISYmap[zoneName]:
            if self.ISYmap[zoneName][ISYkey]['messana'] == 'mStatus':
                Key = ISYkey
        return(Key)  
        

    def zoneSetEnergySave(self, value, zoneNbr):
        print(' zoneSetEnergySave called for zone: ' + str(zoneNbr))
        
        status = self.pushZoneDataIndividual(zoneNbr, 'mEnergySaving', value)
        return(status)
    
    def getZoneEnergySaveISYdriver(self, zoneNbr):
        print('getZoneEnergySaveISYdriver called for zone: '+str(zoneNbr))
        
        Key = ''
        zoneName = self.zoneID+str(zoneNbr)
        for ISYkey in self.ISYmap[zoneName]:
            if self.ISYmap[zoneName][ISYkey]['messana'] == 'mEnergySaving':
                Key = ISYkey
        return(Key)  



    def zoneSetSetpoint(self, value,  zoneNbr):
        print('zoneSetSetpoint called for zone: ' + str(zoneNbr))
        
        status = self.pushZoneDataIndividual(zoneNbr, 'mSetpoint', value)
        return(status)

    def getZoneSetPointISYdriver(self, zoneNbr):
        print('getZoneSetpointISYdriver called for zone: '+str(zoneNbr))
        
        Key = ''
        zoneName = self.zoneID+str(zoneNbr)
        for ISYkey in self.ISYmap[zoneName]:
            if self.ISYmap[zoneName][ISYkey]['messana'] == 'mSetpoint':
                Key = ISYkey
        return(Key)  
  

    def zoneEnableSchedule(self, value, zoneNbr):
        print('zoneEnableSchedule called for zone: ' + str(zoneNbr))
        
        status = self.pushZoneDataIndividual(zoneNbr, 'mScheduleOn', value)
        return(status)


    def getZoneEnableScheduleISYdriver(self, zoneNbr):
        print('getZoneEnableScheduleISYdriver called for zone: '+str(zoneNbr))
        
        Key = ''
        zoneName = self.zoneID+str(zoneNbr)
        for ISYkey in self.ISYmap[zoneName]:
            if self.ISYmap[zoneName][ISYkey]['messana'] == 'mScheduleOn':
                Key = ISYkey
        return(Key) 

    def zonesetCurrentDPt(self, value,  zoneNbr):
        print('zonesetCurrentDPt called for zone: ' + str(zoneNbr))
        
        status = self.pushZoneDataIndividual(zoneNbr, 'mCurrentSetpointDP', value)
        return(status)

    def getZonesetCurrentDPtISYdriver(self, zoneNbr):
        print('getZonesetCurrentDPtISYdriver called for zone: '+str(zoneNbr))
        
        Key = ''
        zoneName = self.zoneID+str(zoneNbr)
        for ISYkey in self.ISYmap[zoneName]:
            if self.ISYmap[zoneName][ISYkey]['messana'] == 'mCurrentSetpointDP':
                Key = ISYkey
        return(Key)  

    def zonesetCurrentRH(self, value,  zoneNbr):
        print('zonesetCurrentRH called for zone: ' + str(zoneNbr))
        
        status = self.pushZoneDataIndividual(zoneNbr, 'mCurrentSetpointRH', value)
        return(status)

    def getZonesetCurrentRHISYdriver(self, zoneNbr):
        print('getZonesetCurrentRHISYdriver called for zone: '+str(zoneNbr))
        
        Key = ''
        zoneName = self.zoneID+str(zoneNbr)
        for ISYkey in self.ISYmap[zoneName]:
            if self.ISYmap[zoneName][ISYkey]['messana'] == 'mCurrentSetpointRH':
                Key = ISYkey
        return(Key)  

    def zonesetDehumDpt(self, value,  zoneNbr):
        print('zonesetDehumDpt called for zone: ' + str(zoneNbr))
        
        status = self.pushZoneDataIndividual(zoneNbr, 'mDehumSetpointDP', value)
        return(status)

    def getZonesetDehumDPtISYdriver(self, zoneNbr):
        print('getZonesetDehumDPtISYdriver called for zone: '+str(zoneNbr))
        Key = ''
        zoneName = self.zoneID+str(zoneNbr)
        for ISYkey in self.ISYmap[zoneName]:
            if self.ISYmap[zoneName][ISYkey]['messana'] == 'mDehumSetpointDP':
                Key = ISYkey
        return(Key)  

    def zonesetDehumRH(self, value,  zoneNbr):
        print('zonesetDehumRH called for zone: ' + str(zoneNbr))
        
        status = self.pushZoneDataIndividual(zoneNbr, 'mDehumSetpointRH', value)
        return(status)

    def getZonesetDehumRHISYdriver(self, zoneNbr):
        print('getZonesetDehumRHISYdriver called for zone: '+str(zoneNbr))
        Key = ''
        zoneName = self.zoneID+str(zoneNbr)
        for ISYkey in self.ISYmap[zoneName]:
            if self.ISYmap[zoneName][ISYkey]['messana'] == 'mDehumSetpointRH':
                Key = ISYkey
        return(Key)  

    def zonesetHumRH(self, value,  zoneNbr):
        print('zonesetHumRH called for zone: ' + str(zoneNbr))
        
        status = self.pushZoneDataIndividual(zoneNbr, 'mHumSetpointRH', value)
        return(status)

    def getZonesetHumRHISYdriver(self, zoneNbr):
        print('getZonesetHumRHISYdriver called for zone: '+str(zoneNbr))
        Key = ''
        zoneName = self.zoneID+str(zoneNbr)
        for ISYkey in self.ISYmap[zoneName]:
            if self.ISYmap[zoneName][ISYkey]['messana'] == 'mHumSetpointRH':
                Key = ISYkey
        return(Key)  

    def zonesetHumDpt(self, value,  zoneNbr):
        print('zonesetDehumDpt called for zone: ' + str(zoneNbr))
        
        status = self.pushZoneDataIndividual(zoneNbr, 'mHumSetpointDP', value)
        return(status)

    def getZonesetHumDPtISYdriver(self, zoneNbr):
        print('getZonesetDehumDPtISYdriver called for zone: '+str(zoneNbr))
        Key = ''
        zoneName = self.zoneID+str(zoneNbr)
        for ISYkey in self.ISYmap[zoneName]:
            if self.ISYmap[zoneName][ISYkey]['messana'] == 'mHumSetpointDP':
                Key = ISYkey
        return(Key)  

    def zonesetCO2 (self, value,  zoneNbr):
        print('zonesetDehumDpt called for zone: ' + str(zoneNbr))
        
        status = self.pushZoneDataIndividual(zoneNbr, 'mCO2', value)
        return(status)

    def getZonesetCO2ISYdriver(self, zoneNbr):
        print('getZonesetDehumDPtISYdriver called for zone: '+str(zoneNbr))
        Key = ''
        zoneName = self.zoneID+str(zoneNbr)
        for ISYkey in self.ISYmap[zoneName]:
            if self.ISYmap[zoneName][ISYkey]['messana'] == 'mCO2':
                Key = ISYkey
        return(Key)  

    def getZoneISYdriverInfo(self, mKey, zoneNbr):
        info = {}
        zoneStr = self.zoneID+str(zoneNbr)
        if mKey in self.setupFile['nodeDef'][zoneStr]['sts']:
            keys = list(self.setupFile['nodeDef'][zoneStr]['sts'][mKey].keys())
            info['driver'] = keys[0]
            tempData =  self.GETNodeData(self.zoneID, zoneNbr, mKey)
            if tempData['statusOK']:
                val = tempData['data']        
                if val in  ['Celcius', 'Fahrenheit']:
                    if val == 'Celcius':
                        val = 0
                    else:  
                        val = 1 
                info['value'] = val
            else:
                info['value'] = ''
            editor = self.setupFile['nodeDef'][zoneStr]['sts'][mKey][keys[0]]

            info['uom'] = self.setupFile['editors'][editor]['ISYuom']
        return(info)


    ###################################################################        
    #MacroZone

    def updateMacrozoneData(self,  level, macrozoneNbr):
        print('updatMacrozoneData: ' + str(macrozoneNbr))

        keys =[]
        if level == 'all':
            print('ALL update macrozone ' + str(macrozoneNbr))
            keys =  self.macrozonePullKeys(macrozoneNbr)
        elif level == 'active':
            print('ACTIVE update macrozone ' + str(macrozoneNbr))
            keys =  self.macrozoneActiveKeys(macrozoneNbr)
        
        self.dataOK = True
        for mKey in keys:
            self.data = self.pullMacrozoneDataIndividual(macrozoneNbr, mKey)
            self.dataOK = self.dataOK and self.data['statusOK']
        return(self.dataOK)


    def pullMacrozoneDataIndividual(self, macrozoneNbr, mKey): 
        print('pullMacroZoneDataIndividual: ' +str(macrozoneNbr)  + ' ' + mKey)    
        return(self.pullNodeDataIndividual(macrozoneNbr, self.macrozoneID, mKey))

    def pushMacrozoneDataIndividual(self, macrozoneNbr, mKey, value):
        print('pushMacroZoneDataIndividual: ' +str(macrozoneNbr)  + ' ' + mKey + ' ' + str(value))  
        return(self.pushNodeDataIndividual(macrozoneNbr, self.macrozoneID, mKey, value))

    def macrozonePullKeys(self, macrozoneNbr):
        print('macrozonePullKeys')
        return( self.getNodeKeys (macrozoneNbr, self.macrozoneID, 'GETstr'))

    def macrozonePushKeys(self, macrozoneNbr):
        print('macrozonePushKeys')
        return( self.getNodeKeys (macrozoneNbr, self.macrozoneID, 'PUTstr'))
  
    def macrozoneActiveKeys(self, macrozoneNbr):
        print('macrozoneActiveKeys')
        return( self.getNodeKeys (macrozoneNbr, self.macrozoneID, 'Active'))    

    def getMacrozoneCount(self):
        return(self.mSystem[self.systemID]['data']['mMacrozoneCount'])


    def getMacrozoneName(self, macroZoneNbr):
        tempName = self.pullNodeDataIndividual(macroZoneNbr, self.macrozoneID, 'mName')
        if tempName['statusOK']:
            return(tempName['data'])
        else:
            return('NA')

    def getMacrozoneCapability(self, macrozoneNbr): 
        print('getMacrozoneCapability')        
        self.getNodeCapability(self.macrozoneID, macrozoneNbr)

    def getMacrozoneAddress(self, macrozoneNbr):
        return(self.macrozoneID + str(macrozoneNbr))

    def getMacrozoneMessanaISYkey(self, ISYkey, macrozoneNbr):
        macrozoneName = self.macrozoneID+str(macrozoneNbr)
        return(self.ISYmap[macrozoneName][ISYkey]['messana'])

    def getMacrozoneISYValue(self, ISYkey, macrozoneNbr):
        macrozoneName = self.macrozoneID+str(macrozoneNbr)
        messanaKey = self.ISYmap[macrozoneName][ISYkey]['messana']
        try:
            data = self.pullMacrozoneDataIndividual(macrozoneNbr, messanaKey)
            if data['statusOK']:
                val = data['data']        
                if val in  ['Celcius', 'Fahrenheit']:
                    if val == 'Celcius':
                        val = 0
                    else:  
                        val = 1 
                systemValue = val
                status = True
            else:
                systemValue = None
                status = False
        except:
            status = False
            systemValue = None
        return (status, systemValue)


    def getMacrozoneISYdriverInfo(self, mKey, macrozoneNbr):
        info = {}
        macrozoneStr = self.macrozoneID+str(macrozoneNbr)
        if mKey in self.setupFile['nodeDef'][macrozoneStr]['sts']:
            keys = list(self.setupFile['nodeDef'][macrozoneStr]['sts'][mKey].keys())
            info['driver'] = keys[0]
            tempData =  self.GETNodeData(self.macrozoneID, macrozoneNbr, mKey)
            if tempData['statusOK']:
                val = tempData['data']        
                if val in  ['Celcius', 'Fahrenheit']:
                    if val == 'Celcius':
                        val = 0
                    else:  
                        val = 1 
                info['value'] = val
            else:
                info['value'] = ''
            editor = self.setupFile['nodeDef'][macrozoneStr]['sts'][mKey][keys[0]]

            info['uom'] = self.setupFile['editors'][editor]['ISYuom']
        return(info)

    def macrozoneSetStatus(self, value, macrozoneNbr):
        print(' macrozoneSetstatus called for zone: ' + str(macrozoneNbr))
        
        status = self.pushMacrozoneDataIndividual(macrozoneNbr, 'mStatus', value)
        return(status)
 

    def getMacrozoneStatusISYdriver(self, macrozoneNbr):
        print('getMacrozoneStatusISYdriver called for zone: '+str(macrozoneNbr))
        
        Key = ''
        macrozoneName = self.zoneID+str(macrozoneNbr)
        for ISYkey in self.ISYmap[macrozoneName]:
            if self.ISYmap[macrozoneName][ISYkey]['messana'] == 'mStatus':
                Key = ISYkey
        return(Key)  
        


    def macrozoneSetSetpoint(self, value,  macrozoneNbr):
        print('macrozoneSetSetpoint called for zone: ' + str(macrozoneNbr))
        
        status = self.pushMacrozoneDataIndividual(macrozoneNbr, 'mSetpoint', value)
        return(status)

    def getMacrozoneSetPointISYdriver(self, macrozoneNbr):
        print('getMacrozoneSetpointISYdriver called for zone: '+str(macrozoneNbr))
        
        Key = ''
        macrozoneName = self.zoneID+str(macrozoneNbr)
        for ISYkey in self.ISYmap[macrozoneName]:
            if self.ISYmap[macrozoneName][ISYkey]['messana'] == 'mSetpoint':
                Key = ISYkey
        return(Key)  
  

    def macrozoneEnableSchedule(self, value, macrozoneNbr):
        print('macrozoneEnableSchedule called for zone: ' + str(macrozoneNbr))
        
        status = self.pushMacrozoneDataIndividual(macrozoneNbr, 'mScheduleOn', value)
        return(status)


    def getMacrozoneEnableScheduleISYdriver(self, macrozoneNbr):
        print('getMacrozoneEnableScheduleISYdriver called for zone: '+str(macrozoneNbr))
        
        Key = ''
        macrozoneName = self.zoneID+str(macrozoneNbr)
        for ISYkey in self.ISYmap[macrozoneName]:
            if self.ISYmap[macrozoneName][ISYkey]['messana'] == 'mScheduleOn':
                Key = ISYkey
        return(Key) 






    ##############################################################
    # Hot Cold Change Over
    def updateHC_COData(self, HC_CONbr):
        print('updatHC_COData: ' + str(HC_CONbr))
        return(self.updateNodeData(HC_CONbr, self.HotColdcoID ))

    def getHC_COCapability(self, HC_CONbr): 
        print('getHC_COCapability')        
        self.getNodeCapability(self.HotColdcoID , HC_CONbr)

    def pullHC_CODataIndividual(self, HC_CONbr, mKey): 
        print('pullHC_CODataIndividual: ' +str(HC_CONbr)  + ' ' + mKey)    
        return(self.pullNodeDataIndividual(HC_CONbr, self.HotColdcoID , mKey))

    def pushHC_CODataIndividual(self, HC_CONbr, mKey, value):
        print('pushHC_CODataIndividual: ' +str(HC_CONbr)  + ' ' + mKey + ' ' + str(value))  
        return(self.pushNodeDataIndividual(HC_CONbr, self.HotColdcoID , mKey, value))

    def HcCoPullKeys(self, HC_CONbr):
        print('hc_coPullKeys')
        return( self.getNodeKeys (HC_CONbr, self.HotColdcoID , 'GETstr'))

    def hc_coPushKeys(self, HC_CONbr):
        print('hc_coPushKeys')
        return( self.getNodeKeys (HC_CONbr, self.HotColdcoID , 'PUTstr'))
  
    def hc_coActiveKeys(self, HC_CONbr):
        print('hc_coActiveKeys')
        return( self.getNodeKeys (HC_CONbr, self.HotColdcoID , 'Active'))    

    def getHotColdChangeOverCount(self):
        return(self.mSystem[ self.systemID]['data']['mhc_coCount'])

    ####################################################
    #ATU
    def updateATUData(self, atuNbr):
        print('updatATUData: ' + str(atuNbr))
        return(self.updateNodeData(atuNbr, self.atuID))
    '''
    def getATUCapability(self, atuNbr): 
        print('getATUCapability')               
        self.getNodeCapability(self.atuID, atuNbr)
    '''
    def getAtuCapability(self, atuNbr): 
        print('getAtuCapability')             
        self.getNodeCapability(self.atuID, atuNbr)

    def updateAtuData(self,  level, atuNbr):
        print('updateAtuData: ' + str(atuNbr))

        keys =[]
        if level == 'all':
            print('ALL update atu ' + str(atuNbr))
            keys =  self.atuPullKeys(atuNbr)
        elif level == 'active':
            print('ACTIVE update atu ' + str(atuNbr))
            keys =  self.atuActiveKeys(atuNbr)
        
        self.dataOK = True
        for mKey in keys:
            self.data = self.pullAtuDataIndividual(atuNbr, mKey)
            self.dataOK = self.dataOK and self.data['statusOK']
        return(self.dataOK)

    def getAtuMessanaISYkey(self, ISYkey, atuNbr):
        atuName = self.atuID+str(atuNbr)
        return(self.ISYmap[atuName][ISYkey]['messana'])

    def getAtuISYValue(self, ISYkey, atuNbr):
        atuName = self.atuID+str(atuNbr)
        messanaKey = self.ISYmap[atuName][ISYkey]['messana']
        try:
            data = self.pullAtuDataIndividual(atuNbr, messanaKey)
            if data['statusOK']:
                val = data['data']        
                if val in  ['Celcius', 'Fahrenheit']:
                    if val == 'Celcius':
                        val = 0
                    else:  
                        val = 1 
                systemValue = val
                status = True
            else:
                systemValue = None
                status = False
        except:
            status = False
            systemValue = None
        return (status, systemValue)


    def pullAtuDataIndividual(self, atuNbr, mKey): 
        print('pullAtuDataIndividual: ' +str(atuNbr)  + ' ' + mKey)    
        return(self.pullNodeDataIndividual(atuNbr, self.atuID, mKey))

    def pushAtuDataIndividual(self, ATUNbr, mKey, value):
        print('pushATUDataIndividual: ' +str(ATUNbr)  + ' ' + mKey + ' ' + str(value))  
        return(self.pushNodeDataIndividual(ATUNbr, self.atuID, mKey, value))

    def atuPullKeys(self, ATUNbr): 
        print('atusPullKeys')
        return( self.getNodeKeys (ATUNbr, self.atuID, 'GETstr'))

    def atuPushKeys(self, ATUNbr):
        print('atusPushKeys')
        return( self.getNodeKeys (ATUNbr, self.atuID, 'PUTstr'))
  
    def atuActiveKeys(self, ATUNbr):
        print('atusActiveKeys')
        return( self.getNodeKeys (ATUNbr, self.atuID, 'Active'))    
  
    def getAtuCount(self):
        return(self.mSystem[ self.systemID]['data']['mATUcount'])

    
    def getAtuName(self, atuNbr):
        tempName = self.pullNodeDataIndividual(atuNbr, self.atuID, 'mName')
        if tempName['statusOK']:
            return(tempName['data'])
        else:
            return('NA')
            
    def getAtuAddress(self, atuNbr):
        return(self.atuID + str(atuNbr))

    def getAtuISYdriverInfo(self, mKey, atuNbr):
        info = {}
        atuStr = self.atuID+str(atuNbr)
        if mKey in self.setupFile['nodeDef'][atuStr]['sts']:
            keys = list(self.setupFile['nodeDef'][atuStr]['sts'][mKey].keys())
            info['driver'] = keys[0]
            tempData =  self.GETNodeData(self.atuID, atuNbr, mKey)
            if tempData['statusOK']:
                val = tempData['data']        
                if val in  ['Celcius', 'Fahrenheit']:
                    if val == 'Celcius':
                        val = 0
                    else:  
                        val = 1 
                info['value'] = val
            else:
                info['value'] = ''
            editor = self.setupFile['nodeDef'][atuStr]['sts'][mKey][keys[0]]
            info['uom'] = self.setupFile['editors'][editor]['ISYuom']
        return(info)

    def atuSetStatus(self, value, atuNbr):
        print ('atuSetStatus not implemented yet')
        return(True)

    def getAtuStatusISYdriver(self, atuNbr):
        print ('getAtuStatusISYdriver not implemented yet')
        return(None)

    def atuSetEnergySave(self, value, atuNbr):
        print ('atuSetEnergySave not implemented yet')
        return(True)

    def getAtuEnergySaveISYdriver(self, atuNbr):
        print ('getAtuEnergySaveISYdriver not implemented yet')
        return(None) 

    def atuSetSetpoint(self, value, atuNbr):
        print ('atuSetSetpoint not implemented yet')
        return(True)

    def getAtuSetPointISYdriver(self, atuNbr):
        print ('getAtuSetPointISYdriver not implemented yet')
        return(None) 
        
    def atuEnableSchedule(self, value, atuNbr):
        print ('atuEnableSchedule not implemented yet')
        return(True)

    def getAtuEnableScheduleISYdriver(self, atuNbr):
        print ('getAtuEnableScheduleISYdriver not implemented yet')
        return(None) 


    #################################################################
    #Fan Coils
    def updateFanCoilData(self, FanCoilNbr):
        print('updatFanCoilData: ' + str(FanCoilNbr))
        return(self.updateNodeData(FanCoilNbr, self.fcID))

    def getFanCoilCapability(self, FanCoilNbr): 
        print('getFanCoilCapability')              
        self.getNodeCapability(self.fcID, FanCoilNbr)

    def pullFanCoilDataIndividual(self, FanCoilNbr, mKey): 
        print('pullFanCoilDataIndividual: ' +str(FanCoilNbr)  + ' ' + mKey)    
        return(self.pullNodeDataIndividual(FanCoilNbr, self.fcID, mKey))

    def pushFanCoilDataIndividual(self, FanCoilNbr, mKey, value):
        print('pushFanCoilDataIndividual: ' +str(FanCoilNbr)  + ' ' + mKey + ' ' + str(value))  
        return(self.pushNodeDataIndividual(FanCoilNbr, self.fcID, mKey, value))

    def fan_coilPullKeys(self, FanCoilNbr):
        print('fan_coilPullKeys')
        return( self.getNodeKeys (FanCoilNbr, self.fcID, 'GETstr'))

    def fan_coilPushKeys(self, FanCoilNbr):
        print('fan_coilPushKeys')
        return( self.getNodeKeys (FanCoilNbr, self.fcID, 'PUTstr'))
  
    def fan_coilActiveKeys(self, FanCoilNbr):
        print('fan_coilActiveKeys')
        return( self.getNodeKeys (FanCoilNbr, self.fcID, 'Active'))    
    
    def getFanCoilCount(self):
        return(self.mSystem[ self.systemID]['data']['mFanCoilCount'])

    #############################################################
    #EnergySources
    def updateEnergySourceData(self, EnergySourceNbr):
        print('updatEnergySourceData: ' + str(EnergySourceNbr))
        return(self.updateNodeData(EnergySourceNbr,  self.energySaveID))

    def getEnergySourceCapability(self, EnergySourceNbr): 
        print('getEnergySourceCapability')          
        self.getNodeCapability( self.energySaveID, EnergySourceNbr)

    def pullEnergySourceDataIndividual(self, EnergySourceNbr, mKey): 
        print('pullEnergySourceDataIndividual: ' +str(EnergySourceNbr)  + ' ' + mKey)    
        return(self.pullNodeDataIndividual(EnergySourceNbr,  self.energySaveID, mKey))

    def pushEnergySourceDataIndividual(self, EnergySourceNbr, mKey, value):
        print('pushEnergySourceDataIndividual: ' +str(EnergySourceNbr)  + ' ' + mKey + ' ' + str(value))  
        return(self.pushNodeDataIndividual(EnergySourceNbr,  self.energySaveID, mKey, value))

    def energy_sourcePullKeys(self, EnergySourceNbr):
        print('energy_sourcePullKeys')
        return( self.getNodeKeys (EnergySourceNbr,  self.energySaveID, 'GETstr'))

    def energy_sourcePushKeys(self, EnergySourceNbr):
        print('EnergySourcePushKeys')
        return( self.getNodeKeys (EnergySourceNbr,  self.energySaveID, 'PUTstr'))
  
    def energy_sourceActiveKeys(self, EnergySourceNbr):
        print('energy_sourceActiveKeys')
        return( self.getNodeKeys (EnergySourceNbr,  self.energySaveID, 'Active'))    
    
    def getenergySourceCount(self):
        return(self.mSystem[ self.systemID]['data']['mEnergySourceCount'])

    #####################################################
    #Buffer Tank
    def updateBufferTankData(self, BufferTankNbr):
        print('updatBufferTankData: ' + str(BufferTankNbr))
        return(self.updateNodeData(BufferTankNbr, self.bufferTankID))

    def getBufferTankCapability(self, BufferTankNbr): 
        print('getBufferTankCapability')              
        self.getNodeCapability(self.bufferTankID, BufferTankNbr)


    def pullBufferTankDataIndividual(self, BufferTankNbr, mKey): 
        print('pullBufferTankDataIndividual: ' +str(BufferTankNbr)  + ' ' + mKey)    
        return(self.pullNodeDataIndividual(BufferTankNbr, self.bufferTankID, mKey))

    def pushBufferTankDataIndividual(self, BufferTankNbr, mKey, value):
        print('pushBufferTankDataIndividual: ' +str(BufferTankNbr)  + ' ' + mKey + ' ' + str(value))  

        if mKey == 'mStatus':
            BTdata = {}
            BTdata = self.pullNodeDataIndividual(BufferTankNbr, self.bufferTankID, 'mMode')
            if BTdata['data'] != 0:
                return(self.pushNodeDataIndividual(BufferTankNbr, self.bufferTankID, mKey, value))
            else:
                print('Mode = 0, Cannot set status if mode = 0')
                return(False)
        else:
             return(self.pushNodeDataIndividual(BufferTankNbr, self.bufferTankID, mKey, value))

    def buffer_tankPullKeys(self, BufferTankNbr):
        print('buffer_tankPullKeys')
        return( self.getNodeKeys (BufferTankNbr, self.bufferTankID, 'GETstr'))

    def buffer_tankPushKeys(self, BufferTankNbr):
        print('buffer_tankPushKeys')
        return( self.getNodeKeys (BufferTankNbr, self.bufferTankID, 'PUTstr'))
  
    def buffer_tankActiveKeys(self, BufferTankNbr):
        print('buffer_tankActiveKeys')
        return( self.getNodeKeys (BufferTankNbr, self.bufferTankID, 'Active'))    
    
    def getBufferTankCount(self):
        return(self.mSystem[ self.systemID]['data']['mBufTankCount'])

        #Domestic Hot Water
 
    ##################################################################
    # Domestic Hot Water
    def updateDHWData(self, DHWNbr):
        print('updatDHWData: ' + str(DHWNbr))
        return(self.updateNodeData(DHWNbr, self.dhwID))

    def getDHWCapability(self, DHWNbr): 
        print('getDHWCapability')                      
        self.getNodeCapability(self.dhwID, DHWNbr)

    def pullDHWDataIndividual(self, DHWNbr, mKey): 
        print('pullDHWDataIndividual: ' +str(DHWNbr)  + ' ' + mKey)    
        return(self.pullNodeDataIndividual(DHWNbr, self.dhwID, mKey))

    def pushDHWDataIndividual(self, DHWNbr, mKey, value):
        print('pushDHWDataIndividual: ' +str(DHWNbr)  + ' ' + mKey + ' ' + str(value))  
        return(self.pushNodeDataIndividual(DHWNbr, self.dhwID, mKey, value))


    def DHWPullKeys(self, DHWNbr):
        print('DHWPullKeys')
        return( self.getNodeKeys (DHWNbr, self.dhwID, 'GETstr'))

    def DHWPushKeys(self, DHWNbr):
        print('DHWPushKeys')
        return( self.getNodeKeys (DHWNbr, self.dhwID, 'PUTstr'))
  
    def DHWActiveKeys(self, DHWNbr):
        print('DHWActiveKeys')
        return( self.getNodeKeys (DHWNbr, self.dhwID, 'active'))    

    def getDomesticHotWaterCount(self):
        return(self.mSystem[ self.systemID]['data']['mDHWcount'])


    
