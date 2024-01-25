import json
from datetime import datetime, timedelta

class TransactionHistory:
    @staticmethod
    def view_transaction_history(username, file_name, transaction_type, duration="all"):
        try:
            print(f"{file_name},filename")
            with open(file_name, "r") as f:
                all_entries = [json.loads(line.strip()) for line in f]

                if duration == "all":
                    filtered_entries = [entry for entry in all_entries if entry['username'] == username]
                else:
                    current_datetime = datetime.now()

                    if duration == "last_7_days":
                        cutoff_date = current_datetime - timedelta(days=7)
                    elif duration == "last_30_days":
                        cutoff_date = current_datetime - timedelta(days=30)
                    elif duration == "last_90_days":
                        cutoff_date = current_datetime - timedelta(days=90)
                    else:
                        print("Invalid duration. Showing all transactions.")
                        return False

                    filtered_entries = [entry for entry in all_entries
                                        if entry['username'] == username and datetime.strptime(entry['datetime'], "%Y-%m-%d %H:%M:%S") >= cutoff_date]

                if filtered_entries:
                    print("\nTransactions Details:")
                    for entry in filtered_entries:
                        print(f"Date and Time: {entry['datetime']}")
                        print(f"{transaction_type.capitalize()} : {entry[f'{transaction_type}']}")
                        print(f"New Balance: {entry['new_balance']}")
                        print("----------------------------")
                else:
                    print(f"No {transaction_type} transactions found for the specified duration.")

        except FileNotFoundError:
            print(f"{file_name} file not found.")
            return False

        return True


