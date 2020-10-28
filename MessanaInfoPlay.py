#!/usr/bin/env python3
import requests
from subprocess import call
import json
from collections import defaultdict
import pickle

#LOGGER = polyinterface.LOGGER

class MessanaInfo:
    def __init__ (self, mIPaddress, mAPIKeyVal):
        self.mSystem = defaultdict(dict)
        self.mSystem = {'system': {  'ISYnode':{ 'nlsICON' :'Thermostat'
                                                ,'sends'   : ['DON', 'DOF']
                                                ,'accepts' : {'UPDATE'        : ''
                                                            ,'SET_STATUS'     : 'mStatus'
                                                            ,'SET_ENERGYSAVE' : 'mEnergySaving'
                                                            ,'SET_SETBACK'    : 'mSetback'}}
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
                                                     'ISYuom': 107
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
                                                     'ISYuom': 107
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
                                                     'ISYuom': 107
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
                                                     'ISYuom': 107
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
                                                     'ISYuom': 107
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
                                                     'ISYuom': 107
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
                                        ,'mHC_changeoverCount':{
                                             'GETstr':'/api/system/HCgroupCount/'
                                            ,'PUTstr': None 
                                            ,'Active': None                                       
                                            ,'ISYeditor':{   
                                                     'ISYuom': 107
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
                                                     'ISYuom': 107
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
                                                    ,'nlsValues' : {0:'F', 1:'C'}
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
                                                    ,'nlsValues' : { 0:'Off', 1:'On' }
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
                                                    ,'nlsValues' : { 0:'Off',  1:'On' }
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
                                         
                        },
                        'zones': {   'ISYnode':{'nlsICON':'TempSensor'
                                                ,'sends'   : []
                                                ,'accepts' : {'SET_SETPOINT'   : 'mSetPoint'
                                                             ,'SET_STATUS'     : 'mStatus'
                                                             ,'SET_ENERGYSAVE' : 'mEnergySaving'
                                                             ,'SET_SCHEDULEON' : 'mScheduleOn'}}
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
                                        ,'mSetPoint' :{
                                             'GETstr': '/api/zone/setpoint/'
                                            ,'PUTstr': '/api/zone/setpoint/'
                                            ,'Active': None 
                                            ,'ISYeditor':{   
                                                     'ISYuom':17
                                                    ,'ISYmin':40
                                                    ,'ISYmax':120
                                                    ,'ISYsubset':None
                                                    ,'ISYstep':1
                                                    ,'ISYprec':0 }
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
                                        ,'mHumSetPointRH': { 
                                             'GETstr': '/api/zone/humidSetpointRH/'
                                            ,'PUTstr': '/api/zone/humidSetpointRH/'
                                            ,'Active': None 
                                            ,'ISYeditor':{   
                                                     'ISYuom':107
                                                    ,'ISYmin':0
                                                    ,'ISYmax':1000
                                                    ,'ISYsubset':None
                                                    ,'ISYstep':1
                                                    ,'ISYprec':0 }
                                            , 'ISYnls': {    
                                                     'nlsTEXT' : 'Hum Set Point RH'  
                                                    ,'nlsValues' : None 
                                                        }
                                                    }
                                        ,'mHumSetPointDP': { 
                                             'GETstr': '/api/zone/humidSetpointDP/'
                                            ,'PUTstr': '/api/zone/humidSetpointDP/'
                                            ,'Active': None 
                                            ,'ISYeditor':{   
                                                     'ISYuom':107
                                                    ,'ISYmin':0
                                                    ,'ISYmax':1000
                                                    ,'ISYsubset':None
                                                    ,'ISYstep':1
                                                    ,'ISYprec':0 }
                                            , 'ISYnls': {    
                                                     'nlsTEXT' : 'Hum Set Point DP'  
                                                    ,'nlsValues' : None 
                                                        }
                                                    }
                                        ,'mDehumSetPointRH':{ 
                                             'GETstr': '/api/zone/dehumSetpointRH/'
                                            ,'PUTstr': '/api/zone/dehumSetpointRH/'
                                            ,'Active': None 
                                            ,'ISYeditor':{   
                                                     'ISYuom':107
                                                    ,'ISYmin':0
                                                    ,'ISYmax':1000
                                                    ,'ISYsubset':None
                                                    ,'ISYstep':1
                                                    ,'ISYprec':0 }
                                            , 'ISYnls': {    
                                                     'nlsTEXT' : 'DeHum Set Point RH'  
                                                    ,'nlsValues' : None 
                                                        }
                                                    }
                                        ,'mDehumSetPointDP': { 
                                             'GETstr': '/api/zone/dehumSetpointDP/'
                                            ,'PUTstr': '/api/zone/dehumSetpointDP/'
                                            ,'Active': None 
                                            ,'ISYeditor':{   
                                                     'ISYuom':107
                                                    ,'ISYmin':0
                                                    ,'ISYmax':1000
                                                    ,'ISYsubset':None
                                                    ,'ISYstep':1
                                                    ,'ISYprec':0 }
                                            , 'ISYnls': {    
                                                     'nlsTEXT' : 'DeHum Set Point DP'  
                                                    ,'nlsValues' : None 
                                                        }
                                                    }
                                        ,'mCurrentSetPointRH': { 
                                             'GETstr': '/api/zone/currentSetpointRH/'
                                            ,'PUTstr': None
                                            ,'Active': '/api/zone/currentSetpointRH/'
                                            ,'ISYeditor':{   
                                                     'ISYuom':107
                                                    ,'ISYmin':0
                                                    ,'ISYmax':1000
                                                    ,'ISYsubset':None
                                                    ,'ISYstep':1
                                                    ,'ISYprec':0 }
                                            , 'ISYnls': {    
                                                     'nlsTEXT' : 'Current Set Point RH'  
                                                    ,'nlsValues' : None 
                                                        }
                                                    }
                                        ,'mCurrentSetPointDP': { 
                                             'GETstr': '/api/zone/currentSetpointDP/'
                                            ,'PUTstr': None
                                            ,'Active': '/api/zone/currentSetpointDP/' 
                                            ,'ISYeditor':{   
                                                     'ISYuom':107
                                                    ,'ISYmin':0
                                                    ,'ISYmax':1000
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
                                            ,'Active': '/api/zone/humidity/' 
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
                                            ,'Active': '/api/zone/dewpoint/'
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
                                                    ,'ISYstep':1
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
                                                     'ISYuom':107
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
                                                     'ISYuom':107
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
                                                     'ISYuom':107
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
                                                     'ISYuom':107
                                                    ,'ISYmin':0
                                                    ,'ISYmax':40
                                                    ,'ISYsubset':None
                                                    ,'ISYstep':1
                                                    ,'ISYprec':0 }
                                            , 'ISYnls': {    
                                                     'nlsTEXT' : 'MAcro Zone member'  
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
                                            ,'Active': None 
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
                                    ,'NOcapability' : {}
                        },
                        'macrozones' : {   'ISYnode':{   'nlsICON' :'TempSensor'
                                                        ,'sends'   : []
                                                        ,'accepts' : {'UPDATE'        : ''
                                                                    ,'SET_STATUS'     : 'mStatus'
                                                                    ,'SET_ENERGYSAVE' : 'mEnergySaving'
                                                                    ,'SET_SETBACK'    : 'mSetback'}}
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
                                        ,'mSetPoint': {
                                              'GETstr':'/api/macrozone/setpoint/'
                                             ,'PUTstr':'/api/macrozone/setpoint/'
                                             ,'Active': None 
                                             ,'ISYeditor':{   
                                                     'ISYuom':17
                                                    ,'ISYmin':40
                                                    ,'ISYmax':120
                                                    ,'ISYsubset':None
                                                    ,'ISYstep':1
                                                    ,'ISYprec':0 }
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
                                                     'nlsTEXT' : 'Macro Zone state'
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
                                                    ,'nlsValues' : { 0:'Off', 1:'On' }
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
                                    ,'NOcapability' : {}
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
                                            'active':None
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
        
        '''
        self.setupStruct = {'nodeDef': nodeNbr: { 'nodeDef':{}
                                            ,'sts':{}
                                            ,'cmds':{
                                                    'sends':{}
                                                    ,'accepts':{}
                                                    } 
                                            }
                                }
                    ,'editors':{id:Name, range:{}}
                    ,'nls':{}
                        }
        '''
        self.nodeCount = 0
        self.setupFile = { 'nodeDef':{}
                            ,'editors':{}
                            ,'nls':{}}



        #self.APIKeyVal = '9bf711fc-54e2-4387-9c7f-991bbb02ab3a'
        #self.IP = '192.168.2.65'    

        self.APIKey = 'apikey'
        self.APIKeyVal = mAPIKeyVal
        self.APIStr = self.APIKey + '=' + self.APIKeyVal

        self.IP ='http://'+ mIPaddress

        self.RESPONSE_OK = '<Response [200]>'
        self.RESPONSE_NO_SUPPORT = '<Response [400]>'
        self.RESPONSE_NO_RESPONSE = '<Response [404]>'

        self.zoneCapability = {}
        self.atuCapability = {}
        
        self.updateSystemData()
        self.addSystemDefStruct('system')
        for zoneNbr in range(0,self.mSystem['system']['data']['mZoneCount']):
            self.getZoneCapability(zoneNbr)
            self.updateZoneData(zoneNbr)
            zoneName = 'zone'+str(zoneNbr) # why do we need an extra  level of nbr?
            self.addNodeDefStruct(zoneNbr, 'zones', zoneName )
       
        for macrozoneNbr in range(0,self.mSystem['system']['data']['mMacrozoneCount']):
            self.getMacrozoneCapability(macrozoneNbr)
            self.updateMacroZoneData(macrozoneNbr)
            macrozoneName = 'macrozone'+str(macrozoneNbr)
            self.addNodeDefStruct(macrozoneNbr, 'macrozones', macrozoneName )

        #more modules mnissing 

        self.createSetupFiles('./profile/nodedef/nodeTest.xml','./profile/editor/editorTest.xml', './profile/nls/en_us.txt')

        '''
        print ('Reading Messana System')
        #self.pullAllMessanaStatus()
        print('Finish Reading Messana system')
        '''
    def init(self):

        return(True)

    def getSystemISYdriverInfo(self, mKey):
        info = {}
        keys = list(self.setupFile['system']['nodeDef']['sts'][mKey].keys())
        info['driver'] = keys[0]
        tempData =  self.GETSystem(mKey)
        if tempData['statusOK']:
            info['value'] = tempData['data']
        info['uom'] = self.setupFile['system']['editors']['ISYoum']
        return(info)


    def addNodeDefStruct(self, NodeNbr, NodeName, nodeId):
        self.keyCount = 0
        nodeId.lower()

        self.name = nodeId+'_'+str(NodeNbr)
        self.nlsKey = 'nls' + self.name
        self.nlsKey.lower()
        #editorName = nodeName+'_'+str(keyCount)
        self.setupFile['nodeDef'][self.name]={}
        self.setupFile['nodeDef'][self.name]['CodeId'] = nodeId
        self.setupFile['nodeDef'][self.name]['nlsId'] = self.nlsKey
        self.setupFile['nodeDef'][self.name]['nlsNAME']=self.mSystem[NodeName]['data'][NodeNbr]['mName']
        self.setupFile['nodeDef'][self.name]['nlsICON']=self.mSystem[NodeName]['ISYnode']['nlsICON']
        self.setupFile['nodeDef'][self.name]['sts']={}

        for mKey in self.mSystem[NodeName]['data'][NodeNbr]: 
            #make check if system has unit installed
            if self.mSystem[NodeName]['KeyInfo'][mKey]['ISYeditor']['ISYuom']:
                self.keyCount = self.keyCount + 1
                editorName = NodeName.upper()+str(NodeNbr)+'_'+str(self.keyCount)
                nlsName = editorName
                ISYvar = 'GV'+str(self.keyCount)
                self.setupFile['nodeDef'][self.name]['sts'][mKey]={ISYvar:editorName}
                self.setupFile['editors'][editorName]={}
                #self.setupFile['nls'][editorName][ISYparam]
                for ISYparam in self.mSystem[NodeName]['KeyInfo'][mKey]['ISYeditor']:
                    if self.mSystem[NodeName]['KeyInfo'][mKey]['ISYeditor'][ISYparam]!= None:
                        self.setupFile['editors'][editorName][ISYparam]=self.mSystem[NodeName]['KeyInfo'][mKey]['ISYeditor'][ISYparam]

                if self.mSystem[NodeName]['KeyInfo'][mKey]['ISYnls']:
                    self.setupFile['nls'][nlsName]={}
                for ISYnls in self.mSystem[NodeName]['KeyInfo'][mKey]['ISYnls']:
                    print ( mKey + ' ' + ISYnls)
                    if  self.mSystem[NodeName]['KeyInfo'][mKey]['ISYnls'][ISYnls]:      
                        self.setupFile['nls'][nlsName][ISYnls] = self.mSystem[NodeName]['KeyInfo'][mKey]['ISYnls'][ISYnls]
                        if ISYnls == 'nlsValues':
                            self.setupFile['editors'][editorName]['nlsKey'] = nlsName 

        self.setupFile['nodeDef'][self.name]['cmds']= {}
        if 'accepts' in self.mSystem[NodeName]['ISYnode']:
            self.setupFile['nodeDef'][self.name]['cmds']['accepts']={}
            for key in  self.mSystem[NodeName]['ISYnode']['accepts']:
                if self.mSystem[NodeName]['ISYnode']['accepts'][key] in self.setupFile['nodeDef'][self.name]['sts']:
                    self.setupFile['nodeDef'][self.name]['cmds']['accepts'][key]= self.setupFile['nodeDef'][self.name]['sts'][self.mSystem[NodeName]['ISYnode']['accepts'][key]]
                else:
                    self.setupFile['nodeDef'][self.name]['cmds']['accepts'][key]= {}
        if 'sends' in self.mSystem[NodeName]['ISYnode']:         
            self.setupFile['nodeDef'][self.name]['cmds']['sends'] = self.mSystem[NodeName]['ISYnode']['sends']                                 
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
            print ('Unknown name: ' + nodeId)
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
                print (messanaKey + 'not defined')
        return() 


    def addSystemSendComand(self, idName):
        if 'sends' in self.setupFile['nodeDef']['system']['cmds']:
            self.setupFile['nodeDef']['system']['cmds']['sends'].append(idName)
        else:
            self.setupFile['nodeDef']['system']['cmds']['sends']=[]
            self.setupFile['nodeDef']['system']['cmds']['sends'].append(idName)
        return()
   
    def addSystemAcceptComand(self, functionName, messanaKey):
        if len(messanaKey) == 0:
            if 'accepts' in self.setupFile['nodeDef']['system']['cmds']:
                self.setupFile['nodeDef']['system']['cmds']['accepts'][functionName] = {}
            else:
                self.setupFile['nodeDef']['system']['cmds']['accepts'] = {}
                self.setupFile['nodeDef']['system']['cmds']['accepts'][functionName] = {}
        else:
            if not('accepts' in self.setupFile['nodeDef']['system']['cmds']):
                self.setupFile['nodeDef']['system']['cmds']['accepts'] = {}
            if messanaKey in self.setupFile['nodeDef']['system']['sts']:
                self.setupFile['nodeDef']['system']['cmds']['accepts'][functionName] = self.setupFile['nodeDef']['system']['sts'][messanaKey]
            else:
                print (messanaKey + 'not defined')
        return() 

    '''
    def getSystemDriver(self, driverKey):
        tempDict= {}
        if driverKey in  self.setupFile['nodeDef']['system']['sts']:
            tempDict = self.setupFile['nodeDef']['system']['sts'][driverKey]
            if len(tempDict) == 1:
            else:
                print('Error more than one element associated with :' + driverKey)
        else:
            print(driverKet + ' not found')
        return(tempDict)
    '''
    def addSystemDefStruct(self, nodeId):
        self.keyCount = 0
        nodeId.lower()
        self.nlsKey= 'nls' + nodeId
        self.nlsKey.lower()
        self.setupFile['nodeDef']['system']={}
        self.setupFile['nodeDef']['system']['CodeId'] = nodeId
        self.setupFile['nodeDef']['system']['nlsId'] = self.nlsKey
        self.setupFile['nodeDef']['system']['nlsNAME']=self.mSystem['system']['data']['mName']
        self.setupFile['nodeDef']['system']['nlsICON']=self.mSystem['system']['ISYnode']['nlsICON']
        self.setupFile['nodeDef']['system']['sts']={}

        for mKey in self.mSystem['system']['data']: 
            #make check if system has unit installed
            if self.mSystem['system']['KeyInfo'][mKey]['ISYeditor']['ISYuom']:
                if ((self.mSystem['system']['KeyInfo'][mKey]['ISYeditor']['ISYuom'] == 107
                   and self.mSystem['system']['data'][mKey] != 0)
                   or self.mSystem['system']['KeyInfo'][mKey]['ISYeditor']['ISYuom'] != 107):
                    self.keyCount = self.keyCount + 1
                    editorName = 'SYSTEM_'+str(self.keyCount)
                    nlsName = editorName
                    ISYvar = 'GV'+str(self.keyCount)
                    self.setupFile['nodeDef']['system']['sts'][mKey]={ISYvar:editorName}
                    self.setupFile['editors'][editorName]={}
                    #self.setupFile['nls'][editorName][ISYparam]
                    for ISYparam in self.mSystem['system']['KeyInfo'][mKey]['ISYeditor']:
                        if self.mSystem['system']['KeyInfo'][mKey]['ISYeditor'][ISYparam]!= None:
                            self.setupFile['editors'][editorName][ISYparam]=self.mSystem['system']['KeyInfo'][mKey]['ISYeditor'][ISYparam]

                    if self.mSystem['system']['KeyInfo'][mKey]['ISYnls']:
                        self.setupFile['nls'][nlsName]={}
                    for ISYnls in self.mSystem['system']['KeyInfo'][mKey]['ISYnls']:
                        print ( mKey + ' ' + ISYnls)
                        if  self.mSystem['system']['KeyInfo'][mKey]['ISYnls'][ISYnls]:      
                            self.setupFile['nls'][nlsName][ISYnls] = self.mSystem['system']['KeyInfo'][mKey]['ISYnls'][ISYnls]
                            if ISYnls == 'nlsValues':
                                self.setupFile['editors'][editorName]['nlsKey'] = nlsName
        
        self.setupFile['nodeDef']['system']['cmds']={}
        if 'accepts' in self.mSystem['system']['ISYnode']:
            self.setupFile['nodeDef']['system']['cmds']['accepts'] = {}
            for key in  self.mSystem['system']['ISYnode']['accepts']:
                if self.mSystem['system']['ISYnode']['accepts'][key] in self.setupFile['nodeDef']['system']['sts']:
                    mVal = self.mSystem['system']['ISYnode']['accepts'][key]
                    self.setupFile['nodeDef']['system']['cmds']['accepts'][key]= self.setupFile['nodeDef']['system']['sts'][mVal]
                else:
                    self.setupFile['nodeDef']['system']['cmds']['accepts'][key]= {}   
        if 'sends' in self.mSystem['system']['ISYnode']:
            self.setupFile['nodeDef']['system']['cmds']['sends']=self.mSystem['system']['ISYnode']['sends']                              
        return()




    def getNodeCapability (self, nodeKey, nodeNbr):     
        self.keyList = {}
        if 'mCapability' in self.mSystem[nodeKey]['KeyInfo']:
            if 'GETstr' in self.mSystem[nodeKey]['KeyInfo']['mCapability']:
                GETStr =self.IP+self.mSystem[nodeKey]['KeyInfo']['mCapability']['GETstr']+str(nodeNbr)+'?'+ self.APIStr 
                Nodep = requests.get(GETStr)
                if str(Nodep) == self.RESPONSE_OK:
                    tempKeys= Nodep.json()
                    for key in tempKeys:
                        if key == 'operative_temperature':
                            if tempKeys[key] == 0:
                                self.keyList['mTemp'] = tempKeys["operative_temperature"]
                                self.keyList['mSetPoint'] = tempKeys["operative_temperature"]
                        elif key == 'air_temperature':
                            self.keyList['mAirTemp'] = tempKeys["air_temperature"]
                        elif key == 'relative_humidity':
                            self.keyList['mHumidSetpointRH'] = tempKeys["relative_humidity"]
                            self.keyList['mHumidSetpointDP'] = tempKeys["relative_humidity"]
                            self.keyList['mDehumSetpointRH'] = tempKeys["relative_humidity"]
                            self.keyList['mDehumSetpointDP'] = tempKeys["relative_humidity"]
                            self.keyList['mCurrentSetpointRH'] = tempKeys["relative_humidity"]
                            self.keyList['mCurrentSetpointDP'] = tempKeys["relative_humidity"]
                            self.keyList['mHumidity'] = tempKeys["relative_humidity"]
                        elif key == 'dewpoint':
                            self.keyList['mDewPoint'] = tempKeys["relative_humidity"]
                        elif key == 'co2':
                            self.keyList['mCO2'] = tempKeys['co2'] 
                            self.keyList['mAirQuality'] = tempKeys['co2']            
                        elif key == 'voc':
                            self.keyList['mVoc'] = tempKeys['voc']   
                        else:
                            print(key + ' unknown keyword')
        self.mSystem[nodeKey]['NOcapability'][nodeNbr] = self.keyList
       
    
    def GETSystem(self, mKey):
        sysData= {}
        print('GETSystem: ' + mKey )
        GETStr = self.IP+self.mSystem['system']['KeyInfo'][mKey]['GETstr'] + '?' + self.APIStr 
        #print( GETStr)
        try:
            systemTemp = requests.get(GETStr)
            print(str(systemTemp))
            if str(systemTemp) == self.RESPONSE_OK:
                systemTemp = systemTemp.json()
                #print(systemTemp)
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
            if mKey in self.mSystem['system']['KeyInfo']:
                if self.mSystem['system']['KeyInfo'][mKey]['PUTstr']:
                    PUTStr = self.IP+self.mSystem['system']['KeyInfo'][mKey]['PUTstr']
                    if PUTStr == None:
                        sysData['statusOK'] = False
                        sysData['error'] = 'Not able to PUT Key: : '+ mKey + ' value:' + str( value )
                        print(sysData)    
                        return(sysData)   
                    #print(PUTStr)
            mData = {'value':value, self.APIKey : self.APIKeyVal}
            #mHeaders = { 'accept': 'application/json' , 'Content-Type': 'application/json' }
            #print(mData)
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
        print('GETNodeData: ' + mNodeKey + ' ' + str(nodeNbr)+ ' ' + mKey)
        nodeData = {}
        if 'NOcapability' in self.mSystem[mNodeKey]:
            if self.mSystem[mNodeKey]['NOcapability'][nodeNbr]:
                if  mKey in self.mSystem[mNodeKey]['NOcapability'][nodeNbr]:
                    nodeData['error'] = 'Does not support keyword: ' + mKey
                    nodeData['statusOK'] =False
                    return (nodeData)
        if 'GETstr' in self.mSystem[mNodeKey]['KeyInfo'][mKey]:
            GETStr =self.IP+self.mSystem[mNodeKey]['KeyInfo'][mKey]['GETstr']+str(nodeNbr)+'?'+ self.APIStr 
            Nodep = requests.get(GETStr)
            if str(Nodep) == self.RESPONSE_OK:
                Nodep = Nodep.json()
                nodeData['data']  = Nodep[str(list(Nodep.keys())[0])] 
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

    def getNodeKeys (self, NodeNbr, NodeKey, cmdKey):
        keys = []
        if self.mSystem[NodeKey]['data']:
            if NodeNbr in self.mSystem[NodeKey]['data']: 
                for mKey in self.mSystem[NodeKey]['data'][NodeNbr]:
                    if mKey in self.mSystem[NodeKey]['KeyInfo'][mKey][cmdKey]:
                        if not(mKey in keys):
                            keys.append(mKey)
            else:
                self.updateNodeData(NodeNbr, NodeKey)
                for mKey in self.mSystem[NodeKey]['data'][NodeNbr]:
                    if mKey in self.mSystem[NodeKey]['KeyInfo'][mKey][cmdKey]:
                        if not(mKey in keys):
                            keys.append(mKey)
        else:
            print('No Keys found - trying to fetch Messana data')
            self.updateSystemData()
            self.updateNodeData(NodeNbr, NodeKey)
            if self.mSystem[NodeKey]['data']:
                for mKey in self.mSystem[NodeKey]['data'][NodeNbr]:
                    if mKey in self.mSystem[NodeKey]['KeyInfo']:
                        if not(mKey in keys):
                            keys.append(mKey)
            else:
                print('No '+ NodeKey + ' present')
        if 'NOcapabiility' in self.mSystem[NodeKey]:
            if self.mSystem[NodeKey]['NOcapability']:
                if NodeNbr in self.mSystem[NodeKey]['NOcapability']:
                    for mKey in keys:
                        if mKey in self.mSystem[NodeKey]['NOcapability'][NodeNbr]:
                            keys.remove(mKey)                            
        return(keys)

    def updateNodeData(self, NodeNbr, NodeKey):
        print('updatNodeData: ' + str(NodeNbr) + ' ' + NodeKey)
        Data = {}
        dataOK = True
        for mKey in self.mSystem[NodeKey]['KeyInfo']:
            #print ('GET ' + mKey + ' in zone ' + str(NodeNbr))
            Data = self.pullNodeDataIndividual(NodeNbr, NodeKey,  mKey)
            if not(Data['statusOK']):
                dataOK = False
                #print ('Error GET' + Data['error'])
        return(dataOK)
    
    def pullNodeDataIndividual(self, NodeNbr, NodeKey, mKey): 
        Data = {} 
        print('pullNodeDataIndividual: ' +str(NodeNbr)  + ' ' + mKey)    
        if mKey in mKey in self.mSystem[NodeKey]['KeyInfo']:
            Data = self.GETNodeData(NodeKey, NodeNbr, mKey)
        else:
            Data['statusOK'] = False
            Data['error'] = mKey +' is not a supported GETstr command'
        return(Data)    

    def pushNodeDataIndividual(self, NodeNbr, NodeKey, mKey, value):
        print('pushZoneDataIndividual: ' +str(NodeNbr)  + ' ' + mKey + ' ' + str(value))  
        zoneData = {}
        zoneData= self.PUTNodeData(NodeKey, NodeNbr, mKey, value)
        if zoneData['statusOK']:
            return(True)
        else:
            print(zoneData['error'])
            return(False)

    #Setup file generation 
    def createSetupFiles(self, nodeDefFileName, editorFileName, nlsFileName):
        status = True
        try:
            nodeFile = open(nodeDefFileName, 'w+')
            editorFile = open(editorFileName, 'w+')
            nlsFile = open(nlsFileName, 'w+')
            editorFile.write('<editors> \n')
            nodeFile.write('<nodeDefs> \n')
            for node in self.setupFile['nodeDef']:
                nodeDefStr ='   <nodeDef id="' + self.setupFile['nodeDef'][node]['CodeId']+'" '+ 'nls="'+self.setupFile['nodeDef'][node]['nlsId']+'">\n'
                #print(nodeDefStr)
                nodeFile.write(nodeDefStr)
                nodeFile.write('      <sts>\n')
                nlsStr = 'ND-'+self.setupFile['nodeDef'][node]['CodeId']+'-NAME = '+self.setupFile['nodeDef'][node]['nlsNAME']+ '\n'
                nlsFile.write(nlsStr)
                nlsStr = 'ND-'+self.setupFile['nodeDef'][node]['CodeId']+'-ICON = '+self.setupFile['nodeDef'][node]['nlsICON']+ '\n'
                nlsFile.write(nlsStr)
                for status in self.setupFile['nodeDef'][node]['sts']:
                    for statusId in self.setupFile['nodeDef'][node]['sts'][status]:
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
                        editorStr = editorStr + ' >\n'
                        #print (editorStr)
                        editorFile.write(editorStr)
                        editorFile.write('</editor>\n')

                        for nlsInfo in self.setupFile['nls'][nodeName]:
                            if nlsInfo == 'nlsTEXT':
                                nlsStr = 'ST-' + self.setupFile['nodeDef'][node]['nlsId']+'-'+nodeName+'-NAME = '
                                nlsStr = nlsStr + self.setupFile['nls'][nodeName][nlsInfo] + '\n'
                                nlsFile.write(nlsStr)
                            elif nlsInfo == 'nlsValues':
                                nlsValues = 0
                                for key in self.setupFile['nls'][nodeName][nlsInfo]:
                                    nlsStr = nlsEditorKey+'-'+str(nlsValues)+'='+self.setupFile['nls'][nodeName][nlsInfo][key]+'\n'
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
                            cmdStr = '            <cmd id="' +acceptCmd+'" /> \n'        
                            #print(cmdStr)
                            nodeFile.write(cmdStr)
                            if self.setupFile['nodeDef'][node]['cmds']['accepts'][acceptCmd] != {}:
                                cmdStr = '               <p id="" editor="'
                                for key in self.setupFile['nodeDef'][node]['cmds']['accepts'][acceptCmd]:
                                    cmdStr = cmdStr + self.setupFile['nodeDef'][node]['cmds']['accepts'][acceptCmd][key]+ '" init="' + key +'"/> \n' 
                                #print(cmdStr)                              
                                nodeFile.write(cmdStr)
                                nodeFile.write('            </cmd> \n')
                nodeFile.write('         </accepts>\n')                   

                nodeFile.write('      </cmds>\n')                
                                 
                nodeFile.write('</nodeDef> \n')

            nodeFile.write('</nodeDefs> \n' )
            nodeFile.close()
            editorFile.write('</editors> \n')
            editorFile.close()
            nlsFile.close()
        except:
            print('something went wrong in creating setup files')
            status = False
        return(status)

    def createNodedeFile(self, fileName):
        file = open(fileName, 'w+')
        file.close()
        return()

    def createNLSFile(self, fileName):
        file = open(fileName, 'w+')
        file.close()
        return()

    def saveData (self):
        file1 = open(r'MessanaData.pkl','wb')
        pickle.dump(self.mSystem, file1)
        file1.close()

    def loadData (self):
        file1 = open(r'MessanaData.pkl','rb')
        self.mSystem = pickle.load(file1)
        print (self.mSystem['system']['ISYnode']['nlsNAME'])        
        file1.close() 

    
    #System
    def updateSystemData(self):
        print('Update Messana Sytem Data')
        #LOGGER.info(self.mSystem['system'])
        sysData = {}
        DataOK = True
        for mKey in self.mSystem['system']['KeyInfo']:
            if self.mSystem['system']['KeyInfo'][mKey]['GETstr']:
                #print('GET ' + mKey)
                sysData= self.pullSystemDataIndividual(mKey)
                if not(sysData['statusOK']):
                    print ('Error System GET: ' + mKey)
                    DataOK = False       
            else:
                print ('GET string does not exist for : ' + mKey)
                DataOK = False               
        return(DataOK)

    def pullSystemDataIndividual(self, mKey):
        print('MessanaInfo pull System Data: ' + mKey)
        sysData = {}
        if mKey in self.mSystem['system']['KeyInfo']:
            if 'GETstr' in self.mSystem['system']['KeyInfo'][mKey]:
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
                if mKey in self.mSystem['system']['KeyInfo']:
                    if self.mSystem['system']['KeyInfo'][mKey]['PUTstr']:
                        keys.append(mKey)
        else:
            print('No Keys found - trying to fetch system data ')
            self.updateSystemData()
            for mKey in self.mSystem['system']['data']:
                if mKey in self.mSystem['system']['KeyInfo']:
                    if self.mSystem['system']['KeyInfo'][mKey]['PUTstr']:
                        keys.append(mKey)
        return(keys)  
            
    def systemActiveKeys(self):
        print('systemActiveKeys')
        keys=[]
        if self.mSystem['system']['data']:
            for mKey in self.mSystem['system']['data']:
                if mKey in self.mSystem['system']['KeyInfo']:
                    if self.mSystem['system']['KeyInfo'][mKey]['Active']:
                        keys.append(mKey)
        else:
            print('No Keys found - trying to fetch system data ')
            self.updateSystemData()
            for mKey in self.mSystem['system']['data']:
                if mKey in self.mSystem['system']['KeyInfo']:
                    if self.mSystem['system']['KeyInfo'][mKey]['Active']:
                        keys.append(mKey)
        return(keys)  
            
    # Zones
    def getZoneCapability(self, zoneNbr): 
        self.getNodeCapability('zones', zoneNbr)

    def addZoneDefStruct(self, zoneNbr, nodeId):
        self.addNodeDefStruct(zoneNbr, 'zones', nodeId)

    def updateZoneData(self, zoneNbr):
        print('updatZoneData: ' + str(zoneNbr))
        self.zoneKeys = self.zonePullKeys(zoneNbr)
        self.dataOK = True
        for mKey in self.zoneKeys:
            self.data = self.pullZoneDataIndividual(zoneNbr, mKey)
            self.dataOK = self.dataOK and self.data['dataAll']
        return(self.dataOK)

    def pullZoneDataIndividual(self, zoneNbr, mKey): 
        print('pullZoneDataIndividual: ' +str(zoneNbr)  + ' ' + mKey)    
        return(self.pullNodeDataIndividual(zoneNbr, 'zones', mKey))


    def pushZoneDataIndividual(self, zoneNbr, mKey, value):
        print('pushZoneDataIndividual: ' +str(zoneNbr)  + ' ' + mKey + ' ' + str(value))  
        return(self.pushNodeDataIndividual(zoneNbr, 'zones', mKey, value))

    def zonePullKeys(self, zoneNbr):
        print('zonePullKeys')
        self.tempZoneKeys =  self.getNodeKeys (zoneNbr, 'zones', 'GETstr')
        return( self.tempZoneKeys)

    def zonePushKeys(self, zoneNbr):
        print('zonePushKeys')

        return( self.getNodeKeys (zoneNbr, 'zones', 'PUTstr'))
  
    def zoneActiveKeys(self, zoneNbr):
        print('zoneActiveKeys')
        return( self.getNodeKeys (zoneNbr, 'zones', 'active'))


    #MacroZone
    def getMacrozoneCapability(self, macrozoneNbr): 
        self.getNodeCapability('macrozones', macrozoneNbr)

    def updateMacroZoneData(self, macrozoneNbr):
        print('updatMacroZoneData: ' + str(macrozoneNbr))
        return(self.updateNodeData(macrozoneNbr, 'macrozones'))

    def pullMacroZoneDataIndividual(self, macrozoneNbr, mKey): 
        print('pullMacroZoneDataIndividual: ' +str(macrozoneNbr)  + ' ' + mKey)    
        return(self.pullNodeDataIndividual(macrozoneNbr, 'macrozones', mKey))

    def pushMacroZoneDataIndividual(self, macrozoneNbr, mKey, value):
        print('pushMacroZoneDataIndividual: ' +str(macrozoneNbr)  + ' ' + mKey + ' ' + str(value))  
        return(self.pushNodeDataIndividual(macrozoneNbr, 'macrozones', mKey, value))

    def macrozonePullKeys(self, macrozoneNbr):
        print('macrozonePullKeys')
        return( self.getNodeKeys (macrozoneNbr, 'macrozones', 'GETstr'))

    def macrozonePushKeys(self, macrozoneNbr):
        print('macrozonePushKeys')
        return( self.getNodeKeys (macrozoneNbr, 'macrozones', 'PUTstr'))
  
    def macrozoneActiveKeys(self, macrozoneNbr):
        print('macrozoneActiveKeys')
        return( self.getNodeKeys (macrozoneNbr, 'macrozones', 'active'))    


    # Hot Cold Change Over
    def updateHC_COData(self, HC_CONbr):
        print('updatHC_COData: ' + str(HC_CONbr))
        return(self.updateNodeData(HC_CONbr, 'hc_changeover'))

    def pullHC_CODataIndividual(self, HC_CONbr, mKey): 
        print('pullHC_CODataIndividual: ' +str(HC_CONbr)  + ' ' + mKey)    
        return(self.pullNodeDataIndividual(HC_CONbr, 'hc_changeover', mKey))

    def pushHC_CODataIndividual(self, HC_CONbr, mKey, value):
        print('pushHC_CODataIndividual: ' +str(HC_CONbr)  + ' ' + mKey + ' ' + str(value))  
        return(self.pushNodeDataIndividual(HC_CONbr, 'hc_changeover', mKey, value))

    def hc_changeoverPullKeys(self, HC_CONbr):
        print('hc_changeoverPullKeys')
        return( self.getNodeKeys (HC_CONbr, 'hc_changeover', 'GETstr'))

    def hc_changeoverPushKeys(self, HC_CONbr):
        print('hc_changeoverPushKeys')
        return( self.getNodeKeys (HC_CONbr, 'hc_changeover', 'PUTstr'))
  
    def hc_changeoverActiveKeys(self, HC_CONbr):
        print('hc_changeoverActiveKeys')
        return( self.getNodeKeys (HC_CONbr, 'hc_changeover', 'active'))    
   

    #ATU
    def updateATUData(self, ATUNbr):
        print('updatATUData: ' + str(ATUNbr))
        return(self.updateNodeData(ATUNbr, 'atus'))

    def pullATUDataIndividual(self, ATUNbr, mKey): 
        print('pullATUDataIndividual: ' +str(ATUNbr)  + ' ' + mKey)    
        return(self.pullNodeDataIndividual(ATUNbr, 'atus', mKey))

    def pushATUDataIndividual(self, ATUNbr, mKey, value):
        print('pushATUDataIndividual: ' +str(ATUNbr)  + ' ' + mKey + ' ' + str(value))  
        return(self.pushNodeDataIndividual(ATUNbr, 'atus', mKey, value))

    def atuPullKeys(self, ATUNbr): 
        print('atusPullKeys')
        return( self.getNodeKeys (ATUNbr, 'atus', 'GETstr'))

    def atuPushKeys(self, ATUNbr):
        print('atusPushKeys')
        return( self.getNodeKeys (ATUNbr, 'atus', 'PUTstr'))
  
    def atuActiveKeys(self, ATUNbr):
        print('atusActiveKeys')
        return( self.getNodeKeys (ATUNbr, 'atus', 'active'))    
  
    #Fan Coils
    def updateFanCoilData(self, FanCoilNbr):

        print('updatFanCoilData: ' + str(FanCoilNbr))
        return(self.updateNodeData(FanCoilNbr, 'fan_coils'))

    def pullFanCoilDataIndividual(self, FanCoilNbr, mKey): 
        print('pullFanCoilDataIndividual: ' +str(FanCoilNbr)  + ' ' + mKey)    
        return(self.pullNodeDataIndividual(FanCoilNbr, 'fan_coils', mKey))

    def pushFanCoilDataIndividual(self, FanCoilNbr, mKey, value):
        print('pushFanCoilDataIndividual: ' +str(FanCoilNbr)  + ' ' + mKey + ' ' + str(value))  
        return(self.pushNodeDataIndividual(FanCoilNbr, 'fan_coils', mKey, value))

    def fan_coilPullKeys(self, FanCoilNbr):
        print('fan_coilPullKeys')
        return( self.getNodeKeys (FanCoilNbr, 'fan_coils', 'GETstr'))

    def fan_coilPushKeys(self, FanCoilNbr):
        print('fan_coilPushKeys')
        return( self.getNodeKeys (FanCoilNbr, 'fan_coils', 'PUTstr'))
  
    def fan_coilActiveKeys(self, FanCoilNbr):
        print('fan_coilActiveKeys')
        return( self.getNodeKeys (FanCoilNbr, 'fan_coils', 'active'))    
  
    #energy_sources
    def updateEnergySourceData(self, EnergySourceNbr):
        print('updatEnergySourceData: ' + str(EnergySourceNbr))
        return(self.updateNodeData(EnergySourceNbr, 'energy_sources'))

    def pullEnergySourceDataIndividual(self, EnergySourceNbr, mKey): 
        print('pullEnergySourceDataIndividual: ' +str(EnergySourceNbr)  + ' ' + mKey)    
        return(self.pullNodeDataIndividual(EnergySourceNbr, 'energy_sources', mKey))

    def pushEnergySourceDataIndividual(self, EnergySourceNbr, mKey, value):
        print('pushEnergySourceDataIndividual: ' +str(EnergySourceNbr)  + ' ' + mKey + ' ' + str(value))  
        return(self.pushNodeDataIndividual(EnergySourceNbr, 'energy_sources', mKey, value))

    def energy_sourcePullKeys(self, EnergySourceNbr):
        print('energy_sourcePullKeys')
        return( self.getNodeKeys (EnergySourceNbr, 'energy_sources', 'GETstr'))

    def energy_sourcePushKeys(self, EnergySourceNbr):
        print('energy_sourcePushKeys')
        return( self.getNodeKeys (EnergySourceNbr, 'energy_sources', 'PUTstr'))
  
    def energy_sourceActiveKeys(self, EnergySourceNbr):
        print('energy_sourceActiveKeys')
        return( self.getNodeKeys (EnergySourceNbr, 'energy_sources', 'active'))    


    #Buffer Tank
    def updateBufferTankData(self, BufferTankNbr):
        print('updatBufferTankData: ' + str(BufferTankNbr))
        return(self.updateNodeData(BufferTankNbr, 'buffer_tanks'))

    def pullBufferTankDataIndividual(self, BufferTankNbr, mKey): 
        print('pullBufferTankDataIndividual: ' +str(BufferTankNbr)  + ' ' + mKey)    
        return(self.pullNodeDataIndividual(BufferTankNbr, 'buffer_tanks', mKey))

    def pushBufferTankDataIndividual(self, BufferTankNbr, mKey, value):
        print('pushBufferTankDataIndividual: ' +str(BufferTankNbr)  + ' ' + mKey + ' ' + str(value))  

        if mKey == 'mStatus':
            BTdata = {}
            BTdata = self.pullNodeDataIndividual(BufferTankNbr, 'buffer_tanks', 'mMode')
            if BTdata['data'] != 0:
                return(self.pushNodeDataIndividual(BufferTankNbr, 'buffer_tanks', mKey, value))
            else:
                print ('Mode = 0, Cannot set status if mode = 0')
                return(False)
        else:
             return(self.pushNodeDataIndividual(BufferTankNbr, 'buffer_tanks', mKey, value))

    def buffer_tankPullKeys(self, BufferTankNbr):
        print('buffer_tankPullKeys')
        return( self.getNodeKeys (BufferTankNbr, 'buffer_tanks', 'GETstr'))

    def buffer_tankPushKeys(self, BufferTankNbr):
        print('buffer_tankPushKeys')
        return( self.getNodeKeys (BufferTankNbr, 'buffer_tanks', 'PUTstr'))
  
    def buffer_tankActiveKeys(self, BufferTankNbr):
        print('buffer_tankActiveKeys')
        return( self.getNodeKeys (BufferTankNbr, 'buffer_tanks', 'active'))    


        #Domestic Hot Water
 

    # Domestic Hot Water
    def updateDHWData(self, DHWNbr):
        print('updatDHWData: ' + str(DHWNbr))
        return(self.updateNodeData(DHWNbr, 'domsetic_hot_waters'))

    def pullDHWDataIndividual(self, DHWNbr, mKey): 
        print('pullDHWDataIndividual: ' +str(DHWNbr)  + ' ' + mKey)    
        return(self.pullNodeDataIndividual(DHWNbr, 'domsetic_hot_waters', mKey))

    def pushDHWDataIndividual(self, DHWNbr, mKey, value):
        print('pushDHWDataIndividual: ' +str(DHWNbr)  + ' ' + mKey + ' ' + str(value))  
        return(self.pushNodeDataIndividual(DHWNbr, 'domsetic_hot_waters', mKey, value))


    def DHWPullKeys(self, DHWNbr):
        print('DHWPullKeys')
        return( self.getNodeKeys (DHWNbr, 'domsetic_hot_waters', 'GETstr'))

    def DHWPushKeys(self, DHWNbr):
        print('DHWPushKeys')
        return( self.getNodeKeys (DHWNbr, 'domsetic_hot_waters', 'PUTstr'))
  
    def DHWActiveKeys(self, DHWNbr):
        print('DHWActiveKeys')
        return( self.getNodeKeys (DHWNbr, 'domsetic_hot_waters', 'active'))    


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
