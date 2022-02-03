# strong_password (input)

# true or false 

# strong_password:
# at least one capital letter
# at least one lowercase letter
# at least 8 letters long
# at least one symbol
# can't be a weak password 

# password
# opensesame
# letmein!
# bill_for_president
# 12345678
badpasswords = ['LetMeIn!', 'password', 'opensesame', 'bill_for_president']
capitals = ["A","B","C","D","E","F","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
lowers = ["a","b","c","d","e","f","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
numbers = ["1","2","3","4","5","6","7","8","9"]
def strong_password(input):
    if input in badpasswords:
        print("Can't Be a weak passowrd")
        return False      
    