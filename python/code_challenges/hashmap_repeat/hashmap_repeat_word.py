import re

def repeated_word(string):
    new_string = re.sub(r'[^\w\s]', '', string).lower().split()
    new_list = []
    for i in new_string:
        if len(new_string) == 1:
            return i
        if i in new_list:
            return i
        else:
            new_list.append(i)

#Another way using a dictionary better for stretch goals
def repeated_word2(string):
    new_string = re.sub(r'[^\w\s]', '', string).lower().split()
    new_list = {}
    for i in new_string:
        if len(new_string) == 1:
            return i
        if i not in new_list.keys():
            new_list[i] = 1
        else:
            return i

# Returns dictionary with number of occurences for each word
def repeated_word3(string):
    new_string = re.sub(r'[^\w\s]', '', string).lower().split()
    new_list = {}
    for i in new_string:
        if len(new_string) == 1:
            return i
        if i not in new_list.keys():
            new_list[i] = 1
        else:
            new_list[i] +=1
    return new_list
            


string = "It was a queer, sultry summer, the summer they electrocuted the Rosenbergs, and I didn’t know what I was doing in New York..."

print(repeated_word2(string))