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
