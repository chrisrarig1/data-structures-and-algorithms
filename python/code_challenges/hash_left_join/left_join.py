from code_challenges.hash_table.hash_table import HashTable

def left_join(hash1, hash2):
    new_list = []
    keys1 = HashTable.keys(hash1)
    keys2 = HashTable.keys(hash2)
    for i in keys1:
        if i in keys2:
            new_list.append(i)
            new_list.append(HashTable.get(hash1,i))
            new_list.append(HashTable.get(hash2,i))
        else:
            new_list.append(i)
            new_list.append(HashTable.get(hash1,i))
            new_list.append('Null')
    return new_list
