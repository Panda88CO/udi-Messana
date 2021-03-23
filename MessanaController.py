#!/usr/bin/env python3

import polyinterface
from subprocess import call
import json
import sys
from collections import defaultdict
from MessanaInfoPlay import messanaInfo
from MessanaZone import messanaZone
import shutil


LOGGER = polyinterface.LOGGER
               
class MessanaController(polyinterface.Controller):

    def __init__(self, messanaName):
        super(MessanaController, self).__init__(polyglot)
        LOGGER.info('_init_ Messsana Controller')
        self.messanaImportOK = 0
        self.ISYforced = False
        self.name = 'MessanaMain' # must be less than 14 characters
        self.address ='messanasys'
        LOGGER.debug('Name/address: '+ self.name + ' ' + self.address)
        self.primary = self.address
        self.hb = 0
        self.ISYdrivers=[]
        self.ISYcommands = {}
        self.ISYTempUnit = 0
        self.id = self.name
        self.drivers = []



    def defineInputParams(self):
        self.removeNoticesAll()
        self.addNotice('Please Set IP address (IP_ADDRESS) and Messana Key (MESSANA_KEY)')
        self.addNotice('Please restart node server after setting parameters')

        self.addNotice('Please Set IP address (IP_ADDRESS)')

        self.IPAddress = self.getCustomParam('IP_ADDRESS')
        if self.IPAddress is None:
            self.addNotice('Please Set IP address (IP_ADDRESS)')
            LOGGER.error('IP address not set')
            #self.IPAddress= '192.168.2.65'
            #self.addCustomParam({'IP_ADDRESS': self.IPAddress})
        
        if self.MessanaKey is None:
            self.addNotice('Please Set IP Messana Key (MESSANA_KEY)')
            LOGGER.error('check_params: Messana Key not specified')
            #self.MessanaKey =  '9bf711fc-54e2-4387-9c7f-991bbb02ab3a'
            #self.addCustomParam({'MESSANA_KEY': self.MessanaKey})
        self.addNotice('Please restart Node server after setting the parameters')



    def start(self):
        LOGGER.info('Start  Messana Main NEW')
        self.IPAddress = self.getCustomParam('IP_ADDRESS')
        self.MessanaKey = self.getCustomParam('MESSANA_KEY')

        if (self.IPAddress is None) or (self.MessanaKey is None):
            self.defineInputParams()
            self.stop()

        else:
            LOGGER.info('Retrieving info from Messana System')
            self.messana = messanaInfo( self.IPAddress, self.MessanaKey , self.name)
            self.messana.updateSystemData('all')
            self.systemGETKeys = self.messana.systemPullKeys()
            self.systemPUTKeys = self.messana.systemPushKeys()
            self.systemActiveKeys = self.messana.systemActiveKeys()
            
            
            for key in self.systemGETKeys:
                temp = self.messana.getSystemISYdriverInfo(key)
                if  temp != {}:
                    self.drivers.append(temp)
                    LOGGER.debug(  'driver:  ' +  temp['driver'])

            LOGGER.debug ('Install Profile')    
            self.poly.installprofile()
            LOGGER.debug('Install Profile done')
        self.updateISYdrivers('all')
        self.messanaImportOK = 1
        self.discover()


              


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
        LOGGER.debug('Messana Controller shortPoll')

        if self.messanaImportOK == 1:
            LOGGER.debug('Short Poll System Up')
            if self.ISYforced:
                self.messana.updateSystemData('active')
                self.updateISYdrivers('active')
            else:
                self.messana.updateSystemData('all')
                self.updateISYdrivers('all')
            self.ISYforced = True
            LOGGER.debug('ShoirtPOll nodes: ' + self.nodes )
            '''
            for node in self.nodes:
                if node != self.address:
                    self.nodes[node].shortPoll()
                    LOGGER.debug( ' shortPoll node: ' + node )
            '''

    def longPoll(self):
        LOGGER.debug('Messana Controller longPoll')
        if self.messanaImportOK == 1:
            self.heartbeat()
            self.messana.updateSystemData('all')
            LOGGER.debug( self.drivers)
            self.updateISYdrivers('all')
            self.reportDrivers()
            self.ISYforced = True
            for node in self.nodes:
                if node != self.address:
                    self.nodes[node].longPoll()
        
    def updateISYdrivers(self, level):
        LOGGER.debug('updateISYdrivers')
        for ISYdriver in self.drivers:
            ISYkey = ISYdriver['driver']
            if level == 'active':
                if self.messana.getMessanaSystemKey(ISYkey) in self.systemActiveKeys:
                    LOGGER.debug('MessanaController ISYdrivers ACTIVE ' + self.messana.getMessanaSystemKey(ISYkey))
                    status, value = self.messana.getSystemISYValue(ISYkey)
                    if status:
                        if self.ISYforced:
                            self.setDriver(ISYdriver, value, report = True, force = False)
                        else:
                            self.setDriver(ISYdriver, value, report = True, force = True)
                        LOGGER.debug('driver updated :' + ISYdriver['driver'] + ' =  '+str(value))
                    else:
                        LOGGER.debug('Error getting ' + ISYdriver['driver'])
            elif level == 'all':
                LOGGER.debug('MessanaController ISYdrivers ACTIVE ' + self.messana.getMessanaSystemKey(ISYkey))
                status, value = self.messana.getSystemISYValue(ISYkey)
                if status:
                    if self.ISYforced:
                        self.setDriver(ISYdriver, value, report = True, force = False)
                    else:
                        self.setDriver(ISYdriver, value, report = True, force = True)
                    LOGGER.debug('driver updated :' + ISYdriver['driver'] + ' =  '+str(value))
                else:
                    LOGGER.debug('Error getting ' + ISYdriver['driver'])
            else:
                 LOGGER.debug('Error!  Unknown level passed: ' + level)


    def query(self, command=None):
        LOGGER.debug('TOP querry')
        self.messana.updateSystemData('all')
        self.reportDrivers()

    def discover(self, command=None):
        LOGGER.debug('discover')
        nbrZones =  self.messana.getZoneCount()
        for zoneNbr in range(0,nbrZones):
            LOGGER.debug('Adding zone ' + str(zoneNbr))
            name = self.messana.getZoneName(zoneNbr)
            address = 'zones'+str(zoneNbr)
            LOGGER.debug('zone ' + str(zoneNbr) + ' : name, Address: ' + name +' ' + address) 
            if not address in self.nodes:
               self.addNode(messanaZone(self, self.address, address, name, zoneNbr))


        #nbrMacrozones = 0



    


    '''
    self.getMessanaSystemKeyVal('mMacrooneCount', nbrMacrozones)
    for macrozoneNbr in range(0,nbrMacrozones):
        macrozoneGETKeys = []
        macrozoneGETKeys = self.messana.macrozonePullKeys(macrozoneNbr)
        if 'mName' in macrozoneGETKeys:
            name = str(self.messana.pullMacroZoneDataIndividual(macrozoneNbr, 'mName'))
            address = 'macrozone'+str(zoneNbr)
            LOGGER.debug('macrozone ' + str(zoneNbr) + ' : name, Address' + name +' ' + address) 
            if not address in self.nodes:
                self.addNode(MessanaMacrozones(self, self.address, address, name, zoneNbr, self.messana))


    #nbrATUs = 0

    #nbrDHWs = 0
    
    #nbrFanCoils = 0
    
    #nbrEnergySources = 0

    #nbrHCCOs = 0

    #nbrBufTanks = 0

    '''    
    
    '''
    for zoneNbr in range(0,messana.mSystem['system']['data']['mZoneCount']):
        zoneData = {}
        messana.updateZoneData(zoneNbr)
        zoneGETkeys = messana.zonePullKeys(zoneNbr)
        print (zoneGETkeys)
        zonePUTkeys = messana.zonePushKeys(zoneNbr)
        print(zonePUTkeys)
        zoneActiveKeys = messana.zoneActiveKeys(zoneNbr)
        print (zoneActiveKeys)
        
        for mKey in zoneGETkeys:
            zoneData = messana.pullZoneDataIndividual(zoneNbr, mKey)
            if zoneData['statusOK']:
                print('GET: ' + mKey + str(zoneData['data']))
            if mKey in zoneActiveKeys:
                zoneData = messana.pullZoneDataIndividual(zoneNbr, mKey)
                if zoneData['statusOK']:
                    print('GET: ' + mKey + str(zoneData['data']))
            if mKey in zonePUTkeys:
                if mKey in messana.mSystem['zones']['data'][zoneNbr]:
                    nodeData = messana.pushZoneDataIndividual(zoneNbr, mKey, messana.mSystem['zones']['data'][zoneNbr][mKey])
                    print('PUT zones : ' + mKey + ' ' + str( messana.mSystem['zones']['data'][zoneNbr][mKey]))
                    print('nodeData : ' + str(nodeData))
    '''
    
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
    def checkSetDriver(self, ISYkey, mKey):
        LOGGER.debug('checkset driver ' + ISYkey + ' ,' + mKey)
        if mKey in self.keySet:
            valInfo = self.messana.pullSystemDataIndividual(mKey)
            if valInfo['statusOK']:
                val = valInfo['data']        
                if mKey == 'mUnitTemp': 
                    #"we cannot handle strings"
                    if val in  ['Celcius', 'Fahrenheit']:
                        if val == 'Celcius':
                            val = 0
                        else:  
                            val = 1 
                self.setDriver(ISYkey, val)
            return(True)
        else:
            return(False)



    def updateParamsToISY(self, mKey):
        LOGGER.debug('setSystemParamFromISY')
        temp = self.messana.getSystemISYdriverInfo(mKey)
        if temp != {}:
            LOGGER.debug('update ISY value')
            ISYkey = temp['driver']
            self.checkSetDriver(ISYkey, mKey)
        else:
            LOGGER.info(mKey + ' update failed')
           
    def setParamFromISY(self, mKey, val):
        LOGGER.debug('setParamFromISY')
        if self.messana.pushSystemDataIndividual(mKey, val):
            LOGGER.info(mKey + ' updated to '+ str(val))
            temp = self.messana.getSystemISYdriverInfo(mKey)
            if temp != {}:
                ISYkey = temp['driver']
                LOGGER.debug('update ISY value: ' + ISYkey + ', ' + mKey)
                self.checkSetDriver(ISYkey, mKey)
        else:
            LOGGER.info(mKey + ' update failed')

    def getMessanaSystemKeyVal(self, mKey, val):
        Info = self.messana.pullSystemDataIndividual(mKey)
        if mKey in self.system_GETKeys:
            if Info['statusOK']:
                val = Info['data']        
                if mKey == 'mUnitTemp': 
                    #"we cannot handle strings"
                    if val in  ['Celcius', 'Fahrenheit']:
                        if val == 'Celcius':
                            val = 0
                        else:  
                            val = 1 
            return(True)
        else:
            LOGGER.debug('Unknown key: ' + mKey)
            
    '''


    def check_params(self, command=None):
        LOGGER.debug('Check Params')


 
    def setStatus(self, command):
        LOGGER.debug('set Status Called')
        value = int(command.get('value'))
        LOGGER.debug('set Status Recived:' + str(value))
        if self.messana.systemSetStatus(value):
            ISYdriver = self.messana.getSystemStatusISYdriver()
            self.setDriver(ISYdriver, value, report = True)

    def setEnergySave(self, command):
        LOGGER.debug('setEnergySave Called')
        value = int(command.get('value'))
        LOGGER.debug('SetEnergySave Recived:' + str(value))
        if self.messana.systemSetEnergySave(value):
            ISYdriver = self.messana.getSystemEnergySaveISYdriver()
            self.setDriver(ISYdriver, value, report = True)

    def setSetback(self, command):
        LOGGER.debug('setSetback Called')
        value = int(command.get('value'))
        LOGGER.debug('setSetback Reeived:' + str(value))
        if self.messana.systemSetback(value):
            ISYdriver = self.messana.getSystemSetbackISYdriver()
            self.setDriver(ISYdriver, value, report = True)

    def ISYupdate (self, command):
        LOGGER.info('ISY-update called')
        self.messana.updateSystemData('all')
        self.updateISYdrivers('all')
 
    #id = 'MessanaMain' #self.name must have same value 
    #LOGGER.debug(str(id))
    #drivers = []
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
