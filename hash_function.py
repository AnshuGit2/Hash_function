

def CountFrequency(my_list, fixed_item): 
  
    # Creating an empty dictionary  
    freq = {} 
    for item in my_list: 
        if (item in freq): 
            freq[item] += 1
        else: 
            freq[item] = 1
  
    for key, value in freq.items(): 
        if key==fixed_item:
            return value

places = []
with open('Word_list.txt', 'r') as filehandle:
    for line in filehandle:
        currentPlace = line[:-1]
        places.append(currentPlace)

def weighted_ord_hash(string, table_size):
    hash_val = 0
    for position in range(len(string)):
        hash_val = hash_val + (ord(string[position]) * position)
    return hash_val % table_size

def rehash(oldhash, count_new):
    return (oldhash+3) % count_new


def lp_hash(item_list, table_size):
    lp_hash_table = dict([(i,None) for i,x in enumerate(range(table_size))])   
    for item in item_list:
        i = weighted_ord_hash(item, table_size)

        if lp_hash_table[i] == None:
            lp_hash_table[i] = item
        elif lp_hash_table[i] != None:
            if CountFrequency(item_list, item) > 0:
                t = CountFrequency(item_list, item)
            else:
                t = 1
            next_slot = rehash(i, t)
            while lp_hash_table[next_slot] != None:
                next_slot = rehash(next_slot, len(lp_hash_table.keys()))
            if lp_hash_table[next_slot] == None:
                lp_hash_table[next_slot] = item
    return lp_hash_table

print(lp_hash(places, 1244))