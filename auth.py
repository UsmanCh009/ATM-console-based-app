from bank_accounts import BankAccounts
from admin import Admin
from user import User
from transaction_details import TransactionHistory
import json
class AuthManager(Admin):
    def __init__(self):
        self.logged_in_user = None

    def handle_user(self):
        while True:
            print("\nEnter 1 to login:")
            print("\nEnter 2 to register:")
            print("\nEnter 3 to exit:")

            choice = input("\nEnter 1, 2, or 3:\n")
            match choice:

                case '1':
                    username = input("\nEnter your username:")
                    password = input("\nEnter your password:")

                    if self.login_user(username, password):
                        print("\nYou are now logged in")
                        self.handle_account()
                        break
                    elif Admin.is_admin(username):
                            Admin.login_admin(username,password)
                            
                            
                    else:
                        print("\nInvalid username or password")

                case '2':
                    new_username = input("\nEnter your new username:")
                    new_password = input("\nEnter your new password:")

                    if User.user_exists(new_username) or Admin.admin_exists(new_username):
                        print(f"\n {new_username} username already exists")
                    else:
                        User.register_user(new_username, new_password)
                        self.logged_in_user = new_username

                case '3':
                    break

                case _:
                    print("Invalid choice, Please enter 1, 2, or 3")

    def handle_account(self):
        while True:
            print("\nEnter 1 to deposit amount:")
            print("\nEnter 2 to check balance:")
            print("\nEnter 3 to withdraw amount:")
            print("\nEnter 4 to transfer amount:")
            print("\nEnter 5 to view profile:")
            print("\nEnter 6 to change password:")
            print("\nEnter 7 to view transaction history:")
            
            
            print("\nEnter 8 to exit accounts menu:")
            choice = input("\nEnter 1-8:")
            match choice:

                case '1':
                    try:
                        amount = float(input("\nPlease enter the amount to deposit:"))
                        BankAccounts.deposit(self.logged_in_user, amount)
                    except ValueError:
                        print("Invalid input. Please enter a valid number")
                    
                case '2':
                    
                        balance = BankAccounts.get_balance(self.logged_in_user)
                        print(f"\nyour balance is {balance}")
                    
                case '3':
                    try:
                        amount = float(input("\nPlease enter the amount to withdraw:"))
                        BankAccounts.withdraw(self.logged_in_user, amount)
                        
                    except ValueError:
                        print("Invalid input. Please enter a valid number")
                case '4':
                    try:
                        amount = float(input("\nPlease enter the amount to transfer:"))
                        recepient = input("\nPlease enter the username of recepient:").lower()
                        BankAccounts.transfer(self.logged_in_user, amount, recepient)
                        
                    except ValueError:
                        print("Invalid input. Please enter a valid number or user that exists")
                case '5':
                    User.user_profile(self.logged_in_user)
                    
                case '6':
                    password = input("\nPlease enter your new password:")
                    User.change_password(self.logged_in_user, password)
                    
                
                case '7':
                    self.handle_account_transactions()

                case '8':
                    break
                case _:
                    print("\nInvalid choice, please enter 1-8")
    def handle_account_transactions(self):
        while True:
            print("\nEnter 1 to view deposit  history:")
            print("\nEnter 2 to view withdrawn history:")
            print("\nEnter 3 to view received history:")
            print("\nEnter 4 to view transfer history:")
            print("\nEnter 5 to exit :")
            
            transaction_choice = input("\nEnter1-5: ")
            match transaction_choice:
                case '1':
                    self.view_transaction_history("deposited_amount","deposit.txt")
                case '2':
                    self.view_transaction_history("withdrawn_amount","withdraw.txt")
                case '3':
                    self.view_transaction_history("received_amount","received.txt")
                case '4':
                    self.view_transaction_history("transferred_amount","transfer.txt")
                case '5':
                    break
                case _: 
                    print("\nInvalid choice, please enter 1-5")
                    
    def view_transaction_history(self, transaction_type, file_name):
        
        print("\nEnter 1 to view all transactions")
        print("\nEnter 2 to view last 7 days transactions")
        print("\nEnter 3 to last 30 days transactions")
        print("\nEnter 4 to view last 90 days transactions")
        duration_choice = input("\nEnter 1-4: ")
        if duration_choice in ['1', '2', '3', '4']:
            durations = {
                '1': 'all',
                '2': 'last_7_days',
                '3': 'last_30_days',
                '4': 'last_90_days'
            }
            TransactionHistory.view_transaction_history(self.logged_in_user,file_name, transaction_type,  durations[duration_choice])
        else:
            print("\nInvalid choice. Showing all transactions.")
            TransactionHistory.view_transaction_history(self.logged_in_user,file_name, transaction_type)
    
    
    def login_user(self, username, password):
        with open("user.txt", "r") as f:
            data = json.load(f)
            for entry in data:
                stored_username = entry.get("username")
                stored_password = entry.get("password")
                if stored_username == username and stored_password == password:

                    self.logged_in_user = username
                    return True

        return False
        
if __name__ == "__main__":
    auth_manager = AuthManager()
    auth_manager.handle_user()
