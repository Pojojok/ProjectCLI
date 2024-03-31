#!/usr/bin/env python3 
from random import choice,shuffle
import datetime 
from time import sleep
from os import system,path,chdir,mkdir
import subprocess
import sys


system("")

upper_letters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
lower_letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
digits = ["0","1","2","3","4","5","6","7","8","9"]
special_letters = ["!","@","#","$","%","^","&","*","(",")","_","-","+","=","{","}","[","]"]

letters = upper_letters + lower_letters + digits + special_letters
passwrd = []

pwd = "./CLI_Password_Gen"
doesExists = path.exists(pwd)
if doesExists == False:
	mkdir("./CLI_Password_Gen")
	chdir("./CLI_Password_Gen")
else:
	chdir("./CLI_Password_Gen")

print('''
		
\u001b[33m░█████╗░██╗░░░░░██╗  ██████╗░░█████╗░░██████╗░██████╗░██╗░░░░░░░██╗░█████╗░██████╗░██████╗░
██╔══██╗██║░░░░░██║  ██╔══██╗██╔══██╗██╔════╝██╔════╝░██║░░██╗░░██║██╔══██╗██╔══██╗██╔══██╗
██║░░╚═╝██║░░░░░██║  ██████╔╝███████║╚█████╗░╚█████╗░░╚██╗████╗██╔╝██║░░██║██████╔╝██║░░██║
██║░░██╗██║░░░░░██║  ██╔═══╝░██╔══██║░╚═══██╗░╚═══██╗░░████╔═████║░██║░░██║██╔══██╗██║░░██║
╚█████╔╝███████╗██║  ██║░░░░░██║░░██║██████╔╝██████╔╝░░╚██╔╝░╚██╔╝░╚█████╔╝██║░░██║██████╔╝
░╚════╝░╚══════╝╚═╝  ╚═╝░░░░░╚═╝░░╚═╝╚═════╝░╚═════╝░░░░╚═╝░░░╚═╝░░░╚════╝░╚═╝░░╚═╝╚═════╝░
░██████╗░███████╗███╗░░██╗███████╗██████╗░░█████╗░████████╗░█████╗░██████╗░
██╔════╝░██╔════╝████╗░██║██╔════╝██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗
██║░░██╗░█████╗░░██╔██╗██║█████╗░░██████╔╝███████║░░░██║░░░██║░░██║██████╔╝
██║░░╚██╗██╔══╝░░██║╚████║██╔══╝░░██╔══██╗██╔══██║░░░██║░░░██║░░██║██╔══██╗
╚██████╔╝███████╗██║░╚███║███████╗██║░░██║██║░░██║░░░██║░░░╚█████╔╝██║░░██║
░╚═════╝░╚══════╝╚═╝░░╚══╝╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝\u001b[0m
	# Made by  Roman Timoshkin 
	# Tutor Taras Valerivich 
''')
def process():
	sleep(0.7)
	print("\u001b[36mEnter password length: \u001b[0m")
	pno = str(input("\u001b[32m>\u001b[1C \u001b[0m"))
	
	if pno == "":
		pno = 16
	pno = int(pno)
	if pno <= 0:
		print("\u001b[31mPassword Cannot be 0 or less.\u001b[0m")
		process()
	shuffle(letters)
	i = 1

	while i != pno:
		passwrd.append(choice(letters))
		i = i + 1
	
	shuffle(passwrd)
	c = "".join(passwrd)
	passwrd.clear()
	sleep(0.7)
	print("\u001b[36mEnter your password use-case incase you forget it. (Optional) : \u001b[0m")
	usecase = str(input("\u001b[32m>\u001b[1C \u001b[0m"))
	sleep(0.7)
	print("The password is: " + c)
	print("The generated password is also stored in \u001b[37;1m./CLI_Password_Gen\generated_password.txt\u001b[0m file.")
	generation_time = datetime.datetime.now()
	file = open("generated_password.txt","a")
	if usecase == "":	
		file.write(c + ": " + str(generation_time.strftime("%d/%m/%Y %H:%M:%S")) + "\n")
	else:
		file.write(c + ": " + str(generation_time.strftime("%d/%m/%Y %H:%M:%S")) + "-" + usecase + "\n")	
	file.close()
    

def ask():
	sleep(0.7)
	print("\u001b[36mDo you want to continue ? (\u001b[37;1m[Y]\u001b[0mes/\u001b[37;1m[N]o\u001b[0m\u001b[36m) :\u001b[0m ")
	asks = input("\u001b[32m> \u001b[0m").lower()
	if asks == "yes" or asks == "ye" or asks == "y" or asks == "":
		while asks == "yes" or asks == "ye" or asks == "y" or asks == "":
			print("\u001b[32;1mContinuing...\u001b[0m")
			process()
			ask()
			
			break
	elif asks == "no" or asks == "n":
		print("\u001b[31;1mExiting...\u001b[0m")
		quit()
	else:
		print("\u001b[31;1mInvalid.\u001b[31mPlease try again.\u001b[0m")
		ask()
			
try:
	process()
	ask()
	
except KeyboardInterrupt:
	print(" \u001b[31;1m\nExitng...\u001b[0m")

except ValueError:
	print("\u001b[31mInvalid Values Passed.")
	print("\u001b[31;1mERROR....\u001b[0m")
	process()
	ask()
