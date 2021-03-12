#!/usr/bin/env python3

import polyinterface
from subprocess import call
import json
import sys
from collections import defaultdict
from MessanaInfoPlay import messanaInfo
#from MessanaZone import MessanaZone
import shutil

LOGGER = polyinterface.LOGGER
               
class MessanaController(polyinterface.Controller):

    def __init__(self, polyglot):
        super(MessanaController, self).__init__(polyglot)
        LOGGER.info('_init_ Messsana Controller')
        self.messanaImportOK = 0
        self.ISYforced = False
        self.name = 'MessanaMain'
        self.address ='messanasys'
        
        self.primary = self.address
        self.hb = 0
        self.ISYdrivers=[]
        self.ISYcommands = {}
        self.ISYTempUnit = 0

        '''
        LOGGER.info('Init - configurations')
        
        self.removeNoticesAll()
        self.addNotice('Please Set IP address (IP_ADDRESS) and Messana Key (MESSANA_KEY)')

        self.IPAddress = self.getCustomParam('IP_ADDRESS')
        if self.IPAddress is None:
            self.IPAddress= '192.168.2.65'
            LOGGER.error('IP address not set')
            self.addCustomParam({'IP_ADDRESS': self.IPAddress})
        
        self.MessanaKey = self.getCustomParam('MESSANA_KEY')
        if self.MessanaKey is None:
            self.MessanaKey =  '9bf711fc-54e2-4387-9c7f-991bbb02ab3a'
            LOGGER.error('check_params: Messana Key not specified')
            self.addCustomParam({'MESSANA_KEY': self.MessanaKey})
        self.messana = messanaInfo( self.IPAddress, self.MessanaKey , self.name)
        self.messana.updateSystemData('all')
        self.systemGETKeys = self.messana.systemPullKeys()
        self.systemPUTKeys = self.messana.systemPushKeys()
        self.systemActiveKeys = self.messana.systemActiveKeys()
        
        self.drivers = []
        for key in self.systemGETKeys:
            temp = self.messana.getSystemISYdriverInfo(key)
            if  temp != {}:
                self.drivers.append(temp)
                val = self.messana.pullSystemDataIndividual(key)
                if val['data'] in  ['Celcius', 'Fahrenheit']:
                    if val['data'] == 'Celcius':
                        val['data'] = 0
                    else:  
                        val['data'] = 1
                LOGGER.debug(  'driver:  ' +  temp['driver']+ ' , '+ str(val['data']))

        self.poly.installprofile()
        self.poly.updateprofile()
        self.reportDrivers()
        self.messanaImportOK = 1
        
        self.removeNoticesAll()
        self.discover()
        '''

        #try:
        #self.messana = MessanaInfo( MessanaController.id )
        #messana.setMessanaCredentials ('192.168.2.65', '9bf711fc-54e2-4387-9c7f-991bbb02ab3a')
        #LOGGER.debug('MessanaInfo call done')

        #self.system_GETKeys = self.messana.systemPullKeys()
        #self.system_PUTKeys = self.messana.systemPushKeys()
        #self.system_ActiveKeys = self.messana.systemActiveKeys()
        
        #self.messana.updateSystemData('all')
        #self.messana.addSystemDefStruct(self.address)
    
        #LOGGER.debug('Install Updated profile')
        #self.poly.installprofile()

        #LOGGER.debug('Append System drivers')
        #for key in self.system_GETKeys:
        #    temp = self.messana.getSystemISYdriverInfo(key)
        #    LOGGER.debug('Driver info: ' + str(temp))
        #    if  temp != {}:
        #        if not(str(temp['value']).isnumeric()):                         
        #            LOGGER.debug('non numeric value :' + temp['value'])
        #            if temp['value'] == 'Celcius':
        #                temp['value'] = 0
        #                self.ISYTempUnit = 4
        #            else:
        #                temp['value'] = 1
        #                self.ISYTempUnit = 17
        #        LOGGER.debug(str(temp) + 'before append')      
        #        MessanaController.drivers.append(temp)
        #        LOGGER.debug(str(MessanaController.drivers) + 'after append')                       
        #LOGGER.debug(MessanaController.drivers)
        #self.check_params()
        #self.discover()   
        #self.updateInfo('all')
        #self.messanaImportOK = 1
        #self.discover()


    def start(self):
        LOGGER.info('Start  Messana Main NEW')

        LOGGER.info('Init - configurations')
        
        self.removeNoticesAll()
        self.addNotice('Please Set IP address (IP_ADDRESS) and Messana Key (MESSANA_KEY)')

        self.IPAddress = self.getCustomParam('IP_ADDRESS')
        if self.IPAddress is None:
            self.IPAddress= '192.168.2.65'
            LOGGER.error('IP address not set')
            self.addCustomParam({'IP_ADDRESS': self.IPAddress})
        
        self.MessanaKey = self.getCustomParam('MESSANA_KEY')
        if self.MessanaKey is None:
            self.MessanaKey =  '9bf711fc-54e2-4387-9c7f-991bbb02ab3a'
            LOGGER.error('check_params: Messana Key not specified')
            self.addCustomParam({'MESSANA_KEY': self.MessanaKey})
        LOGGER.debug('Calling Messsana: '+self.IPAddress+' '+ self.MessanaKey+' '+self.name)
        self.messana = messanaInfo( self.IPAddress, self.MessanaKey , self.name)
        
        #LOGGER.debug ('Install Profile')    
        #self.poly.installprofile()
        #LOGGER.debug('Install Profile done')

        self.messana.updateSystemData('all')
        self.systemGETKeys = self.messana.systemPullKeys()
        self.systemPUTKeys = self.messana.systemPushKeys()
        self.systemActiveKeys = self.messana.systemActiveKeys()

        self.reportDrivers()
        self.drivers = []
        for key in self.systemGETKeys:
            temp = self.messana.getSystemISYdriverInfo(key)
            if  temp != {}:
                self.drivers.append(temp)
                val = self.messana.pullSystemDataIndividual(key)
                if val['data'] in  ['Celcius', 'Fahrenheit']:
                    if val['data'] == 'Celcius':
                        val['data'] = 0
                    else:  
                        val['data'] = 1
                LOGGER.debug(  'driver:  ' +  temp['driver']+ ' , '+ str(val['data']))
        


        self.messanaImportOK = 1
        self.removeNoticesAll()
        self.discover()


        #except:
            #LOGGER.debug('Reading data from Messana System NOT successful')
                


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
            if self.ISYforced:
                self.messana.updateSystemData('active')
            else:
                self.messana.updateSystemData('all')

            LOGGER.debug( self.drivers)
            for ISYdriver in self.drivers:
                ISYkey = ISYdriver['driver']
                status, value = self.messana.getSystemISYValue(ISYkey)
                if status:
                    self.setDriver(ISYdriver, value)
                    LOGGER.debug('driver updated :' + ISYdriver['driver'] + ' =  '+str(value))
                else:
                    LOGGER.debug('Error getting ' + ISYdriver['driver'])
            #self.reportDrivers()
            self.ISYforced = True
            '''
            for node in self.nodes:
                if node != self.address:
                    self.nodes[node].updateInfo()
            '''

    def longPoll(self):
        LOGGER.debug('Messana Controller longPoll')

        if self.messanaImportOK == 1:
            LOGGER.debug('Long Poll System Up')
            self.heartbeat()
            self.messana.updateSystemData('all')
            LOGGER.debug( self.drivers)
            for ISYdriver in self.drivers:
                ISYkey = ISYdriver['driver']
                status, value = self.messana.getSystemISYValue(ISYkey)
                if status:
                    if self.ISYforced:
                        self.setDriver(ISYdriver, value, report = True, force = False)
                    else:
                        self.setDriver(ISYdriver, value, report = True, force = True)
                    LOGGER.debug('driver updated :' + ISYdriver['driver'] + ' =  '+str(value))
                else:
                    LOGGER.debug('Error getting ' + ISYdriver['driver'])

            self.reportDrivers()
            self.ISYforced = True
            #for node in self.nodes:
            #    if node != self.address:
            #        self.nodes[node].updateInfo()
        

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
            #if not address in self.nodes:
               #self.addNode(MessanaZone(self, self.address, address, name, zoneNbr, self.messana))
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
        val = int(command.get('value'))
        LOGGER.debug('set Status Recived:' + str(val))
        self.messana.systemSetStatus(val)


        
    def setEnergySave(self, command):
        LOGGER.debug('setEnergySave Called')
        val = int(command.get('value'))
        LOGGER.debug('SetEnergySave Recived:' + str(val))
        self.messana.systemSetEnergySave(val)


    def setSetback(self, command):
        LOGGER.debug('setSetback Called')
        val = int(command.get('value'))
        mKey = 'mSetback'
        LOGGER.debug('setSetback Reeived:' + str(val))
        self.setParamFromISY(mKey, val)
        self.messana.systemSetback(val)

    def ISYupdate (self):
        LOGGER.info('ISY-update called')
        self.updateInfo('all')

    id = self.name
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
