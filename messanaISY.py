#!/usr/bin/env python3

import polyinterface
from MessanaInfoPlay import messanaInfo

LOGGER = polyinterface.LOGGER
class messanaPoly(polyinterface):
    def __init__(self, polyglot ):
        super().__init__(polyglot)
        LOGGER.debug ('__Init__ messanaPoly' )
      
    def start(self):
        self.removeNoticesAll()
        self.addNotice('Please Set IP address (IP_ADDRESS) and Messana Key (MESSANA_KEY):','Credentials')

        self.IPAddress = self.getCustomParam('IP_ADDRESS')
        if self.IPAddress is None:
            self.IPAddress= '192.168.2.65'
            LOGGER.error('IP address not set')
            self.addCustomParam({'IP_ADDRESS': self.IPAddress})
        
        self.MessanaKey = self.getCustomParam('MESSANA_KEY')
        if self.MessanaKey is None:
            self.MessanaKey =  '9bf711fc-54e2-4387-9c7f-991bbb02ab3a'
            LOGGER.error('check_params: Messana Key not specified')
            self.addCustomParam({'MESSANA_KEY': self.MessanaKey})
        '''
        if 'IP_ADDRESS' in self.polyConfig['customParams']:
            LOGGER.debug('IP address detected')
            self.IPaddress = self.polyConfig['customParams']['IP_ADDRESS']
        else:
        '''
        self.messana = messanaInfo(self.IPaddress, self.MessanaKey, messanaPoly.id )
        LOGGER.debug('MessanaInfo call done')
        self.system_GETKeys = self.messana.systemPullKeys()
        self.system_PUTKeys = self.messana.systemPushKeys()
        self.system_ActiveKeys = self.messana.systemActiveKeys()
        
        self.messana.updateSystemData('all')
        self.messana.addSystemDefStruct(self.address)
    
        LOGGER.debug('Install Updated profile')
        self.poly.installprofile()


    def getSystemDrivers(self):
        LOGGER.debug('Append System drivers')
        for key in self.system_GETKeys:
            temp = self.messana.getSystemISYdriverInfo(key)
            LOGGER.debug('Driver info: ' + str(temp))
            if  temp != {}:
                if not(str(temp['value']).isnumeric()):                         
                    LOGGER.debug('non numeric value :' + temp['value'])
                    if temp['value'] == 'Celcius':
                        temp['value'] = 0
                        self.ISYTempUnit = 4
                    else:
                        temp['value'] = 1
                        self.ISYTempUnit = 17
                LOGGER.debug(str(temp) + 'before append')    
        return(temp)

    def getZoneCount(self):
        return(messana.mSystem['system']['data']['mZoneCount'])

    def getMacrozoneCount(self):
    
    def getATUcount(self):
    



class messanaController(messanaPoly.Controller):
    def __init__(self, polyglot, messanaIPaddress, messanaKey ):
        super().__init__(polyglot)
        LOGGER.info('_init_')
        self.messanaImportOK = 0
        self.name = 'Messana Main Control'
        self.address ='messanasys'
        self.primary = self.address
        self.hb = 0
        self.reportDrivers()
        self.ISYdrivers=[]
        self.ISYcommands = {}
        self.ISYTempUnit = 0
        #try:
        #self.messana = messanaInfo('192.168.2.65', '9bf711fc-54e2-4387-9c7f-991bbb02ab3a', MessanaController.id )
        LOGGER.debug('MessanaInfo call done')

        #self.system_GETKeys = self.messana.systemPullKeys()
        #self.system_PUTKeys = self.messana.systemPushKeys()
        #self.system_ActiveKeys = self.messana.systemActiveKeys()

  
        self.temp = messanaPoly.getSystemDrivers()    
        messanaController.drivers.append(self.temp)
        LOGGER.debug(str(messanaController.drivers) + 'after append')                       
        LOGGER.debug(messanaController.drivers)
        #self.check_params()
        #self.discover()   
        
        self.updateInfo('all')
        self.messanaImportOK = 1
        self.discover()

        #except:
            #LOGGER.debug('Reading data from Messana System NOT successful')

class messanaNode(polyinterface.Node):
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