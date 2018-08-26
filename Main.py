# Imports
from view.ATM_View import ATM_View
from controller.ATM_Controller import ATM_Controller
from model.ATM_Model import ATM_Model

'''
Created on 2018-08-20 (YYYY-MM-DD)

Main entry point for the ATM application

@author: Ryan Shoobert
@since: 2018-08-26 (YYYY-MM-DD)
@version: 1.0.1
'''
print("Starting ATM")

#Start GUI -- for debug
s = ATM_Controller(ATM_View(), ATM_Model())
