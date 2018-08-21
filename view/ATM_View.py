# Imports
import tkinter as tk

'''
Created on 2018-08-20 (YYYY-MM-DD)

Graphical user interface for the ATM application

@author: Ryan Shoobert
@since: 2018-08-20 (YYYY-MM-DD)
@version: 1.0.1
'''


class ATM_View:
    # Instance variables
    window = tk.Tk()
    
    # Constructor
    def __init__(self):
        self.window.resizable(False, False)
        self.setupGUI();
        self.window.mainloop();
        
    def setupGUI(self):
        # Window properties
        self.window.title("ATM v1.0.0")
        
        # Withdraw button
        withdrawButton = tk.Button(text="Withdraw", state="disabled")
        withdrawButton.grid(row=0, column=0, padx=10, pady=10)
        
        # Deposit button
        withdrawButton = tk.Button(text="Deposit", state="disabled")
        withdrawButton.grid(row=1, column=0, padx=10, pady=10)
        
        # Display area
        displayArea = tk.Text(width="50", height="10")
        displayArea.grid(row=0, column=1, rowspan=2, columnspan=3, pady=10)
        
        # Show balance button
        withdrawButton = tk.Button(text="Show Balance", state="disabled")
        withdrawButton.grid(row=0, column=5, padx=10, pady=10)
        
        # Change pin button
        withdrawButton = tk.Button(text="Change Pin", state="disabled")
        withdrawButton.grid(row=1, column=5, padx=10, pady=10)
        
        # Keypad buttons
        buttonLabels = ['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9'], ['Cancel', '0', 'Enter']
        
        for y in range(2, 6):
            for x in range(1, 4):
                button = tk.Button(text=buttonLabels[y-2][x-1])
                button.config(width=15, height=2)
                button.grid(row=y, column=x, pady=10)
