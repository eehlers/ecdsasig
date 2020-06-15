#!/usr/bin/env python3

from ledgerblue.ecWrapper import PrivateKey, PublicKey

PRIVATE_KEY="CAE11C52A687BBDBE25F670CAE7906EBA6DB13CEE1C8B7D8F0C208783DE43A91"
PUBLIC_KEY="0480F8889656CE6CCACBAD707D16E9805BA05E160D48066FEBC98FC28E785B46FEA57C854096EA0ED65434283148D84E39567BB379E214ABC8539A25E6605A5882"

MESSAGE = "76955a821a8aa04acb48203a7df7113bfd1a0f479552d9098e032fa9b1917018"

print("MESSAGE=" + MESSAGE)

messageBin = bytes.fromhex(MESSAGE)

privateKey = PrivateKey(bytes.fromhex(PRIVATE_KEY))
signature = privateKey.ecdsa_sign(messageBin, raw=True)
print("signature=" + signature.hex())

publicKey = PublicKey(bytes.fromhex(PUBLIC_KEY), True)
verified = publicKey.ecdsa_verify(messageBin, signature, True)
print("verified=" + str(verified))

