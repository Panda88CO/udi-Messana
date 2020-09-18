#!/usr/bin/env python3
#import polyinterface
import requests
from subprocess import call
import json
from collections import defaultdict
from MessanaInfo import MessanaInfo

#LOGGER = polyinterface.LOGGER
        
#sys.stdout = open('Messanaoutput.txt','wt')
messana = MessanaInfo('192.168.2.65' , '9bf711fc-54e2-4387-9c7f-991bbb02ab3a')


#Retrive basic system info
print('\nSYSTEM')
#systemKeys = messana.pullSystemKeys()
#print(systemKeys)
messana.pullSystemDataAll()
systemKeys = messana.pullSystemKeys()
print(systemKeys)
messana.pullSystemDataActive()
for mKey in messana.mSystem['system']['GETstr']:
    messana.pullSystemDataIndividual(mKey)
    if messana.pushSystemDataIndividual(mKey,messana.mSystem['system']['data'][mKey] ):
        print('Put :' + mKey +' '+ str(messana.mSystem['system']['data'][mKey]) )
    else:
        print('Put failed: ' + mKey +' '+ str(messana.mSystem['system']['data'][mKey]))

print ('\n Zones')

for zoneNbr in range(0,messana.mSystem['system']['data']['mZoneCount']):
    keys = messana.pullZoneKeys(zoneNbr)
    print (keys)
    messana.pullZoneDataAll(zoneNbr)
    messana.pullZoneDataActive(zoneNbr)
    keys = messana.pullZoneKeys(zoneNbr)
    print (keys)  
    for mKey in messana.mSystem['zones']['GETstr']:
        messana.pullZoneDataIndividual(zoneNbr, mKey)
        nodeData = messana.pushZoneDataIndividual(zoneNbr, mKey, messana.mSystem['zones']['data'][zoneNbr][mKey])
        print('PUT zones : ' + mKey + ' ' + str( messana.mSystem['zones']['data'][zoneNbr][mKey]))
        print('nodeData : ' + str(nodeData))

print ('\n Macro Zones')  
for macrozoneNbr in range(0,messana.mSystem['system']['data']['mMacrozoneCount']):
    keys = messana.pullMacroZoneKeys(MacrozoneNbr)
    print (keys)
    messana.pullMacroZoneDataAll(macrozoneNbr)
    messana.pullMacroZoneDataActive(macrozoneNbr)
    keys = messana.pullMacroZoneKeys(macrozoneNbr)
    print (keys)  
    for mKey in messana.mSystem['macrozones']['GETstr']:
        messana.pullMacroZoneDataIndividual(zoneNbr, mKey)
        nodeData = messana.pushMacroZoneDataIndividual(macrozoneNbr, mKey, messana.mSystem['macrozones']['data'][macrozoneNbr][mKey])
        print('PUT zones : ' + mKey + ' ' + str( messana.mSystem['macrozones']['data'][macrozoneNbr][mKey]))
        print('nodeData : ' + str(nodeData))

