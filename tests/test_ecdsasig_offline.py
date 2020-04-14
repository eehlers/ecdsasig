#!/usr/bin/env python3

import binascii

from ledgerblue.ecWrapper import PrivateKey

PRIVATE_KEY="cf1094c960a753e8f848411aaae578a7083391165c4d39b78af6e81c310d0b5e"

message = "745f30a9bf9a90a7d529a6bbba9635762baea83da2e2f147e5738b9795d22b85"

print("message=" + message)

masterPrivate = PrivateKey(binascii.unhexlify(PRIVATE_KEY))
signature = masterPrivate.ecdsa_sign(binascii.unhexlify(message), raw=True)
print("signature=" + str(binascii.hexlify(signature)))

