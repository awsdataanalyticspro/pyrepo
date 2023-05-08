class Customer:
    '''This python project demonstrates bank operations.'''
    bank_name = 'SwissBanK'

    def __init__(self, name, balance=0.0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount
        print('Total balance after amount deposited is:', self.balance)

    def withdraw(self, amount):
        if amount > self.balance:
            print('Insufficient funds.Amount can''t be withdrawn.')
        else:
            self.balance = self.balance - amount
            print('Total balance after amount withdrawal is:', self.balance)


print('Welcome to ', Customer.bank_name)
name = input('Enter your name: ')
c = Customer(name)
while True:
    print()
    print('d-Deposit\nw-Withdraw\ne-Exit')
    option = input('Enter your option:')
    if option.lower() == 'd':
        amount = float(input('Enter amount to be deposited:'))
        c.deposit(amount)
    elif option.lower() == 'w':
        amount = float(input('Enter amount to be withdrawn:'))
        c.withdraw(amount)
    elif option.lower() == 'e':
        print('Thank you for banking.')
        break
    else:
        print('Your option is invalid.Please choose a correct option.')
