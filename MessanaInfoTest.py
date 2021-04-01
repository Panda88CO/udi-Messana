#!/usr/bin/env python3
#import polyinterface
import sys
import time
import requests
from subprocess import call
import json
from collections import defaultdict
from MessanaInfoPlayPRINT import messanaInfo
import shutil
#import ISYsetupFiles

#LOGGER = polyinterface.LOGGER
           
#sys.stdout = open('Messanaoutput.txt','wt')
commands = { 'SET_SETPOINT' : 'setSetpoint'
            ,'SET_STATUS' : 'setStatus'
            ,'SET_ENERGYSAVE' : 'setEnergySave'
            ,'SET_SCHEDULEON' : 'enableSchedule' 
            ,'UPDATE' : 'ISYupdate'
            ,'CurrentSetpointDP' : 'setCurrentDewPt'
            ,'CurrentSetpointRH' : 'setCurRelHum'
            ,'DehumSetpointDP' : 'setDewTempDehum'
            ,'DehumSetpointRH' : 'setRelDehum'
            ,'HumSetpointDP' : 'setDewTempHum'
            ,'HumSetpointRH' : 'setRelHum'
            ,'SET_CO2' : 'setCO2'
            }
messana = messanaInfo('192.168.2.65',  '9bf711fc-54e2-4387-9c7f-991bbb02ab3a', 'msystem')
#messana.init()print (commands)
#Retrive basic system info
print('\nSYSTEM')
print (commands)

messana.updateSystemData('all')
systemGETKeys = messana.systemPullKeys()
systemPUTKeys = messana.systemPushKeys()
systemActiveKeys = messana.systemActiveKeys()
messana.updateSystemData('all')
messana.updateSystemData('active')
drivers = []
for key in systemGETKeys:
    temp = messana.getSystemISYdriverInfo(key)
    if  temp != {}:
        drivers.append(temp)
        val = messana.pullSystemDataIndividual(key)
        print(temp['driver'], val['data'])

print(drivers)
ISYmap = messana.createISYmapping()

'''
for ISYdriver in drivers:
    ISYkey = ISYdriver['driver']
    value = None
    status = None
    status, value = messana.getSystemISYValue(ISYkey)
    print (status, value)
    print(.messana.getZoneISYdriverInfo(key, zoneNbr))
    print(value)
    print()
'''

print (messana.getZoneCount())
for key in systemGETKeys:
    val = messana.pullSystemDataIndividual(key)
    print (key, val)

print('setEnergySave Called')
val = 0
print('SetEnergySave Recived:' + str(val))
messana.systemSetEnergySave(val)
val = 1
print('SetEnergySave Recived:' + str(val))
messana.systemSetEnergySave(val)



print('zones')
MessanaZone = []
zoneCount = messana.getZoneCount()
for zoneNbr in range(0, zoneCount):
    for cmd in commands:
        if not(messana.checkZoneCommand(cmd, zoneNbr)):
            commands.pop(cmd)
    #messana.getZoneCapability(zoneNbr)
    #zoneInfo = messana.pullZoneData(zoneNbr)
    #print(self.zoneInfo)
    zone_GETKeys = messana.zonePullKeys(zoneNbr)
    zone_PUTKeys = messana.zonePushKeys(zoneNbr)
    zone_ActiveKeys = messana.zoneActiveKeys(zoneNbr)
    name = messana.getZoneName(zoneNbr)
    print(name)

    drivers = []
    for key in zone_GETKeys:
        temp = messana.getZoneISYdriverInfo(key, zoneNbr)
        if  temp != {}:
            drivers.append(temp)
            print(  'driver:  ' +  temp['driver'])

    print('Append Zone drivers')
    for key in zone_GETKeys:
        zoneInfo = messana.pullZoneDataIndividual(zoneNbr, key)
        print(zoneInfo)
        temp = messana.getnodeISYdriverInfo('zones', zoneNbr, key)
        print('Driver info: ' + str(temp))
        if  temp != {}:
            if not(str(temp['value']).isnumeric()):                         
                print('non numeric value :' + str(temp['value']))
                if temp['value'] == 'Celcius':
                    temp['value'] = 0
                    ISYTempUnit = 4
                else:
                    temp['value'] = 1
                    ISYTempUnit = 17
            print(str(temp) + 'before append')      
            MessanaZone.append(temp)
            print(str(MessanaZone) + 'after append')                       
        print(MessanaZone)
      
        for ISYdriver in drivers:
            ISYkey = ISYdriver['driver']
            temp = messana.getZoneMessanaISYkey(ISYkey, zoneNbr)
            if  temp in zone_ActiveKeys:                    
                    #LOGGER.debug('Messana Zone ISYdrivers ACTIVE ' + self.messana.getMessanaISYkey(ISYkey, self.zoneNbr))
                    status, value = messana.getZoneISYValue(ISYkey, zoneNbr)

        print('setEnergySave Called')
    val = 0
    print('zoneSetStatus Recived:' + str(val))
    messana.zoneSetStatus(val, zoneNbr)
    val = 1
    print('zoneSetStatus Recived:' + str(val))
    messana.zoneSetStatus(val, zoneNbr)
    key = messana.getZoneStatusISYdriver (zoneNbr)
    print(key)

