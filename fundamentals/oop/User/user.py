class User:
    # Contructor Function!!!  Creates the instance of an object within a class. 
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0

    def make_deposit(self, amt):
        self.account_balance += amt
        return self
    
    def make_withdrawal(self, amt):
        self.account_balance -= amt
        return self

    def disp_user_balance(self):
        print(f"User: {self.name.capitalize()}, Balance: {self.account_balance}")
        return self
    
    def transfer(self, other, amt):
        self.account_balance -= amt
        other.account_balance += amt
        return self

rosencrantz = User("rosencrantz", "rc@rc.com")
guilderstern = User("guilderstern", "gs@gs.com")
joe = User("joe", "joe@joe.com")
        
rosencrantz.make_deposit(400).make_deposit(50).make_withdrawal(350).disp_user_balance()
guilderstern.make_deposit(300).transfer(joe, 47).disp_user_balance()
joe.make_deposit(50000).make_deposit(30).disp_user_balance()
