'''
Created on 2018-08-20 (YYYY-MM-DD)

Controller for the ATM application. Where user input is processed.

@author: Ryan Shoobert
@since: 2018-08-26 (YYYY-MM-DD)
@version: 1.0.2
'''

class ATM_Controller:

    #Constructor
    def __init__(self, view, model):
        self.view = view
        self.model = model
        '''
        NOT YET FULLY IMPLEMENTED
        '''
        
        
    '''
    When a deposit is made, the balance will be updated in the model.
    @param self: The instance of ATM_Controller 
    @param amount: The amount of money to be deposited into the account 
    '''
    def doDeposit(self, amount):
        raise NotImplementedError
    
    '''
    When a withdrawal is requested, the balance will be decreased by the amount provided.
    @param self: The instance of ATM_Controller 
    @param amount: The amount of money to be deposited into the account 
    '''
    def doWithdraw(self, amount):
        raise NotImplementedError
    
    '''
    Changes the users pin. First verifies their current one is correct and then initiates 
    the process of setting the new one.
    @param self: The instance of ATM_Controller
    @param currPin: The users current pin
    @param newPin: The users new pin  
    '''
    def doChangePin(self, currPin, newPin):
        raise NotImplementedError
    
    '''
    When the user requests their balance, the balance will be fetched and displayed on screen.
    @param self: The instance of ATM_Controller
    '''
    def doShowBalance(self):
        raise NotImplementedError