#!/usr/bin/env python3

import polyinterface
class MessanaNode(polyinterface.Node):
    def __init__(self, controller, primary, address, name, nodeType, nodeNbr,  messana):
        super().__init__(controller, primary, address, name)


    def pullAllMessanaStatus(self):
        return(True)

    def updateInfo(self, level):
        LOGGER.info('Update Messana System ')
        if level == 'active':
            for mKey in self.system_ActiveKeys: 
                LOGGER.debug('active ' + mKey)
                self.updateParamsToISY(mKey)
                
        elif level == 'all':
            for mKey in self.system_GETKeys: 
                self.updateParamsToISY(mKey)
                LOGGER.debug('all ' + mKey)
        else:
            LOGGER.debug('unknown level' + level)

 
            
    def pullAllMessanaStatus(self):
        return(True)

    def setParamFromISY(self, mKey, val):
            LOGGER.debug('setParamFromISY')
            if self.messana.pushNodeDataIndividual(mKey, val):
                LOGGER.info(mKey + ' updated to '+ str(val))
                temp = self.messana.getNodeISYdriverInfo('zones', self.zoneNbr, mKey)
                if temp != {}:
                    ISYkey = temp['driver']
                    LOGGER.debug('update ISY value: ' + ISYkey + ', ' + mKey)
                    self.checkSetDriver(ISYkey, mKey)
            else:
                LOGGER.info(mKey + ' update failed')

    def updateInfo(self, level):
        LOGGER.info( 'Update Info - Zone ' + str(self.zoneNbr) + ' Data update')
        if level == 'active':
            for mKey in self.zone_ActiveKeys: 
                LOGGER.debug('Zone active ' + mKey)
                self.updateParamsToISY(mKey)
                
        elif level == 'all':
            for mKey in self.zone_GETKeys: 
                self.updateParamsToISY(self, mKey)
                LOGGER.debug('Zone all ' + mKey)
        else:
            LOGGER.debug('unknown level' + level)
        
    def updateParamsToISY(self, mKey):
        LOGGER.debug('setParamFromISY')
        temp = self.messana.getnodeISYdriverInfo('zones', self.zoneNbr, mKey)
        if temp != {}:
            LOGGER.debug('update ISY value')
            ISYkey = temp['driver']
            self.checkSetDriver(ISYkey, mKey)
        else:
            LOGGER.info(mKey + ' update failed')

    def checkSetDriver(self, ISYkey, mKey):
        if mKey in self.zoneInfo:
            self.setDriver(ISYkey, self.zoneInfo[mKey])
                