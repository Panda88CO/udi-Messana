#!/usr/bin/env python3

import polyinterface
from subprocess import call
import json
from collections import defaultdict
from MessanaInfo import MessanaInfo

LOGGER = polyinterface.LOGGER

class MessanaZones(polyinterface.Node):
    def __init__(self, controller, primary, address, name, zoneNbr, messana):
        super().__init__(controller, primary, address, name)
        LOGGER.info('_init_ Messana Zone')
        self.zoneNbr = zoneNbr
        self.messana = messana
        self.zoneInfo = defaultdict(dict)
        
        self.zoneInfo = self.messana.retrieveZoneData(self.zoneNbr)
        LOGGER.debug(self.zoneInfo)

      
    def start(self):
        return True

    def stop(self):
        LOGGER.debug('stop - Cleaning up Temp Sensors & GPIO')

    def shortPoll(self):
        LOGGER.debug('Messane Zone shortPoll')
        self.updateInfo()
                   
    def longPoll(self):
        LOGGER.debug('Messana Zone longPoll')

    def query(self, command=None):
        LOGGER.debug('TOP querry')

    def checkSetDriver(self, ISYkey, mKey):
        if mkey in self.zoneInfo:
            self.setDriver(ISYkey, self.zoneInfo[mKey])   

    def updateInfo(self):
        LOGGER.info( 'Zone ' + str(self.zoneNbr) + ' Data update')
        self.zoneInfo = self.messana.retrieveZoneData(self.zoneNbr)
        self.checkSetDriver('ST', 'mStatus')
        self.checkSetDriver('GV1', 'mSetPoint')        
        self.checkSetDriver('GV2', 'mTemp')
        self.checkSetDriver('CLITEMP', 'mAirTemp')
        self.checkSetDriver('GV3', 'mScheduleOn')
        self.checkSetDriver('GV5', 'mDewPoint')
        self.checkSetDriver('GV6', 'mAirQuality')
        self.checkSetDriver('CLIHUM', 'mHumidity')
        self.checkSetDriver('CO2LVL', 'mCO2')
        self.checkSetDriver('GV7', 'mMacrozoneId')
        self.checkSetDriver('GV8', 'mEnergySave')
        self.checkSetDriver('GV9', 'mHumSetPointRH')
        self.checkSetDriver('GV10', 'mHumSetPointDP')
        self.checkSetDriver('GV11', 'mDeumSetPointRH')
        self.checkSetDriver('GV12', 'mDehumSetPointDP')
        self.checkSetDriver('ALARM', 'mAlarmOn')
        self.checkSetDriver('GV13', 'mCurrentSetPointRH')
        self.checkSetDriver('GV14', 'mCurrentSetPointDP')


    def setStatus(self, command):
        return True

    def setEnergySave(self, command):
        return True

    def setSetpoint(self, command):
        return True

    def EnSchedule(self, command):
        return True        

    id = 'zone'
    commands = { 'SET_SETPOINT': setSetpoint
                ,'SET_STATUS"': setStatus
                ,'SET_ENERGYSAVE': setEnergySave
                ,'SET_SCHEDULE' : EnSchedule 
                }

    drivers = [  {'driver': 'ST',  'value': 1, 'uom': 2}
                ,{'driver': 'GV1', 'value': 1, 'uom': 4}               
                ,{'driver': 'GV2', 'value': 1, 'uom': 2}
                ,{'driver': 'GV3', 'value': 1, 'uom': 2}
                ,{'driver': 'CLITEMP', 'value': 1, 'uom': 4}
                ,{'driver': 'GV5', 'value': 1, 'uom': 51}
                ,{'driver': 'CLIHUM', 'value': 1, 'uom': 51}
                ,{'driver': 'C02LVL', 'value': 1, 'uom': 107}
                ,{'driver': 'GV6', 'value': 1, 'uom': 107}     
                ,{'driver': 'GV7', 'value': 0, 'uom': 107}
                ,{'driver': 'GV8', 'value': 1, 'uom': 107}
                ,{'driver': 'ALARM', 'value': 0, 'uom': 2}          
                ,{'driver': 'GV9', 'value': 1, 'uom': 107}
                ,{'driver': 'GV10', 'value': 1, 'uom': 107} 
                ,{'driver': 'GV11', 'value': 0, 'uom': 107}
                ,{'driver': 'GV12', 'value': 1, 'uom': 107}
                ,{'driver': 'GV13', 'value': 0, 'uom': 107}
                ,{'driver': 'GV14', 'value': 1, 'uom': 107}
                ]

