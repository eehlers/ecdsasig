#!/usr/bin/env python3

import binascii

from ledgerblue.ecWrapper import PrivateKey, PublicKey
from ledgerblue.comm import getDongle

PUBLIC_KEY="0497E8C92F1ACB346CE29FA0E3D9C5582E39DC2C4F9BD59386822C3B9128EBA8C4FBBBC6A56CCF67B076AC20055EAF95EE9E382EFEFF2F1B9EBF3FF4F8BD9A8EA4"

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

