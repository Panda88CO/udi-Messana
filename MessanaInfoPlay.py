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
        self.mSystem = {'system': {  'ISYnode':{ 'nlsICON':'Thermostat'}
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
                                                    ,'nlsValues' : [ '0=Off'
                                                                    ,'1=On'] 
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
                                                    ,'nlsValues' : []
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
                                                    ,'nlsValues' : []
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
                                                    ,'nlsValues' :[]
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
                                                    ,'nlsValues' : [] 
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
                                                    ,'nlsValues' : []
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
                                                    ,'nlsValues' :  [] 
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
                                                    ,'nlsValues' :  [] 
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
                                                    ,'nlsValues' : []
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
                                                    ,'nlsValues' : ['0=F'
                                                                    ,'1=C']
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
                                                    ,'nlsValues' : [ '0=Off'
                                                                    ,'1=On']
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
                                                    ,'nlsValues' : [ '0=Off'
                                                                    ,'1=On']
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
                                                    ,'nlsValues' : [ '0=Off'
                                                                    ,'1=On']
                                                        }
                                                }   
                                         }                                         
                                     ,'data':{}
                                         
                        },
                        'zones': {   'ISYnode':{'nlsICON':'TempSensor'}
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
                                                    ,'nlsValues' : [] 
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
                                                    ,'nlsValues' : []
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
                                                    ,'nlsValues' : ['0=Off'
                                                                    ,'1=On']
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
                                                    ,'nlsValues' : [] 
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
                                                    ,'nlsValues' : [] 
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
                                                    ,'nlsValues' : [] 
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
                                                    ,'nlsValues' : [] 
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
                                                    ,'nlsValues' : [] 
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
                                                    ,'nlsValues' : [] 
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
                                                    ,'nlsValues' : []
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
                                                    ,'nlsValues' : []
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
                                                     'nlsTEXT' : 'Panel Temp' 
                                                    ,'nlsValues' : []
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
                                                    ,'nlsValues' : [] 
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
                                                    ,'nlsValues' : [ '0=Off'
                                                                    ,'1=On']
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
                                                    ,'nlsValues' : [] 
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
                                                    ,'nlsValues' : [] 
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
                                                     'nlsTEXT' : 'Air/Room Temp' 
                                                    ,'nlsValues' : []
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
                                                    ,'nlsValues' : [] 
                                                        }
                                                    }  
                                        ,'mEnergySave' : { 
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
                                                    ,'nlsValues' : [ '0=Off'
                                                                    ,'1=On']
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
                                                    ,'nlsValues' : [ '0=Off'
                                                                    ,'1=On']
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
                                                    ,'nlsValues' : [ '0=No Thermal'
                                                                    ,'1=Heating Request'
                                                                    ,'2=Cooling Request'
                                                                    ,'3=H & C request'  ] 
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

        '''
        print ('Reading Messana System')
        #self.pullAllMessanaStatus()
        print('Finish Reading Messana system')
        '''
    def init(self):
        return(True)

    def addSubNodeDefStruct(self, subnodeNbr, subnodeName, nodeId):
        self.keyCount = 0
        nodeId.lower()

        self.name = nodeId+str(subnodeNbr)


        self.nlsKey = 'nls' + self.name
        self.nlsKey.lower()
        #editorName = nodeName+'_'+str(keyCount)
        self.setupFile['nodeDef'][self.name]={}
        self.setupFile['nodeDef'][self.name]['CodeId'] = nodeId
        self.setupFile['nodeDef'][self.name]['nlsId'] = self.nlsKey
        self.setupFile['nodeDef'][self.name]['nlsNAME']=self.mSystem[subnodeName]['data'][subnodeNbr]['mName']
        self.setupFile['nodeDef'][self.name]['nlsICON']=self.mSystem[subnodeName]['ISYnode']['nlsICON']
        self.setupFile['nodeDef'][self.name]['sts']={}
        self.setupFile['nodeDef'][self.name]['cmds']={}
        self.setupFile['nodeDef'][self.name]['cmds']['sends'] = []
        self.setupFile['nodeDef'][self.name]['cmds']['accepts'] = {}
        

        for mKey in self.mSystem[subnodeName]['data'][subnodeNbr]: 
            #make check if system has unit installed
            if self.mSystem[subnodeName]['KeyInfo'][mKey]['ISYeditor']['ISYuom']:
                self.keyCount = self.keyCount + 1
                editorName = subnodeName.upper()+'_'+str(self.keyCount)
                nlsName = editorName.lower()
                ISYvar = 'GV'+str(self.keyCount)
                self.setupFile['nodeDef'][subnodeName]['sts'][mKey]={ISYvar:editorName}
                self.setupFile['editors'][editorName]={}
                #self.setupFile['nls'][editorName][ISYparam]
                for ISYparam in self.mSystem[subnodeName]['KeyInfo'][mKey]['ISYeditor']:
                    if self.mSystem['system']['KeyInfo'][mKey]['ISYeditor'][ISYparam]!= None:
                        self.setupFile['editors'][editorName][ISYparam]=self.mSystem[subnodeName]['KeyInfo'][mKey]['ISYeditor'][ISYparam]

                if self.mSystem[subnodeName]['KeyInfo'][mKey]['ISYnls']:
                    self.setupFile['nls'][nlsName]={}
                for ISYnls in self.mSystem['system']['KeyInfo'][mKey]['ISYnls']:
                    print ( mKey + ' ' + ISYnls)
                    if  self.mSystem[subnodeName]['KeyInfo'][mKey]['ISYnls'][ISYnls]:      
                        self.setupFile['nls'][nlsName][ISYnls] = self.mSystem['system']['KeyInfo'][mKey]['ISYnls'][ISYnls]
                        if ISYnls == 'nlsValues':
                            self.setupFile['editors'][editorName]['nlsKey'] = nlsName
            
        #self.editorName = self.name + '_'  + str(self.keyCount)  
        return()

    def addSystemSendComand(self, nodeName, idName):
        if  self.setupFile['nodeDef'][nodeName]['cmds']['sends'] == None:
            self.setupFile['nodeDef'][nodeName]['cmds']['sends']=[]
        self.setupFile['nodeDef'][nodeName]['cmds']['sends'].append(idName)
        return()
   
    def addSystemAcceptComand(self, nodeName, idName, driverName):   
        self.setupFile['nodeDef'][nodeName]['cmds']['accepts'][driverName] = idName
        return()


    def addSystemDefStruct(self, nodeName, nodeId):
        self.keyCount = 0
        nodeId.lower()
        self.nlsKey= 'nls' + nodeId
        self.nlsKey.lower()
        self.setupFile['nodeDef'][nodeName]={}
        self.setupFile['nodeDef'][nodeName]['CodeId'] = nodeId
        self.setupFile['nodeDef'][nodeName]['nlsId'] = self.nlsKey
        self.setupFile['nodeDef'][nodeName]['nlsNAME']=self.mSystem[nodeName]['data']['mName']
        self.setupFile['nodeDef'][nodeName]['nlsICON']=self.mSystem[nodeName]['ISYnode']['nlsICON']
        self.setupFile['nodeDef'][nodeName]['sts']={}
        self.setupFile['nodeDef'][nodeName]['cmds']={}
        self.setupFile['nodeDef'][nodeName]['cmds']['sends'] = []
        self.setupFile['nodeDef'][nodeName]['cmds']['accepts'] = {}
  
        #pullKeys = self.systemPullKeys()
        # Only install if node exists
        for mKey in self.mSystem[nodeName]['data']: 
            #make check if system has unit installed
            if self.mSystem[nodeName]['KeyInfo'][mKey]['ISYeditor']['ISYuom']:
                if ((self.mSystem[nodeName]['KeyInfo'][mKey]['ISYeditor']['ISYuom'] == 107
                   and self.mSystem[nodeName]['data'][mKey] != 0)
                   or self.mSystem[nodeName]['KeyInfo'][mKey]['ISYeditor']['ISYuom'] != 107):
                    self.keyCount = self.keyCount + 1
                    editorName = nodeName.upper()+'_'+str(self.keyCount)
                    nlsName = editorName.lower()
                    ISYvar = 'GV'+str(self.keyCount)
                    self.setupFile['nodeDef'][nodeName]['sts'][mKey]={ISYvar:editorName}
                    self.setupFile['editors'][editorName]={}
                    #self.setupFile['nls'][editorName][ISYparam]
                    for ISYparam in self.mSystem[nodeName]['KeyInfo'][mKey]['ISYeditor']:
                        if self.mSystem['system']['KeyInfo'][mKey]['ISYeditor'][ISYparam]!= None:
                            self.setupFile['editors'][editorName][ISYparam]=self.mSystem[nodeName]['KeyInfo'][mKey]['ISYeditor'][ISYparam]

                    if self.mSystem[nodeName]['KeyInfo'][mKey]['ISYnls']:
                        self.setupFile['nls'][nlsName]={}
                    for ISYnls in self.mSystem['system']['KeyInfo'][mKey]['ISYnls']:
                        print ( mKey + ' ' + ISYnls)
                        if  self.mSystem[nodeName]['KeyInfo'][mKey]['ISYnls'][ISYnls]:      
                            self.setupFile['nls'][nlsName][ISYnls] = self.mSystem['system']['KeyInfo'][mKey]['ISYnls'][ISYnls]
                            if ISYnls == 'nlsValues':
                                self.setupFile['editors'][editorName]['nlsKey'] = nlsName
                    
    def updateZoneCapability (self, zoneNbr):
        self.zoneCapability[zoneNbr] = self.pullZoneDataIndividual(  zoneNbr, 'mCapability')
        self.keyList = {}
        tempKeys = self.zoneCapability[zoneNbr]['dataAll']
        for key in tempKeys:
            if key == 'operative_temperature':
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
                self.keyList['mDewPoint'] = tempKeys["relative_humidity"]
            elif key == 'co2':
                self.keyList['mCO2'] = tempKeys['co2']                
            elif key == 'voc':
                self.keyList['mVoc'] = tempKeys['voc']   
            else:
                print(key + 'unknown keyword')
        return(self.keyList)
    
    def addZoneDefStruct(self, zoneNbr, nodeId):
        self.addSubNodeDefStruct(zoneNbr, 'zones', nodeId)


    def GETSystem(self, mKey):
        sysData= {}
        print('GETSystem: ' + mKey )
        GETStr = self.IP+self.mSystem['system']['KeyInfo'][mKey]['GETstr'] + '?' + self.APIStr 
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
            if mKey in self.mSystem['system']['KeyInfo']:
                if self.mSystem['system']['KeyInfo'][mKey]['PUTstr']:
                    PUTStr = self.IP+self.mSystem['system']['KeyInfo'][mKey]['PUTstr']
                    if PUTStr == None:
                        sysData['statusOK'] = False
                        sysData['error'] = 'Not able to PUT Key: : '+ mKey + ' value:' + str( value )
                        print(sysData)    
                        return(sysData)   
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
        if 'GETstr' in self.mSystem[mNodeKey]['KeyInfo'][mKey]:
            GETStr =self.IP+self.mSystem[mNodeKey]['KeyInfo'][mKey]['GETstr']+str(instNbr)+'?'+ self.APIStr 
            subSysTemp = requests.get(GETStr)
            if str(subSysTemp) == self.RESPONSE_OK:
                subSysTemp = subSysTemp.json()
                nodeData['data']  = subSysTemp[str(list(subSysTemp.keys())[0])] 
                nodeData['dataAll'] = subSysTemp
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
        if 'PUTstr' in self.mSystem[mNodeKey]['KeyInfo'][mKey]:
            PUTStr = self.IP + self.mSystem[mNodeKey]['KeyInfo'][mKey]['PUTstr']
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
                    if mKey in self.mSystem[subsystemKey]['KeyInfo'][mKey][cmdKey]:
                        if not(mKey in keys):
                            keys.append(mKey)
            else:
                self.updateSubSystemData(subsystemNbr, subsystemKey)
                for mKey in self.mSystem[subsystemKey]['data'][subsystemNbr]:
                    if mKey in self.mSystem[subsystemKey]['KeyInfo'][mKey][cmdKey]:
                        if not(mKey in keys):
                            keys.append(mKey)
        else:
            print('No Keys found - trying to fetch Messana data')
            self.updateSystemData()
            self.updateSubSystemData(subsystemNbr, subsystemKey)
            if self.mSystem[subsystemKey]['data']:
                for mKey in self.mSystem[subsystemKey]['data'][subsystemNbr]:
                    if mKey in self.mSystem[subsystemKey]['KeyInfo'][mKey][cmdKey]:
                        if not(mKey in keys):
                            keys.append(mKey)
            else:
                print('No '+ subsystemKey + ' present')
        return(keys)

    def updateSubSystemData(self, subsystemNbr, subsystemKey):
        print('updatSubSystemData: ' + str(subsystemNbr) + ' ' + subsystemKey)
        Data = {}
        dataOK = True
        for mKey in self.mSystem[subsystemKey]['KeyInfo']:
            print ('GET ' + mKey + ' in zone ' + str(subsystemNbr))
            Data = self.pullSubSystemDataIndividual(subsystemNbr, subsystemKey,  mKey)
            if not(Data['statusOK']):
                dataOK = False
                print ('Error GET' + Data['error'])
        return(dataOK)
    
    def pullSubSystemDataIndividual(self, subsystemNbr, subsystemKey, mKey): 
        Data = {} 
        print('pullSubSystemDataIndividual: ' +str(subsystemNbr)  + ' ' + mKey)    
        if mKey in mKey in self.mSystem[subsystemKey]['KeyInfo']:
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
        for mKey in self.mSystem['system']['KeyInfo']:
            if self.mSystem['system']['KeyInfo'][mKey]['GETstr']:
                print('GET ' + mKey)
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
    def updateZoneData(self, zoneNbr):
        print('updatZoneData: ' + str(zoneNbr))
        self.zoneKeys = self.zonePullKeys(zoneNbr)
        self.dataOK = True
        for mKey in self.zoneKeys:
            self.data = self.pullZoneDataIndividual(zoneNbr, mKey)
            self.dataOK = self.dataOK and self.data['dataOK']
        return(self.dataOK)

    def pullZoneDataIndividual(self, zoneNbr, mKey): 
        print('pullZoneDataIndividual: ' +str(zoneNbr)  + ' ' + mKey)    
        return(self.pullSubSystemDataIndividual(zoneNbr, 'zones', mKey))


    def pushZoneDataIndividual(self, zoneNbr, mKey, value):
        print('pushZoneDataIndividual: ' +str(zoneNbr)  + ' ' + mKey + ' ' + str(value))  
        return(self.pushSubSystemDataIndividual(zoneNbr, 'zones', mKey, value))

    def zonePullKeys(self, zoneNbr):
        print('zonePullKeys')
        if self.zoneCapability == {}:
            self.zoneCapability[zoneNbr] = self.updateZoneCapability(zoneNbr)
        if self.zoneCapability[zoneNbr] == None:
            self.zoneCapability[zoneNbr] = self.updateZoneCapability(zoneNbr)
        self.tempZoneKeys =  self.getSubSystemKeys (zoneNbr, 'zones', 'GETstr')
        for mKey in self.tempZoneKeys:
            if mKey in self.zoneCapability[zoneNbr]:
                if self.tempZoneKeys[mKey] == 0:
                    self.tempZoneKeys.remove(mKey)
        return( self.tempZoneKeys)

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

    def saveData (self):
        file1 = open(r'MessanaData.pkl','wb')
        pickle.dump(self.mSystem, file1)
        file1.close()

    def loadData (self):
        file1 = open(r'MessanaData.pkl','rb')
        self.mSystem = pickle.load(file1)
        print (self.mSystem['system']['ISYnode']['nlsNAME'])        
        file1.close() 




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
