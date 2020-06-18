import os
import sys
import glob
import time
import datetime
import os,subprocess
import json
import requests



messanaAPIKey = 'apikey=9bf711fc-54e2-4387-9c7f-991bbb02ab3a'
MessanaIP = 'http://192.168.2.45'
systemStr = '/api/system'
zoneStr = '/api/zone'
GetStr =MessanaIP+systemStr+'/zoneCount/?'+ messanaAPIKey


zones =  requests.get(GetStr).json()
nbrZone = zones['count']
i=0
namedZones=[]
for i in range(0, nbrZones):
    GetStr =MessanaIP+zoneStr+'/name/'+str(i)+'?'+ messanaAPIKey
    namedZones[i] =  requests.get(GetStr).json()
    GetStr =MessanaIP+zoneStr+'/setPoint/'+str(i)+'?'+ messanaAPIKey
    print(namedZones[i]['value'])
print()


