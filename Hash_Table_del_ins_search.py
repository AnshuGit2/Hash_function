hash_table = [[] for _ in range(10)]
print (hash_table)

def insert(hash_table, key, value):
    hash_key = hashing_func(key)
    hash_table[hash_key].append(value)
 
insert(hash_table, 10, 'Nepal')
print (hash_table)
# Output: 
# [['Nepal'], [], [], [], [], [], [], [], [], []]
 
insert(hash_table, 25, 'USA')
print (hash_table)
# Output: 
# [['Nepal'], [], [], [], [], ['USA'], [], [], [], []]
 
insert(hash_table, 20, 'India')
print (hash_table)
# Output: 
# [['Nepal', 'India'], [], [], [], [], ['USA'], [], [], [], []]
