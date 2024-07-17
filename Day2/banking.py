"""
PROBLEM STATEMENT

Scenario:

You are tasked with develpoing basic banking application that handles various operations like depositing money,
withdrawing money and check account balcance, THe application should also handle different types of exceptions 
gracefully such as when a user tries to withdraw more money than available, attempts to deposit a negative amount, 
or enters invalid data types for transaction.

Requirements:

Implement functions for deposit, withdrawal, and balance checking
Handle exceptions for the following cases:

withdrawal amount greater than the balance.
Deposit amount is negative.
Invalid datatype entered for transaction 
Ensure that the application continues running even after throwing an exception....


"""
"""
___.                  __   .__                                      .__  .__               __  .__               
\_ |__ _____    ____ |  | _|__| ____    ____   _____  ______ ______ |  | |__| ____ _____ _/  |_|__| ____   ____  
 | __ \\__  \  /    \|  |/ /  |/    \  / ___\  \__  \ \____ \\____ \|  | |  |/ ___\\__  \\   __\  |/  _ \ /    \ 
 | \_\ \/ __ \|   |  \    <|  |   |  \/ /_/  >  / __ \|  |_> >  |_> >  |_|  \  \___ / __ \|  | |  (  <_> )   |  \
 |___  (____  /___|  /__|_ \__|___|  /\___  /  (____  /   __/|   __/|____/__|\___  >____  /__| |__|\____/|___|  /
     \/     \/     \/     \/       \//_____/        \/|__|   |__|                \/     \/                    \/ 
"""

print("Welcome to the banking application!")
print("You have an account created for you. The current balance is Rs 0")
balance = 0
def deposit(amount):
    global balance
    if amount <=0:
        print("You cannot deposit negative amount or zero amount")
        return     

    balance += amount
def withdraw(amount):
    global balance
    if balance == 0:
        raise ValueError("You have zero balance in your account please deposit to withdraw")
    try:
        if balance - amount < 0:
            raise ValueError(f"You cannot withdraw Rs {amount} as you have less balance than the amount")
    except ValueError as e:
        print(f"You cannot withdraw {amount} as you have less balance")
    

        
def check_balance():
    global balance
    print(f"The current balance is Rs {balance}")


while(True):
    user_option = int(input("Please input the transaction you want to execute:\nPress 1 for Deposit\nPress 2 for Withdrawal\nPress 3 for Checking the bank balance\nPress 4 to exit the application: "))

    if user_option == 1:
        amount_entered_by_user = int(input("Please input the amount to deposit: "))
        deposit(amount_entered_by_user)
    elif user_option == 2:
        amount_entered_by_user = int(input("Please enter the amount to withdraw: "))
        withdraw(amount_entered_by_user)
    elif user_option == 3:
        check_balance()
    elif user_option == 4:
        break


    