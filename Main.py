"""
Written by: Christopher Hutchings | M00571702
Last edit: 25/02/21
Module: CST4550
---
This Module is simply used to run the program, and stores data such as the Version number. 
Not much else happens here once the program is running.

Potentially will hold SQL data too. (?)
"""
import os
import time
import tkinter as tk
import subprocess


from Modules import VulnerabilityScanner as vs
from Modules import Menu as menu
from Modules import Database as db
#Preset OS functions
clear = lambda: os.system('clear')

#Outter-lever Config
SystemName = "MULTI-USE NETWORKING TOOLS"
Version = 1
LastEdit = '09/04/2021'
Author = "Christopher Hutchings"

clear()
db.init() # Init vulnerability database
menu.menu() # Boot program.






















