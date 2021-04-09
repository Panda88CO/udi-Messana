#!/usr/bin/env python3

import polyinterface
from subprocess import call
import json
from collections import defaultdict
#from MessanaInfo import MessanaInfo


LOGGER = polyinterface.LOGGER
#self, controller, primary, address, name, nodeType, nodeNbr, messana
class messanaAtu(polyinterface.Node):
    def __init__(self, controller, primary, address, name,  atuNbr):
        super().__init__(controller, primary, address, name)
        LOGGER.info('_init_ Messana atu ' + str(atuNbr) )
        self.atuNbr = atuNbr
        self.name = name
        self.address = address 
        self.messana = self.parent.messana
        self.id = self.messana.getAtuAddress(atuNbr)

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

        #self.messana.updateAtuData('all', self.atuNbr)
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

    def atuSetStatus(self, command):
        LOGGER.debug('atuSetStatus Called')
        value = int(command.get('value'))
        LOGGER.debug('ATU'+str(self.atuNbr)+' setStatus Received:' + str(value))
        if self.messana.atuSetStatus(value, self.atuNbr):
            ISYdriver = self.messana.getAtuStatusISYdriver(self.atuNbr)
            self.setDriver(ISYdriver, value, report = True)


    def atuSetEnergySave(self, command):
        LOGGER.debug('atuSetEnergySave Called')
        value = int(command.get('value'))
        LOGGER.debug('ATU'+str(self.atuNbr)+' setEnergySave Received:' + str(value))
        if self.messana.atuSetEnergySave(value, self.atuNbr):
            ISYdriver = self.messana.getAtuEnergySaveISYdriver(self.atuNbr)
            self.setDriver(ISYdriver, value, report = True)


    def atuSetSetpoint(self, command):
        LOGGER.debug('atuSetSetpoint Called')
        value = int(command.get('value'))
        LOGGER.debug('ATU'+str(self.atuNbr)+' setSetpoint Received:' + str(value))
        if self.messana.atuSetSetpoint(value, self.atuNbr):
            ISYdriver = self.messana.getAtuSetPointISYdriver(self.atuNbr)
            self.setDriver(ISYdriver, value, report = True)


    def atuEnableSchedule(self, command):
        LOGGER.debug('atuEnableSchedule Called')
        value = int(command.get('value'))
        LOGGER.debug('ATU'+str(self.atuNbr)+' EnSchedule Reeived:' + str(value))      
        if self.messana.atuEnableSchedule(value, self.atuNbr):
            ISYdriver = self.messana.getAtuEnableScheduleISYdriver(self.atuNbr)
            self.setDriver(ISYdriver, value, report = True)     
        


    def atuUpdate(self, command):
        LOGGER.debug(' atuUpdate Not implemented yet')
        return True

    def atuHRV(self, command):
        LOGGER.debug('atuHRV not implemented yet')
        return True

    def atuFlowlevel(self, command):
        LOGGER.debug('atu FlowLevel not implemented yet')
        return True

    def atuHUM(self, command):
        LOGGER.debug('atuHUM Not implemented yet')
        return True

    def atuINT(self, command):
        LOGGER.debug('atuINT Not implemented yet')
        return True
    
    def atuNTD(self, command):
        LOGGER.debug('atuNTD Not implemented yet')
        return True

    def atuHumSetpointRH(self, command):
        LOGGER.debug('atuHumSetpointRH Not implemented yet')
        return True


    def atuHumSetpointDP(self, command):
        LOGGER.debug('atuHumSetpointDP Not implemented yet')
        return True

    def atuDehumSetpointRH(self, command):
        LOGGER.debug('Not implemented yet')
        return True

    def atuDehumSetpointDP(self, command):
        LOGGER.debug('atuDehumSetpointRH Not implemented yet')
        return True

    def atuCurrentSetpointRH(self, command):
        LOGGER.debug('atuCurrentSetpointRH Not implemented yet')
        return True

    def atuCurrentSetpointDP(self, command):
        LOGGER.debug('atuCurrentSetpointDP Not implemented yet')
        return True

    commands = { 'SET_SETPOINT': atuSetSetpoint
                ,'SET_STATUS': atuSetStatus
                ,'SET_ENERGYSAVE': atuSetEnergySave
                ,'SET_SCHEDULE' : atuEnableSchedule
                ,'UPDATE': atuUpdate
                ,'SETHRV_ON': atuHRV
                ,'SET_FLOWLEVEL': atuFlowlevel
                ,'SET_HUM' : atuHUM
                ,'SET_INT' : atuINT
                ,'SET_NTD' : atuNTD
                ,'SET_HUM_SP_RH' : atuHumSetpointRH
                ,'SET_HUM_SP_DP' : atuHumSetpointDP
                ,'SET_DEHUM_SP_RH' : atuDehumSetpointRH
                ,'SET_DEHUM_SP_DP' :atuDehumSetpointDP
                ,'SET_CURR_SP_RH' : atuCurrentSetpointRH
                ,'SET_CURR_SP_DP' : atuCurrentSetpointDP
                }



