"""
Written by: Christopher Hutchings | M00571702
Last edit: 25/02/21
Module: CST4550
---
Database handler for storing Vulnerabilities. Hook up to a webservice or webscrape from vulnerability sites.
"""

import mysql.connector
from mysql.connector import Error
import time

def create_connection():
	mydb = mysql.connector.connect(
		host="localhost",
		database="PenTestingProject",
		user="root",
		password="123"
	)
	connector = mydb.cursor()
	getExploits = 'SELECT * FROM Vulnerabilities'
	connector.execute(getExploits)
	return connector.fetchall()





def init():
	#create_connection()
	print('Doop')
	time.sleep(.1)