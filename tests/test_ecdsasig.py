#!/usr/bin/env python3

import binascii

from ledgerblue.ecWrapper import PrivateKey, PublicKey
from ledgerblue.comm import getDongle
from ledgerblue.loadApp import parse_bip32_path

#PUBLIC_KEY="0480F8889656CE6CCACBAD707D16E9805BA05E160D48066FEBC98FC28E785B46FEA57C854096EA0ED65434283148D84E39567BB379E214ABC8539A25E6605A5882"
PUBLIC_KEY="0499C3F628A6BCDEDCCC4AD6213EBD672A484EB7AE657FE6A8FA05D52AC9ED047C0D856564FD9C75E6FFF0DE70387B9B5AA94675B327078C18A3ED2E1486A4DDCC"

message = "76955a821a8aa04acb48203a7df7113bfd1a0f479552d9098e032fa9b1917018"

print("message=" + message)

messageBin = binascii.unhexlify(message)

apduMessage = "E003"
apdu = bytearray.fromhex(apduMessage)
apdu.extend(parse_bip32_path("42'/0'", 10))
apdu.extend(messageBin)

dongle = getDongle(True)
signature = dongle.exchange(apdu)
print("signature=\n" + str(binascii.hexlify(signature)))

publicKey = PublicKey(binascii.unhexlify(PUBLIC_KEY), True)
verified = publicKey.ecdsa_verify(messageBin, signature, True)
print("verified=" + str(verified))

