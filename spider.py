import  time
from bip_utils import Bip39MnemonicGenerator, Bip39SeedGenerator, Bip44, BitcoinPrivateKey, BitcoinPublicKey
from bit import Key
class Settings:
    MultiLayer=True
    CrossChain=True
    
    Fake = True
    FakePercentage = 0
    Accounts = 0

    Crypto = ""
    Key = ""
    
def ChooseInput():
    print("Welcome to spider, choose your input cryptocurrency:")
    print("[1] btc")
    print("Enter Choice: ")
    if input().strip() == '1':
        Settings.Crypto == "btc"
    else:
        print("Invalid Input")
        ChooseInput()
        
def ChangeSettings():
    print("Select Settings you want to enable, you can choose multiple just type the number out (123 = setting 1 2 and 3):")
    print("[1] MultiLayer [2] Cross Chain [3] Fake Addresses")
    print("Enter Input (leave blank to skip): ")
    choice = input().strip()
    
    Settings.MultiLayer = '1' in choice
    Settings.CrossChain = '2' in choice
    Settings.Fake = '3' in choice
    
    if not any([Settings.MultiLayer, Settings.CrossChain, Settings.Fake]) and choice != "":
        print("Invalid input. Please try again.")
        ChangeSettings()

def SetupWallet():
    print("Would you like to use a new wallet or use your private key")
    print("[1] New Wallet [2] Private Key")
    temp = input().strip()
    if temp == '1':
        if Settings.Crypto == "btc":
            seed_bytes = Bip39SeedGenerator(Bip39MnemonicGenerator.FromWordsNumber(12)).Generate()
            btc_wallet = Bip44.FromSeed(seed_bytes).Purpose().CoinIndex(0).Account(0).Chain(0)
            Settings.Key = btc_wallet.PrivateKey()
            print("Please copy the info below and place it somewhere safe:")
            print(f"Your new wallet is: {btc_wallet}")
            print(f"Your private key is: {Settings.Key}")
            print("Please fund the account now.")
            while True:
                print(f"Waiting for transaction on {btc_wallet}...")
                time.sleep(5) 
                if int(Key(Settings.Key).get_balance('btc')) == 0 :
                    break
            print("Recieved transaction")
            print(f"Your account balance is: {Key(Settings.Key).get_balance('btc')}")
    else:
        while temp:
            print("Enter private key:")
            Settings.Key = input()
            print(f"Your wallet address is: {Key(Settings.Key).address}")
            print("[1] Yes [2] No")
            if input().strip() == 1:
                temp = False
                print(f"Your account balance is: {Key(Settings.Key).get_balance('btc')}")
                
def Configuration():
    if Settings.MultiLayer():
        choice = True
        if Settings.Fake:
            while choice:
                print("How this works is you send transactions to other active wallets which hide your trail. so as a result you will trade money for security")
                print("Enter what percentage of your transactions will be sent off and non recoverable:")
                Settings.FakePercentage = input()
                print(f"Do you want {Settings.FakePercentage}% to be scattered?")
                print(f"{float(Key(Settings.Key).get_balance(Settings.Crypto)) * Settings.FakePercentage * 0.01} will be lost.")
                print("Are you sure?")
                print("[1] Yes [2] No")
                if input() == '1':
                    choice = False
        while choice:
            print("How many accounts will you use?")
            print("Enter an integer: ")
            Settings.Accounts = int(input())
            print("Are you sure?")
            print("[1] Yes [2] No")
            if input() == '1':
                    choice = False
         
            
    if Settings.CrossChain():
        




        
    
print("\033[91m This agreement is made between the Developer and the end-user (\"User\") regarding the use of the software named \"Spider.\" By using Spider, the User agrees to comply with all applicable laws and regulations. The User specifically agrees not to use Spider for any illegal activities. The Developer provides Spider \"as is\" without any warranties and disclaims all liability for damages resulting from its use. The Developer reserves the right to terminate this agreement and the User's access to Spider at any time for any reason. By using Spider and typing out \"I Agree\", the User acknowledges that they have read, understood, and agree to be bound by this agreement. \n")

print("By typing \"I Agree\" below you gain access to the software: \033[92m")
if input().lower() != "i agree":
    exit()
print("\033c", end="", flush=True)

print(r''' 
 _________      .__    .___            
/   _____/_____ |__| __| _/___________ 
\_____  \\____ \|  |/ __ |/ __ \_  __ \
/        \  |_> >  / /_/ \  ___/|  | \/
/_______  /   __/|__\____ |\___  >__|   
        \/|__|           \/    \/        
''')

if __name__ == "__main__":
    ChooseInput()
    ChangeSettings()
    SetupWallet()
    Configuration()
