
export BOLOS_ENV=/home/erik/projects/ledger/bolos-devenv
export BOLOS_SDK=/home/erik/projects/ledger/authorization/repos/nanos-secure-sdk

cp bin/app.elf ~/projects/ledger/speculos/apps/ecdsasig.elf

./speculos.py apps/ecdsasig.elf
./speculos.py -d apps/ecdsasig.elf & ./tools/debug.sh apps/ecdsasig.elf

LEDGER_PROXY_ADDRESS=127.0.0.1 LEDGER_PROXY_PORT=9999 python ./test_example.py

===

./test_example.py

ledgerblue.commException.CommException: Exception : Invalid status 6700 (Unknown reason)

-> ecdsasig app is not open

ledgerblue.commException.CommException: Exception : Invalid status 6d00 (Unexpected state of device: verify that the right application is opened?)

-> wrong app (in this case, Bitcoin) is open

ledgerblue.commException.CommException: Exception : Invalid status 6804 (Unknown reason)

-> ?  I get this error with the device connected and the ecdsasig app open.  FOr some reason the command works against the emulator but not against a physical device.

