import tkinter as tk
from tkinter import messagebox

class BankingAppGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Banking App")
        self.users_file = "users.txt"  # File to store user data
        self.transactions_file = "transactions.txt"  # File to store transactions

        # Set background color
        self.root.configure(bg="#f0f0f0")

        # Create main window widgets
        self.label = tk.Label(root, text="Welcome to Banking App", font=("Helvetica", 16), bg="#f0f0f0")
        self.label.pack(pady=10)

        self.balance_btn = tk.Button(root, text="Check Balance", command=self.open_balance_window, bg="#4CAF50", fg="white")
        self.balance_btn.pack(pady=5)

        self.transfer_btn = tk.Button(root, text="Transfer Funds", command=self.open_transfer_window, bg="#2196F3", fg="white")
        self.transfer_btn.pack(pady=5)

        self.transaction_history_btn = tk.Button(root, text="Transaction History", command=self.open_transaction_history_window, bg="#FF9800", fg="white")
        self.transaction_history_btn.pack(pady=5)

        self.create_user_btn = tk.Button(root, text="Create User", command=self.open_create_user_window, bg="#FF5722", fg="white")
        self.create_user_btn.pack(pady=5)

    def open_balance_window(self):
        balance_window = tk.Toplevel(self.root)
        balance_window.title("Check Balance")

        # Set background color
        balance_window.configure(bg="#f0f0f0")

        # Create widgets for balance window
        user_id_label = tk.Label(balance_window, text="User ID:", bg="#f0f0f0")
        user_id_label.grid(row=0, column=0, padx=10, pady=5)

        self.user_id_entry = tk.Entry(balance_window)
        self.user_id_entry.grid(row=0, column=1, padx=10, pady=5)

        check_balance_btn = tk.Button(balance_window, text="Check Balance", command=self.check_balance, bg="#4CAF50", fg="white")
        check_balance_btn.grid(row=1, column=0, columnspan=2, padx=10, pady=5)

    def open_transfer_window(self):
        transfer_window = tk.Toplevel(self.root)
        transfer_window.title("Transfer Funds")

        # Set background color
        transfer_window.configure(bg="#f0f0f0")

        # Create widgets for transfer window
        user_id_label = tk.Label(transfer_window, text="User ID:", bg="#f0f0f0")
        user_id_label.grid(row=0, column=0, padx=10, pady=5)

        self.user_id_entry = tk.Entry(transfer_window)
        self.user_id_entry.grid(row=0, column=1, padx=10, pady=5)

        amount_label = tk.Label(transfer_window, text="Amount:", bg="#f0f0f0")
        amount_label.grid(row=1, column=0, padx=10, pady=5)

        self.amount_entry = tk.Entry(transfer_window)
        self.amount_entry.grid(row=1, column=1, padx=10, pady=5)

        recipient_label = tk.Label(transfer_window, text="Recipient:", bg="#f0f0f0")
        recipient_label.grid(row=2, column=0, padx=10, pady=5)

        self.recipient_entry = tk.Entry(transfer_window)
        self.recipient_entry.grid(row=2, column=1, padx=10, pady=5)

        transfer_btn = tk.Button(transfer_window, text="Transfer", command=self.transfer_funds, bg="#2196F3", fg="white")
        transfer_btn.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

    def open_create_user_window(self):
        create_user_window = tk.Toplevel(self.root)
        create_user_window.title("Create User")

        # Set background color
        create_user_window.configure(bg="#f0f0f0")

        # Create widgets for create user window
        new_user_id_label = tk.Label(create_user_window, text="New User ID:", bg="#f0f0f0")
        new_user_id_label.grid(row=0, column=0, padx=10, pady=5)

        self.new_user_id_entry = tk.Entry(create_user_window)
        self.new_user_id_entry.grid(row=0, column=1, padx=10, pady=5)

        username_label = tk.Label(create_user_window, text="Username:", bg="#f0f0f0")
        username_label.grid(row=1, column=0, padx=10, pady=5)

        self.username_entry = tk.Entry(create_user_window)
        self.username_entry.grid(row=1, column=1, padx=10, pady=5)

        password_label = tk.Label(create_user_window, text="Password:", bg="#f0f0f0")
        password_label.grid(row=2, column=0, padx=10, pady=5)

        self.password_entry = tk.Entry(create_user_window)
        self.password_entry.grid(row=2, column=1, padx=10, pady=5)

        initial_balance_label = tk.Label(create_user_window, text="Initial Balance:", bg="#f0f0f0")
        initial_balance_label.grid(row=3, column=0, padx=10, pady=5)

        self.initial_balance_entry = tk.Entry(create_user_window)
        self.initial_balance_entry.grid(row=3, column=1, padx=10, pady=5)

        create_btn = tk.Button(create_user_window, text="Create User", command=self.create_user, bg="#FF5722", fg="white")
        create_btn.grid(row=4, column=0, columnspan=2, padx=10, pady=5)

    def open_transaction_history_window(self):
        transaction_history_window = tk.Toplevel(self.root)
        transaction_history_window.title("Transaction History")

        # Set background color
        transaction_history_window.configure(bg="#f0f0f0")

        # Create widgets for transaction history window
        user_id_label = tk.Label(transaction_history_window, text="User ID:", bg="#f0f0f0")
        user_id_label.grid(row=0, column=0, padx=10, pady=5)

        self.user_id_entry = tk.Entry(transaction_history_window)
        self.user_id_entry.grid(row=0, column=1, padx=10, pady=5)

        view_history_btn = tk.Button(transaction_history_window, text="View History", command=self.view_transaction_history, bg="#FFC107", fg="white")
        view_history_btn.grid(row=1, column=0, columnspan=2, padx=10, pady=5)

    def check_balance(self):
        user_id = self.user_id_entry.get()
        found = False
        with open(self.users_file, 'r') as file:
            for line in file:
                data = line.strip().split(',')
                if data[0] == user_id:
                    found = True
                    balance = float(data[3])
                    messagebox.showinfo("Account Balance", f"User ID: {user_id}\nBalance: ${balance}")
                    break
        if not found:
            messagebox.showerror("Error", "User not found")

    def transfer_funds(self):
        user_id = self.user_id_entry.get()
        amount = float(self.amount_entry.get())
        recipient_id = self.recipient_entry.get()

        # Check if sender and recipient exist
        sender_found = False
        recipient_found = False
        sender_index = -1
        recipient_index = -1
        users_data = []

        with open(self.users_file, 'r') as file:
            for line in file:
                data = line.strip().split(',')
                if data[0] == user_id:
                    sender_found = True
                    sender_index = len(users_data)
                if data[0] == recipient_id:
                    recipient_found = True
                    recipient_index = len(users_data)
                users_data.append(data)

        if not sender_found:
            messagebox.showerror("Error", "Sender not found")
            return
        if not recipient_found:
            messagebox.showerror("Error", "Recipient not found")
            return
        sender_balance = float(users_data[sender_index][3])
        recipient_balance = float(users_data[recipient_index][3])

        if sender_balance >= amount:
            sender_balance -= amount
            recipient_balance += amount
            users_data[sender_index][3] = str(sender_balance)
            users_data[recipient_index][3] = str(recipient_balance)

            with open(self.users_file, 'w') as file:
                for data in users_data:
                    file.write(','.join(data) + '\n')

            # Add transaction to transaction history
            with open(self.transactions_file, 'a') as file:
                file.write(f"{user_id},{recipient_id},{amount}\n")

            messagebox.showinfo("Transfer Funds", f"Transfer ${amount} from user ID {user_id} to {recipient_id}")
        else:
            messagebox.showerror("Error", "Insufficient funds")

    def create_user(self):
        new_user_id = self.new_user_id_entry.get()
        username = self.username_entry.get()
        password = self.password_entry.get()
        initial_balance = self.initial_balance_entry.get()

        with open(self.users_file, 'a') as file:
            file.write(f"{new_user_id},{username},{password},{initial_balance}\n")

        messagebox.showinfo("User Created", f"New user created with ID: {new_user_id}")

    def view_transaction_history(self):
        user_id = self.user_id_entry.get()
        found = False
        history = ""
        with open(self.transactions_file, 'r') as file:
            for line in file:
                sender, recipient, amount = line.strip().split(',')
                if sender == user_id or recipient == user_id:
                    found = True
                    history += f"Sender: {sender}, Recipient: {recipient}, Amount: {amount}\n"
        if found:
            messagebox.showinfo("Transaction History", f"Transaction history for user ID {user_id}:\n\n{history}")
        else:
            messagebox.showerror("Error", "User not found in transaction history")

if __name__ == "__main__":
    root = tk.Tk()
    app = BankingAppGUI(root)
    root.mainloop()