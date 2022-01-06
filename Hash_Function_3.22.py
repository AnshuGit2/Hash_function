places = []
with open('Word_list.txt', 'r') as filehandle:
    for line in filehandle:
        currentPlace = line[:-1]
        places.append(currentPlace)
           
def rehash(oldhash, table_size):
    return (oldhash+1) % table_size

def weighted_ord_hash(string, table_size):
    hash_val = 0
    for position in range(len(string)):
        hash_val = hash_val + (ord(string[position]) * position)
    return hash_val % table_size


def lp_hash(item_list, table_size):
    lp_hash_table = dict([(i,None) for i,x in enumerate(range(table_size))])   
    for item in item_list:
        i = weighted_ord_hash(item, table_size)
        
        if lp_hash_table[i] == None:
            lp_hash_table[i] = item
        elif lp_hash_table[i] != None:
           
            next_slot = rehash(i, table_size)
           
            while lp_hash_table[next_slot] != None:
                next_slot = rehash(next_slot, len(lp_hash_table.keys()))
                
            if lp_hash_table[next_slot] == None:
                lp_hash_table[next_slot] = item
    return lp_hash_table

print(lp_hash(places, 1244))