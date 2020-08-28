#!/usr/bin/env python3
import polyinterface
from subprocess import call
import json
from collections import defaultdict


class MessanaZone(polyinterface.Node):
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

    def EnSchedule(self, command):
        return True        

    id = 'zone'
    commands = { 'SET_SETPOINT': setSetpoint
                ,'SET_STATUS"': setStatus
                ,'SET_ENERGYSAVE': setEnergySave
                ,'ENABLE_SCHEDULE' : EnSchedule 
                }

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

