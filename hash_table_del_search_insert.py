   
class hash:  
    def __init__(self):  
        self.size = int(input("Enter the Size of the hash table : "))  
        self.table = list(0 for i in range(self.size))  
        self.countElement = 0  
        self.comparisons = 0  
     
     
      
    def isFull(self):  
        if self.countElement == self.size:  
            return True  
        else:  
            return False  
     
     
      
    def hashfunc(self, element):  
        return element % self.size  
         
     
     
    def insert(self, element):  
          
        if self.isFull():  
            print("Hash Table Full")  
            return False  
             
        isStored = False  
         
        place = self.hashfunc(element)  
         
         
        if self.table[place] == 0:  
            self.table[place] = element  
            print("Element " + str(element) + " at place " + str(place))  
            isStored = True  
            self.countElement += 1  
         
          
        else:  
            print("Collision has occured for element " + str(element) + " at place " + str(place) + " finding new Place.")  
            while self.table[place] != 0:  
                place += 1  
                if place >= self.size:  
                    place = 0  
             
            self.table[place] = element  
            isStored = True  
            self.countElement += 1  
        return isStored  
         
   
      
      
      
    def search(self, element):  
        found = False  
         
        place = self.hashfunc(element)  
        self.comparisons += 1  
         
        if(self.table[place] == element):  
            return place  
            isFound = True  
         
          
          
          
        else:  
            temp = place - 1  
              
            while place < self.size:  
                if self.table[place] != element:  
                    place += 1  
                    self.comparisons += 1  
                else:    
                    return place  
             
              
            place = temp  
            while place >= 0:     
                if self.table[place] != element:  
                    place -= 1  
                    self.comparisons += 1  
                else:    
                    return place  
                     
        if not found:  
            print("Element not found")  
            return False  
             
   
      
    def remove(self, element):  
        place = self.search(element)  
        if place is not False:  
            self.table[place] = 0  
            print("Element " + str(element) + " is Deleted")  
            self.countElement -= 1  
        else:  
            print("Element is not present in the Hash Table")  
        return  
         
     
      
    def display(self):  
        print("\n")  
        for i in range(self.size):  
            print(str(i) + " = " + str(self.table[i]))  
        print("The number of element is the Table are : " + str(self.countElement))  
         
             
  
table1 = hash()  
   
  
table1.insert(22)  
table1.insert(36)  
table1.insert(41)  
table1.insert(27)  
table1.insert(90)  
table1.insert(38)  
table1.insert(98)  
table1.insert(50)  
table1.insert(88)         
   
  
table1.display()  
print()  
   
  
print("The place of element 41 is : " + str(table1.search(41)))  
print("The place of element 38 is : " + str(table1.search(38)))  
print("The place of element 90 is : " + str(table1.search(90)))  
print("The place of element 88 is : " + str(table1.search(88)))  
print("The place of element 1 is : " + str(table1.search(1)))  
print("\nTotal number of comaprisons done for searching = " + str(table1.comparisons))  
print()  
   
table1.remove(90)  
table1.remove(22)  
   
table1.display()  
   
 
 