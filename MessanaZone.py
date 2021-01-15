#!/usr/bin/env python3

import polyinterface
from subprocess import call
import json
from collections import defaultdict
from MessanaInfo import MessanaInfo

LOGGER = polyinterface.LOGGER

class MessanaZone(polyinterface.Node):
    def __init__(self, controller, primary, address, name, zoneNbr, messana):
        super().__init__(controller, primary, address, name)
        LOGGER.info('_init_ Messana Zone')
        self.zoneNbr = zoneNbr
        self.messana = messana     
        self.zoneInfo = self.messana.pullZoneData(self.zoneNbr)
        #LOGGER.debug(self.zoneInfo)

        self.zone_GETKeys = self.messana.zonePullKeys()
        self.zone_PUTKeys = self.messana.zonePushKeys()
        self.zone_ActiveKeys = self.messana.zoneActiveKeys()

        LOGGER.debug('Append Zone drivers')
        for key in self.zone_GETKeys:
            temp = self.messana.getnodeISYdriverInfo('zone', zoneNbr, key)
            LOGGER.debug('Driver info: ' + str(temp))
            if  temp != {}:
                if not(str(temp['value']).isnumeric()):                         
                    LOGGER.debug('non numeric value :' + temp['value'])
                    if temp['value'] == 'Celcius':
                        temp['value'] = 0
                        self.ISYTempUnit = 4
                    else:
                        temp['value'] = 1
                        self.ISYTempUnit = 17
                LOGGER.debug(str(temp) + 'before append')      
                MessanaZone.drivers.append(temp)
                LOGGER.debug(str(MessanaZone.drivers) + 'after append')                       
        LOGGER.debug(MessanaZone.drivers)
        #self.check_params()
        #self.discover()   
        #self.updateInfo('all')    

    def start(self):
        return True

    def stop(self):
        LOGGER.debug('stop - Cleaning up')

    def shortPoll(self):
        LOGGER.debug('Messane Zone shortPoll')
        self.updateInfo()
                   
    def longPoll(self):
        LOGGER.debug('Messana Zone longPoll')

    def query(self, command=None):
        LOGGER.debug('TOP querry')

    def checkSetDriver(self, ISYkey, mKey):
        if mKey in self.zoneInfo:
            self.setDriver(ISYkey, self.zoneInfo[mKey])   

    def updateInfo(self):
        LOGGER.info( 'Zone ' + str(self.zoneNbr) + ' Data update')
        '''
        self.zoneInfo = self.messana.pullZoneData(self.zoneNbr)
        self.checkSetDriver('GV4', 'mStatus')
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
        '''

    def setStatus(self, command):
        LOGGER.debug('setStatus Called')
        val = int(command.get('value'))
        self.zoneInfo['mStatus'] = val
        #LOGGER.debug('Zone'+str(self.zoneNbr)+' setStatus Received:' + str(val))
        #LOGGER.debug(self.zoneInfo)
        self.messana.pushZoneData(self.zoneNbr, self.zoneInfo)
        self.checkSetDriver('GV4', 'mStatus')


    def setEnergySave(self, command):
        LOGGER.debug('setEnergySave Called')
        val = int(command.get('value'))
        LOGGER.debug('Zone'+str(self.zoneNbr)+' setEnergySave Received:' + str(val))
        self.zoneInfo['mEnergySave'] = val
        self.messana.pushZoneData(self.zoneNbr, self.zoneInfo)
        self.checkSetDriver('GV8', 'mEnergySave')

    def setSetpoint(self, command):
        LOGGER.debug('setSetpoint Called')
        val = int(command.get('value'))
        LOGGER.debug('Zone'+str(self.zoneNbr)+' setSetpoint Received:' + str(val))
        self.zoneInfo['mSetPoint'] = val
        self.messana.pushZoneData(self.zoneNbr, self.zoneInfo)
        self.checkSetDriver('GV1', 'mSetPoint')  

    def enableSchedule(self, command):
        LOGGER.debug('EnSchedule Called')
        val = int(command.get('value'))
        LOGGER.debug('Zone'+str(self.zoneNbr)+' EnSchedule Reeived:' + str(val))      
        self.zoneInfo['mScheduleOn'] = val
        self.messana.pushZoneData(self.zoneNbr, self.zoneInfo)
        self.checkSetDriver('GV3', 'mScheduleOn')

    id = 'zone'
    commands = { 'SET_SETPOINT': setSetpoint
                ,'SET_STATUS': setStatus
                ,'SET_ENERGYSAVE': setEnergySave
                ,'SET_SCHEDULE' : enableSchedule 
                }

    drivers = [  ]

