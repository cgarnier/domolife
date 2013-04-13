__author__ = 'Clement'
import serial


ser = serial.Serial('/dev/ttyUSB0', 57600, timeout=1)
def ByteToHex( byteStr ):
    return ''.join( [ "%02X " % ord( x ) for x in byteStr ] ).strip()

while True:
    print ByteToHex(ser.read(100))
