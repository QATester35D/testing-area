#######################################################################################################
# Working through various concepts
#######################################################################################################
import time

# Removing spaces from a string using replace method
wordToRemoveSpaces=" The string with spaces "
print("The string being used to strip spaces out of is:",wordToRemoveSpaces)
newWord=wordToRemoveSpaces.replace(" ","")
print (f"The string has no spaces now and is one big word, it is: {newWord}.")
time.sleep(1)
# Largest subarray of 0's and 1's - gets the starting and ending indexes of the largest 
# subarray with equal number of 0s and 1s. Also returns the size of such subarray.
def findLargestSubArray(arr, n):
    sum = 0
    maxsize = -1

    # Pick a starting point as i
    for i in range(0, n-1):
        sum = -1 if(arr[i] == 0) else 1

        # Consider all subarrays starting from i
        for j in range(i + 1, n):
            sum = sum + (-1) if (arr[j] == 0) else sum + 1
            # If this is a 0 sum subarray, then compare it with maximum size subarray calculated so far
            if (sum == 0 and maxsize < j-i + 1):
                maxsize = j - i + 1
                startindex = i

    if (maxsize == -1):
        print("No such subarray");
    else:
        print(startindex, "to", startindex + maxsize-1);

    return maxsize

# arr = [1, 0, 0, 1, 0, 1, 1] #sub-array 0, 0, 0, 1, 1, 1 <=> 0 to 5
arr = [1, 0, 0, 1, 0, 1, 1, 0] #sub-array 0, 0, 0, 0, 1, 1, 1, 1 <=> 0 to 7
arraySize = len(arr)
findLargestSubArray(arr, arraySize)
print("wait")
##############################
# Bubble Sort For Linked List
##############################
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

#Create Class Linked    
class Linked:
    def __init__(self):
        #Assign default value
        self.head=None

    #insert new node to linked list  
    def insert(self,data):
        node=Node(data)
        node.next=None
        if self.head==None:
            self.head=node
        else:
            temp=self.head
            while temp.next!=None:
                temp=temp.next
            #add node    
            temp.next=node

    def display(self):
        if(self.head==None):
            print("Empty Linked List")
            return

        temp=self.head
       
        while(temp!=None):
          print(temp.data,end=" ")
          temp=temp.next
    
    #perform bubble sort in single linked list
    def bubbleSort(self):
        if(self.head!=None):
          current=None
          new_head=None
          move_node=None
          prev=None
          while(self.head!=None):
            prev=None
            current=self.head
            move_node=self.head
            while(current!=None):
              #When current node value is grator than previous node
              if (current.next!=None):
                print("current.next.data", current.next.data)
              print("move_node.data", move_node.data)
              if(current.next!=None and  current.next.data>move_node.data):
                #Swap node values
                move_node=current.next
                prev=current

              current=current.next
            
            if(move_node==self.head):
              print("\nPrinting self.head being assigned to move_node:",self.head)
              self.head=(self.head).next
            
            if(prev!=None):
              print("\nPrinting move_node.next being assigned to prev.next:",move_node.next)
              prev.next=move_node.next
            
            move_node.next=new_head
            new_head=move_node
          
          #make new head
          self.head=new_head
          
        else:
           print("Empty Linked list")

def main():
    #Create Object of class Linked
    obj=Linked()
    #insert element of linked list
    obj.insert(7)
    obj.insert(50)
    obj.insert(9)
    obj.insert(42)
    obj.insert(5)
    obj.insert(15)
    print("Before sort : ")
    
    #display all node
    obj.display()

    obj.bubbleSort()
    print("\nAfter sort  : ")

    obj.display()

if __name__=="__main__":
    main()

#######################################################################################################
#Bubble sort - swapping improvement to exit after encountering one run with no swapping, so we're done
#######################################################################################################
my_array = [7, 3, 9, 12, 11]

n = len(my_array)
for i in range(n-1):
    swapped = False
    for j in range(n-i-1):
        if my_array[j] > my_array[j+1]:
            my_array[j], my_array[j+1] = my_array[j+1], my_array[j]
            swapped = True
    if not swapped:
        break

print("Sorted array:", my_array)

##################################
#Bubble sort
##################################
my_array = [64, 34, 25, 12, 22, 11, 90, 5]

n = len(my_array)
for i in range(n-1):
    for j in range(n-i-1):
        if my_array[j] > my_array[j+1]:
            my_array[j], my_array[j+1] = my_array[j+1], my_array[j]

print("Sorted array:", my_array)

#################################################################################
#Creating a basic Fibonnaci where you add the previous number to the next number
#################################################################################
print(0)
print(1)
count = 2

def fibonacci(prev1, prev2):
    global count
    if count <= 19:
        newFibo = prev1 + prev2
        print(newFibo)
        prev2 = prev1
        prev1 = newFibo
        count += 1
        fibonacci(prev1, prev2)
    else:
        return

fibonacci(1,0)

##################################
#Find the mininum value in a List
##################################
my_array = [7, 12, 9, 4, 11]
minVal = my_array[0]

for i in my_array:
    if i < minVal:
        minVal = i

print('Lowest value:',minVal)