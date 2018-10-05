import PyCoins as pyCoins
from bit import Key
import time

class SendBTC:
    ReceivingAddress = ''
    Amount = 0
    def GetTXInfo(self):
        addr = input('[+]Enter receiving address:')
        SendBTC.ReceivingAddress = addr
        amt = float(input('[+]Enter amount in BTC:'))
        SendBTC.Amount = amt
        final = input('[+]Confirm transaction? {} BTC to ' + SendBTC.ReceivingAddress).format(SendBTC.Amount)
    def Send(self):
        try:
            pyCoins.BTCInfo.my_key.send('{}', SendBTC.Amount, 'btc').format(SendBTC.ReceivingAddress)
        except:
            print('[+]Transaction failed')
        print('[+]Transaction successful! You sent {} BTC to ' + SendBTC.ReceivingAddress).format(SendBTC.Amount)
        print('[+] Your balance is now {} BTC').format(pyCoins.BTCInfo.my_key.get_balance('btc'))
        # Write function here

