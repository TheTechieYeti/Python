

class User:
    # Contructor Function!!!  Creates the instance of an object within a class. 
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.savings = BankAccount(.4, 4000)
        self.checkings = BankAccount(.1, 20)
        self.business = BankAccount(.6, 50000)
    
    def display_account_balances(self):  #how can I print all the balances at once
        print(f"Savings Balance: {self.savings.balance} Checkings Balance: {self.checkings.balance} Business Balance: {self.business.balance} ")
        
        
class BankAccount:
    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate
        self.balance = balance
    
    def transfer(self, amount, useraccount):
        if amount < self.balance:
            self.balance -= amount
            useraccount.balance += amount
            return self
        else: 
            print("Insufficient funds for transfer")
            return self

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
            
        else: 
            self.balance -= amount
            
        return self

    def display_account_info(self):  #how can I make this print all accounts
        print(f"Balance: {self.balance}")
        return self

    def yield_interest(self):
        if self.balance > 0:
            growth = self.balance * self.int_rate
            self.balance = growth + self.balance
        return self

rose = User("rosencrantz", "rc@rc.com")
guido = User("guilderstern", "gs@gs.com")
joe = User("joe", "joe@joe.com")
joe.savings.transfer(4001,rose.savings).display_account_info().withdraw(4001).display_account_info().transfer(37, joe.business).display_account_info()
rose.savings.deposit(437).yield_interest().display_account_info()
joe.display_account_balances()



# savings.deposit(100).deposit(200).deposit(50).withdraw(400).yield_interest().display_account_info()
# checkings.deposit(20).deposit(500).withdraw(30).withdraw(50).withdraw(3).withdraw(.5).yield_interest().display_account_info()


