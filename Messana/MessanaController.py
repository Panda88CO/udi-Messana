#!/usr/bin/env python3
import polyinterface
from subprocess import call
import json
from collections import defaultdict

class MessanaController(polyinterface.Controller):
    def __init__(self, polyglot):
        super(MessanaController, self).__init__(polyglot)
        LOGGER.info('_init_')
        self.name = 'Messana Main Control'
        self.address = 'messana'
        self.primary = self.address
        self.hb = 0
        self.msysInfo = defaultdict(dict)
        self.mzoneInfo = defaultdict(dict)


                
    def start(self):
        LOGGER.info('Start  Messana Main')
        self.check_params()
        try:
            self.messana = MessanaInfo('192.168.2.65' , '9bf711fc-54e2-4387-9c7f-991bbb02ab3a')
            self.msysInfo = self.messana.retrieveSystemData()

        except:
            LOGGER.debug('Reading data from Messana System NOT successful')
        self.discover()         
        self.updateInfo()
        self.reportDrivers()
 

    def stop(self):
        LOGGER.debug('stop - Cleaning up Temp Sensors & GPIO')

    def heartbeat(self):
        LOGGER.debug('heartbeat: hb={}'.format(self.hb))
        if self.hb == 0:
            self.reportCmd("DON",2)
            self.hb = 1
        else:
            self.reportCmd("DOF",2)
            self.hb = 0

    def shortPoll(self):
        LOGGER.debug('Messane Controller shortPoll')
        #for node in self.nodes:
        #     if node != self.address:
        #        self.nodes[node].updateInfo()
                   
    def longPoll(self):
        LOGGER.debug('Messana Controller longPoll')
        self.heartbeat()
        self.updateInfo()
        #for node in self.nodes:
        #    if node != self.address:
        #        self.nodes[node].updateInfo()
        

    def query(self, command=None):
        LOGGER.debug('TOP querry')

        for node in self.nodes:
            self.nodes[node].updateInfo()
            #self.nodes[node].update24Hqueue()

    def discover(self, command=None):
        LOGGER.debug('discover')
        LOGGER.info('Adding Zone')
        for zoneNbr in range(0,self.msysInfo['mZoneCount']):
            ZoneDict = self.messana.retrieveZoneData(zoneNbr)
            name = str(ZoneDict['mName'])
            address = 'zone'+str(zoneNbr)
            LOGGER.debug('zone ' + str(zoneNbr)+' : name, Address' + name +' ' + address) 
            if not address in self.nodes:
               self.addNode(MessanaZone(self, self.address, address, name, zoneNbr))


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

    
    '''    LOGGER.debug(str(self.polyConfig['customParams'])) 
        params = {}
        count = 0
        self.removeNoticesAll()
        self.addNotice('To add IOpin use portN as Key and IN:name or OUT:name as value to define ports')
        self.addNotice('N is BRCM port number (4 use for temp semnsor)')     
        for mySensor in self.mySensors.get_available_sensors():
            count = count+1
            currentSensor = mySensor.id.lower() 
            if not(currentSensor in self.polyConfig['customParams']):
                params[currentSensor]=['NoName'+str(count)]
        if not(params == {}):
            self.addCustomParam(params)
        LOGGER.debug(str(params))
    
        for customP in self.polyConfig['customParams']:
            LOGGER.debug(str(customP))
            if customP.lower() in BRCM_PORTS:
                PortNumber = BRCM_PORTS[customP.lower()]
                PortDef = self.polyConfig['customParams'][customP]
                PortInfo = PortDef.split(':',1)
                LOGGER.debug(str(PortNumber) + ' ' + str(PortInfo))
                if PortInfo[0].lower() == 'in':
                    self.INPUT_PINS.update({PortNumber:PortInfo[1]})
                    LOGGER.debug('Input Pin: '+str(PortNumber) + ' ' + str(PortInfo[1]))
                elif PortInfo[0].lower() == 'out':
                    self.OUTPUT_PINS.update({PortNumber:PortInfo[1]})
                    LOGGER.debug('Output Pin: '+str(PortNumber) + ' ' + str(PortInfo[1]))

                else:
                    self.addNotice('Must use IN or OUT:name(port 4 is used for temp sensors)')                    
        self.saveCustomData(self.polyConfig['customParams'])
    '''
    def updateInfo(self):
        LOGGER.info('Update Messana System ')
        LOGGER.debug('ST :'+  str(self.msysInfo['mStatus']) + ' GV2:' + str(self.msysInfo['mUnitTemp']) + ' GV9: ' + str(self.msysInfo['mZoneCount']))
        self.setDriver('ST', self.msysInfo['mStatus'])
        self.setDriver('GV2', self.msysInfo['mUnitTemp'])
        self.setDriver('GV3', self.msysInfo['mEnergySaving'])
        self.setDriver('GV4', self.msysInfo['mSetback'])
        self.setDriver('GV5', self.msysInfo['mATUcount'])
        self.setDriver('GV6', self.msysInfo['mDHWcount'])
        self.setDriver('GV7', self.msysInfo['mFanCoilCount'])
        self.setDriver('GV8', self.msysInfo['mEnergySourceCount'])
        self.setDriver('GV9', self.msysInfo['mZoneCount'])
        self.setDriver('GV10', self.msysInfo['mMacrozoneCount'])
        self.setDriver('GV11', self.msysInfo['mHC_changeoverCount'])
        self.setDriver('GV12', self.msysInfo['mBufTankCount'])
        self.setDriver('ALARM', self.msysInfo['mExternalAlarm'])

    def setStatus(self, command):
        return True

    def setEnergySave(self, command):
        return True

    def setSetback(self, command):
        return True


    id = 'messanasys'
    commands = { 'UPDATE': discover
                ,'SET_STATUS"': setStatus
                ,'SET_ENERGYSAVE': setEnergySave
                ,'SET_SETBACK' : setSetback 
                }

    drivers = [  {'driver': 'ST',  'value': 1, 'uom': 2}
                ,{'driver': 'GV2', 'value': 1, 'uom': 2}
                ,{'driver': 'GV3', 'value': 1, 'uom': 2}
                ,{'driver': 'GV4', 'value': 1, 'uom': 4}
                ,{'driver': 'GV5', 'value': 1, 'uom': 107}
                ,{'driver': 'GV6', 'value': 1, 'uom': 107}     
                ,{'driver': 'GV7', 'value': 0, 'uom': 107}
                ,{'driver': 'GV8', 'value': 1, 'uom': 107}          
                ,{'driver': 'GV9', 'value': 1, 'uom': 107}
                ,{'driver': 'GV10', 'value': 1, 'uom': 107} 
                ,{'driver': 'GV11', 'value': 0, 'uom': 107}
                ,{'driver': 'GV12', 'value': 1, 'uom': 107}
                ,{'driver': 'ALARM', 'value': 0, 'uom': 2}  
                ]

