def reverse_list(ll):

    length = len(ll)
    s = length

    new_list = [None] * length
    print(new_list)
    for item in ll:
        s = s - 1
        new_list[s] = item
    return new_list

ll = [1,2,3,4,5]
print(reverse_list(ll))
