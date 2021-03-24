#!/usr/bin/env python3

import polyinterface
from subprocess import call
import json
from collections import defaultdict
#from MessanaInfo import MessanaInfo

LOGGER = polyinterface.LOGGER
#self, controller, primary, address, name, nodeType, nodeNbr, messana
class messanaBufTank(polyinterface.Node):
    def __init__(self, controller, primary, address, name,  bufTankNbr):
        super().__init__(controller, primary, address, name)
        LOGGER.info('_init_ Messana BufferTanks ' + str(bufTankNbr) )
        self.bufTankNbr = bufTankNbr
        self.name = name
        self.address = address 
        self.id = 'buffertanks'+str(bufTankNbr)
        self.messana = self.parent.messana
        self.bufferTank_GETKeys = self.messana.bufferTankPullKeys(self.bufTankNbr)
        self.bufferTank_PUTKeys = self.messana.bufferTankPushKeys(self.bufTankNbr)
        self.bufferTank_ActiveKeys = self.messana.bufferTankActiveKeys(self.bufTankNbr)
        self.ISYforced = False
        
        self.drivers = []
        for key in self.bufferTank_GETKeys:
            self.temp = self.messana.getBufferTankISYdriverInfo(key, self.bufTankNbr)
            if  self.temp != {}:
                self.drivers.append(self.temp)
                LOGGER.debug(  'driver:  ' +  self.temp['driver'])
        self.messana.updateBufferTankData('all', self.bufTankNbr)
        self.updateISYdrivers('all')
        self.ISYforced = True
       
    def start(self):


        return True


    def updateISYdrivers(self, level):
        LOGGER.debug('BufferTanks updateISYdrivers')
        for ISYdriver in self.drivers:
            ISYkey = ISYdriver['driver']
            if level == 'active':
                temp = self.messana.getBufferTankMessanaISYkey(ISYkey, self.bufTankNbr)
                if temp in self.bufferTank_ActiveKeys:                    
                    LOGGER.debug('Messana BufferTanks ISYdrivers ACTIVE ' + temp)
                    status, value = self.messana.getBufferTankISYValue(ISYkey, self.bufTankNbr)
                    if status:
                        if self.ISYforced:
                            self.setDriver(ISYdriver, value, report = True, force = False)
                        else:
                            self.setDriver(ISYdriver, value, report = True, force = True)
                        LOGGER.debug('driver updated :' + ISYdriver['driver'] + ' =  '+str(value))
                    else:
                        LOGGER.debug('Error getting ' + ISYdriver['driver'])
            elif level == 'all':
                temp = self.messana.getBufferTankMessanaISYkey(ISYkey, self.bufTankNbr)
                status, value = self.messana.getBufferTankISYValue(ISYkey, self.bufTankNbr)
                LOGGER.debug('Messana BufferTanks ISYdrivers ALL ' + temp)
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
        LOGGER.debug('stop - Messana BufferTanks Cleaning up')

    def shortPoll(self):
        LOGGER.debug('Messana BufferTanks shortPoll - buffer tanks '+ str(self.bufTankNbr))
        self.messana.updateBufferTankData('active', self.bufTankNbr)
        self.updateISYdrivers('active')
                   
    def longPoll(self):
        LOGGER.debug('Messana BufferTanks longPoll - buffer tanks ' + str(self.bufTankNbr))
        self.messana.updateBufferTankData('all', self.bufTankNbr)
        self.updateISYdrivers('all')
        self.reportDrivers()

    def query(self, command=None):
        LOGGER.debug('TOP querry')

    def setStatus(self, command):
        LOGGER.debug('setStatus Called')
        value = int(command.get('value'))
        LOGGER.debug('BufferTanks'+str(self.bufTankNbr)+' setStatus Received:' + str(value))
        if self.messana.bufferTankSetStatus(value, self.bufTankNbr):
            ISYdriver = self.messana.getBufferTankStatusISYdriver(self.bufTankNbr)
            self.setDriver(ISYdriver, value, report = True)



    def setEnergySave(self, command):
        LOGGER.debug('setEnergySave Called')
        value = int(command.get('value'))
        LOGGER.debug('BufferTanks'+str(self.bufTankNbr)+' setEnergySave Received:' + str(value))
        if self.messana.bufferTankSetEnergySave(value, self.bufTankNbr):
            ISYdriver = self.messana.getBufferTankEnergySaveISYdriver(self.bufTankNbr)
            self.setDriver(ISYdriver, value, report = True)


    def setSetpoint(self, command):
        LOGGER.debug('setSetpoint Called')
        value = int(command.get('value'))
        LOGGER.debug('BufferTanks'+str(self.bufTankNbr)+' setSetpoint Received:' + str(value))
        if self.messana.bufferTankSetSetpoint(value, self.bufTankNbr):
            ISYdriver = self.messana.getBufferTankSetPointISYdriver(self.bufTankNbr)
            self.setDriver(ISYdriver, value, report = True)


    def enableSchedule(self, command):
        LOGGER.debug('EnSchedule Called')
        value = int(command.get('value'))
        LOGGER.debug('BufferTanks'+str(self.bufTankNbr)+' EnSchedule Reeived:' + str(value))      
        if self.messana.bufferTankEnableSchedule(value, self.bufTankNbr):
            ISYdriver = self.messana.getBufferTankEnableScheduleISYdriver(self.bufTankNbr)
            self.setDriver(ISYdriver, value, report = True)     
        
        #self.bufferTankInfo['mScheduleOn'] = val
        #self.messana.pushBufferTankData(self.bufTankNbr, self.bufferTankInfo)
        #self.checkSetDriver('GV3', 'mScheduleOn')

 

    commands = { 'SET_SETPOINT': setSetpoint
                ,'SET_STATUS': setStatus
                ,'SET_ENERGYSAVE': setEnergySave
                ,'SET_SCHEDULE' : enableSchedule 
                }

    drivers = [  ]

