num1 = 42 # variable declaration, number
num2 = 2.3 # variable declaration, number
boolean = True # boolean, variable declaration  
string = 'Hello World' #variable declation, string 
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] #variable declaration, list? 
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #variable declaration, dictionary
fruit = ('blueberry', 'strawberry', 'banana') #variable declaration, tuple
print(type(fruit)) #log statement tuple
print(pizza_toppings[1]) #Sausage
pizza_toppings.append('Mushrooms') #same as push in Java
print(person['name']) #John
person['name'] = 'George' #access and change dictionary
person['eye_color'] = 'blue' #access and change dictionary
print(fruit[2]) #access and log statement for tuple

if num1 > 45: #conditional if
    print("It's greater") #log statement
else: #conditional else
    print("It's lower") #log statement

if len(string) < 5: #length check, conditional if, 
    print("It's a short word!") #log statement
elif len(string) > 15: #conditional else if, length check 
    print("It's a long word!") #log statement
else: #conditional else
    print("Just right!") #log statement

for x in range(5):
    print(x)
for x in range(2,5):
    print(x)
for x in range(2,10,3):
    print(x)
x = 0
while(x < 5):
    print(x)
    x += 1

pizza_toppings.pop() #list remove last value
pizza_toppings.pop(1) #list remove "sausage"

print(person) #log statement dictionary
person.pop('eye_color') #remove dictionary value
print(person)

for topping in pizza_toppings:
    if topping == 'Pepperoni':
        continue
    print('After 1st if statement')
    if topping == 'Olives':
        break

def print_hello_ten_times():
    for num in range(10):
        print('Hello')

print_hello_ten_times()

def print_hello_x_times(x):
    for num in range(x):
        print('Hello')

print_hello_x_times(4)

def print_hello_x_or_ten_times(x = 10):
    for num in range(x):
        print('Hello')

print_hello_x_or_ten_times()
print_hello_x_or_ten_times(4)


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)