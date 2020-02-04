from threading import Lock

class BankAccount:
    def __init__(self):
        self.balance = 0
        self.account = "Closed"
        self.lock = Lock()

    def get_balance(self):
        if self.account == "Open":
            return self.balance
        raise ValueError("Account Closed")

    def open(self):
        if self.account == "Open":
            raise ValueError("Account already open")
        self.account = "Open"
        self.balance = 0

    def deposit(self, amount):
        if self.account == "Closed":
            raise ValueError("Account Closed")
        if amount < 0:
            raise ValueError("Cannot deposit negative")
        self.lock.acquire()
        self.balance += amount
        self.lock.release()

    def withdraw(self, amount):
        if self.account == "Closed":
            raise ValueError("Account Closed")
        if amount > self.balance or amount < 0:
            raise ValueError("Insufficient Funds")
        self.lock.acquire()
        self.balance -= amount
        self.lock.release()

    def close(self):
        if self.account != "Open":
            raise ValueError("Account Closed")
        self.account = "Closed"
        self.balance = 0
