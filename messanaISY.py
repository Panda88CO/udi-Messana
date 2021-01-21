class MessanaISY:
    def checkSetDriver(self, nodeName, keySet, ISYkey, mKey):
        LOGGER.debug('checkset driver ' + ISYkey + ' ,' + mKey)
        if nodeName == 'system':
            if mKey in self.keySet:
                valInfo = self.messana.pullSystemDataIndividual(mKey)
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
        else:
            return(False)


    def setParamFromISY(self, mKey, val):
        LOGGER.debug('setParamFromISY')
        if self.messana.pushSystemDataIndividual(mKey, val):
            LOGGER.info(mKey + ' updated to '+ str(val))
            temp = self.messana.getSystemISYdriverInfo(mKey)
            if temp != {}:
                ISYkey = temp['driver']
                LOGGER.debug('update ISY value: ' + ISYkey + ', ' + mKey)
                self.checkSetDriver(ISYkey, mKey)
        else:
            LOGGER.info(mKey + ' update failed')

    def updateParamsToISY(self, mKey):
        LOGGER.debug('setParamFromISY')
        temp = self.messana.getSystemISYdriverInfo(mKey)
        if temp != {}:
            LOGGER.debug('update ISY value')
            ISYkey = temp['driver']
            self.checkSetDriver(ISYkey, mKey)
        else:
            LOGGER.info(mKey + ' update failed')

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

            
    def setParamFromISY(self, mKey, val):
        LOGGER.debug('setParamFromISY')
        if self.messana.pushSystemDataIndividual(mKey, val):
            LOGGER.info(mKey + ' updated to '+ str(val))
            temp = self.messana.getSystemISYdriverInfo(mKey)
            if temp != {}:
                ISYkey = temp['driver']
                LOGGER.debug('update ISY value: ' + ISYkey + ', ' + mKey)
                self.checkSetDriver(ISYkey, mKey)
        else:
            LOGGER.info(mKey + ' update failed')

    def getMessanaSystemKeyVal(self, mKey, val):
        Info = self.messana.pullSystemDataIndividual(mKey)
        if mKey in self.system_GETKeys:
            if Info['statusOK']:
                val = Info['data']        
                if mKey == 'mUnitTemp': 
                    #"we cannot handle strings"
                    if val in  ['Celcius', 'Fahrenheit']:
                        if val == 'Celcius':
                            val = 0
                        else:  
                            val = 1 
            return(True)
        else:
            LOGGER.debug('Unknown key: ' + mKey)
            

    def updateParamsToISY(self, mKey):
        LOGGER.debug('setParamFromISY')
        temp = self.messana.getSystemISYdriverInfo(mKey)
        if temp != {}:
            LOGGER.debug('update ISY value')
            ISYkey = temp['driver']
            self.checkSetDriver(ISYkey, mKey)
        else:
            LOGGER.info(mKey + ' update failed')

            
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
                