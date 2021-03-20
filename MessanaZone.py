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
        self.messana.updateZoneData('all', self.zoneNbr)
        self.updateISYdrivers()
       
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


        
    def stop(self):
        LOGGER.debug('stop - Messana Zone Cleaning up')

    def shortPoll(self):
        LOGGER.debug('Messane Zone shortPoll')
        self.messana.updateZoneData('active', self.zoneNbr)
        self.updateISYdrivers()
                   
    def longPoll(self):
        LOGGER.debug('Messana Zone longPoll')
        self.messana.updateZoneData('all', self.zoneNbr)
        self.updateISYdrivers()
        self.reportDrivers()

    def query(self, command=None):
        LOGGER.debug('TOP querry')



    def setStatus(self, command):
        LOGGER.debug('setStatus Called')
        value = int(command.get('value'))
        LOGGER.debug('Zone'+str(self.zoneNbr)+' setStatus Received:' + str(value))
        if self.messana.ZoneSetStatus(value, self.zoneNbr):
            ISYdriver = self.messana.getZoneStatusISYdriver(self.zoneNbr)
            self.setDriver(ISYdriver, value, report = True)



    def setEnergySave(self, command):
        LOGGER.debug('setEnergySave Called')
        value = int(command.get('value'))
        LOGGER.debug('Zone'+str(self.zoneNbr)+' setEnergySave Received:' + str(value))
        if self.messana.ZoneSetEnergySave(value, self.zoneNbr):
            ISYdriver = self.messana.getZoneEnergySaveISYdriver(self.zoneNbr)
            self.setDriver(ISYdriver, value, report = True)


    def setSetpoint(self, command):
        LOGGER.debug('setSetpoint Called')
        value = int(command.get('value'))
        LOGGER.debug('Zone'+str(self.zoneNbr)+' setSetpoint Received:' + str(value))
        if self.messana.ZoneSetSetpoint(value, self.zoneNbr):
            ISYdriver = self.messana.getZoneSetPointISYdriver(self.zoneNbr)
            self.setDriver(ISYdriver, value, report = True)


    def enableSchedule(self, command):
        LOGGER.debug('EnSchedule Called')
        value = int(command.get('value'))
        LOGGER.debug('Zone'+str(self.zoneNbr)+' EnSchedule Reeived:' + str(value))      
        if self.messana.ZoneEnableSchedule(value, self.zoneNbr):
            ISYdriver = self.messana.getZoneEnableScheduleISYdriver(self.zoneNbr)
            self.setDriver(ISYdriver, value, report = True)     
        
        #self.zoneInfo['mScheduleOn'] = val
        #self.messana.pushZoneData(self.zoneNbr, self.zoneInfo)
        #self.checkSetDriver('GV3', 'mScheduleOn')

 

    commands = { 'SET_SETPOINT': setSetpoint
                ,'SET_STATUS': setStatus
                ,'SET_ENERGYSAVE': setEnergySave
                ,'SET_SCHEDULE' : enableSchedule 
                }

    drivers = [  ]

