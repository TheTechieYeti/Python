import re
from string import punctuation
test_string = "This is a test string.  It is not very long."

def jean_luc(test_string):
    string_test = isinstance(test_string, str)
    if string_test == True:
        res = re.findall(r'\w+', test_string)
        length = len(res)
#         # print (res, length) #test print for ensuring my variables are correct
#         for i in range(length):
#             test_word = res[i-1]
#             print(test_word) #test print to make sure for loop is working
#             for q in range (length):
#                 # print(res[q]) #test print to make sure second for loop is working
#                 if test_word == res[q]:
#                     print("found duplicate")
            
        
        
        
        
        
        # for i in range (length):
        #     word = res[i]
        #     word_counter = 1
        #     for t in range (1, length):
        #         if word != res[t]:
        #             print(f'{word} vs {res[t]}')
        #             word_list.append(word)
        #             count_list.append(word_counter)
        #             length -= 1
        #             print(length)
        #             del res[i]
            

        #     print(f"This is my new word list {word_list}")
        #     print(count_list)

# jean_luc(test_string)


# {
#   this: 1,
#   is: 2,
#   a: 1,
#   test: 1
#   string: 1
#   it: 1,
#   not: 1,
#   very: 1,
#   long: 1
# }




def word_count(data):
    # make an empty dict
    words = {}
    data = data.replace(".", "")
    punctuation = [",","."]
    for c in punctuation:
        if c in data:
            data = data.replace(c, "")
    #split into a list 
    data = data.split(" ") #delimiter
    #take the first index of that list and store it as a variable
    # put the words into a dict
    for word in data:
        if word == "":
            continue
        lower = word.lower()
        #test if lower is in the dictionary
        if lower not in words:
            words[lower] = 1
        else:
            words[lower] += 1
    return words                                 
    # return the dictionary


print(word_count(test_string))
