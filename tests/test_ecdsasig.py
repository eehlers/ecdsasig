#!/usr/bin/env python3

import binascii
import hashlib
#import sys

#from ledgerblue.hexLoader import HexLoader
#from ledgerblue.hexParser import IntelHexParser, IntelHexPrinter
from ledgerblue.ecWrapper import PrivateKey
from ledgerblue.comm import getDongle

#from btchip.btchip import *
#from btchip.btchipUtils import *

#targetId = 0x31000004
#targetVersion="1.6.0"
#PRIVATE_KEY="ac67919e420220906bca628c9a7ad5cfe3934ac5740f38a49435c10e6f01e2db"

#parser = IntelHexParser("bin/app.hex")
#printer = IntelHexPrinter(parser)
#
#fileTarget = open("/tmp/app.bin", "wb")
#class FileCard():
#    def __init__(self, target):
#        self.target = target
#    def exchange(self, apdu):
#        #if (args.apdu):
#        #    print(binascii.hexlify(apdu))
#        apdu = binascii.hexlify(apdu)
#        if sys.version_info.major == 2:
#            self.target.write(str(apdu) + '\n')
#        else:
#            self.target.write(apdu + '\n'.encode())
#        return bytearray([])
#    def apduMaxDataSize(self):
#        # ensure to allow for encryption of those apdu afterward
#        return 240
#dongle = FileCard(fileTarget)
#
#loader = HexLoader(dongle, 0xe0, False, None, cleardata_block_len=None)
##hash = loader.load(0x0, 0xF0, printer, targetId=targetId, targetVersion=targetVersion, doCRC=True)
hash = "76955a821a8aa04acb48203a7df7113bfd1a0f479552d9098e032fa9b1917018"

print("Application full hash : " + hash)

#masterPrivate = PrivateKey(bytes(bytearray.fromhex(PRIVATE_KEY)))
#sig = masterPrivate.ecdsa_sign(bytes(binascii.unhexlify(hash)), raw=True)
#signature = masterPrivate.ecdsa_serialize(sig)
#print("Application signature: " + str(binascii.hexlify(signature)))

messageBin = binascii.unhexlify(hash)

h2 = hashlib.sha256()
h2.update(messageBin)
print("hash=\n" + h2.hexdigest())

MESSAGE = messageBin

apduMessage = "E003"
apdu = bytearray.fromhex(apduMessage)
apdu.extend(messageBin)

dongle = getDongle(True)
ret = dongle.exchange(apdu)
print("ret=\n" + str(binascii.hexlify(ret)))

