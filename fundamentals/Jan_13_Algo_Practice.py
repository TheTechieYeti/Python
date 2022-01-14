def new_list(old_list):
    for x in range(len(old_list)):
        if old_list[x] % 2 == 0:
            old_list[x] += old_list[x-1]
    return old_list

print(new_list([1,2,3,4])) #1137

print(new_list([2,2,3,4])) #6837 Since the first value was even, the function looped around and used the last value of the list to add to the first. 


