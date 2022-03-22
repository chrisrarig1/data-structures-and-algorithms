from code_challenges.hash_table.hash_table import HashTable

def left_join(hash1, hash2):
    key = HashTable.keys()
    new_list = []
    keys1 = hash1.key
    for i in keys1:
        if i in keys2:
            new_list.append(hash1[i])
            new_list.append(hash2[i])
        else:
            new_list.append(hash1[i])
            new_list.append('Null')
    return new_list
