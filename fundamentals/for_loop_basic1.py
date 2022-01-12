for x in range (151): #print all integers from 0-150
    print(x)

for x in range(5 , 1001, 5): #pring all the multiples of 5 from 5 to 1,000
    print(x)

for x in range(1 , 101): #print integers 1 to 100. If divisible by 5, print "Coding". If by 10, print "Coding Dojo"
    if x % 10 == 0:
        print("Coding Dojo")
    elif x % 5 == 0:
        print("Coding")
    else:
        print(x)
#Add odd integers from 0 to 500000 and print the final sum
odds = []
for x in range(1 , 500000 , 2):
    odds.append(x)
print(sum(odds))

#5 Print positive numbers starting at 2018, counting down by fours
for x in range(2018 , 0 , -4):
    print(x)

"""6 Flexible Counter - Set three variables: lowNum, highNum, mult. 
Starting at lowNum and going through highNum, 
print only the integers that are a multiple of mult. 
""" 
low_num = 4
high_Num = 40
mult = 6
for x in range(low_num , high_Num):
    if x % mult == 0:
        print(x)