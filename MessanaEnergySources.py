#!/usr/bin/env python3

import polyinterface
from subprocess import call
import json
from collections import defaultdict
#from MessanaInfo import MessanaInfo

LOGGER = polyinterface.LOGGER
#self, controller, primary, address, name, nodeType, nodeNbr, messana
class messanaEnergySource(polyinterface.Node):
    def __init__(self, controller, primary, address, name,  energySourceNbr):
        super().__init__(controller, primary, address, name)
        LOGGER.info('_init_ Messana EnergySource ' + str(energySourceNbr) )
        self.energySourceNbr = energySourceNbr
        self.name = name
        self.address = address 
        self.id = 'energysource'+str(energySourceNbr)
        self.messana = self.parent.messana
        self.energySource_GETKeys = self.messana.energySourcePullKeys(self.energySourceNbr)
        self.energySource_PUTKeys = self.messana.energySourcePushKeys(self.energySourceNbr)
        self.energySource_ActiveKeys = self.messana.energySourceActiveKeys(self.energySourceNbr)
        self.ISYforced = False
        
        self.drivers = []
        for key in self.energySource_GETKeys:
            self.temp = self.messana.getEnergySourceISYdriverInfo(key, self.energySourceNbr)
            if  self.temp != {}:
                self.drivers.append(self.temp)
                LOGGER.debug(  'driver:  ' +  self.temp['driver'])
        self.messana.updateEnergySourceData('all', self.energySourceNbr)
        self.updateISYdrivers('all')
        self.ISYforced = True
       
    def start(self):


        return True


    def updateISYdrivers(self, level):
        LOGGER.debug('EnergySource updateISYdrivers')
        for ISYdriver in self.drivers:
            ISYkey = ISYdriver['driver']
            if level == 'active':
                temp = self.messana.getEnergySourceMessanaISYkey(ISYkey, self.energySourceNbr)
                if temp in self.energySource_ActiveKeys:                    
                    LOGGER.debug('Messana EnergySource ISYdrivers ACTIVE ' + temp)
                    status, value = self.messana.getEnergySourceISYValue(ISYkey, self.energySourceNbr)
                    if status:
                        if self.ISYforced:
                            self.setDriver(ISYdriver, value, report = True, force = False)
                        else:
                            self.setDriver(ISYdriver, value, report = True, force = True)
                        LOGGER.debug('driver updated :' + ISYdriver['driver'] + ' =  '+str(value))
                    else:
                        LOGGER.debug('Error getting ' + ISYdriver['driver'])
            elif level == 'all':
                temp = self.messana.getEnergySourceMessanaISYkey(ISYkey, self.energySourceNbr)
                status, value = self.messana.getEnergySourceISYValue(ISYkey, self.energySourceNbr)
                LOGGER.debug('Messana EnergySource ISYdrivers ALL ' + temp)
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
        LOGGER.debug('stop - Messana EnergySource Cleaning up')

    def shortPoll(self):
        LOGGER.debug('Messana EnergySource shortPoll - energySource '+ str(self.energySourceNbr))
        self.messana.updateEnergySourceData('active', self.energySourceNbr)
        self.updateISYdrivers('active')
                   
    def longPoll(self):
        LOGGER.debug('Messana EnergySource longPoll - energySource ' + str(self.energySourceNbr))
        self.messana.updateEnergySourceData('all', self.energySourceNbr)
        self.updateISYdrivers('all')
        self.reportDrivers()

    def query(self, command=None):
        LOGGER.debug('TOP querry')

    def setStatus(self, command):
        LOGGER.debug('setStatus Called')
        value = int(command.get('value'))
        LOGGER.debug('EnergySource'+str(self.energySourceNbr)+' setStatus Received:' + str(value))
        if self.messana.energySourceSetStatus(value, self.energySourceNbr):
            ISYdriver = self.messana.getEnergySourceStatusISYdriver(self.energySourceNbr)
            self.setDriver(ISYdriver, value, report = True)



    def setEnergySave(self, command):
        LOGGER.debug('setEnergySave Called')
        value = int(command.get('value'))
        LOGGER.debug('EnergySource'+str(self.energySourceNbr)+' setEnergySave Received:' + str(value))
        if self.messana.energySourceSetEnergySave(value, self.energySourceNbr):
            ISYdriver = self.messana.getEnergySourceEnergySaveISYdriver(self.energySourceNbr)
            self.setDriver(ISYdriver, value, report = True)


    def setSetpoint(self, command):
        LOGGER.debug('setSetpoint Called')
        value = int(command.get('value'))
        LOGGER.debug('EnergySource'+str(self.energySourceNbr)+' setSetpoint Received:' + str(value))
        if self.messana.energySourceSetSetpoint(value, self.energySourceNbr):
            ISYdriver = self.messana.getEnergySourceSetPointISYdriver(self.energySourceNbr)
            self.setDriver(ISYdriver, value, report = True)


    def enableSchedule(self, command):
        LOGGER.debug('EnSchedule Called')
        value = int(command.get('value'))
        LOGGER.debug('EnergySource'+str(self.energySourceNbr)+' EnSchedule Reeived:' + str(value))      
        if self.messana.energySourceEnableSchedule(value, self.energySourceNbr):
            ISYdriver = self.messana.getEnergySourceEnableScheduleISYdriver(self.energySourceNbr)
            self.setDriver(ISYdriver, value, report = True)     
        
        #self.energySourceInfo['mScheduleOn'] = val
        #self.messana.pushEnergySourceData(self.energySourceNbr, self.energySourceInfo)
        #self.checkSetDriver('GV3', 'mScheduleOn')

 

    commands = { 'SET_SETPOINT': setSetpoint
                ,'SET_STATUS': setStatus
                ,'SET_ENERGYSAVE': setEnergySave
                ,'SET_SCHEDULE' : enableSchedule 
                }

    drivers = [  ]

