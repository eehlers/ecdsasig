#!/usr/bin/env python3

from ledgerblue.ecWrapper import PrivateKey, PublicKey
from ledgerblue.comm import getDongle
from ledgerblue.loadApp import parse_bip32_path

# This test assumes that your ledger has been initialized with the seed below,
# which comes from the ledger emulator,
# speculos.py in repo https://github.com/LedgerHQ/speculos.git.
# If you use a different seed then you will need to modify the test accordingly.
#DEFAULT_SEED = 'glory promote mansion idle axis finger extra february uncover one trip resource lawn turtle enact monster seven myth punch hobby comfort wild raise skin'

TEST_PATH = "42'/0'"

# The public key that will be used to verify the signature that comes back from the ledger.
# This key corresponds to DEFAULT_SEED and TEST_PATH.
# If you change the seed and/or path then you will need a different key to verify the signature.
PUBLIC_KEY="0499C3F628A6BCDEDCCC4AD6213EBD672A484EB7AE657FE6A8FA05D52AC9ED047C0D856564FD9C75E6FFF0DE70387B9B5AA94675B327078C18A3ED2E1486A4DDCC"

MESSAGE = "76955a821a8aa04acb48203a7df7113bfd1a0f479552d9098e032fa9b1917018"

print("MESSAGE=" + MESSAGE)

messageBin = bytes.fromhex(MESSAGE)

apduMessage = "E003"
apdu = bytearray.fromhex(apduMessage)
apdu.extend(parse_bip32_path(TEST_PATH, 10))
apdu.extend(messageBin)

dongle = getDongle(True)
signature = dongle.exchange(apdu)
print("signature=\n" + signature.hex())

publicKey = PublicKey(bytes.fromhex(PUBLIC_KEY), True)
verified = publicKey.ecdsa_verify(messageBin, signature, True)
print("verified=" + str(verified))

