import  bip_utils, time
class Settings:
    MultiLayer=True
    CrossChain=True
    Fake = True
    Crypto = ""
    
def ChooseInput():
    print("Welcome to spider, choose your input cryptocurrency:")
    print("[1] BTC")
    print("Enter Choice: ")
    if input().strip() == 1:
        Settings.Crypto == "BTC"
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
    

