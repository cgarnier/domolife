from sys import argv
from enOcean.Modules.Rcm250 import Rcm250
import serial


" Python example script - light on/off something with an EnOcean Rcm250"

ser = serial.Serial('/dev/ttyUSB0', 57600, timeout=1)



# Rcm 250
rcm = Rcm250(ser)
rcm.setId([0xFF, 0xFF, 0xff, 0xff])

senderId = [0xFF, 0xFF, 0x77, 0x01]


def printUsage():
    print 'Usage: python light.py [On|Off] [Virtual button address].'
    print 'Virtual sender address - default FF:FF:77:01.'


if len(argv) == 3:
    senderIdstr = argv[2].split(':')
    if len(senderIdstr) != 4:
        printUsage()
        exit()
    else:
        # str list to int list
        senderId = []
        for x in senderIdstr:
            senderId.append(int(x, 16))

rcm.setSenderId(senderId)

error = True;
if len(argv) > 1:
    if argv[1] in ['on', 'On', 'ON']:
        error = False
        rcm.switchOn()
    if argv[1] in ['off', 'Off', 'OFF']:
        error = False
        rcm.switchOff()
    if error:
        printUsage()
        exit()
else:
    printUsage()