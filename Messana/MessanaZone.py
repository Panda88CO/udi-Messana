#!/usr/bin/env python3



LOGGER = polyinterface.LOGGER

class MessanaZone(polyinterface.node):
    def __init__(self, controller, primary, address, name, zonenbr):
        super(MessanaZone, self).__init__(controller, primary, address, name)
        LOGGER.info('_init_ Messana Zone')


                
    def start(self):
        return True

    def stop(self):
        LOGGER.debug('stop - Cleaning up Temp Sensors & GPIO')


    def shortPoll(self):
        LOGGER.debug('Messane Zone shortPoll')
        #for node in self.nodes:
        #     if node != self.address:
        #        self.nodes[node].updateInfo()
                   
    def longPoll(self):
        LOGGER.debug('Messana Zone longPoll')


    def query(self, command=None):
        LOGGER.debug('TOP querry')

    def updateInfo(self):
        return True
        
    def setStatus(self, command):
        return True

    def setEnergySave(self, command):
        return True

    def setSetpoint(self, command):
        return True

    def ENABLE_SCHEDULE(self, command):
        return True        


                <cmd id="SET_STATUS" />
                <cmd id="SET_SETPOINT" />
                <cmd id="ENABLE_ENERGYSAVE" />
                <cmd id="ENABLE_SCHEDULE" />
    id = 'zone'
    commands = { 'SET_SETPOINT': setSetpoint
                ,'SET_STATUS"': setStatus
                ,'SET_ENERGYSAVE': setEnergySave
                ,'ENABLE_SCHEDULE' : EnSchedule 
                }

'''
            <st id="ST"  editor="STATUS" />
            <st id='GV1' editor='SETPOINT' />
            <st id='GV2' editor='PANELTEMP'/>
            <st id='CLITEMP' editor='AIRTEMP'/>
            <st id='GV3' editor='SCHEDULE'/>
            <st id='GV5' editor='DEWPOINT'/>
            <st id='GV6' editor='AIRQUALITY'/>
            <st id='CLIHUM' editor='HUMIDIDTY'/>
            <st id='CO2LVL' editor='CO2'/>
            <st id='GV7' editor='MACROZONE_MEMBER'/>
            <st id='GV8' editor='ENERGYSAVE'/>
            <st id='ALARM' editor='EXTALARM'/>
            <st id='GV9' editor='HSETPOINTRH'/>
            <st id='GV10' editor='HSETPOINTDP'/>            
            <st id='GV11' editor='DHSETPOINTRH'/>
            <st id='GV12' editor='FHSETPOINTDP'/>
            <st id='GV13' editor='CURSETPOINTRH'/>
            <st id='GV14' editor='CURSETPOINTDP'/>
'''

    drivers = [  {'driver': 'ST',  'value': 1, 'uom': 2}
                ,{'driver': 'GV1', 'value': 1, 'uom': 4}               
                ,{'driver': 'GV2', 'value': 1, 'uom': 2}
                ,{'driver': 'GV3', 'value': 1, 'uom': 2}
                ,{'driver': 'CLITEMP', 'value': 1, 'uom': 4}
                ,{'driver': 'GV5', 'value': 1, 'uom': 51}
                ,{'driver': 'CLIHUM', 'value': 1, 'uom': 51}
                ,{'driver': 'C02LVL', 'value': 1, 'uom': 107}
                ,{'driver': 'GV6', 'value': 1, 'uom': 107}     
                ,{'driver': 'GV7', 'value': 0, 'uom': 107}
                ,{'driver': 'GV8', 'value': 1, 'uom': 107}
                ,{'driver': 'ALARM', 'value': 1, 'uom': 2}          
                ,{'driver': 'GV9', 'value': 1, 'uom': 107}
                ,{'driver': 'GV10', 'value': 1, 'uom': 107} 
                ,{'driver': 'GV11', 'value': 0, 'uom': 107}
                ,{'driver': 'GV12', 'value': 1, 'uom': 107}
                ,{'driver': 'GV13', 'value': 0, 'uom': 107}
                ,{'driver': 'GV14', 'value': 1, 'uom': 107}
                ]

