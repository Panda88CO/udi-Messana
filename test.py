#!/usr/bin/env python3
#import polyinterface
import sys
import requests
from subprocess import call
import json
from collections import defaultdict



#self.messana = MessanaInfo
#self.messana.updateSystemData()
#self.systemGETKeys = self.messana.systemPullKeys()
#self.systemPUTKeys = self.messana.systemPushKeys()
#self.nodedef = open('nodedefTemp.xml', 'wt')
#self.en_us = open('en_usTemp.txt', 'wt')
#self.editor = open('editorTemp.xml', 'wt')
nodeCount = 0
nodedefIdName = 'node'
nlsIdName = 'nls'
setupStruct = {'nodeDef':{}
                    ,'editors':{}
                    ,'nls':{}}
'''
self.setupStruct = {'nodeDef': {}nodeNbr: { 'nodeDef':{}
                                            ,'sts':{}
                                            ,'cmds':{
                                                    'sends':{}
                                                    ,'accepts':{}
                                                    } 
                                            }
                                }
                    ,'editors':{id:Name, range:{}}
                    ,'nls':{}
                    }
'''


setupStruct['nodeDef'][nodeCount] = {}
setupStruct['nodeDef'][nodeCount]['id'] = nodedefIdName
setupStruct['nodeDef'][nodeCount]['nlsId'] = nlsIdName
setupStruct['nodeDef'][nodeCount]['sts'] = {}
setupStruct['nodeDef'][nodeCount]['cmds'] = {}
setupStruct['nodeDef'][nodeCount]['cmds']['sends'] = {}
setupStruct['nodeDef'][nodeCount]['cmds']['accepts'] = {}
setupStruct['nodeDef'][nodeCount]['cmds']['accepts']['SET_STATUS'] = {}
setupStruct['nodeDef'][nodeCount]['cmds']['accepts']['UPDATE'] = None

print(setupStruct)




