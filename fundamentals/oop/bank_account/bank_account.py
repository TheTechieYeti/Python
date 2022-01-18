class BankAccount:
    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate, balance = 0): 
        self.int_rate = .1
        self.balance = balance
        # your code here! (remember, instance attributes go here)
        # don't worry about user info here; we'll involve the User class soon
    
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

    def display_account_info(self):
        print(f"Balance: {self.balance}")
        return self

    def yield_interest(self):
        if self.balance > 0:
            growth = self.balance * self.int_rate
            self.balance = growth + self.balance
        return self

savings = BankAccount(.02, 300)
checkings = BankAccount(.1, 1000)
savings.deposit(100).deposit(200).deposit(50).withdraw(400).yield_interest().display_account_info()
checkings.deposit(20).deposit(500).withdraw(30).withdraw(50).withdraw(3).withdraw(.5).yield_interest().display_account_info()


# vTo the first account, make 3 deposits and 1 withdrawal, then yield interest and display the account's info all in one line of code (i.e. chaining)

# To the second account, make 2 deposits and 4 withdrawals, then yield interest and display the account's info all in one line of code (i.e. chaining