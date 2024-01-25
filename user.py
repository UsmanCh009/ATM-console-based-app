import json

class User:
    @staticmethod
    def user_exists(username:str)->bool:
        try:
            with open("user.txt", "r") as f:
                data = json.load(f)
                for entry in data:
                    stored_username = entry.get("username")
                    if stored_username == username:
                        return True
        except FileNotFoundError:
            print("User file not found.")
        return False
    
    @staticmethod
    def register_user(username:str, password:str):
        user_data = {"username": username, "password": password}
        try:
            with open("user.txt", "r") as f:
                data = json.load(f)
        except FileNotFoundError:
            data = []
        data.append(user_data)
        with open("user.txt", "w") as f:
            json.dump(data, f, indent=2)
            print(f"\nusername {username}, Registered successfully")
        
        account_data = {"username": username, "balance": 0.0, "transfer_limit": 100}
        try:
            with open("accounts.txt", "r") as f:
                data = json.load(f)
        except FileNotFoundError:
            data = []
        data.append(account_data)
        with open("accounts.txt","w") as f:
            json.dump(data, f, indent=2)
            print(f"{username}, your account created successfully")
    
    @staticmethod
    def user_profile(username:str):
        with open("user.txt","r") as f:
            data = json.load(f)
            for entry in data:
                stored_username = entry.get("username")
                stored_password = entry.get("password")
                if stored_username == username:
                    print(f"username is:{stored_username}\n")
                    print(f"password is:{stored_password}\n")
        with open("accounts.txt","r") as f:
            data = json.load(f)
            for entry in data:
                stored_username = entry.get("username")
                balance = entry.get("balance")
                if stored_username == username:
                    print(f"balance is:{balance}\n")
                    
    @staticmethod
    def view_user_data():
        try:
            with open("user.txt", "r") as f:
                data = json.load(f)
                print(f"\nUsers usernames:\n")
                for entry in data:
                    stored_username = entry.get("username")
                    print(f"{stored_username},\n")
        
        except FileNotFoundError:
            print("User file not found")
            
    @staticmethod
    def change_password(username,new_password):
    
        with open("user.txt", "r") as f:
            data = json.load(f)
            for entry in data:
                stored_username = entry.get("username")
                if stored_username == username:
                    entry["password"] = new_password
                    print(f"\n{username}, your password has changed\n")
                        
        with open("user.txt", "w") as f:
            json.dump(data, f, indent= 2)
            
    @staticmethod
    def delete_user(username:str):
        
        try:
            with open("user.txt", "r") as f:
                data = json.load(f)
                updated_data = [entry for entry in data if entry.get("username") != username]
            
                with open("user.txt","w") as f:
                    json.dump(updated_data,f,indent=2)
                print("\nuser deleted successfully")
                           
        except FileNotFoundError:
            print("\nUser file not found.")  
            
    @staticmethod
    def update_username_in_all_files(old_username, new_username):
        files_to_update = [ "transfer.txt", "received.txt", "withdraw.txt", "deposit.txt"]

        for file_name in files_to_update:
            User.update_username_in_file(file_name, old_username, new_username)
            
    @staticmethod
    def update_username_in_file(file_name, old_username, new_username):
        try:
            with open(file_name, "r") as f:
                lines = f.readlines()
                data = [json.loads(line) for line in lines]
                for entry in data:
                    if entry.get("username") == old_username:
                        entry["username"] = new_username

            with open(file_name, "w") as f:
                for entry in data:
                    json.dump(entry, f)
                    f.write('\n')
        except FileNotFoundError:
            print(f"\nFile {file_name} not found.")
            
    @staticmethod
    def update_username_in_accounts(old_username, new_username):
        try:
            with open("accounts.txt", "r") as f:
                data = json.load(f)
                for entry in data:
                    if entry.get("username") == old_username:
                        entry["username"] = new_username

            with open("accounts.txt", "w") as f:
                json.dump(data, f, indent=2)
        except FileNotFoundError:
            print("\nFile accounts.txt not found.")
    
            
    @staticmethod
    def update_user(username:str):
        username_found = False
        new_username_exists = False
        from admin import Admin
        try:
            with open("user.txt", "r") as f:
                data = json.load(f)
                for entry in data:
                    stored_username = entry.get("username")
                    
                    if stored_username == username:
                        print("\nEnter the new username and password to update:\n")
                        new_username = input("\nusername:")
                        new_password = input("\npassword:")
                        
                        if Admin.admin_exists(new_username) or User.user_exists(new_username):
                            print(f"\nUser:{new_username} already exists")
                            new_username_exists = True
                            break
                        else:
                            entry["username"] = new_username
                            entry["password"] = new_password
                            username_found = True
                            print(f"User {username}, Updated successfully")
                            User.update_username_in_all_files(username, new_username)
                            User.update_username_in_accounts(username, new_username)
                            
            if not username_found and not new_username_exists:
                print(f"username {username} does not exists")
            with open("user.txt", "w") as f:
                json.dump(data, f, indent=2)
                
                        
        except FileNotFoundError:
            print("\nUser file not found.")