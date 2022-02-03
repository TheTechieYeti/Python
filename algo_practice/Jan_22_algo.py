###Nathans Algo from sesson

def pal_check2 (word):
    word = word.lower()
    for i in range(0, (len(word) // 2)):
        last = word[len(word) - (i+1]}
        if word[i] != last:
            continue
        print("True")
        return True
######Nathans Algo from sesson ^^^^^^^^^^^


def split(word):
    word = word.lower()
    print(word)
    char_list = [char for char in word]
    length_list = len(char_list)
    for char in range(len(char_list)):
        if char_list[char] != char_list[length_list-1]:
            return False
        else:
            return True

        
print(split("hannaH"))
print(split("hNnah"))
print(split("HannA"))
print(split("hanah"))
print(split("frAnk"))
print(split("tattarrattat"))
print(split("helleh"))