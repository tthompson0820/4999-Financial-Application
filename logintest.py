import tkinter as tk
from tkinter import messagebox
from customtkinter import * 





class BankingAppGUI(CTk):
    def __init__(self):
        

    
        self.users = {}
        
  

        # Create main window widgets
        self.label = CTkLabel(master=root, text="Manage Your Funds", font=("Helvetica", 16), )
        
        self.label.pack(pady=10)

        
        self.balance_btn = CTkButton(master=root, text="Check Balance", command=self.open_balance_window, border_color="#90f0d4", fg_color="black")
        self.balance_btn.pack(pady=5)
        
        self.transfer_btn = CTkButton(master=root, text="Transfer Funds", command=self.open_transfer_window, border_color="#90f0d4", fg_color="black")
        self.transfer_btn.pack(pady=5)
        
        self.create_user_btn = CTkButton(master=root, text="Create User", command=self.open_create_user_window, border_color="#90f0d4", fg_color="black")
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
        
    def check_balance(self):
        user_id = self.user_id_entry.get()
        if user_id in self.users:
            balance = self.users[user_id]['balance']
            messagebox.showinfo("Account Balance", f"User ID: {user_id}\nBalance: ${balance}")
        else:
            messagebox.showerror("Error", "User not found")
        
    def transfer_funds(self):
        user_id = self.user_id_entry.get()
        amount = float(self.amount_entry.get())
        recipient_id = self.recipient_entry.get()
        if user_id in self.users:
            if self.users[user_id]['balance'] >= amount:
                if recipient_id in self.users:
                    # Update sender's balance
                    self.users[user_id]['balance'] -= amount
                    # Update recipient's balance
                    self.users[recipient_id]['balance'] += amount
                    messagebox.showinfo("Transfer Funds", f"Transfer ${amount} from user ID {user_id} to {recipient_id}")
                else:
                    messagebox.showerror("Error", "Recipient not found")
            else:
                messagebox.showerror("Error", "Insufficient funds")
        else:
            messagebox.showerror("Error", "User not found")
        
    def create_user(self):
        user_id = self.new_user_id_entry.get()
        username = self.username_entry.get()
        password = self.password_entry.get()
        balance = float(self.initial_balance_entry.get())
        self.users[user_id] = {'username': username, 'password': password, 'balance': balance}
        messagebox.showinfo("User Created", f"New user created with ID: {user_id}")

if __name__ == "__main__":
    root = tk.Tk()
    app = BankingAppGUI(root)
    root.mainloop()
                   
