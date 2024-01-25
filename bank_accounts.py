import json
from datetime import datetime
class BankAccounts:
    @staticmethod
    def account_exists(username):
        try:
            with open("accounts.txt", "r") as f:
                data =json.load(f)
                return any(entry.get("username") == username for entry in data)
        except FileNotFoundError:
            print("Accounts file not found.")
        return False
    @staticmethod
    def create_account(username):
        try:
            with open("accounts.txt", "a") as f:
                data = json.load(f)
        except FileNotFoundError:
            data = []
        data.append({"username":username,"balance":0.0})
        with open("accounts.txt", "w") as f:
            json.dump(data, f, indent= 2)

    @staticmethod
    def get_balance(username):
        try:
            
            with open("accounts.txt", "r") as f:
                data = json.load(f)
               
                for entry in data:
                    stored_username = entry.get("username")
                    stored_balance = entry.get("balance")
                    
                    if stored_username == username:
                        return float(stored_balance)
                             
            raise ValueError("Username not found in accounts.txt")
        except ValueError as e:
            print(f"Error: {e}")
    
    @staticmethod
    def deposit(username, amount):
        try:
            current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            with open("accounts.txt", "r") as f:
                data = json.load(f)
            for entry in data:
                stored_username = entry.get("username")
                if stored_username == username:
                    current_balance = entry.get("balance",0.0)
                    entry["balance"] = current_balance + amount
                    
                        
                    with open("deposit.txt", "a") as transaction_file:
                        transaction_data = {
                            "username": username,
                            "datetime": current_datetime,
                            "deposited_amount": amount,
                            "new_balance": entry["balance"]
                        }
                        json.dump(transaction_data, transaction_file)
                        transaction_file.write("\n")
                    print(f"{username}, you have deposited amount:{amount} successfully\n")
                    print(f"{username}, your remaining balance is: {entry["balance"]}\n")

            with open("accounts.txt", "w") as f:
                json.dump(data,f, indent=2)
          
        except FileNotFoundError:
            print("Accounts file not found.")
    @staticmethod
    def withdraw(username:str, amount):
        try:
            current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            with open("accounts.txt", "r") as f:
                data = json.load(f)
                for entry in data:
                    stored_username = entry.get("username")
                    withdraw_limit = entry.get("withdrawl_limit")
                    if stored_username == username:
                        current_balance = entry.get("balance",0.0)
                        if amount <= float(current_balance):
                            if amount <= float(withdraw_limit):
                                entry["balance"] = float(current_balance) - amount
                                
                            
                                with open("withdraw.txt", "a") as withdraw_file:
                                    withdraw_data = {
                                        "username": username,
                                        "datetime": current_datetime,
                                        "withdrawn_amount": amount,
                                        "new_balance": entry["balance"] 
                                    }
                                    json.dump(withdraw_data, withdraw_file)
                                    withdraw_file.write("\n")
                                    print(f"{entry["balance"]},new Balance")
                                print(f"{username}, you have withdrawn amount:{amount} successfully\n")
                                print(f"{username}, your remaining balance is: {entry["balance"]}\n")
                            else:
                                print(f"your amount:{amount} exceeds the withdraw limit of {withdraw_limit}")
                            
                        else:
                            print(f"your withdraw amount {amount} exceeds your current balance {current_balance}")
                            
                    

            with open("accounts.txt", "w") as f:
                json.dump(data,f, indent=2)
            
        except FileNotFoundError:
            print("Accounts file not found.")
       
    @staticmethod
    def transfer(username:str, amount, recipient:str):
        try:
            current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            with open("accounts.txt", "r") as accounts_file:
                data = json.load(accounts_file)

            recipient_exists = False
            limit_exceeds = False
            amount_exceeds = False

            for account in data:
                stored_username = account.get("username")
                balance = account.get("balance")
                transfer_limit = account.get("transfer_limit")

                if stored_username == username:
                    if float(amount) <= float(balance) :
                        if float(amount) <= float(transfer_limit):
                            for recipient_account in data:
                                recipient_username = recipient_account.get("username")

                                if recipient_username == recipient:
                                    recipient_exists = True
                                    recipient_new_balance = float(recipient_account["balance"]) + float(amount)
                                    account["balance"] = float(balance) - float(amount)
                                    recipient_account["balance"] = recipient_new_balance

                                    with open("received.txt", "a") as received_file:
                                        received_file.write(json.dumps({
                                            "username": recipient_username,
                                            "datetime": current_datetime,
                                            "deposited_amount": amount,
                                            "new_balance": recipient_new_balance
                                        }) + "\n")

                                    with open("transfer.txt", "a") as transfer_file:
                                        transfer_file.write(json.dumps({
                                            "username": username,
                                            "datetime": current_datetime,
                                            "transferred_amount": amount,
                                            "new_balance": account["balance"]
                                        }) + "\n")
                                    print(f"{username}, you have transfer amount:{amount} successfully\n")
                                    print(f"{username}, your remaining balance is: {account["balance"]}\n")

                                    break
                            else:
                                break
                                
                        else: 
                            print(f"Your amount: {amount} to transfer exceeds your transaction limit of: {transfer_limit}")
                            limit_exceeds = True
                            break
                            
                    else:
                        print(f"Your amount: {amount} to transfer exceeds your balance: {balance}")
                        amount_exceeds = True
                        break
                else:
                    continue

            if not recipient_exists and not limit_exceeds and not amount_exceeds:
                print(f"Recipient: {recipient} account does not exist")

            with open("accounts.txt", "w") as accounts_file:
                json.dump(data, accounts_file, indent=2)
            

        except FileNotFoundError:
            print("Account file not found")
   

            