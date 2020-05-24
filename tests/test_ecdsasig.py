#!/usr/bin/env python3

import binascii

from ledgerblue.ecWrapper import PrivateKey, PublicKey
from ledgerblue.comm import getDongle

PUBLIC_KEY="0480F8889656CE6CCACBAD707D16E9805BA05E160D48066FEBC98FC28E785B46FEA57C854096EA0ED65434283148D84E39567BB379E214ABC8539A25E6605A5882"

message = "76955a821a8aa04acb48203a7df7113bfd1a0f479552d9098e032fa9b1917018"

print("message=" + message)

messageBin = binascii.unhexlify(message)

apduMessage = "E003"
apdu = bytearray.fromhex(apduMessage)
apdu.extend(messageBin)

dongle = getDongle(True)
signature = dongle.exchange(apdu)
print("signature=\n" + str(binascii.hexlify(signature)))

publicKey = PublicKey(binascii.unhexlify(PUBLIC_KEY), True)
verified = publicKey.ecdsa_verify(messageBin, signature, True)
print("verified=" + str(verified))

