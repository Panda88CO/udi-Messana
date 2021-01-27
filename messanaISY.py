#!/usr/bin/env python3

import polyinterface

LOGGER = polyinterface.LOGGER
class MessanaNode(polyinterface.Node):
    def __init__(self, controller, primary, address, name, nodeType, nodeNbr, messana):
        super().__init__(controller, primary, address, name)
        self.nodePullKeys = messana.getNodeKeys (nodeNbr, nodeType, 'GETstr')
        self.nodePushKeys = messana.getNodeKeys (nodeNbr, nodeType, 'PUTstr')
        self.nodeActiveKeys = messana.getNodeKeys (nodeNbr, nodeType, 'Active')
        self.nodeNbr = nodeNbr
        self.node = nodeType

    def updateInfo(self, level):
        #LOGGER.info('Update Messana ' + self.node + ' ' + str(self.nodeNbr)) 
        print('Update Messana ' + self.node + ' ' + str(self.nodeNbr))
        if level == 'active':
            for mKey in self.nodeActiveKeys: 
                #LOGGER.debug('active ' + mKey)
                self.updateParamsToISY(mKey)
                
        elif level == 'all':
            for mKey in self.nodePullKeys: 
                self.updateParamsToISY(mKey)
                #LOGGER.debug('all ' + mKey)
        #else:
            #LOGGER.debug('unknown level' + level)

 
            
    def pullAllMessanaStatus(self):
        return(True)

    def setParamFromISY(self, mKey, val):
            #LOGGER.debug('setParamFromISY')
            if self.messana.pushNodeDataIndividual(mKey, val):
                #LOGGER.info(mKey + ' updated to '+ str(val))
                temp = self.messana.getNodeISYdriverInfo('zones', self.zoneNbr, mKey)
                if temp != {}:
                    ISYkey = temp['driver']
                    #LOGGER.debug('update ISY value: ' + ISYkey + ', ' + mKey)
                    self.checkSetDriver(ISYkey, mKey)
            else:
                LOGGER.info(mKey + ' update failed')

        
    def updateParamsToISY(self, mKey):
        #LOGGER.debug('setParamFromISY ' + self.node + ' ' + str(self.nodeNbr))
        temp = self.messana.getnodeISYdriverInfo(self.node, self.nodeNbr, mKey)
        if temp != {}:
            #LOGGER.debug('update ISY value')
            ISYkey = temp['driver']
            self.checkSetDriver(ISYkey, mKey)
        else:
            LOGGER.info(mKey + ' update failed')

    def checkSetDriver(self, ISYkey, mKey):
        #LOGGER.debug('checkset driver ' + self.node + ' '+ str(self.nodeNbr)+ ' ' + ISYkey + ' ,' + mKey)
        if mKey in self.keySet:
            valInfo = self.pullNodeDataIndividual(self.nodeNbr, self.node, mKey)
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