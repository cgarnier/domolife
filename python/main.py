from enOcean.telegram.BaseTelegram import BaseTelegram



# Construction d un telegram de base (Allumer)
base = BaseTelegram()
base.setType(BaseTelegram.RADIO)
base.setData([0xF6, 0x10, 0x00, 0x00, 0x00, 0x00, 0x30 ])
base.setOptionalData([0x01, 0xFF, 0xFF, 0xFF, 0xFF, 0x2D, 0x00])







print base.toString()
print '\n'
print base.fromBytes(base.toByte())
print base.toString()

