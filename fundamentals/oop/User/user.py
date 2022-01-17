class User:
    # Contructor Function!!!  Creates the instance of an object within a class. 
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0

    def make_deposit(self, amt):
        self.account_balance += amt
    def make_withdrawal(self, amt):
        self.account_balance -= amt
    def disp_user_balance(self):
        print(self.account_balance)
    def transfer(self, other, amt):
        self.account_balance -= amt
        other.account_balance += amt

rosencrantz = User("rosencrantz", "rc@rc.com")
guilderstern = User("guilderstern", "gs@gs.com")
joe = User("joe", "joe@joe.com")
        
joe.make_deposit(200)
        
joe.disp_user_balance()
joe.make_deposit(300)
joe.disp_user_balance()
joe.transfer(rosencrantz, 45)
print(joe.account_balance)
print(rosencrantz.account_balance)
