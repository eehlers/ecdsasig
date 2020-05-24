# ecdsasig

<https://github.com/eehlers/ecsdasig>

## Overview
This is an app for the Ledger Nano S/X, the app generates an ECDSA signature of a message.

Normally you would use the Nano to sign a bitcoin transaction.  But your security model might call for you to generate an ECDSA signature of some other message.  For example, you might sign a hash of an application binary, as a means of authenticating the binary.  It can be convenient to use the Nano to generate such signatures.  Ideally when signing an arbitrary message, you would use Bitcoin Message Signing, which prepends a hard coded value to the signed message, thereby preventing an attacker from tricking you into inadvertently signing a transaction.  But sometimes Bitcoin Message Signing is not an option, for example if that format is not supported by the consumer to whom you are passing the signature.  This `ecsdsasig` app supports that use case by generating an ECDSA signature of an arbitrary message.  It is not advisable to install this app to a device whose secret relates to real funds.

## Building and installing
To build and install the app on your Ledger Nano S you must set up the Ledger Nano S build environments. Please follow the Getting Started instructions that are found [here](https://ledger.readthedocs.io/en/latest/userspace/getting_started.html).

If you don't want to set up a global environnment, you can also set one up just for this app by sourcing `prepare-devenv.sh` with the right target (`s` or `x`).

Install prerequisites and switch to a Nano X dev-env:
```bash
sudo apt install python3-venv python3-dev libudev-dev libusb-1.0-0-dev

# (x or s, depending on your device)
source prepare-devenv.sh x 
```

Compile and load the app onto the device:
```bash
make load
```

Refresh the repo (required after Makefile edits):
```bash
make clean
```

Remove the app from the device:
```bash
make delete
```

## Example usage

Test functionality:
```bash
cd ecdsasig/tests
python -m venv venv
source venv/bin/activate
cd /home/projects/ledger/blue-loader-python
pip install .
cd -
./test_ecdsasig.py
```
The app is headless and there is no user interaction.  The app is currently hard coded to sign using the key found at derivation path `m/42h/0h`.  The app could easily be enhanced to parameterize this value.

Here is a screenshot of an example test run against the emulator:
![screenshot](img/screenshot.png)

The script `test_ecdsasig_offline.py` generates a signature in software, without calling the ledger, this can be useful for purposes of troubleshooting.
