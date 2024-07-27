import time
#################################################################################
# Working with queues - A queue is a data structure that can hold many elements.
# In python this would be a list. A queue is like a stack but follows FIFO instead.
# But you control the queues approach to using FIFO, this is really not built in
# Using:
# - Enqueue: Adds a new element to the queue. (this is really append)
# - Dequeue: Removes and returns the first (front) element from the queue. - you control which element is removed
# - Peek: Returns the first element in the queue. - again you control which element is peeked
# - isEmpty: Checks if the queue is empty.
# - Size: Finds the number of elements in the queue.
#################################################################################
#################################################################################
# A better approach to working with queues (really lists) in python using classes
#################################################################################
class Queue:
    def __init__(self):
        self.queue = []
    
    def enqueue(self, element):
        self.queue.append(element)
    
    def dequeue(self):
        if self.isEmpty():
            return "queue is empty"
        return self.queue.pop(0)
    
    def peek(self):
        if self.isEmpty():
            return "queue is empty"
        return self.queue[0]
    
    def isEmpty(self):
        return len(self.queue) == 0
    
    def size(self):
        return len(self.queue)

# Create a queue
myQueueList = Queue()

myQueueList.enqueue('A')
myQueueList.enqueue('B')
myQueueList.enqueue('C')
print("The queue (really a list in Python) that was just created:", myQueueList.queue)

itemBeingRemoved=myQueueList.dequeue()
print("Item being removed using Pop (FIFO approach):", itemBeingRemoved)
print("The queue/list at this point is:",myQueueList.queue)

print("Peek at the element at the front of the queue/list after the pop was performed:", myQueueList.peek())

myQueueList.enqueue('D') #this is really an append
print("The queue/list is now:", myQueueList.queue)

print("Checking isEmpty on the queue/list:", myQueueList.isEmpty())

print("What is the size of the queue/list?", myQueueList.size())
time.sleep(1)

#################################################################################
# Basic approach to working with queues/lists - it's basically like queues.
# The enqueue is really an append
# 
# to control what is popped you specify the list element
#################################################################################
queue = []

# Enqueue
queue.append('A')
queue.append('B')
queue.append('C')
print("The queue that was just created is:", queue)
# Dequeue
element = queue.pop(0)
print("Dequeue - the element being removed (popped) is:", element)
print("The queue is now:",queue)
# Peek
frontElement = queue[0]
print("Peek at the front element of queue/list after the pop:", frontElement)
valToAppend='D'
queue.append(valToAppend)
print(f"The value {valToAppend} was just added to the queue. The queue is now:", queue)

# isEmpty
isEmpty = not bool(queue)
print("Checking isEmpty on the queue/list:", isEmpty)

# Size
print("What is the size of the queue/list?", len(queue))
time.sleep(1)