"""
Klasa bankomat ma mieć możliwości
1. stan konta jako pole
2. metody do: sprawdzania stanu, wpłaty gotówki oraz wypłaty
"""

class BankAccount:
    '''
    symulacja konta w banku
    '''

    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def __withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
        else:
            print('Zbyt mała ilość środków!')

    def pin(self, amount):
        pin = int(input("Podaj pin:"))
        if pin == 4455:
            self.__withdraw(amount)
        else:
            print("Zły PIN!")

    def get_balance(self):
        return self.__balance

    def __str__(self):
        return 'Wysokość salda wynosi ' + format(self.__balance, '.2f')


start_bal = float(input('podaj wysokosc salda '))
savings = BankAccount(start_bal)
pay = float(input('jaka kwote chcesz wplacic?'))
print('wplacam srodki...')
savings.deposit(pay)
cash = float(input('jaka kwote chcesz wyplacic?'))
pin = savings.pin(cash)
print(savings)