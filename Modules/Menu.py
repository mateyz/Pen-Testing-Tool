"""
Written by: Christopher Hutchings | M00571702
Last edit: 25/02/21
Module: CST4550
---
Menu for selecting which tools to execute.
"""

#Dictionary Imports
from pprint import pprint
from colorama import Fore, Back, Style
from pyfiglet import Figlet

#Self_Module Imports
from Modules import VulnerabilityScanner as vs
from Modules import Database as db

#Module Imports
import inquirer
import shutil
import os
import socket
import keyboard
import threading
import time
import ipaddress

#Preset OS functions
clear = lambda: os.system('clear')

#Variables
IP = 0
SubIP = 0

# Initiate Main Menu
def menu():
	clear()
	###########################
	
	# Fancy looking menu screen
	###########################
	print('\033[1m')
	print(Fore.RED + '                              MULTI-USE NETWORKING TOOLS V0.9')
	print(Fore.GREEN + '                                 BY CHRISTOPHER HUTCHINGS')
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.connect(("8.8.8.8", 80))
	print(Fore.GREEN + '				     ' +  socket.getfqdn() + ' | ' + s.getsockname()[0])# socket.gethostbyname(socket.gethostname()))#
	print(Fore.YELLOW + '\n \nWelcome back, ' + os.getlogin() + ".")
	print(Fore.YELLOW + 'Please select a Tool')
	IP = format(ipaddress.ip_network(s.getsockname()[0]))
	SubIP = ipaddress.ip_network(s.getsockname()[0] +'/24', strict=False)
	s.close()
	###########################
	
	# Menu Selection
	###########################
	menuPrompt = [
    	inquirer.List(
       		"ToolSelection",
        	message="Selected Tool",
        	choices=["Vulnerability scanner", "EXIT"],
			carousel=True,
		),
	]
	option = inquirer.prompt(menuPrompt)


	###########################
	if option["ToolSelection"] == "Vulnerability scanner":
		#network_discovery()
		vs.main(IP, SubIP)
	elif option["ToolSelection"] == "EXIT":
		clear() #Clear CMD & Exit the program.
