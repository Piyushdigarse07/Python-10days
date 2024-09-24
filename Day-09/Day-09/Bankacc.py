class MinimumBalanceError(Exception):
    def __repr__(self):
        return "Withdrawal beyond minimum balance"

class ZeroAmountError(Exception):
    def __repr__(self):
        return "Amount cannot be zero or less than zero"

class BankAccount:
    def __init__(self, name, number, curbalance, minbalance):
        self.name = name
        self.number = number
        self.curbalance = curbalance
        self.minbalance = minbalance

    def withdraw(self, amount):
        if amount <= 0:
            raise ZeroAmountError()
        if self.curbalance - amount < self.minbalance:
            raise MinimumBalanceError()
        self.curbalance -= amount

    def deposit(self, amount):
        if amount <= 0:
            raise ZeroAmountError()
        self.curbalance += amount

    def getCurrentBalance(self):
        return self.curbalance

try:
    bob_account = BankAccount(name="bob", number=12345, curbalance=1000, minbalance=500)
    pat_account = BankAccount(name="pat", number=23415, curbalance=1500, minbalance=800)

    print(f"Bob's initial balance: {bob_account.getCurrentBalance()}")
    bob_account.deposit(500)
    print(f"Bob's balance after deposit: {bob_account.getCurrentBalance()}")
    bob_account.withdraw(700)
    print(f"Bob's balance after withdrawal: {bob_account.getCurrentBalance()}")

    print(f"Pat's initial balance: {pat_account.getCurrentBalance()}")
    pat_account.deposit(300)
    print(f"Pat's balance after deposit: {pat_account.getCurrentBalance()}")
    pat_account.withdraw(1000)
    print(f"Pat's balance after withdrawal: {pat_account.getCurrentBalance()}")

except MinimumBalanceError as e:
    print(e)
except ZeroAmountError as e:
    print(e)
