#!/usr/bin/python3
from fints.client import FinTS3PinTanClient
import configparser
import json

config = config = configparser.ConfigParser()
config.read('environment.conf') # We hardcode for now, because... we can
blz = config['fints']['blz']
account = config['fints']['username']
pin = config['fints']['pin']
endpoint = config['fints']['endpoint']


# Connect to the bank
BankConnection = FinTS3PinTanClient(blz, account, pin, endpoint)

with BankConnection:
    MyInformation = BankConnection.get_information()
    MyAccount = BankConnection.get_sepa_accounts()[0]
    MyBalance = BankConnection.get_balance(MyAccount)
    print("Current balance is: %s" % MyBalance.amount.amount)
    print(json.dumps({MyInformation['bank']['name'] : { MyInformation['accounts'][0]['iban'] : '%10.2f' % ( MyBalance.amount.amount)}}))
