#1
def number_of_food_groups():
    return 5
print(number_of_food_groups())
# predicted 5, output was 5

#2
def number_of_military_branches():
    return 5
print(number_of_days_in_a_week_silicon_or_triangle_sides() + number_of_military_branches())
#predicted error, output was error

#3
def number_of_books_on_hold():
    return 5
    return 10
print(number_of_books_on_hold())
#predicted 10, output was 5. 

#4
def number_of_fingers():
    return 5
    print(10)
print(number_of_fingers())
#predicted output of 10,5 out put was actually 5. Printing funtion is not the same as calling. It prints only the value

#5
def number_of_great_lakes():
    print(5)
x = number_of_great_lakes()
print(x)
#predicted 5, none output was expected

#6
def add(b,c):
    print(b+c)
print(add(1,2) + add(2,3))
#predicted outcome of none, was accurate

#7
def concatenate(b,c):
    return str(b)+str(c)
print(concatenate(2,5))
#predicted [2,5] output was 25


#8
def number_of_oceans_or_fingers_or_continents():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(number_of_oceans_or_fingers_or_continents())
#predicted 100 10, output was 100 7. Why does last return value not count?

#9
def number_of_days_in_a_week_silicon_or_triangle_sides(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3) + number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
#predicted outcome was correct

#10
def addition(b,c):
    return b+c
    return 10
print(addition(3,5))
#predicted outcome was correct 8 

#11
b = 500
print(b)
def foobar():
    b = 300
    print(b)
print(b)
foobar()
print(b)
#predicted outcome was correct, 500 n/ 500n/ 300n/ 500n/

#12
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
foobar()
print(b)
#predicted outcome was different due to the fact that the function does not change the global variable

#13
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
b=foobar()
print(b)
#predicted outcome was correct

#14
def foo():
    print(1)
    bar()
    print(2)
def bar():
    print(3)
foo()
#predicted outcome was correct

#15
def foo():
    print(1)
    x = bar()
    print(x)
    return 10
def bar():
    print(3)
    return 5
y = foo()
print(y)
#predicted outcome was correct 