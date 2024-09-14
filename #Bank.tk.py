import tkinter as tk
from tkinter import messagebox
import random
import datetime

class BankAccount:
    def __init__(self, name, pin):
        self.name = name
        self.pin = pin
        self.account_number = self.generate_account_number()
        self.balance = 0
        self.transaction_history = []

    def generate_account_number(self):
        return random.randint(10000000, 99999999)  # Generate an 8-digit account number

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            transaction_id = self.generate_transaction_id()
            self.transaction_history.append((transaction_id, datetime.datetime.now(), 'Deposit', amount))
            return f'{amount} deposited successfully. Transaction ID: {transaction_id}'
        else:
            return 'Deposit amount must be greater than zero.'

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            transaction_id = self.generate_transaction_id()
            self.transaction_history.append((transaction_id, datetime.datetime.now(), 'Withdrawal', amount))
            return f'{amount} withdrawn successfully. Transaction ID: {transaction_id}'
        else:
            return 'Insufficient funds.'

    def get_balance(self):
        return f'Your balance is {self.balance}.'

    def print_transaction_history(self):
        history_str = 'Transaction History:\n'
        for transaction_id, date, action, amount in self.transaction_history:
            history_str += f'Transaction ID: {transaction_id} - {date} - {action}: {amount}\n'
        return history_str

    def generate_transaction_id(self):
        return random.randint(100000, 999999)  # Generate a 6-digit transaction ID

# Tkinter GUI
class BankApp:
    def __init__(self, root):
        self.root = root
        self.root.title('Banking Application')

        self.account_name = tk.StringVar()
        self.account_pin = tk.StringVar()
        self.amount = tk.DoubleVar()

        self.account = None

        self.create_widgets()

    def create_widgets(self):
        # Labels and Entry fields
        tk.Label(self.root, text="Name:").grid(row=0, column=0, padx=10, pady=10)
        tk.Entry(self.root, textvariable=self.account_name).grid(row=0, column=1, padx=10, pady=10)

        tk.Label(self.root, text="PIN (4 digits):").grid(row=1, column=0, padx=10, pady=10)
        tk.Entry(self.root, textvariable=self.account_pin, show='*').grid(row=1, column=1, padx=10, pady=10)

        tk.Label(self.root, text="Amount:").grid(row=2, column=0, padx=10, pady=10)
        tk.Entry(self.root, textvariable=self.amount).grid(row=2, column=1, padx=10, pady=10)

        # Buttons
        tk.Button(self.root, text="Create Account", command=self.create_account).grid(row=3, column=0, padx=10, pady=10)
        tk.Button(self.root, text="Deposit", command=self.deposit).grid(row=3, column=1, padx=10, pady=10)
        tk.Button(self.root, text="Withdraw", command=self.withdraw).grid(row=4, column=0, padx=10, pady=10)
        tk.Button(self.root, text="Check Balance", command=self.check_balance).grid(row=4, column=1, padx=10, pady=10)
        tk.Button(self.root, text="Transaction History", command=self.show_history).grid(row=5, column=0, columnspan=2, padx=10, pady=10)
        tk.Button(self.root, text="Exit", command=self.root.quit).grid(row=6, column=0, columnspan=2, padx=10, pady=10)

    def create_account(self):
        name = self.account_name.get()
        pin = self.account_pin.get()

        if not name or not pin or len(pin) != 4 or not pin.isdigit():
            messagebox.showerror("Error", "Invalid name or PIN. PIN must be a 4-digit number.")
            return

        self.account = BankAccount(name, pin)
        messagebox.showinfo("Account Created", f'Account created successfully!\nAccount Number: {self.account.account_number}')

    def deposit(self):
        if not self.account:
            messagebox.showerror("Error", "No account created.")
            return

        amount = self.amount.get()
        result = self.account.deposit(amount)
        messagebox.showinfo("Deposit", result)

    def withdraw(self):
        if not self.account:
            messagebox.showerror("Error", "No account created.")
            return

        amount = self.amount.get()
        result = self.account.withdraw(amount)
        messagebox.showinfo("Withdrawal", result)

    def check_balance(self):
        if not self.account:
            messagebox.showerror("Error", "No account created.")
            return

        balance = self.account.get_balance()
        messagebox.showinfo("Balance", balance)

    def show_history(self):
        if not self.account:
            messagebox.showerror("Error", "No account created.")
            return

        history = self.account.print_transaction_history()
        messagebox.showinfo("Transaction History", history)


if __name__ == "__main__":
    root = tk.Tk()
    app = BankApp(root)
    root.mainloop()
