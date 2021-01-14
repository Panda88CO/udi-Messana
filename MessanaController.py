#!/usr/bin/env python3

import polyinterface
from subprocess import call
import json
import sys
from collections import defaultdict
from MessanaInfoPlay import MessanaInfo
from MessanaZones import MessanaZones
import shutil

LOGGER = polyinterface.LOGGER
               
class MessanaController(polyinterface.Controller):

    def __init__(self, polyglot):
        super().__init__(polyglot)
        LOGGER.info('_init_')
        self.messanaImportOK = 0
        self.name = 'Messana Main Control'
        self.address ='messanasys'
        self.primary = self.address
        self.hb = 0
        self.reportDrivers()
        self.ISYdrivers=[]
        self.ISYcommands = {}
        self.ISYTempUnit = 0
        #try:
        self.messana = MessanaInfo('192.168.2.65', '9bf711fc-54e2-4387-9c7f-991bbb02ab3a', MessanaController.id )
        LOGGER.debug('MessanaInfo call done')

        self.system_GETKeys = self.messana.systemPullKeys()
        self.system_PUTKeys = self.messana.systemPushKeys()
        self.system_ActiveKeys = self.messana.systemActiveKeys()
        
        self.messana.updateSystemData('all')
        self.messana.addSystemDefStruct(self.address)
    
        LOGGER.debug('Install Updated profile')
        self.poly.installprofile()

        LOGGER.debug('Append drivers')
        for key in self.system_GETKeys:
            temp = self.messana.getSystemISYdriverInfo(key)
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
                MessanaController.drivers.append(temp)
                LOGGER.debug(str(MessanaController.drivers) + 'after append')                       
        LOGGER.debug(MessanaController.drivers)
        #self.check_params()
        #self.discover()   
        
        self.updateInfo('all')
        self.messanaImportOK = 1
        #except:
            #LOGGER.debug('Reading data from Messana System NOT successful')
                
    def start(self):
        LOGGER.info('Start  Messana Main')

 
    def stop(self):
        LOGGER.debug('stop - Cleaning up')

    def heartbeat(self):
        LOGGER.debug('heartbeat: hb={}'.format(self.hb))
        if self.hb == 0:
            self.reportCmd('DON',2)
            self.hb = 1
        else:
            self.reportCmd('DOF',2)
            self.hb = 0


    def shortPoll(self):
        LOGGER.debug('Messane Controller shortPoll')
        if self.messanaImportOK == 1:
            LOGGER.debug('Short Poll System Up')
            self.messana.updateSystemData('active')
            self.reportDrivers()
            '''
            for node in self.nodes:
                if node != self.address:
                    self.nodes[node].updateInfo()
            '''
        
    def pullAllMessanaStatus(self):
        return(True)

    def longPoll(self):
        LOGGER.debug('Messana Controller longPoll')
        if self.messanaImportOK == 1:
            LOGGER.debug('Long Poll System Up')
            self.heartbeat()
            #self.messana.pullAllMessanaStatus() #update from Messana to internal structure
            self.messana.updateSystemData('all')
            self.reportDrivers()
            #for node in self.nodes:
            #    if node != self.address:
            #        self.nodes[node].updateInfo()
        

    def query(self, command=None):
        LOGGER.debug('TOP querry')
        self.messana.updateSystemData('all')
        self.reportDrivers()

    def discover(self, command=None):
        LOGGER.debug('discover')
        #LOGGER.info('Adding Zones' + str(self.msysInfo['mZoneCount']))

        '''
        for zoneNbr in range(0,self.msysInfo['mZoneCount']):
            zoneKeys = []
            zoneKeys = self.messana.zonePullKeys(zoneNbr)
            if 'mName' in zoneKeys:
                name = str(self.messana.pullZoneDataIndividual(zoneNbr, 'mName'))
                address = 'zone'+str(zoneNbr)
                LOGGER.debug('zone ' + str(zoneNbr) + ' : name, Address' + name +' ' + address) 
                if not address in self.nodes:
                    self.addNode(MessanaZones(self, self.address, address, name, zoneNbr, self.messana))

        '''   
        #count = 0
        '''for mySensor in self.mySensors.get_available_sensors():
            count = count+1
            currentSensor = mySensor.id.lower() 
            LOGGER.info(currentSensor+ 'Sensor Serial Number Detected - use Custom Params to rename')
            address = 'rpitemp'+str(count)
            # check if sensor serial number exist in custom parapms and then replace name
            if currentSensor in self.polyConfig['customParams']:
               LOGGER.debug('A customParams name for sensor detected')
               name = self.polyConfig['customParams'][currentSensor]
            else:
               LOGGER.debug('Default Naming')
               name = 'Sensor'+str(count)
            #LOGGER.debug( address + ' '+ name + ' ' + currentSensor)
            if not address in self.nodes:
               self.addNode(TEMPsensor(self, self.address, address, name, currentSensor))
        '''

    '''
        for out_pin in RELAY_IO_PINS :
            LOGGER.info( ' gpio output :' + str(out_pin))
            address = 'outpin'+  str(out_pin)
            name = 'pin' + str(out_pin)
            LOGGER.debug( address + ' ' + name + ' ' + str(out_pin))
            if not address in self.nodes:
               LOGGER.debug('GPIO out'+ self.address +' ' + address + ' ' + name  )
               self.addNode(GPOUTcontrol(self, self.address, address, name, out_pin))
               GPIO.setup(int(out_pin), GPIO.OUT) 

        for in_pin in INPUT_PINS :
            LOGGER.info( ' gpio input :' + str(in_pin))
            address = 'inpin'+  str(in_pin)
            name = 'pin' + str(in_pin)
            LOGGER.debug( address + ' ' + name + ' ' + str(in_pin))
            if not address in self.nodes:
               LOGGER.debug('GPIO in'+ self.address +' ' + address + ' ' + name  )
               self.addNode(GPINcontrol(self, self.address, address, name, in_pin))
               GPIO.setup(int(in_pin), GPIO.IN)   
    '''

    def check_params(self, command=None):
        LOGGER.debug('Check Params')

    
    def ISYupdate (self):
        LOGGER.info('ISY-update called')
        self.updateInfo('all')


    def updateInfo(self, level):
        LOGGER.info('Update Messana System ')
        if level == 'active':
            for mKey in self.system_ActiveKeys: 
                LOGGER.debug('active ' + mKey)
                self.updateParamsToISY(mKey)
                
        elif level == 'all':
             for mKey in self.system_GETKeys: 
                self.updateParamsToISY(mKey)
                LOGGER.debug('all ' + mKey)
        else:
            LOGGER.debug('unknown level' + level)

