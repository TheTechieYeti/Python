# defein a function fine_two(lst). Find two integers that total to 2020 and then returns the product of those two integers 



data = [1721,
        979,
        366,
        278,
        675,
        1456,
        1001,
        999]
data1 = [5]

#iterate through the list skipping the first number
def fine_two(lst):
    sum = 2000
    if len(lst) < 2:
        print("Not enough numbers to execute function.")
    for i in range(len(lst)):
        for z in range(i,len(lst)):
            if (lst[i] + lst[z]) == sum:
                return lst[i] * lst[z]
    print("No such numbers are in this list")

    
fine_two(data)
print(fine_two(data))
#compare the sume of the first value and every other number in the list
#if the sum is 2020 return the product of the two numbers
#else display no such numbers exist 