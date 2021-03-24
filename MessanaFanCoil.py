#!/usr/bin/env python3

import polyinterface
from subprocess import call
import json
from collections import defaultdict
#from MessanaInfo import MessanaInfo

LOGGER = polyinterface.LOGGER
#self, controller, primary, address, name, nodeType, nodeNbr, messana
class messanaZone(polyinterface.Node):
    def __init__(self, controller, primary, address, name,  fanCoilNbr):
        super().__init__(controller, primary, address, name)
        LOGGER.info('_init_ Messana Zone ' + str(fanCoilNbr) )
        self.fanCoilNbr = fanCoilNbr
        self.name = name
        self.address = address 
        self.id = 'zones'+str(fanCoilNbr)
        self.messana = self.parent.messana
        self.zone_GETKeys = self.messana.zonePullKeys(self.fanCoilNbr)
        self.zone_PUTKeys = self.messana.zonePushKeys(self.fanCoilNbr)
        self.zone_ActiveKeys = self.messana.zoneActiveKeys(self.fanCoilNbr)
        self.ISYforced = False
        
        self.drivers = []
        for key in self.zone_GETKeys:
            self.temp = self.messana.getZoneISYdriverInfo(key, self.fanCoilNbr)
            if  self.temp != {}:
                self.drivers.append(self.temp)
                LOGGER.debug(  'driver:  ' +  self.temp['driver'])
        self.messana.updateZoneData('all', self.fanCoilNbr)
        self.updateISYdrivers('all')
        self.ISYforced = True
       
    def start(self):


        return True


    def updateISYdrivers(self, level):
        LOGGER.debug('Zone updateISYdrivers')
        for ISYdriver in self.drivers:
            ISYkey = ISYdriver['driver']
            if level == 'active':
                temp = self.messana.getZoneMessanaISYkey(ISYkey, self.fanCoilNbr)
                if temp in self.zone_ActiveKeys:                    
                    LOGGER.debug('Messana Zone ISYdrivers ACTIVE ' + temp)
                    status, value = self.messana.getZoneISYValue(ISYkey, self.fanCoilNbr)
                    if status:
                        if self.ISYforced:
                            self.setDriver(ISYdriver, value, report = True, force = False)
                        else:
                            self.setDriver(ISYdriver, value, report = True, force = True)
                        LOGGER.debug('driver updated :' + ISYdriver['driver'] + ' =  '+str(value))
                    else:
                        LOGGER.debug('Error getting ' + ISYdriver['driver'])
            elif level == 'all':
                temp = self.messana.getZoneMessanaISYkey(ISYkey, self.fanCoilNbr)
                status, value = self.messana.getZoneISYValue(ISYkey, self.fanCoilNbr)
                LOGGER.debug('Messana Zone ISYdrivers ALL ' + temp)
                if status:
                    if self.ISYforced:
                        self.setDriver(ISYdriver, value, report = True, force = False)
                    else:
                        self.setDriver(ISYdriver, value, report = True, force = True)
                    LOGGER.debug('driver updated :' + ISYdriver['driver'] + ' =  '+str(value))
                else:
                    LOGGER.debug('Error getting ' + ISYdriver['driver'])
            else:
                LOGGER.debug('Error!  Unknow level: ' + level)
        
    def stop(self):
        LOGGER.debug('stop - Messana Zone Cleaning up')

    def shortPoll(self):
        LOGGER.debug('Messana Zone shortPoll - zone '+ str(self.fanCoilNbr))
        self.messana.updateZoneData('active', self.fanCoilNbr)
        self.updateISYdrivers('active')
                   
    def longPoll(self):
        LOGGER.debug('Messana Zone longPoll - zone ' + str(self.fanCoilNbr))
        self.messana.updateZoneData('all', self.fanCoilNbr)
        self.updateISYdrivers('all')
        self.reportDrivers()

    def query(self, command=None):
        LOGGER.debug('TOP querry')

    def setStatus(self, command):
        LOGGER.debug('setStatus Called')
        value = int(command.get('value'))
        LOGGER.debug('Zone'+str(self.fanCoilNbr)+' setStatus Received:' + str(value))
        if self.messana.zoneSetStatus(value, self.fanCoilNbr):
            ISYdriver = self.messana.getZoneStatusISYdriver(self.fanCoilNbr)
            self.setDriver(ISYdriver, value, report = True)



    def setEnergySave(self, command):
        LOGGER.debug('setEnergySave Called')
        value = int(command.get('value'))
        LOGGER.debug('Zone'+str(self.fanCoilNbr)+' setEnergySave Received:' + str(value))
        if self.messana.zoneSetEnergySave(value, self.fanCoilNbr):
            ISYdriver = self.messana.getZoneEnergySaveISYdriver(self.fanCoilNbr)
            self.setDriver(ISYdriver, value, report = True)


    def setSetpoint(self, command):
        LOGGER.debug('setSetpoint Called')
        value = int(command.get('value'))
        LOGGER.debug('Zone'+str(self.fanCoilNbr)+' setSetpoint Received:' + str(value))
        if self.messana.zoneSetSetpoint(value, self.fanCoilNbr):
            ISYdriver = self.messana.getZoneSetPointISYdriver(self.fanCoilNbr)
            self.setDriver(ISYdriver, value, report = True)


    def enableSchedule(self, command):
        LOGGER.debug('EnSchedule Called')
        value = int(command.get('value'))
        LOGGER.debug('Zone'+str(self.fanCoilNbr)+' EnSchedule Reeived:' + str(value))      
        if self.messana.zoneEnableSchedule(value, self.fanCoilNbr):
            ISYdriver = self.messana.getZoneEnableScheduleISYdriver(self.fanCoilNbr)
            self.setDriver(ISYdriver, value, report = True)     
        
        #self.zoneInfo['mScheduleOn'] = val
        #self.messana.pushZoneData(self.fanCoilNbr, self.zoneInfo)
        #self.checkSetDriver('GV3', 'mScheduleOn')

 

    commands = { 'SET_SETPOINT': setSetpoint
                ,'SET_STATUS': setStatus
                ,'SET_ENERGYSAVE': setEnergySave
                ,'SET_SCHEDULE' : enableSchedule 
                }

    drivers = [  ]