#need to debug 
    def checkSetDriver(self, ISYkey, mKey, val):
        LOGGER.debug('checkset driver ' + ISYkey + ' ,' + mKey)
        if mKey in self.system_GETKeys:
            if mKey == 'mUnitTemp': 
                valInfo = self.messana.pullSystemDataIndividual(mKey)
                if valInfo['statusOK']:
                    ISYval = valInfo['data']        
                    #"we cannot handle strings"
                    if ISYval in  ['Celcius', 'Fahrenheit']:
                       if ISYval == 'Celcius':
                          val = 0
                       else:
                          val = 1 
            self.setDriver(ISYkey, val)   

    def setParamFromISY(self, mKey, val):
        LOGGER.debug('setParamFromISY')
        if self.messana.pushSystemDataIndividual(mKey, val):
            LOGGER.info(mKey + ' updated to '+ str(val))
            temp = self.messana.getSystemISYdriverInfo(mKey)
            if temp != {}:
                LOGGER.debug('update ISY value')
                ISYkey = temp['driver']
                valInfo = self.messana.pullSystemDataIndividual(mKey)
                if valInfo['statusOK']:
                    ISYval = valInfo['data']                    
                    LOGGER.debug('ISYkey, ISYval:' + ISYkey+ ', ' + str(ISYval))
                    self.checkSetDriver(ISYkey, mKey, ISYval)
        else:
            LOGGER.info(mKey + ' update failed')

    def updateParamsToISY(self, mKey):
        LOGGER.debug('setParamFromISY')
        temp = self.messana.getSystemISYdriverInfo(mKey)
        if temp != {}:
            LOGGER.debug('update ISY value')
            ISYkey = temp['driver']
            valInfo = self.messana.pullSystemDataIndividual(mKey)
            if valInfo['statusOK']:
                ISYval = valInfo['data']
                LOGGER.debug('ISYkey, ISYval:' + ISYkey+ ', ' + str(ISYval))
                self.checkSetDriver(ISYkey, mKey, ISYval)
        else:
            LOGGER.info(mKey + ' update failed')

    def setStatus(self, command):
        LOGGER.debug('set Status Called')
        val = int(command.get('value'))
        mKey = 'mStatus'
        LOGGER.debug('set Status Recived:' + str(val))
        self.setParamFromISY(mKey, val)

        
    def setEnergySave(self, command):
        LOGGER.debug('setEnergySave Called')
        val = int(command.get('value'))
        mKey = 'mEnergySaving'
        LOGGER.debug('SetEnergySave Recived:' + str(val))
        self.setParamFromISY(mKey, val)


    def setSetback(self, command):
        LOGGER.debug('setSetback Called')
        val = int(command.get('value'))
        mKey = 'mSetback'
        LOGGER.debug('setSetback Reeived:' + str(val))
        self.setParamFromISY(mKey, val)

    id = 'system'
    drivers = []
    commands = { 'UPDATE': ISYupdate
                ,'SET_STATUS': setStatus
                ,'SET_ENERGYSAVE': setEnergySave
                ,'SET_SETBACK' : setSetback 
                }

  
if __name__ == "__main__":
    try:
        LOGGER.info('Starting Messana Controller')
        polyglot = polyinterface.Interface('Messana_Control')
        polyglot.start()
        control = MessanaController(polyglot)
        control.runForever()
    except (KeyboardInterrupt, SystemExit):
        sys.exit(0)
