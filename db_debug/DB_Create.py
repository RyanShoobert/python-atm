import sqlite3 as db
from _sqlite3 import OperationalError
'''
Created on 2018-08-26 (YYYY-MM-DD)

Class creating a template sqlite database for the ATM's backend.

@author: Ryan Shoobert
@since: 2018-08-28 (YYYY-MM-DD)
@version: 1.1.0
'''
print("Creating ATM database")

# Connect to the database
dbConnection = db.connect("../atm_database")
cursor = dbConnection.cursor()

# Create table for holding customer data
try:
    cursor.execute('''CREATE TABLE IF NOT EXISTS customer
                    (customerID INTEGER PRIMARY KEY, customerFirstName TEXT, customerLastName TEXT)
    ''')
    print("Created customer table")
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS account
                    (accountNumber INTEGER PRIMARY KEY, balance REAL)
    ''')
    print("Created account table")
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS customerAccount
                    (accountNumber INTEGER, customerID INTEGER)
    ''')
    print("Created customer/account resolution table")
    
    dbConnection.commit()
    
except OperationalError as oe:
    # Not needed to actually safeguard the SQL but good for debug output
    print("Database already exists")
    
# Insert data into tables
cursor.execute(''' INSERT INTO customer(customerFirstName, customerLastName)
                   VALUES("John", "Doe")''')
cursor.execute(''' INSERT INTO customer(customerFirstName, customerLastName)
                   VALUES(?, ?) ''', ("Julie", "Jones"))
dbConnection.commit()
print("Customer table populated")

cursor.execute(''' INSERT INTO account(balance)
                   VALUES(200.50)''')
cursor.execute(''' INSERT INTO account(balance)
                   VALUES(70000)''')
dbConnection.commit()
print("Account table populated")

cursor.execute(''' INSERT INTO customerAccount(accountNumber, customerID)
                   VALUES(1, 1)''')
cursor.execute(''' INSERT INTO customerAccount(accountNumber, customerID)
                   VALUES(2, 1)''')
dbConnection.commit()
print("Customer/account table populated")

# Finish by closing the connection
dbConnection.close()
print("Finished!")
