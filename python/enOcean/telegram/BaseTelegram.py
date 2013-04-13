from tools.CRC8 import CRC8

__author__ = 'Clement'

class BaseTelegram:
    """ BaseTelegram used to make an EnOcean telegram.




    """
    RADIO               = 0x01
    RESPONSE            = 0x02
    RADIO_SUB_TEL       = 0x03
    EVENT               = 0x04
    COMMON_COMMAND      = 0x05
    SMART_ACK_COMMAND   = 0x06
    REMOTE_MAN_COMMAND  = 0x07

    def __init__(self):
        self.sync = [0x55]
        self.dataLength = [0x00 , 0x00]
        self.optionalLength = [ 0x00]
        self.packetType = [0x00]
        self.crcHeader = [0x00]
        self.data = [ ]
        self.optionalData = [ ]
        self.crcData = [0x00]


        self.CRCGen = CRC8()


    def fromBytes(self, bytes):
        "Convert byte list to BaseTelegram"
        values = []
        for x in bytes:
            values.append(ord(x))

        crc = values[5]
        caCrc = self.CRCGen.fromInt(values[1:5])

        if crc != caCrc:
            raise BadCrcException('Header CRC check has failed')

        self.dataLength[0] = values[1]
        self.dataLength[1] = values[2]
        l = values[1] * 0xFF + values[2]
        self.optionalLength[0] = values[3]
        self.packetType[0] = values[4]

        crc = values[len(values) -1]
        caCrc = self.CRCGen.fromInt(values[6:len(values) -1])

        if crc != caCrc:
            raise BadCrcException('Data CRC check has failed')

        if len(values[6:len(values) -1]) != l + self.optionalLength[0]:
            raise BadDataLengthException()

        self.data = values[6:6+l]
        self.optionalData = values[6+l: 6+l+self.optionalLength[0]]






    def toIntList(self):
        "Return the BaseTelegram in integer list form"

        self.prepare()
        res = []
        res.extend(self.sync)
        res.extend(self.dataLength)
        res.extend(self.optionalLength)
        res.extend(self.packetType)
        res.extend(self.crcHeader)
        res.extend(self.data)
        res.extend(self.optionalData)
        res.extend(self.crcData)
        return res


    def toByte(self ):
        "return the bytes values of the telegram"
        bytes = []
        for x in self.toIntList():
            bytes.append(chr(x))
        return ''.join( bytes )

    def toString(self):
        "return the hexadecimal values of the telegram"
        res = ''
        for x in self.toIntList():
            res += ' '+hex(x)
        return res

    def setType(self,type):
        """Set the type of telegram
            Values are:

    RADIO               = 0x01
    RESPONSE            = 0x02
    RADIO_SUB_TEL       = 0x03
    EVENT               = 0x04
    COMMON_COMMAND      = 0x05
    SMART_ACK_COMMAND   = 0x06
    REMOTE_MAN_COMMAND  = 0x07
    other (0xXX)
        """
        self.packetType[0] = type

    def setOptionalData(self,opData):
        "Set the telegram optional data"
        self.optionalData = opData

    def setData(self,data):
        "Set the telegram data"
        self.data = data

    def prepare(self):
        "Prepare the telegram. Compute header lengths and CRCs."
        self.computeLengths()
        self.computeCrc8()


    def computeCrc8(self):
        "Compute header and data CRCs"
        header = []
        header.extend(self.dataLength)
        header.extend(self.optionalLength)
        header.extend(self.packetType)
        self.crcHeader[0] = self.CRCGen.fromInt(header)

        data = []
        data.extend(self.data)
        data.extend(self.optionalData)
        self.crcData[0] = self.CRCGen.fromInt(data)


    def computeLengths(self):
        "Compute data length and optional data length"
        size  = len(self.data)
        self.dataLength[0] = size / 0xFF
        self.dataLength[1] = size % 0xFF
        self.optionalLength[0] = len(self.optionalData)

class BadCrcException(Exception):

    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

class BadDataLengthException(Exception):
    def __init__(self):
        pass
    def __str__(self):
        return repr('Data length in header mismatched with packet length')

