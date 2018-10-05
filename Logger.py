import PyCoins as pyCoins
import Transactions as transactions
from bit import Key
import os
import time

def WriteTransaction():
    address = transactions.SendBTC.ReceivingAddress
    amt = transactions.SendBTC.Amount
    tx_log = open('Transactions.txt', 'w')
    tx_log.write(address)
    tx_log.write(amt)
    tx_log.close()
