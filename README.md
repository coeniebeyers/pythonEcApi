# Hashblock

Example Python 2/3 code for interfacing with the ECC API Server at https://github.com/rynobey/ECC-API

Two endpoints are requested:

1. `/isAlive`
2. `/ec/add`

This pattern may be followed for requesting any of the other ECC endpoints which may be needed.

## Dependencies
1. Follow the installation instructions of https://github.com/rynobey/ECC-API
2. Follow the instructions to on https://pip.pypa.io/en/stable/installing to install Pip
3. Python `requests`
   1. `pip install requests` - Python 2
   2. `pip3 install requests` - Python 3


## Installation + Running
1. Ensure https://github.com/rynobey/ECC-API is running
2. `git clone git@github.com:coeniebeyers/hashblock2018_3.git`
3. `cd hashblock2018_3`
4. Runing `ecc.py`
   1. `python2 ecc.py` - Python 2
   2. `python3 ecc.py` - Python 3
