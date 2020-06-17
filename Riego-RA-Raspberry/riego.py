
import config
import arduinoUtils
import utils


v = '0.5'

arduinoSerialPort = None

def init(portArduino):
    global arduinoSerialPort
    arduinoSerialPort = portArduino
    testArduinoPort()
    
def testArduinoPort():
    global arduinoSerialPort
    getFullData()

def bombaOn():
    enciendeRele(config.ReleBomba)

def bombaOff():
    apagaRele(config.ReleBomba)    
    
def riegoOn():
    for i in config.Sectores:
        riegoOnSector(i)

def riegoOff():
    for i in config.Sectores:
        riegoOffSector(i)

def riegoOnSector(sectorID):
    if sectorID not in config.Sectores:
        utils.myLog("Sector {} no definido".format(sectorID))
    enciendeRele(sectorID)
    bombaOn()

def riegoOffSector(sectorID):
    if sectorID not in config.Sectores:
        utils.myLog("Sector {} no definido".format(sectorID))
    apagaRele(sectorID)
    bombaOff()

def enciendeRele(releID):
    global arduinoSerialPort
    if arduinoSerialPort != None:
        arduinoUtils.sendCommand(arduinoSerialPort,config.setReleCommand + str(releID) + config.releOnCommand, config.TimeoutRespuesta)
    else:
        utils.myLog('arduinoSerialPort == None')

def apagaRele(releID):
    global arduinoSerialPort
    if arduinoSerialPort != None:
        arduinoUtils.sendCommand(arduinoSerialPort,config.setReleCommand + str(releID) + config.releOffCommand, config.TimeoutRespuesta)
    else:
        utils.myLog('arduinoSerialPort == None')      

def getFullData():
    global arduinoSerialPort
    arduinoUtils.getDataArduino(arduinoSerialPort,config.TimeoutRespuesta)