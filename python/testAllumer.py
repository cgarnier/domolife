from time import sleep
from enOcean.Modules.Rcm250 import Rcm250
from enOcean.telegram.BaseTelegram import BaseTelegram
import serial



ser = serial.Serial('/dev/ttyUSB0', 57600, timeout=1)


# Construction d un telegram de base (Allumer)
base = BaseTelegram()
base.setType(BaseTelegram.COMMON_COMMAND)
base.setData([0x07, 0xFF, 0xFF, 0x77, 0x01])
#base.setOptionalData([0x01, 0xFF, 0xFF, 0xFF, 0xFF, 0x2D, 0x00])

# Envoi
#ser.write(base.toByte())



# Reception
#base.fromBytes(ser.read(100))   #Raise BadCrcException ou BadDataLengthException si le packet est mal forme

# Rcm 250
rcm = Rcm250(ser)
rcm.setId([0xFF, 0xFF, 0xff, 0xff])
rcm.setSenderId([0xFF, 0xFF, 0x77, 0x01])
rcm.switchOn()
sleep(3)
rcm.switchOff()