'''
ZONEDRIVER  = {}
for zoneNbr in range(0,messana.mSystem['system']['data']['mZoneCount']):
    zoneData = {}
    messana.getZoneCapability(zoneNbr)
    messana.updateZoneData(zoneNbr)
    zoneName = 'zone'
    messana.addNodeDefStruct(zoneNbr, 'zones', zoneName )
    ZONEDRIVER[zoneNbr] = []
    for key in systemGETKeys:
        temp = messana.getnodeISYdriverInfo('zones', zoneNbr, key)
        if  temp != {}:
           ZONEDRIVER[zoneNbr].append(temp)

messana.createSetupFiles('nodeTest.xml','editorTest.xml', 'nlsTest.txt')
shutil.copy('./nodeTest.xml', './profile/nodedef/nodedefs.xml')
shutil.copy('./editorTest.xml', './profile/editor/editors.xml')
shutil.copy('./nlsTest.txt', './profile/nls/en_us.txt')
print('systemKeys')

sysData={}
for mKey in systemPUTKeys:
    sysData = messana.pullSystemDataIndividual(mKey)
    if sysData['statusOK']:
        print ('GET:' + mKey + ' ' + str(sysData['data']))
    else:
        print(sysData['error'])
    if mKey in systemPUTKeys:
        if messana.pushSystemDataIndividual(mKey,messana.mSystem['system']['data'][mKey] ):
            print('PUT :' + mKey +' '+ str(messana.mSystem['system']['data'][mKey]) )
        else:
            print('Put failed: ' + mKey +' '+ str(messana.mSystem['system']['data'][mKey]))
#messana.saveData()
'''

