#!/usr/bin/env python3
#import polyinterface
import sys
import requests
from subprocess import call
import json
from collections import defaultdict
from MessanaInfo import MessanaInfo

#LOGGER = polyinterface.LOGGER
        
sys.stdout = open('Messanaoutput.txt','wt')
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
        if mKey in messana.mSystem['zones']['PUTstr']:
            nodeData = messana.pushZoneDataIndividual(zoneNbr, mKey, messana.mSystem['zones']['data'][zoneNbr][mKey])
            print('PUT zones : ' + mKey + ' ' + str( messana.mSystem['zones']['data'][zoneNbr][mKey]))
            print('nodeData : ' + str(nodeData))

print ('\n Macro Zones')  
for macrozoneNbr in range(0,messana.mSystem['system']['data']['mMacrozoneCount']):
    keys = messana.pullMacroZoneKeys(macrozoneNbr)
    print (keys)
    messana.pullMacroZoneDataAll(macrozoneNbr)
    messana.pullMacroZoneDataActive(macrozoneNbr)
    keys = messana.pullMacroZoneKeys(macrozoneNbr)
    print (keys)  
    for mKey in messana.mSystem['macrozones']['GETstr']:
        messana.pullMacroZoneDataIndividual(macrozoneNbr, mKey)
        if mKey in  messana.mSystem['macrozones']['PUTstr']:
            nodeData = messana.pushMacroZoneDataIndividual(macrozoneNbr, mKey, messana.mSystem['macrozones']['data'][macrozoneNbr][mKey])
            print('PUT macrozones : ' + mKey + ' ' + str( messana.mSystem['macrozones']['data'][macrozoneNbr][mKey]))
            print('nodeData : ' + str(nodeData))



print ('\n Hot Cold Change Over')  
for HCCO_Nbr in range(0,messana.mSystem['system']['data']['mHC_changeoverCount']):
    keys = messana.pullHCCOKeys(HCCO_Nbr)
    print (keys)
    messana.pullHCCODataAll(HCCO_Nbr)
    messana.pullHCCODataActive(HCCO_Nbr)
    keys = messana.pullHCCOKeys(HCCO_Nbr)
    print (keys)  
    for mKey in messana.mSystem['hc_changeover']['GETstr']:
        messana.pullHCCODataIndividual(HCCO_Nbr, mKey)
        if mKey in  messana.mSystem['hc_changeover']['PUTstr']:
            nodeData = messana.pushHCCODataIndividual(HCCO_Nbr, mKey, messana.mSystem['hc_changeover']['data'][HCCO_Nbr][mKey])
            print('PUT HC changeover : ' + mKey + ' ' + str( messana.mSystem['hc_changeover']['data'][HCCO_Nbr][mKey]))
            print('nodeData : ' + str(nodeData))


print ('\n ATU')  
for ATU_Nbr in range(0,messana.mSystem['system']['data']['mATUcount']):
    keys = messana.pullATUKeys(ATU_Nbr)
    print (keys)
    messana.pullATUDataAll(ATU_Nbr)
    messana.pullATUDataActive(ATU_Nbr)
    keys = messana.pullATUKeys(ATU_Nbr)
    print (keys)  
    for mKey in messana.mSystem['atus']['GETstr']:
        messana.pullATUDataIndividual(ATU_Nbr, mKey)
        if mKey in  messana.mSystem['atus']['PUTstr']:
            nodeData = messana.pushATUDataIndividual(ATU_Nbr, mKey, messana.mSystem['atus']['data'][ATU_Nbr][mKey])
            print('PUT atu : ' + mKey + ' ' + str( messana.mSystem['atus']['data'][ATU_Nbr][mKey]))
            print('nodeData : ' + str(nodeData))

