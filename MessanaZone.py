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

        self.zone_GETKeys = self.messana.zonePullKeys(self.zoneNbr)
        self.zone_PUTKeys = self.messana.zonePushKeys(self.zoneNbr)
        self.zone_ActiveKeys = self.messana.zoneActiveKeys(self.zonebr)

        LOGGER.debug('Append Zone drivers')
        for key in self.zone_GETKeys:
            self.zoneInfo = self.messana.pullZoneDataIndividual(self.zoneNbr,key )
            temp = self.messana.getnodeISYdriverInfo('zones', zoneNbr, key)
            LOGGER.debug('Driver info: ' + str(temp))
            if  temp != {}:
                if not(str(temp['value']).isnumeric()):                         
                    LOGGER.debug('non numeric value :' + str(temp['value']))
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
        LOGGER.debug('stop - Messana Zone Cleaning up')

    def shortPoll(self):
        LOGGER.debug('Messane Zone shortPoll')
        self.updateInfo('active')
                   
    def longPoll(self):
        LOGGER.debug('Messana Zone longPoll')
        self.updateInfo('all')
    def query(self, command=None):
        LOGGER.debug('TOP querry')

    def checkSetDriver(self, ISYkey, mKey):
        if mKey in self.zoneInfo:
            self.setDriver(ISYkey, self.zoneInfo[mKey])
            

    def updateParamsToISY(self, mKey):
        LOGGER.debug('setParamFromISY')
        temp = self.messana.getnodeISYdriverInfo('zones', self.zoneNbr, mKey)
        if temp != {}:
            LOGGER.debug('update ISY value')
            ISYkey = temp['driver']
            self.checkSetDriver(ISYkey, mKey)
        else:
            LOGGER.info(mKey + ' update failed')

    def updateInfo(self, level):
        LOGGER.info( 'Update Info - Zone ' + str(self.zoneNbr) + ' Data update')
        if level == 'active':
            for mKey in self.zone_ActiveKeys: 
                LOGGER.debug('Zone active ' + mKey)
                self.updateParamsToISY(mKey)
                
        elif level == 'all':
             for mKey in self.zone_GETKeys: 
                self.updateParamsToISY(mKey)
                LOGGER.debug('Zone all ' + mKey)
        else:
            LOGGER.debug('unknown level' + level)
       

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