'''
print ('\n Zones')
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

print ('\n Macro Zones')  
for macrozoneNbr in range(0,messana.mSystem['system']['data']['mMacrozoneCount']):
    nodeData = {}
    messana.updateMacroZoneData(macrozoneNbr)
    macrozoneGETkeys = messana.macrozonePullKeys(macrozoneNbr)
    print (macrozoneGETkeys)
    macrozonePUTkeys = messana.macrozonePushKeys(macrozoneNbr)
    print(macrozonePUTkeys)
    macrozoneActiveKeys = messana.macrozoneActiveKeys(macrozoneNbr)
    print (macrozoneActiveKeys)
    
    for mKey in macrozoneGETkeys:
        nodeData = messana.pullMacroZoneDataIndividual(macrozoneNbr, mKey)
        if nodeData['statusOK']:
            print('GET: ' + mKey + str(nodeData['data']))
        if mKey in macrozoneActiveKeys:
            nodeData = messana.pullZoneDataIndividual(macrozoneNbr, mKey)
            if nodeData['statusOK']:
                print('GET: ' + mKey + str(nodeData['data']))
        if mKey in macrozonePUTkeys:
            if mKey in messana.mSystem['macrozones']['data'][macrozoneNbr]:
                nodeData = messana.pushMacroZoneDataIndividual(macrozoneNbr, mKey, messana.mSystem['macrozones']['data'][macrozoneNbr][mKey])
                print('PUT macrozones : ' + mKey + ' ' + str( messana.mSystem['macrozones']['data'][macrozoneNbr][mKey]))
                print('nodeData : ' + str(nodeData))


print ('\n Hot Cold Change Over')  
for HC_CONbr in range(0,messana.mSystem['system']['data']['mHC_changeoverCount']):
    nodeData = {}
    messana.updateHC_COData(HC_CONbr)
    hc_changeoverGETkeys = messana.hc_changeoverPullKeys(HC_CONbr)
    print (hc_changeoverGETkeys)
    hc_changeoverPUTkeys = messana.hc_changeoverPushKeys(HC_CONbr)
    print(hc_changeoverPUTkeys)
    hc_changeoverActiveKeys = messana.hc_changeoverActiveKeys(HC_CONbr)
    print (hc_changeoverActiveKeys)
    
    for mKey in hc_changeoverGETkeys:
        nodeData = messana.pullHC_CODataIndividual(HC_CONbr, mKey)
        if nodeData['statusOK']:
            print('GET: ' + mKey + str(nodeData['data']))
        if mKey in hc_changeoverActiveKeys:
            nodeData = messana.pullHC_CODataIndividual(HC_CONbr, mKey)
            if nodeData['statusOK']:
                print('GET: ' + mKey + str(nodeData['data']))
        if mKey in hc_changeoverPUTkeys:
            if mKey in messana.mSystem['hc_changeover']['data'][HC_CONbr]:
                nodeData = messana.pushHC_CODataIndividual(HC_CONbr, mKey, messana.mSystem['hc_changeover']['data'][HC_CONbr][mKey])
                print('PUT HC_CO : ' + mKey + ' ' + str( messana.mSystem['hc_changeover']['data'][HC_CONbr][mKey]))
                print('nodeData : ' + str(nodeData))


print ('\n ATU')  
for ATUNbr in range(0,messana.mSystem['system']['data']['mATUcount']):
    nodeData = {}
    messana.updateATUData(ATUNbr)
    atuGETkeys = messana.atuPullKeys(ATUNbr)
    print (atuGETkeys)
    atuPUTkeys = messana.atuPushKeys(ATUNbr)
    print(atuPUTkeys)
    atuActiveKeys = messana.atuActiveKeys(ATUNbr)
    print (atuActiveKeys)
    
    for mKey in atuGETkeys:
        nodeData = messana.pullATUDataIndividual(ATUNbr, mKey)
        if nodeData['statusOK']:
            print('GET: ' + mKey + str(nodeData['data']))
        if mKey in atuActiveKeys:
            nodeData = messana.pullATUDataIndividual(ATUNbr, mKey)
            if nodeData['statusOK']:
                print('GET: ' + mKey + str(nodeData['data']))
        if mKey in atuPUTkeys:
            if mKey in messana.mSystem['hc_changeover']['data'][ATUNbr]:
                nodeData = messana.pushATUDataIndividual(ATUNbr, mKey, messana.mSystem['atus']['data'][ATUNbr][mKey])
                print('PUT ATU: ' + mKey + ' ' + str( messana.mSystem['atus']['data'][ATUNbr][mKey]))
                print('nodeData : ' + str(nodeData))


print ('\n Fan Coil')  
for FCNbr in range(0,messana.mSystem['system']['data']['mFanCoilCount']):
    nodeData = {}
    messana.updateFanCoilData(FCNbr)
    fan_coilGETkeys = messana.fan_coilPullKeys(FCNbr)
    print (fan_coilGETkeys)
    fan_coilPUTkeys = messana.fan_coilPushKeys(FCNbr)
    print(fan_coilPUTkeys)
    fan_coilActiveKeys = messana.fan_coilActiveKeys(FCNbr)
    print (fan_coilActiveKeys)
    
    for mKey in fan_coilGETkeys:
        nodeData = messana.pullFanCoilDataIndividual(FCNbr, mKey)
        if nodeData['statusOK']:
            print('GET: ' + mKey + str(nodeData['data']))
        if mKey in fan_coilActiveKeys:
            nodeData = messana.pullFanCoilDataIndividual(FCNbr, mKey)
            if nodeData['statusOK']:
                print('GET: ' + mKey + str(nodeData['data']))
        if mKey in fan_coilPUTkeys:
            if mKey in messana.mSystem['hc_changeover']['data'][FCNbr]:
                nodeData = messana.pushFanCoilDataIndividual(FCNbr, mKey, messana.mSystem['fan_coils']['data'][FCNbr][mKey])
                print('PUT FanCoil: ' + mKey + ' ' + str( messana.mSystem['fan_coils']['data'][FCNbr][mKey]))
                print('nodeData : ' + str(nodeData))



print ('\n energy_sources')  
for energySourceNbr in range(0,messana.mSystem['system']['data']['mEnergySourceCount']):
    nodeData = {}
    messana.updateEnergySourceData(energySourceNbr)
    energy_sourceGETkeys = messana.energy_sourcePullKeys(energySourceNbr)
    print (energy_sourceGETkeys)
    energy_sourcePUTkeys = messana.energy_sourcePushKeys(energySourceNbr)
    print(energy_sourcePUTkeys)
    energy_sourceActiveKeys = messana.energy_sourceActiveKeys(energySourceNbr)
    print (energy_sourceActiveKeys)
    
    for mKey in energy_sourceGETkeys:
        nodeData = messana.pullEnergySourceDataIndividual(energySourceNbr, mKey)
        if nodeData['statusOK']:
            print('GET: ' + mKey + str(nodeData['data']))
        if mKey in energy_sourceActiveKeys:
            nodeData = messana.pullEnergySourceDataIndividual(energySourceNbr, mKey)
            if nodeData['statusOK']:
                print('GET: ' + mKey + str(nodeData['data']))
        if mKey in energy_sourcePUTkeys:
            if mKey in messana.mSystem['hc_changeover']['data'][energySourceNbr]:
                nodeData = messana.pushEnergySourceDataIndividual(energySourceNbr, mKey, messana.mSystem['energy_sources']['data'][energySourceNbr][mKey])
                print('PUT EnergySource: ' + mKey + ' ' + str( messana.mSystem['energy_sources']['data'][energySourceNbr][mKey]))
                print('nodeData : ' + str(nodeData))


print ('\n Buffer Tank')  
for BufferTankNbr in range(0,messana.mSystem['system']['data']['mBufTankCount']):
    nodeData = {}
    messana.updateBufferTankData(BufferTankNbr)
    buffer_tankGETkeys = messana.buffer_tankPullKeys(BufferTankNbr)
    print (buffer_tankGETkeys)
    buffer_tankPUTkeys = messana.buffer_tankPushKeys(BufferTankNbr)
    print(buffer_tankPUTkeys)
    buffer_tankActiveKeys = messana.buffer_tankActiveKeys(BufferTankNbr)
    print (buffer_tankActiveKeys)
    
    for mKey in buffer_tankGETkeys:
        nodeData = messana.pullBufferTankDataIndividual(BufferTankNbr, mKey)
        if nodeData['statusOK']:
            print('GET: ' + mKey + str(nodeData['data']))
        if mKey in buffer_tankActiveKeys:
            nodeData = messana.pullBufferTankDataIndividual(BufferTankNbr, mKey)
            if nodeData['statusOK']:
                print('GET: ' + mKey + str(nodeData['data']))
        if mKey in buffer_tankPUTkeys:
            if mKey in messana.mSystem['buffer_tanks']['data'][BufferTankNbr]:
                nodeData = messana.pushBufferTankDataIndividual(BufferTankNbr, mKey, messana.mSystem['buffer_tanks']['data'][BufferTankNbr][mKey])
                print('PUT BufferTank: ' + mKey + ' ' + str( messana.mSystem['buffer_tanks']['data'][BufferTankNbr][mKey]))
                print('nodeData : ' + str(nodeData))



print ('\n Domestic How Water')  
for DHWNbr in range(0,messana.mSystem['system']['data']['mDHWcount']):
    nodeData = {}
    messana.updateDHWData(DHWNbr)
    DHWGETkeys = messana.DHWPullKeys(DHWNbr)
    print (DHWGETkeys)
    DHWPUTkeys = messana.DHWPushKeys(DHWNbr)
    print(DHWPUTkeys)
    DHWActiveKeys = messana.DHWActiveKeys(DHWNbr)
    print (DHWActiveKeys)
    
    for mKey in DHWGETkeys:
        nodeData = messana.pullDHWDataIndividual(DHWNbr, mKey)
        if nodeData['statusOK']:
            print('GET: ' + mKey + str(nodeData['data']))
        if mKey in DHWActiveKeys:
            nodeData = messana.pullDHWDataIndividual(DHWNbr, mKey)
            if nodeData['statusOK']:
                print('GET: ' + mKey + str(nodeData['data']))
        if mKey in DHWPUTkeys:
            if mKey in messana.mSystem['domsetic_hot_waters']['data'][DHWNbr]:
                nodeData = messana.pushDHWDataIndividual(DHWNbr, mKey, messana.mSystem['domsetic_hot_waters']['data'][DHWNbr][mKey])
                print('PUT DHW: ' + mKey + ' ' + str( messana.mSystem['domsetic_hot_waters']['data'][DHWNbr][mKey]))
                print('nodeData : ' + str(nodeData))


#messana.PUTSystemData(msysInfo)
sys.stdout.close() 
'''