import json
from user import User
class Admin:
    
    @staticmethod
    def is_admin(username: str) -> bool:
        try:
            with open("admin.txt", "r") as f:
                data = json.load(f)
                return any(entry.get("username") == username for entry in data)
            
        except FileNotFoundError:
            print("Admin file not found.")
            return False
            
    @staticmethod
    def register_admin(username: str, password: str):
        admin_data = {"username": username, "password": password}
        try:
            with open("admin.txt", "r") as f:
                data = json.load(f)
        except FileNotFoundError:
            data = []
        data.append(admin_data)
        with open("admin.txt", "w") as f:
            json.dump(data, f, indent=2)
            print(f"\nAdmin {username}, Registered successfully")
            
    @staticmethod
    def admin_exists(username:str) -> bool:
        try:
            with open("admin.txt", "r") as f:
                data = json.load(f)
                return any(entry.get("username") == username for entry in data)
        except FileNotFoundError:
            print("User file not found.")
        return False
    
    @staticmethod
    def update_admin(username:str):
        username_found = False
        new_username_exists = False
        try:
            with open("admin.txt", "r") as f:
                data = json.load(f)
                for entry in data:
                    stored_username = entry.get("username")
                    
                    if stored_username == username:
                        print("\nEnter the new username and password to update:\n")
                        new_username = input("\nusername:")
                        new_password = input("\npassword:")
                        if User.user_exists(new_username) or Admin.admin_exists(new_username):
                            print(f"User:{new_username} already exists")
                            new_username_exists = True
                            break
                        else:
                            entry["username"] = new_username
                            entry["password"] = new_password
                            username_found = True
                            
                            print(f"\nAdmin {username}, Updated successfully")
                        
            if not username_found and not new_username_exists:
                print(f"username {username} does not exists")
            with open("admin.txt", "w") as f:
                json.dump(data, f, indent=2)
                
                        
        except FileNotFoundError:
            print("\nAdmin file not found.")
            
    @staticmethod
    def login_admin(username:str, password:str)->bool:
        try:
            with open("admin.txt", "r") as f:
                data = json.load(f)
                if any(entry.get("username") == username and entry.get("password") == password for entry in data):
                        print(f"\nAdmin {username}, you are now logged in.\n")
                        Admin.handle_admin()
                        return True
        except FileNotFoundError:
            print("\nAdmin file not found.")

        print("\nInvalid admin username or password.")
        return False
        
    @staticmethod
    def delete_admin(username:str):
        
        try:
            with open("admin.txt", "r") as f:
                data = json.load(f)
                updated_data = [entry for entry in data if entry.get("username") != username]
            
                with open("admin.txt","w") as f:
                    json.dump(updated_data,f,indent=2)
                print("\nadmin deleted successfully")
                           
        except FileNotFoundError:
            print("\nAdmin file not found.")
            
        
    @staticmethod
    def view_admin_data():
        try:
            with open("admin.txt", "r") as f:
                data = json.load(f)
                print(f"\nAdmin usernames:\n")
                for entry in data:
                    stored_username = entry.get("username")
                    print(f"{stored_username},\n")
        
        except FileNotFoundError:
            print("Admin file not found")
            
    @staticmethod
    def set_transaction_limit(username:str):
        username_found = False
        try:
            with open("accounts.txt","r") as f:
                data = json.load(f)
                for entry in data:
                    stored_username = entry.get("username")
                    if stored_username == username:
                        username_found = True
                        print(f"\nEnter the transfer limit for user:{username}")
                        new_transfer_limit = input("\nTransfer Limit:")
                        entry["transfer_limit"] = new_transfer_limit
                        print(f"\nuser:{username} transfer limit is changed to {new_transfer_limit}")
            if not username_found:
                print(f"{username}, user not found ")
            with open("accounts.txt","w") as f:
                json.dump(data,f,indent=2)
        except FileNotFoundError:
            print("accounts.txt not found")
    @staticmethod
    def set_withdrawl_limit(username:str):
        username_found = False
        try:
            with open("accounts.txt","r") as f:
                data = json.load(f)
                for entry in data:
                    stored_username = entry.get("username")
                    if stored_username == username:
                        username_found = True
                        print(f"\nEnter the withdrawl limit for user:{username}")
                        new_withdrawl_limit = input("\nWithdrawl Limit:")
                        entry["withdrawl_limit"] = new_withdrawl_limit
                        print(f"\nuser:{username} withdrawl limit is changed to {new_withdrawl_limit}")
            if not username_found:
                print(f"{username}, user not found ")
            with open("accounts.txt","w") as f:
                json.dump(data,f,indent=2)
        except FileNotFoundError:
            print("accounts.txt not found")
    @staticmethod
    def handle_admin():
        while True:
            print("\nEnter 1 for admin settings:")
            print("\nEnter 2 for user settings:")
            print("\nEnter 3 to exit:")
            
            choice = input("\nEnter 1-3: ")
            
            match choice :
                case "1":
                    while True:
                        print("\nWelcome to Admin Settings:")
                        print("\nEnter 1 to view all admins:")
                        print("\nEnter 2 to delete admin:")
                        print("\nEnter 3 to register admin:")
                        print("\nEnter 4 to update admin:")
                        print("\nEnter 5 to exit admin settings:")
                        
                        admin_choice = input("\nEnter 1-5: ")
                        match admin_choice :
                            case '1':
                                Admin.view_admin_data()
                                
                            case '2':
                                
                                print("\nEnter the username of admin to delete ")
                                user = input("\nusername: ")
                                if not Admin.admin_exists(user) or User.user_exists(user):
                                    print(f"\n Admin,{user} does not exists")
                                else:
                                    Admin.delete_admin(user)
                                
                            case '3':
                                print("\nEnter the username and password of admin to register:")
                                user = input("\nusername: ")
                                password = input("\npassword: ")
                                if Admin.admin_exists(user):
                                    print("\n Admin already exists")
                                else:
                                    Admin.register_admin(user, password)
                                
                            case '4':
                                admin_name = input("\nEnter the username of admin to update:")
                                Admin.update_admin(admin_name)
                            
                            case '5':
                                break
                            
                            case _: print("Invalid choice. please enter 1-5:")
                
                case '2':
                    while True:
                        print("\nWelcome to user Settings:")
                        print("\nEnter 1 to view all users:")
                        print("\nEnter 2 to delete user:")
                        print("\nEnter 3 to register user:")
                        print("\nEnter 4 to update user:")
                        print("\nEnter 5 to search user :")
                        print("\nEnter 6 to change transfer limit of user :")
                        print("\nEnter 7 to change withdrawl  limit of user :")
                        print("\nEnter 8 to exit user settings:")
                        
                        user_choice = input("\nEnter 1-8: ")
                        match user_choice :
                            case '1':
                                User.view_user_data()
                            case '2':
                                print("\nEnter the username of user to delete ")
                                user = input("\nusername: ")
                                if not User.user_exists(user):
                                    print(f"\n User,{user} does not exists")
                                else:
                                    User.delete_user(user)
                            case '3':
                                print("\nEnter the username and password of user to register:")
                                user = input("\nusername: ")
                                password = input("\npassword: ")
                                if User.user_exists(user):
                                    print("\n user already exists")
                                else:
                                    User.register_user(user, password)
                            case '4':
                                print("\nEnter the username of user to update:")
                                user_name = input("\nusername:")
                                User.update_user(user_name)
                            case '5':
                                print("\nEnter the username of user to search ")
                                user = input("\nusername: ")
                                if User.user_exists(user):
                                    User.user_profile(user)
                                else:
                                    print(f"\n User,{user} does not  exists")
                            case '6':
                                print("\nEnter the username of user to change transfer limit:")
                                user_name = input("\nusername:")
                                Admin.set_transaction_limit(user_name)
                            case '7':
                                print("\nEnter the username of user to change withdrawl limit:")
                                user_name = input("\nusername:")
                                Admin.set_withdrawl_limit(user_name)
                            case '8':
                                break
                            case _:
                                print("Invalid choice. please enter 1-8:")
                    
                    
                case '3':
                    break
                case _: print("Invalid choice. please enter 1-3:")