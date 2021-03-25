#!/usr/bin/env python3

import polyinterface
from subprocess import call

LOGGER = polyinterface.LOGGER
#self, controller, primary, address, name, nodeType, nodeNbr, messana
class messanaMacrozone(polyinterface.Node):
    def __init__(self, controller, primary, address, name,  macrozoneNbr):
        super().__init__(controller, primary, address, name)
        LOGGER.info('_init_ Messana Macrozone ' + str(macrozoneNbr) )
        self.macrozoneNbr = macrozoneNbr
        self.name = name
        self.address = address 
        self.messana = self.parent.messana
        
        self.id =  self.messana.getMacrozoneAddress(self.macrozoneNbr)
        
        self.macrozone_GETKeys = self.messana.macrozonePullKeys(self.macrozoneNbr)
        self.macrozone_PUTKeys = self.messana.macrozonePushKeys(self.macrozoneNbr)
        self.macrozone_ActiveKeys = self.messana.macrozoneActiveKeys(self.macrozoneNbr)
        self.ISYforced = False
        
        self.drivers = []
        for key in self.macrozone_GETKeys:
            self.temp = self.messana.getMacrozoneISYdriverInfo(key, self.macrozoneNbr)
            if  self.temp != {}:
                self.drivers.append(self.temp)
                LOGGER.debug(  'driver:  ' +  self.temp['driver'])
        self.messana.updateMacrozoneData('all', self.macrozoneNbr)
        self.updateISYdrivers('all')
        self.ISYforced = True
       
    def start(self):


        return True


    def updateISYdrivers(self, level):
        LOGGER.debug('Macrozone updateISYdrivers')
        for ISYdriver in self.drivers:
            ISYkey = ISYdriver['driver']
            if level == 'active':
                temp = self.messana.getMacrozoneMessanaISYkey(ISYkey, self.macrozoneNbr)
                if temp in self.zone_ActiveKeys:                    
                    LOGGER.debug('Messana Macrozone ISYdrivers ACTIVE ' + temp)
                    status, value = self.messana.getMacrozoneISYValue(ISYkey, self.macrozoneNbr)
                    if status:
                        if self.ISYforced:
                            self.setDriver(ISYdriver, value, report = True, force = False)
                        else:
                            self.setDriver(ISYdriver, value, report = True, force = True)
                        LOGGER.debug('driver updated :' + ISYdriver['driver'] + ' =  '+str(value))
                    else:
                        LOGGER.debug('Error getting ' + ISYdriver['driver'])
            elif level == 'all':
                temp = self.messana.getMacrozoneMessanaISYkey(ISYkey, self.macrozoneNbr)
                status, value = self.messana.getMacrooneISYValue(ISYkey, self.macrozoneNbr)
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
        LOGGER.debug('Messana Zone shortPoll - zone '+ str(self.macrozoneNbr))
        self.messana.updateMacrozoneData('active', self.macrozoneNbr)
        self.updateISYdrivers('active')
                   
    def longPoll(self):
        LOGGER.debug('Messana Zone longPoll - zone ' + str(self.macrozoneNbr))
        self.messana.updateMacrozoneData('all', self.macrozoneNbr)
        self.updateISYdrivers('all')
        self.reportDrivers()

    def query(self, command=None):
        LOGGER.debug('TOP querry')

    def setStatus(self, command):
        LOGGER.debug('setStatus Called')
        value = int(command.get('value'))
        LOGGER.debug('Zone'+str(self.zoneNbr)+' setStatus Received:' + str(value))
        if self.messana.zoneSetStatus(value, self.zoneNbr):
            ISYdriver = self.messana.getZoneStatusISYdriver(self.zoneNbr)
            self.setDriver(ISYdriver, value, report = True)



    def setEnergySave(self, command):
        LOGGER.debug('setEnergySave Called')
        value = int(command.get('value'))
        LOGGER.debug('Zone'+str(self.zoneNbr)+' setEnergySave Received:' + str(value))
        if self.messana.zoneSetEnergySave(value, self.zoneNbr):
            ISYdriver = self.messana.getZoneEnergySaveISYdriver(self.zoneNbr)
            self.setDriver(ISYdriver, value, report = True)


    def setSetpoint(self, command):
        LOGGER.debug('setSetpoint Called')
        value = int(command.get('value'))
        LOGGER.debug('Zone'+str(self.zoneNbr)+' setSetpoint Received:' + str(value))
        if self.messana.zoneSetSetpoint(value, self.zoneNbr):
            ISYdriver = self.messana.getZoneSetPointISYdriver(self.zoneNbr)
            self.setDriver(ISYdriver, value, report = True)


    def enableSchedule(self, command):
        LOGGER.debug('EnSchedule Called')
        value = int(command.get('value'))
        LOGGER.debug('Zone'+str(self.zoneNbr)+' EnSchedule Reeived:' + str(value))      
        if self.messana.zoneEnableSchedule(value, self.zoneNbr):
            ISYdriver = self.messana.getZoneEnableScheduleISYdriver(self.zoneNbr)
            self.setDriver(ISYdriver, value, report = True)     
        
    def ISYupdate(self, command):
        self.messana.updateMacrozoneData('all', self.macrozoneNbr)
        self.updateISYdrivers('all')
        self.reportDrivers()
 

    commands = { 'SET_SETPOINT': setSetpoint
                ,'SET_STATUS': setStatus
                ,'UPDATE': ISYupdate
                ,'SET_SCHEDULEON' : enableSchedule 
                }



