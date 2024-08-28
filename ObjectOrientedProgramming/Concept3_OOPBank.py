import sys


class Customer:
    """The customer class can be used to perform several bank operations"""
    bank_name = "Swiss Bank"

    def __init__(self, customer_name, balance=0.0):
        self.customer_name = customer_name
        self.balance = balance

    def deposit(self, amt):
        self.balance += amt
        print(f"The amount present in the account after deposit is : {self.balance}")

    def withdrawal(self, amt):
        if amt > self.balance:
            print("Insufficient funds")
            sys.exit()
        self.balance -= amt
        print(f"The amount present in the account after withdrawal is : {self.balance}")


print(f"Welcome to {Customer.bank_name}")
name = input("Enter your name : ")
customer_balance = float(input("Enter the amount you want to do as an initial deposit : "))
c = Customer(name, customer_balance)

while True:
    print("d-deposit \nw:withdrawal \ne:exit")
    option = input("Please select your option : ")
    if option.lower() == 'd':
        amount = float(input("Enter the amount you want to deposit : "))
        c.deposit(amount)
    elif option.lower() == 'w':
        amount = float(input("Enter the amount you want to withdraw : "))
        c.withdrawal(amount)
    elif option.lower() == 'e':
        print("Thanks for banking with us")
        sys.exit()
    else:
        print("Please select valid option to proceed further")


