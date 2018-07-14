#Written by 《ERFAN》
#t.me/ErfanMAfshar

import os,random,time
os.system('clear')
def main():
    print("-----------------------------")
    print("|                           |")
    print("|       Bitcoin Miner       |")
    print("|                           |")
    print("|   {00} Mine Bitcoin       |")
    print("|   {99} Exit               |")
    print("|                           |")
    print("-----------------------------")
    i = input("~~> ")

    def pyRed(skk) : print("\033[91m {}\033[00m".format(skk))
    def pyGreen(skk) : print("\033[92m {}\033[00m".format(skk))
    def pycolor (skk) : print("\033[94m {}\033[00m".format(skk))

    if i == "00" :
        wallet = input("Enter Your Wallet Address: ")
        if len(wallet) == 34 :
            pyRed("Connecting to your Wallet \nPlease Wait...")
            time.sleep(7)
            pycolor("Connected to your Wallet --> " + str(wallet))
            while True :
                print("Sleep for 20sec...")
                time.sleep(20)
                hashRate = random.randint(100, 150)
                pyRed("Your HashRate is --> "+ str(hashRate) + " H/s")
                print("New Block Detected.")
                aa = random.randint(20,30)
                pyGreen("Success! you Claimed " + "0.000000" + str(aa) + " BTC")


        else :
            print("Your Wallet is not Invalid !")
            pp = input("\nPress Enter ")
            if pp == "":
                os.system('clear')
                main()
    elif i == "99" :
        print("...GoodBye...")
        exit()
    else :
        print("Please select the correct option!")
        main()
main()