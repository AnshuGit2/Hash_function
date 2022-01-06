
from random import randrange
 

class TreapClass:
    
    def __init__(self, K2, PQ=100, leftnode=None, rightnode=None):
        self.K2 = K2
        self.PQ = randrange(PQ)
        self.leftnode = leftnode
        self.rightnode = rightnode
 
 
def sinkLeftnode(K1):
 
    R = K1.rightnode
    X = K1.rightnode.leftnode
 
    # sink
    R.leftnode = K1
    K1.rightnode = X
 
    # set a new K1
    return R
 
 
def sinkRightnode(K1):
 
    L = K1.leftnode
    Y = K1.leftnode.rightnode
 
    # sink
    L.rightnode = K1
    K1.leftnode = Y
 
   
    return L
 

def put(K1, K2):
 
    #basecase:
    if K1 is None:
        return TreapClass(K2)
 
    # if the given K2 is less than the K1 node, insert in the leftnode subtree;
    # otherwise, insert in the rightnode subtree
    if K2 < K1.K2:
        K1.leftnode = put(K1.leftnode, K2)
 
        # sink rightnode if heap property is violated
        if K1.leftnode and K1.leftnode.PQ > K1.PQ:
            K1 = sinkRightnode(K1)
    else:
        K1.rightnode = put(K1.rightnode, K2)
 
        # sink leftnode if heap property is violated
        if K1.rightnode and K1.rightnode.PQ > K1.PQ:
            K1 = sinkLeftnode(K1)
 
    return K1
 
 

def get(K1, key):
    
    if K1 is None:
        return False
    
    if K1.K2 == key:
        return True
    
    if key < K1.K2:
        return get(K1.leftnode, key)
 
   
    return get(K1.rightnode, key)
 
 

def removeMax(K1, key):
 
    # base case: if the key is not found in the tree
    if K1 is None:
        return None
 
    # if the key is less than the K1 node, recur for the leftnode subtree
    if key < K1.K2:
        K1.leftnode = removeMax(K1.leftnode, key)
 
    # if the key is more than the K1 node, recur for the rightnode subtree
    elif key > K1.K2:
        K1.rightnode = removeMax(K1.rightnode, key)
 
   
    else:
 
        # Case first: node should be deleted have no child because it is  leaf node
        if K1.leftnode is None and K1.rightnode is None:
            # deallocate the memory and update K1 to None
            K1 = None
 
        # Case second: node should be deleted have 2 childs 
        elif K1.leftnode and K1.rightnode:
            # if the leftnode child has less PQ than the rightnode child
            if K1.leftnode.PQ < K1.rightnode.PQ:
                # call `sinkLeftnode()` on the K1
                K1 = sinkLeftnode(K1)
 
                # recursively delete the leftnode child
                K1.leftnode = removeMax(K1.leftnode, key)
            else:
                # call `sinkRightnode()` on the K1
                K1 = sinkRightnode(K1)
 
                # recursively delete the rightnode child
                K1.rightnode = removeMax(K1.rightnode, key)
 
        # Case three: node should be deleted have one child only
        else:
            # pick a child node
            child = K1.leftnode if (K1.leftnode) else K1.rightnode
            K1 = child
 
    return K1
 

# reverse inorder traversal
def returnTreap(K1, space):
 
    height = 10
 
    #Base case
    if K1 is None:
        return
 
    #increase length between levels
    space += height
 
    #return the rightnode child first
    returnTreap(K1.rightnode, space)
 
    #return the node after space
    for i in range(height, space):
        print(' ', end='')
 
    print((K1.K2, K1.PQ))
 
    # return the leftnode child
    returnTreap(K1.leftnode, space)
    

# the score for the beauty_pageant is generated using random function 
beauty_pageant = [5, 2, 1, 4, 9, 8, 10, 12, 13, 14, 15, 3, 6, 7, 11]
#beauty_pageant_number = input("Enter the contestants number: ")
#beauty_pageant_name  = input("Enter the contestants name: ")
#print(beauty_pageant_name + str(beauty_pageant_number))

# build a treap
K1 = None
for key in beauty_pageant:
    K1 = put(K1, key)

print("Implementing a Treap: ")
returnTreap(K1, 0)

#return(Deleted node)
K1 = removeMax(K1,K1.K2)

print("After Deleting A Root Treap: ")

returnTreap(K1, 0)


