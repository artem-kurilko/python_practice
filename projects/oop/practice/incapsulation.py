class BankAccount:
    __balance = 0

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            raise ValueError('Insufficient funds')

    def get_balance(self):
        return self.__balance


account = BankAccount()
account.deposit(1000)
account.withdraw(500)
print(account.get_balance())  # 500
