#!/usr/bin/env python3

import polyinterface
from subprocess import call
import json
from collections import defaultdict
#from MessanaInfo import MessanaInfo

LOGGER = polyinterface.LOGGER
#self, controller, primary, address, name, nodeType, nodeNbr, messana
class messanaZone(polyinterface.Node):
    def __init__(self, controller, primary, address, name,  zoneNbr):
        super().__init__(controller, primary, address, name)
        LOGGER.info('_init_ Messana Zone ' + str(zoneNbr) )
        self.zoneNbr = zoneNbr
        self.name = name
        self.address = address 
        self.id = 'zones'+str(zoneNbr)
        self.messana = self.parent.messana
        self.zone_GETKeys = self.messana.zonePullKeys(self.zoneNbr)
        self.zone_PUTKeys = self.messana.zonePushKeys(self.zoneNbr)
        self.zone_ActiveKeys = self.messana.zoneActiveKeys(self.zoneNbr)
        
        self.drivers = []
        for key in self.zone_GETKeys:
            self.temp = self.messana.getZoneISYdriverInfo(key, self.zoneNbr)
            if  self.temp != {}:
                self.drivers.append(self.temp)
                LOGGER.debug(  'driver:  ' +  self.temp['driver'])

       
    def start(self):


        return True


    def updateISYdrivers(self):
        LOGGER.debug('updateISYdrivers')
        for ISYdriver in self.drivers:
            ISYkey = ISYdriver['driver']
            status, value = self.messana.getZoneISYValue(ISYkey)
            if status:
                if self.ISYforced:
                    self.setDriver(ISYdriver, value, report = True, force = False)
                else:
                    self.setDriver(ISYdriver, value, report = True, force = True)
                LOGGER.debug('driver updated :' + ISYdriver['driver'] + ' =  '+str(value))
            else:
                LOGGER.debug('Error getting ' + ISYdriver['driver'])
        self.reportDrivers()

        
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

 

    commands = { 'SET_SETPOINT': setSetpoint
                ,'SET_STATUS': setStatus
                ,'SET_ENERGYSAVE': setEnergySave
                ,'SET_SCHEDULE' : enableSchedule 
                }

    drivers = [  ]