#messana.PUTSystemData(msysInfo)
'''
print('\nHC changeover')
HC_CoDict = defaultdict(dict)   
for HC_CoNbr in range(0,  msysInfo['mHC_changeoverCount'] ):
    HC_CoDict[HC_CoNbr] = messana.pullHC_COData(HC_CoNbr)  
for HC_CoNbr in range(0,  msysInfo['mHC_changeoverCount'] ):
    messana.pushHC_COData(HC_CoNbr, HC_CoDict)  

print('\nATU')
atuDict = defaultdict(dict)   
for atuNbr in range(0,  msysInfo['mATUcount'] ):
    atuDict[atuNbr] = messana.pullATUData(atuNbr)  
for atuNbr in range(0,  msysInfo['mATUcount'] ):
    messana.pushATUData(atuNbr, atuDict)

print('\n END')

for mzoneNbr in range(0,systemDict['mMacrozoneCount']):
    messana.pullSubSystemData(messana.mSystem['macrozones'], mzoneNbr, macrozoneDict)

print('\nhc_changeover')
for hcchangeoverNbr in range (0,systemDict['mHCGroupCount']):
    messana.pullSubSystemData(messana.mSystem['hc_changeover'],hcchangeoverNbr , hc_changeoverDict)

print('\nFAN COILS')
for fcNbr in range(0,systemDict['mFanCoilCount']):
    messana.pullSubSystemData(messana.mSystem['fan_coils'], fcNbr, fan_coilsDict)

print('\nATU')
for zoneNbr in range(0,systemDict['mATUcount']):
    messana.pullSubSystemData(messana.mSystem['atus'], zoneNbr, atusDict)

print('\nBUFFER TANK')
for zoneNbr in range(0,systemDict['mBufTankCount']):
    pullSubSystemData(messana.mSystem['buffer_tanks'], zoneNbr, buffer_tanksDict)

print('\nENERGY SOURCE')
for zoneNbr in range(0,systemDict['mEnergySourceCount']):
    messana.pullSubSystemData(messana.mSystem['energy_sources'], zoneNbr, energy_sourcesDict)

print('\nDHW')
for zoneNbr in range(0,systemDict['mDHWcount']):
    messana.pullSubSystemData(messana.mSystem['domsetic_hot_waters'], zoneNbr, domsetic_hot_waterDict)

print('\n end extracting data')

print('\nSYSTEM - PUT')
for mKey in systemDict:
    pushmessana.mSystem(messana.mSystem['system'], mKey, systemDict[mKey], systemDict)

print('\nZONES - PUT')
for zoneNbr in zoneDict:
    for mKey in zoneDict[zoneNbr]:
        pushMessanaSubSystem(messana.mSystem['zones'], mKey, zoneNbr,zoneDict[zoneNbr][mKey], zoneDict)
        

print('\nMACROZONES - PUT')
for macrozoneNbr in macrozoneDict:
    for mKey in macrozoneDict[macrozoneNbr]:
        PUTSubNode(messana.mSystem['macrozones'], mKey, macrozoneNbr, macrozoneDict[macrozoneNbr][mKey], macrozoneDict)

print('\nhc_changeover - PUT')
for hcgroupcountNbr in hc_changeoverDict:
    for mKey in hc_changeoverDict[hcgroupcountNbr]:
        PUTSubNode(messana.mSystem['hc_changeover'], mKey, hcgroupcountNbr, hc_changeoverDict[hcgroupcountNbr][mKey], hc_changeoverDict)

print('\nFAN COILS - PUT')
for fan_coilNbr in fan_coilsDict:
    for mKey in fan_coilsDict[fan_coilNbr]:
        PUTSubNode(messana.mSystem['fan_coils'], mKey, fan_coilNbr, fan_coilsDict[fan_coilNbr][mKey], fan_coilsDict)

print('\nATU - PUT')
for atuNbr in atusDict:
    for mKey in atusDict[atuNbr]:
        PUTSubNode(messana.mSystem['atus'], mKey, atuNbr, atusDict[atuNbr][mKey],  atusDict)

print('\nBUFFER TANK - PUT')
for bufferTankNbr in buffer_tanksDict:
    for mKey in buffer_tanksDict[bufferTankNbr]:
        PUTSubNode(messana.mSystem['buffer_tanks'], mKey, bufferTankNbr, buffer_tanksDict[bufferTankNbr][mKey], buffer_tanksDict)

print('\nENERGY SOURCE - PUT')
for energySourceNbr in energy_sourcesDict:
    for mKey in energy_sourcesDict[energySourceNbr]:
        PUTSubNode(messana.mSystem['energy_sources'], mKey, energySourceNbr, energy_sourcesDict[energySourceNbr][mKey], energy_sourcesDict)

print('\nDHW - PUT')
for DHwaterNbr in domsetic_hot_waterDict:
    for mKey in domsetic_hot_waterDict[DHwaterNbr]:
        pushMessanaSubSystem(messana.mSystem['domsetic_hot_waters'], mKey, DHwaterNbr, domsetic_hot_waterDict[DHwaterNbr][mKey], domsetic_hot_waterDict)
print('\nEND put')
'''
#sys.stdout.close() 
