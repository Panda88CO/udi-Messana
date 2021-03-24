#!/usr/bin/env python3

import polyinterface
from subprocess import call
import json
from collections import defaultdict
#from MessanaInfo import MessanaInfo

LOGGER = polyinterface.LOGGER
#self, controller, primary, address, name, nodeType, nodeNbr, messana
class pullMessanaStatus(polyinterface.Node):
    def __init__(self, controller, primary, address, name,  atuNbr):
        super().__init__(controller, primary, address, name)
        LOGGER.info('_init_ Messana atu ' + str(atuNbr) )
        self.atuNbr = atuNbr
        self.name = name
        self.address = address 
        self.id = 'atu'+str(atuNbr)
        self.messana = self.parent.messana
        self.atu_GETKeys = self.messana.atuPullKeys(self.atuNbr)
        self.atu_PUTKeys = self.messana.atuPushKeys(self.atuNbr)
        self.atu_ActiveKeys = self.messana.atuActiveKeys(self.atuNbr)
        self.ISYforced = False
        
        self.drivers = []
        for key in self.atu_GETKeys:
            self.temp = self.messana.getAtuISYdriverInfo(key, self.atuNbr)
            if  self.temp != {}:
                self.drivers.append(self.temp)
                LOGGER.debug(  'driver:  ' +  self.temp['driver'])
        self.messana.updateAtuData('all', self.atuNbr)
        self.updateISYdrivers('all')
        self.ISYforced = True
       
    def start(self):


        return True


    def updateISYdrivers(self, level):
        LOGGER.debug('ATU updateISYdrivers')
        for ISYdriver in self.drivers:
            ISYkey = ISYdriver['driver']
            if level == 'active':
                temp = self.messana.getAtuMessanaISYkey(ISYkey, self.atuNbr)
                if temp in self.atu_ActiveKeys:                    
                    LOGGER.debug('Messana ATU ISYdrivers ACTIVE ' + temp)
                    status, value = self.messana.getAtuISYValue(ISYkey, self.atuNbr)
                    if status:
                        if self.ISYforced:
                            self.setDriver(ISYdriver, value, report = True, force = False)
                        else:
                            self.setDriver(ISYdriver, value, report = True, force = True)
                        LOGGER.debug('driver updated :' + ISYdriver['driver'] + ' =  '+str(value))
                    else:
                        LOGGER.debug('Error getting ' + ISYdriver['driver'])
            elif level == 'all':
                temp = self.messana.getAtuMessanaISYkey(ISYkey, self.atuNbr)
                status, value = self.messana.getAtuISYValue(ISYkey, self.atuNbr)
                LOGGER.debug('Messana ATU ISYdrivers ALL ' + temp)
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
        LOGGER.debug('stop - Messana ATU Cleaning up')

    def shortPoll(self):
        LOGGER.debug('Messana ATU shortPoll - atu '+ str(self.atuNbr))
        self.messana.updateAtuData('active', self.atuNbr)
        self.updateISYdrivers('active')
                   
    def longPoll(self):
        LOGGER.debug('Messana ATU longPoll - atu ' + str(self.atuNbr))
        self.messana.updateAtuData('all', self.atuNbr)
        self.updateISYdrivers('all')
        self.reportDrivers()

    def query(self, command=None):
        LOGGER.debug('TOP querry')

    def setStatus(self, command):
        LOGGER.debug('setStatus Called')
        value = int(command.get('value'))
        LOGGER.debug('ATU'+str(self.atuNbr)+' setStatus Received:' + str(value))
        if self.messana.atuetStatus(value, self.atuNbr):
            ISYdriver = self.messana.getatutatusISYdriver(self.atuNbr)
            self.setDriver(ISYdriver, value, report = True)



    def setEnergySave(self, command):
        LOGGER.debug('setEnergySave Called')
        value = int(command.get('value'))
        LOGGER.debug('ATU'+str(self.atuNbr)+' setEnergySave Received:' + str(value))
        if self.messana.atuetEnergySave(value, self.atuNbr):
            ISYdriver = self.messana.getAtuEnergySaveISYdriver(self.atuNbr)
            self.setDriver(ISYdriver, value, report = True)


    def setSetpoint(self, command):
        LOGGER.debug('setSetpoint Called')
        value = int(command.get('value'))
        LOGGER.debug('ATU'+str(self.atuNbr)+' setSetpoint Received:' + str(value))
        if self.messana.atuetSetpoint(value, self.atuNbr):
            ISYdriver = self.messana.getatuetPointISYdriver(self.atuNbr)
            self.setDriver(ISYdriver, value, report = True)


    def enableSchedule(self, command):
        LOGGER.debug('EnSchedule Called')
        value = int(command.get('value'))
        LOGGER.debug('ATU'+str(self.atuNbr)+' EnSchedule Reeived:' + str(value))      
        if self.messana.atuEnableSchedule(value, self.atuNbr):
            ISYdriver = self.messana.getAtuEnableScheduleISYdriver(self.atuNbr)
            self.setDriver(ISYdriver, value, report = True)     
        
        #self.atuInfo['mScheduleOn'] = val
        #self.messana.pushAtuData(self.atuNbr, self.atuInfo)
        #self.checkSetDriver('GV3', 'mScheduleOn')

 

    commands = { 'SET_SETPOINT': setSetpoint
                ,'SET_STATUS': setStatus
                ,'SET_ENERGYSAVE': setEnergySave
                ,'SET_SCHEDULE' : enableSchedule 
                }

    drivers = [  ]

