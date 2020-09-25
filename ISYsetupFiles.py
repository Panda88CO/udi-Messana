#!/usr/bin/env python3
#import polyinterface
import sys
import requests
from subprocess import call
import json
from collections import defaultdict
from MessanaInfoPlay import MessanaInfo


#LOGGER = polyinterface.LOGGER
        
#sys.stdout = open('Messanaoutput.txt','wt')

messana = MessanaInfo('192.168.2.65' , '9bf711fc-54e2-4387-9c7f-991bbb02ab3a')
messana.init()

#Retrive basic system info
print('\nSYSTEM')
#messana.updateSystemData()
systemGETKeys = messana.systemPullKeys()
systemPUTKeys = messana.systemPushKeys()
systemActiveKeys = messana.systemActiveKeys()

class ISYsetupFiles:
    def __init__ (self, MessanaInfo):
        self.messana = MessanaInfo
        self.messana.updateSystemData()
        self.systemGETKeys = self.messana.systemPullKeys()
        self.systemPUTKeys = self.messana.systemPushKeys()
        #self.nodedef = open('nodedefTemp.xml', 'wt')
        #self.en_us = open('en_usTemp.txt', 'wt')
        #self.editor = open('editorTemp.xml', 'wt')
        self.nodeCount = 0
        self.nodedefIdName = 'node'
        self.nlsIdName = 'nls'
        self.setupStruct = {'nodeDef':{}
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

    def initializeNodeDefFile(self, nodedefName, nodedefIdName, nlsIdName):
        self.nodedef = open(nodedefName, 'wt')

    
    def addSTSNodeDef(self, id, editor, nodeId):

        return()

    def addCMDsendsNodeDef(self):
        return()

    def addCMDacceptsNodeDef(self):
        return()


