from bit import Key
import time
import Transactions as transactions
def Terminal():
    print('-' * 70)
    command = input('[+]COMMAND:')
    if command == "send":
        transactions.SendBTC().GetTXInfo()
    else:
        Terminal()
class BTCInfo:
    firstRun = True
    username = ''
    my_key = Key('')
    def PrintBalance(self):
        balance = BTCInfo.my_key.get_balance('USD')
        balanceBTC = BTCInfo.my_key.get_balance('BTC')
        print("[+]Your Balances: " + balance, balanceBTC)
    def firstTimeSetup(self):
        print('Welcome to PyCoins!')
        name = input('[+]Please enter your name:')
        BTCInfo.username = name
        print('Welcome, {}!'.format(BTCInfo.username))
        key = input('[+]Enter your private key:')
        BTCInfo.my_key = key
        print('[+]PyCoins is ready!')
        time.sleep(3)

class Boot:
    def Banner(self):
        print('''
 _______              ______             __                     
/       \            /      \           /  |                    
$$$$$$$  | __    __ /$$$$$$  |  ______  $$/  _______    _______ 
$$ |__$$ |/  |  /  |$$ |  $$/  /      \ /  |/       \  /       |
$$    $$/ $$ |  $$ |$$ |      /$$$$$$  |$$ |$$$$$$$  |/$$$$$$$/ 
$$$$$$$/  $$ |  $$ |$$ |   __ $$ |  $$ |$$ |$$ |  $$ |$$      \ 
$$ |      $$ \__$$ |$$ \__/  |$$ \__$$ |$$ |$$ |  $$ | $$$$$$  |
$$ |      $$    $$ |$$    $$/ $$    $$/ $$ |$$ |  $$ |/     $$/ 
$$/        $$$$$$$ | $$$$$$/   $$$$$$/  $$/ $$/   $$/ $$$$$$$/  
          /  \__$$ |                                            
          $$    $$/                                             
           $$$$$$/             
                                            
A DunkinPirate Product
Uses the Bitcoin API 
Copyright (C) 2018 DunkinPirate''')
        print('-' * 80)
    def SetInfo(self):
        if BTCInfo.firstRun == True:
            print('''
[+]PyCoins has detected that this is the first time you have run the program.
---INITIATING FIRST-TIME SETUP---
''')
            BTCInfo().firstTimeSetup()
        elif BTCInfo.firstRun == False:
            pass

def main():
    Boot().Banner()
    Boot().SetInfo()
    BTCInfo().PrintBalance()

if __name__ == "__main__":
    main()