print ('\n Fan Coil')  
for FC_Nbr in range(0,messana.mSystem['system']['data']['mFanCoilCount']):
    keys = messana.pullFanCoilKeys(FC_Nbr)
    print (keys)
    messana.pullFanCoilDataAll(FC_Nbr)
    messana.pullFanCoilDataActive(FC_Nbr)
    keys = messana.pullFanCoilKeys(FC_Nbr)
    print (keys)  
    for mKey in messana.mSystem['fan_coils']['GETstr']:
        messana.pullFanCoilDataIndividual(FC_Nbr, mKey)
        if mKey in  messana.mSystem['fan_coils']['PUTstr']:
            nodeData = messana.pushFanCoilDataIndividual(FC_Nbr, mKey, messana.mSystem['fan_coils']['data'][FC_Nbr][mKey])
            print('PUT fan coil : ' + mKey + ' ' + str( messana.mSystem['fan_coils']['data'][FC_Nbr][mKey]))
            print('nodeData : ' + str(nodeData))


print ('\n energy_sources')  
for EnergySourceNbr in range(0,messana.mSystem['system']['data']['mEnergySourceCount']):
    keys = messana.pullEnergySourceKeys(EnergySourceNbr)
    print (keys)
    messana.pullEnergySourceDataAll(EnergySourceNbr)
    messana.pullEnergySourceDataActive(EnergySourceNbr)
    keys = messana.pullEnergySourceKeys(EnergySourceNbr)
    print (keys)  
    for mKey in messana.mSystem['energy_sources']['GETstr']:
        messana.pullEnergySourceDataIndividual(EnergySourceNbr, mKey)
        if messana.mSystem['energy_sources']['data']:
            if mKey in  messana.mSystem['energy_sources']['PUTstr']:
                nodeData = messana.pushEnergySourceDataIndividual(EnergySourceNbr, mKey, messana.mSystem['energy_sources']['data'][EnergySourceNbr][mKey])
                print('PUT Buffer Tank : ' + mKey + ' ' + str( messana.mSystem['energy_sources']['data'][EnergySourceNbr][mKey]))
                print('nodeData : ' + str(nodeData))


print ('\n Buffer Tank')  
for BufferTankNbr in range(0,messana.mSystem['system']['data']['mBufTankCount']):
    keys = messana.pullBufferTankKeys(BufferTankNbr)
    print (keys)
    messana.pullBufferTankDataAll(BufferTankNbr)
    messana.pullBufferTankDataActive(BufferTankNbr)
    keys = messana.pullBufferTankKeys(BufferTankNbr)
    print (keys)  
    for mKey in messana.mSystem['buffer_tanks']['GETstr']:
        messana.pullBufferTankDataIndividual(BufferTankNbr, mKey)
        if mKey in  messana.mSystem['buffer_tanks']['PUTstr']:
            nodeData = messana.pushBufferTankDataIndividual(BufferTankNbr, mKey, messana.mSystem['buffer_tanks']['data'][BufferTankNbr][mKey])
            print('PUT Energy Source : ' + mKey + ' ' + str( messana.mSystem['buffer_tanks']['data'][BufferTankNbr][mKey]))
            print('nodeData : ' + str(nodeData))



print ('\n Domestic How Water')  
for DHW_Nbr in range(0,messana.mSystem['system']['data']['mDHWcount']):
    keys = messana.pullDHWKeys(DHW_Nbr)
    print (keys)
    messana.pullDHWDataAll(DHW_Nbr)
    messana.pullDHWDataActive(DHW_Nbr)
    keys = messana.pullDHWKeys(DHW_Nbr)
    print (keys)  
    for mKey in messana.mSystem['domsetic_hot_waters']['GETstr']:
        messana.pullDHWDataIndividual(DHW_Nbr, mKey)
        if mKey in  messana.mSystem['domsetic_hot_waters']['PUTstr']:
            nodeData = messana.pushDHWDataIndividual(DHW_Nbr, mKey, messana.mSystem['domsetic_hot_waters']['data'][DHW_Nbr][mKey])
            print('PUT Domestic Hot Water : ' + mKey + ' ' + str( messana.mSystem['domsetic_hot_waters']['data'][DHW_Nbr][mKey]))
            print('nodeData : ' + str(nodeData))



#messana.PUTSystemData(msysInfo)

sys.stdout.close() 
