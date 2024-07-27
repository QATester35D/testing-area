import time
#################################################################################
# Working with stacks - A stack is a data structure that can hold many elements.
# In python you would use a list as an array for stacks
# Stacks use a LIFO approach
# Using:
# - Push: Adds a new element on the stack.
# - Pop: Removes and returns the top element from the stack.
# - Peek: Returns the top element on the stack.
# - isEmpty: Checks if the stack is empty.
# - Size: Finds the number of elements in the stack.
#################################################################################
#################################################################################
# A better approach to working with stacks (really lists) in python using classes
#################################################################################
class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, element):
        self.stack.append(element)
    
    def pop(self):
        if self.isEmpty():
            return "Stack is empty"
        return self.stack.pop()
    
    def peek(self):
        if self.isEmpty():
            return "Stack is empty"
        return self.stack[-1]
    
    def isEmpty(self):
        return len(self.stack) == 0
    
    def size(self):
        return len(self.stack)

# Create a stack
myStackList = Stack()

myStackList.push('A')
myStackList.push('B')
myStackList.push('C')
print("Stack (really a list in Python) that was just created:", myStackList.stack)

itemBeingRemoved=myStackList.pop()
print("Item being removed using Pop (LIFO approach):", itemBeingRemoved)
print("Stack/list at this point is:",myStackList.stack)

print("Peek at top element of stack/list after the pop:", myStackList.peek())

myStackList.push('D') #this is really an append
print("Performed an append to push a new item to the stack/list. The new top item is:",myStackList.peek())
print("The stack/list is now:", myStackList.stack)

print("Checking isEmpty on the stack/list:", myStackList.isEmpty())

print("What is the size of the stack/list?", myStackList.size())
time.sleep(1)
#################################################################################
# Basic approach to working with stacks/lists
#################################################################################
stack = []

# Push
stack.append('A')
stack.append('B')
stack.append('C')
print("Stack (really a list in Python) that was just created:", stack)

# Pop
element = stack.pop()
print("Item being removed using Pop (LIFO approach):", element)
print("Stack/list at this point is:",stack)

# Peek
topElement = stack[-1]
print("Peek at top element of stack/list:", topElement)

# Push
stack.append('D')
print("Performing an append to push a new item to the stack/list. The item is:",stack[-1])
print("The stack/list is now:", stack)

# isEmpty
isEmpty = not bool(stack)
print("Checking isEmpty on the stack/list:", isEmpty)

# Size
print("What is the size of the stack/list?",len(stack))
time.sleep(1)
