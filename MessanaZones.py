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
        self.checkSetDriver('ST', self.zoneInfo['mStatus'])
        self.checkSetDriver('GV1', self.zoneInfo['mSetPoint'])        
        self.checkSetDriver('GV2', self.zoneInfo['mTemp'])
        self.checkSetDriver('CLITEMP', self.zoneInfo['mAirTemp'])
        self.checkSetDriver('GV3', self.zoneInfo['mScheduleOn'])
        self.checkSetDriver('GV5', self.zoneInfo['mDewPoint'])
        self.checkSetDriver('GV6', self.zoneInfo['mAirQuality'])
        self.checkSetDriver('CLIHUM', self.zoneInfo['mHumidity'])
        self.checkSetDriver('CO2LVL', self.zoneInfo['mCO2'])
        self.checkSetDriver('GV7', self.zoneInfo['mMacrozoneId'])
        self.checkSetDriver('GV8', self.zoneInfo['mEnergySave'])
        self.checkSetDriver('GV9', self.zoneInfo['mHumSetPointRH'])
        self.checkSetDriver('GV10', self.zoneInfo['mHumSetPointDP'])
        self.checkSetDriver('GV11', self.zoneInfo['mDeumSetPointRH'])
        self.checkSetDriver('GV12', self.zoneInfo['mDehumSetPointDP'])
        self.checkSetDriver('ALARM', self.zoneInfo['mAlarmOn'])
        self.checkSetDriver('GV13', self.zoneInfo['mCurrentSetPointRH'])
        self.checkSetDriver('GV14', self.zoneInfo['mCurrentSetPointDP'])


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

