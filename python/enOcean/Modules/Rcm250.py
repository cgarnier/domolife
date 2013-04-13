

__author__ = 'Clement'
from enOcean.telegram.BaseTelegram import BaseTelegram

class Rcm250:
    """ This class permit to use a rcm250.

    Learning:
    - Pull LRN button on Rcm250
    - Set the sender id you want with setSenderId method
    - Use the switchOn method.

    """
    def __init__(self, serial):
        self.id = [0xFF, 0xFF, 0xFF, 0xFF]
        self.senderId = [0x00, 0x00, 0x00, 0x00]

        self.action = [0x10]
        self.serial = serial

        self.tel = BaseTelegram()
        self.tel.setType(BaseTelegram.RADIO)

    def setId(self,id):
        self.id = id

    def setSenderId(self,id):
        self.senderId = id


    def switchOn(self):
        data = [0xF6, 0x10] + self.senderId + [0x30]
        self.tel.setData(data)
        opData = [0x01] + self.id + [0x2D,0x00]
        self.tel.setOptionalData(opData)
        self.serial.write(self.tel.toByte())


    def switchOff(self):
        data = [0xF6, 0x30] + self.senderId + [0x30]
        self.tel.setData(data)
        opData = [0x01] + self.id + [0x2D,0x00]
        self.tel.setOptionalData(opData)
        self.serial.write(self.tel.toByte())



