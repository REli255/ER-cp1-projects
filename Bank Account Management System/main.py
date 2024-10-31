#------------------------------------------------------------------------------------------------------------------
#Name:          Bank Account Management System
#Purpus:        allow user to manage their bank account
#
#Author:        MsLaRose
#
#Created:       10/1/2024
#Licence:        none
#------------------------------------------------------------------------------------------------------------------

class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        return False
    #this checks if the amount is greater than 0 then if so it adds that amount to your balance
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return True
        return False
    #this this checks if the amount is greater than 0 and less than your balance then if so it subtracts that amount from your balance
    def get_balance(self):
        return self.balance
    #this returns the amount in our ballance

def create_account():
    account_number = input("Enter account number: ")
    initial_balance = float(input("Enter initial balance: "))
    return BankAccount(account_number, initial_balance)
#this allows you to make a new account by entering the account number and initial balance you want for the new account

def main():
    accounts = {}
    while True:
        print("\n1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
    #this allows you to chose what you want to use the manager for
        if choice == '1':
            account = create_account()
            accounts[account.account_number] = account
            print(f"Account {account.account_number} created successfully!")
        #this makes it so if you chose 1 you can make a new account
        elif choice in ['2', '3', '4']:
            account_number = input("Enter account number: ") 
            if account_number in accounts:
                account = accounts[account_number] #this makes you enter a valid account number
                if choice == '2':
                    amount = float(input("Enter deposit amount: "))
                    if account.deposit(amount):
                        print(f"Deposited ${amount:.2f} successfully!")
                    else:
                        print("Invalid deposit amount.") #this lets you chose how much you want deposit and if that amount is valid
                elif choice == '3':
                    amount = float(input("Enter withdrawal amount: "))
                    if account.withdraw(amount):
                        print(f"Withdrawn ${amount:.2f} successfully!")
                    else:
                        print("Invalid withdrawal amount or insufficient funds.") #this lets you chose how much you want withdraw, if that amount is valid and if you hav enough funds
                else:
                    print(f"Current balance: ${account.get_balance():.2f}") #this tells you what your current ballance is
            else:
                print("Account not found.") # this tells you if you entered an invalid account number
        
        elif choice == '5':
            print("Thank you for using our banking system. Goodbye!")
            break
        # this ends the loop
        else:
            print("Invalid choice. Please try again.")
        # this tells you if you made an invalid choice
if __name__ == "__main__":
    main()