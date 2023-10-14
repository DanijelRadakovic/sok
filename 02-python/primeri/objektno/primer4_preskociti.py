import random
from abc import ABC, abstractmethod


class Account(object):
    num_accounts = 0

    def __init__(self, name, balance):
        print("Account init", end=" ")
        self.name = name
        self.balance = balance
        Account.num_accounts += 1  # Pristup deljenom class atributu

    def __del__(self):
        Account.num_accounts -= 1

    def deposit(self, amt):
        print("deposit Account", end=" ")
        self.balance = self.balance + amt

    def withdraw(self, amt):
        print("withdraw Account", end=" ")
        self.balance = self.balance - amt

    def inquiry(self):
        return self.balance


# nasledjivanje
class EvilAccount(Account):

    def __init__(self, name, balance, evilfactor):
        print("EvilAccount init", end=" ")
        # poziv konstruktora iz roditeljske klase
        # Account.__init__(self,name,balance)
        # super(EvilAccount, self).__init__(name,balance)
        super().__init__(name, balance)
        self.evilfactor = evilfactor

    # redefinisanje metode
    def inquiry(self):
        if random.randint(0, 4) == 1:
            return self.balance * self.evilfactor
        else:
            return self.balance


class DepositCharge(Account):
    fee = 5.00

    def __init__(self, name, balance):
        print("DepositCharge init", end=" ")
        super().__init__(name, balance)

    def deposit_fee(self):
        print("deposit_fee DepositCharge", end=" ")
        super().withdraw(self.fee)


class WithdrawCharge(Account, ABC):
    fee = 2.50

    def __init__(self, name, balance):
        print("WithdrawCharge init", end=" ")
        super().__init__(name, balance)

    @abstractmethod
    def withdraw_fee(self):
        print("withdraw_fee WithdrawCharge", end=" ")
        super().withdraw(self.fee)


# Visestruko nasledjivanje
class MostEvilAccount(EvilAccount,
                      DepositCharge,
                      WithdrawCharge):

    def __init__(self, name, balance, evilfactor):
        print("MostEvilAccount init", end=" ")
        super().__init__(name, balance, evilfactor)

    def deposit(self, amt):
        print("deposit MostEvilAccount", end=" ")
        self.deposit_fee()
        super(MostEvilAccount, self).deposit(amt)

    def withdraw_fee(self):
        pass

    def withdraw(self, amt):
        print("withdraw MostEvilAccount", end=" ")
        self.withdraw_fee()
        super(MostEvilAccount, self).withdraw(amt)


if __name__ == '__main__':
    d = MostEvilAccount("Dave", 500.00, 1.10)
    print()
    d.deposit_fee()
    print("Balance:{}".format(d.balance))
    print()
    d.withdraw_fee()
    print("Balance:{}".format(d.balance))

    print()
    print("Method resolution order")
    print(MostEvilAccount.__mro__)
    print(DepositCharge.__mro__)

    tmp = DepositCharge("asd", 100)