#!/usr/bin/env python3

import binascii

from ledgerblue.ecWrapper import PrivateKey
from ledgerblue.comm import getDongle

message = "76955a821a8aa04acb48203a7df7113bfd1a0f479552d9098e032fa9b1917018"

print("message=" + message)

messageBin = binascii.unhexlify(message)

apduMessage = "E003"
apdu = bytearray.fromhex(apduMessage)
apdu.extend(messageBin)

dongle = getDongle(True)
ret = dongle.exchange(apdu)
print("sig=\n" + str(binascii.hexlify(ret)))

