
export BOLOS_ENV=/home/erik/projects/ledger/bolos-devenv
export BOLOS_SDK=/home/erik/projects/ledger/boilerplate/nanos-secure-sdk

make
cp bin/app.elf ~/projects/ledger/speculos/apps/ecdsasig.elf

make load

===

export SEED="barely sun snack this snack relief pipe attack disease boss enlist lawsuit"
./speculos.py apps/ecdsasig.elf
./speculos.py -d apps/ecdsasig.elf & ./tools/debug.sh apps/ecdsasig.elf
./speculos.py --seed "$SEED" apps/ecdsasig.elf
./speculos.py --seed "$SEED" -d apps/ecdsasig.elf & ./tools/debug.sh apps/ecdsasig.elf

===

# foo

echo 'e003000000' | LEDGER_PROXY_ADDRESS=127.0.0.1 LEDGER_PROXY_PORT=9999 python3 -m ledgerblue.runScript --apdu
1ae450e248537de7092a6d295522b5c610bf4412f7bc557c7dcc0cda82550a6f
echo 'e0031ae450e248537de7092a6d295522b5c610bf4412f7bc557c7dcc0cda82550a6f' | LEDGER_PROXY_ADDRESS=127.0.0.1 LEDGER_PROXY_PORT=9999 python3 -m ledgerblue.runScript --apdu

===

# without confirmation
echo 'e00200000900003039' | python3 -m ledgerblue.runScript --apdu
echo 'e00200000900003039' | LEDGER_PROXY_ADDRESS=127.0.0.1 LEDGER_PROXY_PORT=9999 python3 -m ledgerblue.runScript --apdu
# with confirmation
echo 'e00201000900003039' | python3 -m ledgerblue.runScript --apdu
echo 'e00201000900003039' | LEDGER_PROXY_ADDRESS=127.0.0.1 LEDGER_PROXY_PORT=9999 python3 -m ledgerblue.runScript --apdu
" app configuration
echo 'e001000000' | python3 -m ledgerblue.runScript --apdu
echo 'e001000000' | LEDGER_PROXY_ADDRESS=127.0.0.1 LEDGER_PROXY_PORT=9999 python3 -m ledgerblue.runScript --apdu

=== ledger-app-boilerplate/tests

LEDGER_PROXY_ADDRESS=127.0.0.1 LEDGER_PROXY_PORT=9999 ./test_foo.py

./test_example.py --account_number 12345

LEDGER_PROXY_ADDRESS=127.0.0.1 LEDGER_PROXY_PORT=9999 ./test_example.py --account_number 12345

PYTHONPATH=/home/erik/projects/ledger/boilerplate/btchip-python-1:/home/erik/projects/ledger/boilerplate/blue-loader-python LEDGER_PROXY_ADDRESS=127.0.0.1 LEDGER_PROXY_PORT=9999 python test_example.py --account_number 12345

===

- in the bitcoin main app, the APDU for message signing is E048

