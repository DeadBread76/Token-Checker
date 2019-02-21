import requests
from tkinter import *
from tkinter.filedialog import *
from colorama import init
from termcolor import colored

init()
vcounter = 0
icounter = 0
print("Select the text file containing the tokens to check...")
Tk().withdraw()
token = askopenfilename()
with open(token) as handle:
    txtf = handle.read()

f = open("tokens.txt","a")
f.write("\n" + txtf)
f.close()

print ("Checking tokens...")

with open('tokens.txt','r') as handle:
        tokens = handle.readlines()
        for x in tokens:
            token = x.rstrip()
            headers={
                'Authorization': token
                }
            src = requests.get('https://discordapp.com/api/v6/auth/login', headers=headers)
            try:
                if src.status_code == 200:
                    print (colored(token + ' Valid.',"green"))
                    vcounter +=1
                    with open('valid.txt','a') as handle:
                        handle.write(token + '\n')
                else:
                    print(colored(token + ' Invalid.',"red"))
                    icounter +=1
                    with open('invalid.txt','a') as handle:
                        handle.write(token + '\n')
            except Exception:
                print("Yeah we can't contact discordapp.com")
        print ("---------------------------------------")
        print (colored("Number of valid tokens: " + str(vcounter),"green"))
        print (colored("Number of invalid tokens: " + str(icounter),"red"))
        print ("---------------------------------------")
        input()
